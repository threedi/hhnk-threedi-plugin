# %%
# # -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 09:17:26 2021

@author: chris.kerklaan

#TODO:
    1. Let groups be unique
    2. Add printcomposers
    
"""
import os
from tokenize import group
from qgis.utils import iface
from qgis.core import (
    QgsProject,
    QgsVectorLayer,
    QgsRasterLayer,
    QgsLayerTreeGroup,
    QgsMapThemeCollection,
    QgsPrintLayout,
    QgsReadWriteContext,
)
# %%
from qgis.PyQt.QtXml import QDomDocument
import pandas as pd
import logging
import itertools


logger=logging.getLogger(__name__)

# # project structure
TEST_STRUCTURE = {
    "eerste": [],
    "test": ["g1", "g2", "g3"],
    "derde": ["layer1", "layer2"],
    "vierde": ["layer1", "layer2"],
    "yolo": [],
}
GROUP_STRUCTURE = list(TEST_STRUCTURE.keys())


class Layer:
    """class used for multiple qgis layer:
    QgsVectorLayer
    QgsRasterLayer
    """

    def __init__(
        self,
        source_path: str,
        layer_name: str,
        type: str = None,
        style_path=None,
        subject="HTT",
        group_lst = [],
    ):
        """
        Parameters
        ----------
        source_path : str
            path to vector
        layer_name : str
            name of layer
        style_path : str
            poth to style
        type : str
            can be 'wms', 'vector' or 'raster'

        """
        if type == None:
            type = self.get_type(source_path)

        if type == "vector":
            self.layer = QgsVectorLayer(source_path, layer_name, "ogr")
        elif type == "raster":
            self.layer = QgsRasterLayer(source_path, layer_name)
        elif type == "wms":
            self.layer = QgsRasterLayer(source_path, layer_name, "wms")
        elif type == "arcgismapserver":
            self.layer = QgsRasterLayer(source_path, layer_name, "arcgismapserver")
        elif type == "arcgisfeatureserver":
            self.layer = QgsVectorLayer(source_path, layer_name, "arcgisfeatureserver")

        self.subject = subject
        self.group_lst = group_lst

        if style_path is not None:
            self.style = style_path
            # check style
            if not os.path.exists(style_path):
                self.send_message(f"Styling {style_path} does not exist")

        # check layer
        if not self.valid:
            self.send_message(f"Layer {layer_name} of {source_path} not valid")

    @property
    def name(self):
        return self.layer.name()

    @name.setter
    def name(self, value):
        self.layer.setLayerName(value)

    @property
    def style(self):
        return self._style

    @style.setter
    def style(self, path):
        self.layer.loadNamedStyle(path)
        self._style = path

    @property
    def valid(self):
        return self.layer.isValid()

    @property
    def source(self):
        return self.layer

    def send_message(self, message, level=1, duration=5):
        print(self.subject, message)
        iface.messageBar().pushMessage(
            self.subject, message, level=level, duration=duration
        )

    def get_type(self, file_name):
        if ".shp" in file_name:
            return "vector"
        if ".gdb" in file_name:
            return "vector"
        if ".tif" in file_name:
            return "raster"


class Project:
    """
    Object used as interface to a qgis project

    Recommended code for adding layers:

    project = Project()
    structure = {"test": ["g1", "g2", "g3"]}
    for group_name, layer_list in structure.items():
        layers = []
        for layer_name in layer_list:
            layers.append(
            Layer(f"{layer_name}.shp",
                  layer_name,
                  "{layer_name}.qml",
                  "vector")
        project.add_layers(layers, group_name, reverse=False)

    Note that all group names should be unique.
    It is best to add all groups and subgroups first, before adding the layers.


    """

    def __init__(self, df_path=None, subjects=None, revisions={'0d1d_test':'','1d2d_test':'','klimaatsommen':''}):
        self.instance = QgsProject.instance()
        self.root = self.instance.layerTreeRoot()
        self.mapthemecollection = self.instance.mapThemeCollection()
        self.layoutmanager = self.instance.layoutManager()
        self.df_path = df_path
        self.subjects = subjects
        self.revisions=revisions
        

        if df_path is not None:
            self.df_full = pd.read_csv(self.df_path, sep=';') #Read csv from file with configuration for the available layers.
            if subjects is not None:
                self.df = self.df_full[self.df_full['subject'].isin(self.subjects)] #Filter on selected subjects.
            else: 
                self.df = self.df_full
        

    def __iter__(self):
        for i in self.root.children():
            yield i


    def get_group_lsts_from_df(self, df, filter=None) -> list:
        """List of group lists in dataframe. df is an input because for generating themes self.df_full is used."""
        # group_structure_lst = self.df[['parent_group','child_group']].stack().groupby(level=0).apply(list).tolist()
        # return list(k for k,_ in itertools.groupby(group_structure_lst))
        
        def local_eval(row):
            """apply(eval) doesnt work, it doesnt recognise revisions unless specified in same function"""
            revisions = self.revisions #required for eval

            return eval(row)

        group_lsts = df['group_lst'].apply(local_eval) 
        if filter is None:
            return group_lsts.to_list()
        else:
            return group_lsts[filter].to_list()


    @property
    def theme_structure(self):
        structure = {}
        for theme in self.theme_names:
            layers = self.get_theme_layers(theme)
            structure[theme] = layers
        return structure

    @property
    def group_list(self):
        return [i for i in self if isinstance(i, QgsLayerTreeGroup)]

    @property
    def group_names(self):
        return [i.name() for i in self.group_list]

    @property
    def layer_list(self):
        layer_list = []
        for k, layer in self.instance.mapLayers().items():
            layer_list.append(layer)
        return layer_list

    @property
    def theme_names(self):
        return self.instance.mapThemeCollection().mapThemes()

    @property
    def mapcanvas_extent(self):
        return iface.mapCanvas().extent()


    # @staticmethod
    def get_layer_information_from_row(self, row, folder, HHNK_THREEDI_PLUGIN_DIR):
        """retrieve all information to construct a layer from a row in the dataframe.
        folder, HHNK_THREEDI_PLUGIN_DIR and revisiosn are needed for the eval functions.
        """

        filetype = row.filetype
        revisions = self.revisions #required for eval in row.filedir and row.group_lst, has the keys: 0d1d_test, 1d2d_test and klimaatsommen

        #Voor wms staat de volledige link die nodig is in row.wms_source.
        if filetype in ['arcgismapserver', 'arcgisfeatureserver', 'wms']:
            full_path = row.wms_source
        else:
            # try:
            filedir = self.filedir_with_revision(row.filedir)
            full_path = os.path.join(eval(str(filedir)), row.filename)
            print(full_path)
            if not pd.isna(row.filters):
                full_path = f"{full_path}|{row.filters}"

            # except Exception as e:
            #     print(f'Could not evaluate {row.filedir}')
            #     logger.warning(f'Could not evaluate {row.filedir}')
            #     full_path=None


        layer_name = row.qgis_name

        if not pd.isna(row.qmldir) and not pd.isna(row.qmlname):
            qml_path = os.path.join(eval(row.qmldir), row.qmlname)
        else:
            qml_path = None
        print("qml_path", qml_path)

        subject = row.subject

        group_lst=eval(row.group_lst)

        return full_path, layer_name, filetype, qml_path, subject, group_lst


    def get_group(self, group_lst):
        """find group recursively"""
        group = self.root
        for group_name in group_lst:
            group = group.findGroup(group_name)
            if group is None:
                logging.warning(f'{group_name} not found')
                return None
        return group


    def get_theme(self, theme_name):
        return self.mapthemecollection.mapThemeState(theme_name)

    def get_theme_layers(self, theme_name):
        theme = self.get_theme(theme_name)

        names = []
        for record in theme.layerRecords():
            names.append(record.layer().name())
        return names

    def get_layout(self, layout_name):
        return self.layoutmanager.layoutByName(layout_name)


    def add_layers(self, layers, group_lst=None, reverse=False):
        if reverse:
            layers.reversed()

        for layer in layers:
            self.add_layer(layer, group_lst)


    def get_layer(self, layer_name, group_lst=[], layertreelayer=False):
        """Return layer in whole project, or only the layer in the given group.
        When group_lst is empty it will search for the layer in the whole project.
        It is currently not possible to search for layers only in the root. 
        When layertreelayer == True, return that object instead of the QgsVectorLayer.
        This object is needed when toggeling visibility in the layer tree"""
        group=None
        if group_lst:
            group = self.get_group(group_lst)
            if group:
                #.layer returns QgsVectorLayer instead of QgsLayerTreeLayer
                layer = [child.layer() for child in group.children() if child.name()==layer_name] 
            else: 
                logging.error(f'group: {group_lst} does not exist')
                return None
        else:
            layer = self.instance.mapLayersByName(layer_name)


        if len(layer)==0:
            return None
        elif not layertreelayer:
            return layer[0]
        elif layertreelayer:
            if group:
                return group.findLayer(layer[0].id())
            else:
                return self.root.findLayer(layer[0].id())


    def add_layer(self, layer: Layer, group_lst=None, visible=False):
        """Appends a layer to a group, creates a group if not exist"""

        self.instance.addMapLayer(layer.source, False)
        if group_lst:
            group = self.add_group(group_lst)
            q_layer=group.addLayer(layer.source)
        else:
            q_layer=self.root.addLayer(layer.source)

        #Set visibility (defaults to off)
        q_layer.setItemVisibilityChecked(visible)
        q_layer.setExpanded(False)


    def set_visibility(self, layer_name, group_lst, visible):
        """Find layer in layertree and set visibility"""
        layer = self.get_layer(layer_name=layer_name, group_lst=group_lst, layertreelayer=True)
        if layer:
            layer.setItemVisibilityChecked(visible)


    def set_expanded(self, layer_name, group_lst, expanded=False):
        """Collapse layers in the layer tree"""
        layer = self.get_layer(layer_name=layer_name, group_lst=group_lst, layertreelayer=True)
        if layer:
            layer.setExpanded(expanded)


    def remove_layer(self, layer_name, group_lst=None):
        """Remove layer, from group if defined."""
        layer = self.get_layer(layer_name=layer_name, group_lst=group_lst)
        if layer:
            self.instance.removeMapLayer(layer.id())


    def _group_index(self, group_name) -> int: #TODO deprecated? fix group_structure?
        """locates the nearest index based on the layer above
        if we cannot find this, we place it on top
        """
        # use a while loop to get the nearest adjacent group
        structure_index = self.group_structure.index(group_name)
        group_names = self.group_names

        index = None
        while structure_index > 0 and index is None:
            group_name_above = self.group_structure[structure_index - 1]
            if group_name_above in group_names:
                index = group_names.index(group_name_above) + 1
            else:
                structure_index = structure_index - 1

        if structure_index == 0:
            index = 0

        return index


    def add_group(self, group_lst: list, index=-1) -> QgsLayerTreeGroup:
        """creates a group and appends the group to the root in the right order
        return an existing group if already exists
        """
        group = self.get_group(group_lst)
        if group is not None:
            return group

        # if index is None: #FIXME Disabled this for now until _group_index works again
        #     index = self._group_index(group_lst[0])

        parent_found=0 #If no parent the whole group_lst should be created
        for i in range(len(group_lst),0,-1):
            # print(group_lst[:i])
            group = self.get_group(group_lst[:i])
            if group:
                # print(f'group {group.name()} found')
                parent_found=1 #group exists, now lets makee the children that didnt exist.
                break

        #Continue loop where broken to start building the groups
        if group is None:
            group = self.root

        for j in range(i-1+parent_found, len(group_lst)): #some magic with index required to create the correct group.
            group = group.insertGroup(index, group_lst[j])
            group.setItemVisibilityChecked(False)
            group.setExpanded(False)
            # print(f'create {group_lst[j]}')
        return group



# %%

    # def add_subgroup(self, group_name, parent_group_name):
    #     """adds a group under a group"""
    #     if pd.isna(group_name):
    #         logger.error('Tried to create subgroup but value isnan.')
    #         return None

    #     parent_group = self.get_group(parent_group_name)
    #     if parent_group is None:
    #         parent_group = self.add_group(parent_group_name)

    #     group = self.get_group(group_name)
    #     if group is not None:
    #         return group

    #     group = parent_group.addGroup(group_name)
    #     group.setExpanded(False)
    #     return group


    def add_theme(self, theme_name, layer_names, group_lsts):
        """theme name is the name of the theme and
        layer names is the name of the layer which is visible
        if layer does not exists it get skipped
        """

        collection = self.instance.mapThemeCollection()
        theme = collection.mapThemeState(theme_name)

        records = []
        for layer_name, group_lst in zip(layer_names, group_lsts):
            print(layer_name, group_lst)
            layer = self.get_layer(layer_name=layer_name, group_lst=group_lst)
            print(layer)
            if layer:
                records.append(QgsMapThemeCollection.MapThemeLayerRecord(layer))

        theme.setLayerRecords(records)
        collection.insert(theme_name, theme)


    def add_print_layout_template(self, template_path, name):
        layout = self.get_layout(name)
        if layout is not None:
            self.send_message(f"Layout {name} already exists, replacing!")

        layout = QgsPrintLayout(self.instance)
        with open(template_path) as f:
            template_content = f.read()
        doc = QDomDocument()
        doc.setContent(template_content)

        # adding to existing items
        items, ok = layout.loadFromTemplate(doc, QgsReadWriteContext(), True)
        print("items", items, "ok", ok)
        layout.setName(name)
        self.instance.layoutManager().addLayout(layout)


    def generate_themes(self, revision=None):
        """Generate themes based on all columns in the dataframe that start with 'theme_'"""
        theme_col_names = [i for i in self.df_full.keys() if i.startswith('theme_')]

        for theme_col_name in theme_col_names:
            layer_names = self.df_full.loc[self.df_full[theme_col_name]==True, 'qgis_name'].tolist()
            group_lsts = self.get_group_lsts_from_df(df=self.df_full, filter=self.df_full[theme_col_name]==True)
            theme_name = theme_col_name[6:] #remove str theme_

            #TODO - Super ugly quick fix for adding the background and adding revisions
            
            # don't forget the background
            layer_names.extend(["Luchtfoto actueel (PDOK)"])
            group_lsts.extend([["Achtergrond"]])
            
            for i in range(0, len(group_lsts)):
                group_lsts[i][0] = group_lsts[i][0].replace("Klimaatsommen []", f"Klimaatsommen [{self.revisions['klimaatsommen']}]")
            
            # and dont for
            print(theme_name, layer_names, group_lsts)
            self.add_theme(theme_name, layer_names, group_lsts=group_lsts)


    def generate_groups(self, group_index=-1):
        """generates all groups and subgroups based on self.structure"""
        for group_lst in self.get_group_lsts_from_df(df=self.df):
            self.add_group(group_lst=group_lst, index=group_index)


    def write_styling(self, path):
        for layer in self.layer_list:
            name = layer.name()
            name = self.standardize_name(name)
            layer.saveNamedStyle(f"{path}/{name}.qml")
            layer.saveSldStyle(f"{path}/{name}.sld")


    def standardize_name(self, name):
        """names are edited spaces become _ and are : removed, lowered"""
        return name.replace(" ", "_").replace(":", "").lower()


    def send_message(self, message, level=1, duration=5):
        self.subject="" #FIXME self.subject was replaced by self.subjects
        # print(self.subject, message)
        iface.messageBar().pushMessage(
            self.subject, message, level=level, duration=duration
        )
        
    
    def zoom_to_layer(self, layer_name, group_lst=[]):

        layer = self.get_layer(layer_name=layer_name, group_lst=group_lst)
        if layer is None:
            print("Layer unvalid not setting extent")
            return
            
        canvas = iface.mapCanvas()
        extent = layer.extent()
        print("Setting extent to", extent)
        print("Canvas", canvas)
        canvas.setExtent(extent)
        canvas.setExtent(extent)

    def filedir_with_revision(self, filedir):
        if "one_d_two_d" in filedir:
            return filedir.replace("revision", f"'{self.revisions['1d2d_test']}'")
        elif "zero_d_one_d" in filedir:
            return filedir.replace("revision", f"'{self.revisions['0d1d_test']}'")
        else:
            return filedir
    # def iter_parent(self, parent_group):
    #     """iter over a single parent in the df. """
    #     df_parent = self.df.query(f"parent_group=='{parent_group}'")
    #     for index, row in df_parent.iterrows():
    #         yield index, row


    # def iterrows(self):
    #     """Iter over the whole df"""
    #     for group_lst in self.get_group_lsts:
    #         for index, row in self.iter_parent(group_lst[0]):
    #             yield index, row
            

# project = Project(df_path=r"C:\Users\chris.kerklaan\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\hhnk_threedi_plugin\qgis_interaction\layer_structure/klimaatsommen.csv")
# project.generate_themes()
