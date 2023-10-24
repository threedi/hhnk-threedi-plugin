# %%
# # -*- coding: utf-8 -*-
"""
#TODO:
    2. Add printcomposers
    
"""
import os
from qgis.utils import iface
from qgis.core import (
    QgsProject,
    QgsVectorLayer,
    QgsRasterLayer,
    QgsLayerTreeGroup,
    QgsLayerTreeLayer,
    QgsMapThemeCollection,
    QgsPrintLayout,
    QgsReadWriteContext,
    QgsMapLayerStyle,
)
# %%
from qgis.PyQt.QtXml import QDomDocument
import pandas as pd
import numpy as np
import logging
import hhnk_threedi_tools as htt
from hhnk_threedi_tools.qgis import layer_structure

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



class QgisLayer():
    """class used for multiple qgis layer:
    QgsVectorLayer
    QgsRasterLayer
    """
    def __init__(self,
        settings:htt.qgis.QgisLayerSettings,
    ):
        """
        Parameters
        ----------
        settings : htt.qgis.QgisLayerSettings
            
        layer_name : str
            name of layer
        style_path : str
            poth to style
        type : str
            can be 'wms', 'vector' or 'raster'

        """

        self.settings = settings
        self.instance = QgsProject.instance()
        self.layer = None

    def get_qgis_layer(self):
        """
        create a qgis layer instance based on settings.

        Do not make this an attribute of QgisLayer! When removing the layer 
        the id will remain the same and weird errors will occur. 
        """
        if  self.settings.ftype in ["ogr", "arcgisfeatureserver"]:
            return QgsVectorLayer(self.settings.source, self.settings.name, self.settings.ftype)
        elif self.settings.ftype in ["gdal", "wms", "arcgismapserver"]:
            return QgsRasterLayer(self.settings.source, self.settings.name, self.settings.ftype)
        else:
            logger.error(f"Layer {self.settings.name} has unknown ftype: {self.settings.ftype}")


    @property
    def name(self):
        return self.settings.name
    @property
    def id(self):
        return self.settings.id
    # @name.setter
    # def name(self, value):
    #     self.layer.setLayerName(value)
    # @property
    # def source(self):
    #     return self.layer

    # @property
    # def style(self):
    #     return self._style

    # @style.setter
    # def style(self, path):
    #     self.layer.loadNamedStyle(path)
    #     self._style = path
    def add_styles(self):
        """
        Add styles to layer in project. Can add multiple styles.
        """
        style = QgsMapLayerStyle()
        style.readFromLayer(self.layer) #doesnt seem to work.
        style_manager = self.layer.styleManager()

        for qml_path in self.settings.qml_lst:
            if "__" in qml_path.base:
                style_name = qml_path.stem.split("__")[-1]
            else:
                style_name = "default"

            style_manager.addStyle(style_name, style)
            style_manager.setCurrentStyle(style_name)

            # load qml to current style
            (message, success) = self.layer.loadNamedStyle(qml_path.base)
            if not success:  # if style not loaded remove it
                print(message)
                style_manager.removeStyle(style_name)

        style_manager.setCurrentStyle("default")


    def add_to_project(self, qgis_group, reload=True):
        """
        qgis_group (QgisGroup)
        """
        qgis_layer = self.get_qgis_layer() #dont set this as attribute. id must change when its removed.
        if self.isValid(qgis_layer):
            #Find index of layer in avalailable layers in group
            # print(self.id)
            layer_keys = [l.layerId() for l in qgis_group.layer_list if self.name == l.name()]
            if layer_keys:
                #Break loop if no reload required
                if not reload:
                    pass
                #remove all layers with name in group.
                else:
                    try:
                        # for l in layer_keys:
                        # Note that using removeMapLayers does not work because the 
                        # group has ownership of the layer. See addLayer in;
                        # https://qgis.org/pyqgis/3.2/core/Layer/QgsLayerTreeGroup.html
                        # Therefore we need to remove the child from the group itself.
                        # Correction. using group.addLayer will not work properly 
                        self.instance.removeMapLayers(layer_keys)
#                        for l in layer_keys:
#                            qgis_group.layertreegroup.removeChildNode(l)
#                            print(l)
                    except:
                        print(f"Could not remove {self.id} from project")
                        raise
                            
            #We also need to add the layer to the instance, otherwise the group
            #gets ownership over the layer, which will break some other things with
            #styling and removing the layer.
            self.instance.addMapLayer(qgis_layer, False)
            self.layertreelayer = qgis_group.layertreegroup.addLayer(qgis_layer) # returns QgsLayerTreeLayer.
            #We need the QgsMapLayer for styles so we access that here.
            self.layer = self.layertreelayer.layer()
            self.add_styles()

            #Set visibility (defaults to off)
            self.layertreelayer.setItemVisibilityChecked(False)
            self.layertreelayer.setExpanded(False)



    def isValid(self, qgis_layer) -> bool:
        valid = True
        for qml_path in self.settings.qml_lst:
            if not qml_path.exists():
                valid=False
                #TODO add logger.warnings
                print(f"Styling {qml_path} does not exist")

        # check layer
        try:
            valid = qgis_layer.isValid()
        except:
            valid=False
            print(f"Layer {self.id} not valid. Please check data-source: {self.settings.file}")
        return valid


    def send_message(self, message, level=1, duration=5):
        """Send message to qgis messagebar."""
        print(self.subject, message)
        iface.messageBar().pushMessage(
            self.subject, message, level=level, duration=duration
        )



    def get_group(self):
        """find group recursively"""
        group = self.instance.layerTreeRoot()
        for group_name in self.settings.group_lst:
            group = group.findGroup(group_name)
            if group is None:
                return None
        return group
    

    def get_layer(self, layertreelayer=False):
        """Return layer in whole project, or only the layer in the given group.
        When group_lst is empty it will search for the layer in the whole project.
        It is currently not possible to search for layers only in the root. 
        When layertreelayer == True, return that object instead of the QgsVectorLayer.
        This object is needed when toggeling visibility in the layer tree"""
        group=None
        if self.settings.group_lst:
            group = self.get_group()
            if group:
                #.layer() returns QgsVectorLayer instead of QgsLayerTreeLayer
                layer = [child.layer() for child in group.children() if child.name()==self.name] 
            else: 
                return None
        else:
            layer = self.instance.mapLayersByName(self.name)


        if len(layer)==0:
            return None
        elif not layertreelayer:
            return layer[0]
        else:
            raise NotImplementedError

# class Project:
#     """
#     Object used as interface to a qgis project

#     Recommended code for adding layers:

#     project = Project()
#     structure = {"test": ["g1", "g2", "g3"]}
#     for group_name, layer_list in structure.items():
#         layers = []
#         for layer_name in layer_list:
#             layers.append(
#             Layer(f"{layer_name}.shp",
#                   layer_name,
#                   "{layer_name}.qml",
#                   "vector")
#         project.add_layers(layers, group_name, reverse=False)

#     Note that all group names should be unique.
#     It is best to add all groups and subgroups first, before adding the layers.


#     """

#     def __init__(self, df_path=None, subjects=None, revisions={'0d1d_test':'','1d2d_test':'','klimaatsommen':''}):
#         self.instance = QgsProject.instance()
#         self.root = self.instance.layerTreeRoot()
#         self.mapthemecollection = self.instance.mapThemeCollection()
#         self.layoutmanager = self.instance.layoutManager()
#         self.df_path = df_path
#         self.subjects = subjects
#         self.revisions=revisions



#         revisions = layer_structure.SelectedRevisions(check_0d1d="callantsoog #23 0d1d_test")


#         #Generate structure
#         layer_struct = layer_structure.LayerStructure(layer_structure_path=LAYER_STRUCTURE_PATH,
#                                             subjects=['test_0d1d'],
#                                             revisions=revisions,
#                                             folder=folder)
#         layer_struct.run()







#     def __iter__(self):
#         for i in self.root.children():
#             yield i


#     # def get_group_lsts_from_df(self, df, filter=None) -> list:
#     #     """List of group lists in dataframe. df is an input because for generating themes self.df_full is used."""
#     #     # group_structure_lst = self.df[['parent_group','child_group']].stack().groupby(level=0).apply(list).tolist()
#     #     # return list(k for k,_ in itertools.groupby(group_structure_lst))
        
#     #     def local_eval(row):
#     #         """apply(eval) doesnt work, it doesnt recognise revisions unless specified in same function"""
#     #         revisions = self.revisions #required for eval

#     #         return eval(row)

#     #     group_lsts = df['group_lst'].apply(local_eval) 
#     #     if filter is None:
#     #         return group_lsts.to_list()
#     #     else:
#     #         return group_lsts[filter].to_list()



#     @property
#     def layer_list(self):
#         layer_list = []
#         for k, layer in self.instance.mapLayers().items():
#             layer_list.append(layer)
#         return layer_list


#     @property
#     def mapcanvas_extent(self):
#         return iface.mapCanvas().extent()






#     def add_layers(self, layers, group_lst=None, reverse=False):
#         if reverse:
#             layers.reversed()

#         for layer in layers:
#             self.add_layer(layer, group_lst)


#     def get_layer(self, layer_name, group_lst=[], layertreelayer=False):
#         """Return layer in whole project, or only the layer in the given group.
#         When group_lst is empty it will search for the layer in the whole project.
#         It is currently not possible to search for layers only in the root. 
#         When layertreelayer == True, return that object instead of the QgsVectorLayer.
#         This object is needed when toggeling visibility in the layer tree"""
#         group=None
#         if group_lst:
#             group = self.get_group(group_lst)
#             if group:
#                 #.layer returns QgsVectorLayer instead of QgsLayerTreeLayer
#                 layer = [child.layer() for child in group.children() if child.name()==layer_name] 
#             else: 
#                 logging.error(f'group: {group_lst} does not exist')
#                 return None
#         else:
#             layer = self.instance.mapLayersByName(layer_name)


#         if len(layer)==0:
#             return None
#         elif not layertreelayer:
#             return layer[0]
#         elif layertreelayer:
#             if group:
#                 return group.findLayer(layer[0].id())
#             else:
#                 return self.root.findLayer(layer[0].id())


#     def add_layer(self, layer: QgisLayer, group_lst=None, visible=False):
#         """Appends a layer to a group, creates a group if not exist"""

#         self.instance.addMapLayer(layer.source, False)
#         if group_lst:
#             group = self.add_group(group_lst)
#             q_layer=group.addLayer(layer.source)
#         else:
#             q_layer=self.root.addLayer(layer.source)

#         #Set visibility (defaults to off)
#         q_layer.setItemVisibilityChecked(visible)
#         q_layer.setExpanded(False)


#     def set_visibility(self, layer_name, group_lst, visible):
#         """Find layer in layertree and set visibility"""
#         layer = self.get_layer(layer_name=layer_name, group_lst=group_lst, layertreelayer=True)
#         if layer:
#             layer.setItemVisibilityChecked(visible)


#     def set_expanded(self, layer_name, group_lst, expanded=False):
#         """Collapse layers in the layer tree"""
#         layer = self.get_layer(layer_name=layer_name, group_lst=group_lst, layertreelayer=True)
#         if layer:
#             layer.setExpanded(expanded)


#     def remove_layer(self, layer_name, group_lst=None):
#         """Remove layer, from group if defined."""
#         layer = self.get_layer(layer_name=layer_name, group_lst=group_lst)
#         if layer:
#             self.instance.removeMapLayer(layer.id())


#     def write_styling(self, path):
#         for layer in self.layer_list:
#             name = layer.name()
#             name = self.standardize_name(name)
#             layer.saveNamedStyle(f"{path}/{name}.qml")
#             layer.saveSldStyle(f"{path}/{name}.sld")


#     def standardize_name(self, name):
#         """names are edited spaces become _ and are : removed, lowered"""
#         return name.replace(" ", "_").replace(":", "").lower()


#     def send_message(self, message, level=1, duration=5):
#         self.subject="" #FIXME self.subject was replaced by self.subjects
#         # print(self.subject, message)
#         iface.messageBar().pushMessage(
#             self.subject, message, level=level, duration=duration
#         )
        
    
#     def zoom_to_layer(self, layer_name, group_lst=[]):

#         layer = self.get_layer(layer_name=layer_name, group_lst=group_lst)
#         if layer is None:
#             print("Layer unvalid not setting extent")
#             return
            
#         canvas = iface.mapCanvas()
#         extent = layer.extent()
#         print("Setting extent to", extent)
#         print("Canvas", canvas)
#         canvas.setExtent(extent)
#         canvas.setExtent(extent)


#     #FIXME in htt
#     def filedir_with_revision(self, filedir):
#         if "one_d_two_d" in filedir:
#             return filedir.replace("revision", f"'{self.revisions['1d2d_test']}'")
#         elif "zero_d_one_d" in filedir:
#             return filedir.replace("revision", f"'{self.revisions['0d1d_test']}'")
#         else:
#             return filedir
        

#     # def iter_parent(self, parent_group):
#     #     """iter over a single parent in the df. """
#     #     df_parent = self.df.query(f"parent_group=='{parent_group}'")
#     #     for index, row in df_parent.iterrows():
#     #         yield index, row


#     # def iterrows(self):
#     #     """Iter over the whole df"""
#     #     for group_lst in self.get_group_lsts:
#     #         for index, row in self.iter_parent(group_lst[0]):
#     #             yield index, row
            

class QgisAllThemes():

# project = Project(df_path=r"C:\Users\chris.kerklaan\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\hhnk_threedi_plugin\qgis_interaction\layer_structure/klimaatsommen.csv")
# project.generate_themes()

    def __init__(self) -> None:
        self.instance = QgsProject.instance()
        self.mapthemecollection = self.instance.mapThemeCollection()        


    @property
    def theme_structure(self):
        structure = {}
        for theme in self.theme_names:
            layers = self.get_theme_layers(theme)
            structure[theme] = layers
        return structure
    

    @property
    def theme_names(self):
        return self.instance.mapThemeCollection().mapThemes()


    def get_theme(self, theme_name):
        return self.mapthemecollection.mapThemeState(theme_name)


    def get_theme_layers(self, theme_name):
        theme = self.get_theme(theme_name)

        names = []
        for record in theme.layerRecords():
            names.append(record.layer().name())
        return names
    

    def add_theme(self, theme_settings, layers, verbose=False):
        """
        theme_settings (htt.qgis.QgisThemeSettings): class with name and layerids
        layers (pd.Series): series with QgisLayer entries. 
        """
        if verbose:
            print(f"Creating theme: {theme_settings.name}")
            
        theme = self.mapthemecollection.mapThemeState(theme_settings.name)

        records = []

        for layer_id in theme_settings.layer_ids: 
            layer = layers[layer_id]

            #Layer.layer is filled when its loaded in project. If it is already present
            #we will look for it in the tree.
            if layer.layer is None:
                layer.layer = layer.get_layer()

            if layer.layer is not None:
                if verbose:
                    print(f"\t{layer.layer}")
                records.append(QgsMapThemeCollection.MapThemeLayerRecord(layer.layer))
            else:
                if verbose:
                    print(f"\t--- {layer.name} layer not found")

        theme.setLayerRecords(records)
        self.mapthemecollection.insert(theme_settings.name, theme)



# class QgisAllGroups():
#     def __init__(self, settings:htt.qgis.QgisAllGroupsSettings):
#         self.settings=settings
#         self.instance = QgsProject.instance()
#         self.root = self.instance.layerTreeRoot()
#         self.groups = {} #group.id: layertreegroup


#     def create_groups(self):
#         """Create groups recursively. Adds groups to the self.groups dict so we
#         can access those later."""
#         for group in self.settings.groups.get_all_children():

#             #Load parent group layertree
#             if group.parent_id not in self.groups.keys():
#                 self.groups[group.parent_id] = QgisGroup(settings=group,
#                         self.get_layertreegroup(group_lst=group.parent_group_lst),
#                 )
                

#             parent_layertreegroup = self.groups[group.parent_id]
            
#             if parent_layertreegroup is None:
#                 raise Exception(f"{group.id} parent group ({group.parent_id}) not found, but it should always exist.")
            
#             if group.id == "__qgis_main":
#                 continue
            
#             #Get the group and create if doesnt exist.
#             if group.id not in self.groups.keys():
#                 self.groups[group.id] = parent_layertreegroup.findGroup(group.name)
#             layertreegroup = self.groups[group.id] 
            
#             if layertreegroup is None:
#                 layertreegroup = parent_layertreegroup.insertGroup(index=-1, 
#                                                 name=group.name)
#                 layertreegroup.setItemVisibilityChecked(False)
#                 layertreegroup.setExpanded(False)

#             self.groups[group.id] = layertreegroup
                

#     def get_layertreegroup(self, group_lst):
#         """find group recursively. Groups in the root have an empty group_lst"""
#         layertreegroup = self.root
#         for group_name in group_lst:
#             layertreegroup = layertreegroup.findGroup(group_name)
#             if layertreegroup is None:
#                 return None
#         return layertreegroup
    
    

    
class QgisAllGroups():
    def __init__(self, settings:htt.qgis.QgisAllGroupsSettings):
        self.settings=settings
        self.instance = QgsProject.instance()
        self.root = self.instance.layerTreeRoot()
        self.groups = {} #group.id: class QgisGroup
        self.layertreegroups = {} #group.id: layertreegroup


    def create_groups(self):
        """Create groups recursively. Adds groups to the self.groups dict so we
        can access those later."""
        for group_settings in self.settings.groups.get_all_children():

            #Load parent group layertree
            
            if group_settings.parent_id == '':
                self.layertreegroups[group_settings.id] = self.root
            else:
                self.layertreegroups[group_settings.id] = self.groups[group_settings.parent_id].parent_layertreegroup.findGroup(group_settings.parent_name)
                
            if group_settings.id not in self.groups.keys():
                self.groups[group_settings.id] = QgisGroup(settings=group_settings,
                            parent_layertreegroup = self.layertreegroups[group_settings.id],
                    )


class QgisGroup():

    def __init__(self, settings, parent_layertreegroup):
        """
        settings (htt.QgisGroupSettings)
        """
        self.settings = settings
        self.parent_layertreegroup = parent_layertreegroup

        self.layertreegroup = self.get_or_create()

    @property
    def id(self):
        return self.settings.id
    @property
    def name(self):
        return self.settings.name


    def get_or_create(self):
        #Get the group and create if doesnt exist.
        layertreegroup = None
        if self.parent_layertreegroup is not None:
            layertreegroup = self.parent_layertreegroup.findGroup(self.name)
        
        if layertreegroup is None:
            if self.settings.load_group:
                layertreegroup = self.parent_layertreegroup.insertGroup(index=-1, 
                                                name=self.name)
                layertreegroup.setItemVisibilityChecked(False)
                layertreegroup.setExpanded(False)
        return layertreegroup


    # @property
    # def layers(self):
    #     """dict with id:name"""
    #     return {i.layerId():i.name() for i in self.layertreegroup.children() if isinstance(i, QgsLayerTreeLayer)}
    @property
    def layer_list(self):
        #returns the QgsVectorLayer instead of the QgsLayerTreeLayer.
        # QgsLayerTreeLayer is only usable in 
        # return [j for j in [i.layer() for i in self.layertreegroup.findLayers()] if j is not None]
        return [i for i in self.layertreegroup.findLayers()]

    # @property
    # def group_list(self):
    #     return [i for i in self.root.children() if isinstance(i, QgsLayerTreeGroup)]

    # @property
    # def group_names(self):
    #     return [i.name() for i in self.group_list]
    

    # def _group_index(self, group_name) -> int: #TODO deprecated? fix group_structure?
    #     """locates the nearest index based on the layer above
    #     if we cannot find this, we place it on top
    #     """
    #     # use a while loop to get the nearest adjacent group
    #     structure_index = self.group_structure.index(group_name)
    #     group_names = self.group_names

    #     index = None
    #     while structure_index > 0 and index is None:
    #         group_name_above = self.group_structure[structure_index - 1]
    #         if group_name_above in group_names:
    #             index = group_names.index(group_name_above) + 1
    #         else:
    #             structure_index = structure_index - 1

    #     if structure_index == 0:
    #         index = 0

    #     return index

    # def add_group(self, group_lst: list, index=-1) -> QgsLayerTreeGroup:
    #     """creates a group and appends the group to the root in the right order
    #     return an existing group if already exists
    #     """
    #     group = self.get_group(group_lst)
    #     if group is not None:
    #         return group

    #     # if index is None: #FIXME Disabled this for now until _group_index works again
    #     #     index = self._group_index(group_lst[0])

    #     parent_found=0 #If no parent the whole group_lst should be created
    #     for i in range(len(group_lst),0,-1):
    #         # print(group_lst[:i])
    #         group = self.get_group(group_lst[:i])
    #         if group:
    #             # print(f'group {group.name()} found')
    #             parent_found=1 #group exists, now lets makee the children that didnt exist.
    #             break

    #     #Continue loop where broken to start building the groups
    #     if group is None:
    #         group = self.root

    #     for j in range(i-1+parent_found, len(group_lst)): #some magic with index required to create the correct group.
    #         group = group.insertGroup(index, group_lst[j])
    #         group.setItemVisibilityChecked(False)
    #         group.setExpanded(False)
    #         # print(f'create {group_lst[j]}')
    #     return group


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


    # def generate_groups(self, group_index=-1):
    #     """generates all groups and subgroups based on self.structure"""
    #     for group_lst in self.get_group_lsts_from_df(df=self.df):
    #         self.add_group(group_lst=group_lst, index=group_index)



class QgisPrintLayout():

    def __init__(self) -> None:
        self.instance = QgsProject.instance()
        self.layoutmanager = self.instance.layoutManager()
        

    def get_layout(self, layout_name):
        return self.layoutmanager.layoutByName(layout_name)


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



class Project:
    def __init__(self):
        self.structure = None #fill using self.get_structure() or self.run()
        self.groups = None
        self.layers = {}
        self.themes = QgisAllThemes()


    def get_structure(self, layer_structure_path, subjects, revisions, folder):
        self.structure = layer_structure.LayerStructure(layer_structure_path=layer_structure_path,
                                    subjects=subjects,
                                    revisions=revisions,
                                    folder=folder)
        self.structure.run()


    def get_layers(self):
        """get layers from settings."""


    def add_layers(self):
        for layer in self.structure.layers:
            layer = QgisLayer(layer)
            if layer.settings.load_layer:
                layer.add_to_project(qgis_group=self.groups.groups[layer.settings.group_id])
            self.layers[layer.id] = layer


    def add_themes(self, verbose=False):
        """get themes from settings."""
        for theme_settings in self.structure.themes:
            self.themes.add_theme(theme_settings=theme_settings, layers=self.layers, verbose=verbose)


    def run(self, **kwargs):
        # pass
        self.get_structure(**kwargs)
        self.groups = QgisAllGroups(settings=self.structure.groups)

        self.groups.create_groups()
        self.add_layers()
        self.add_themes()


# %%


# self = layer
# reload=True
# qgis_group = p.groups.groups['05. Hydraulische Toets en 0d1d tests[callantsoog #23 0d1d_test]__Kaart 3: Streefpeilhandhaving']
# import numpy as np
# if self.isValid():
#             #Find index of layer in avalailable layers in group
#             group_layers =  qgis_group.layers
#             layer_keys = [l for l in group_layers if self.name in l]
#             if layer_keys:
#                 #Break loop if no reload required
#                 if not reload:
#                     pass
#                 #remove all layers with name in group.
#                 else:
#                     try:
#                         # for l in layer_keys:
#                         # Note that using removeMapLayers does not work because the 
#                         # group has ownership of the layer. See addLayer in;
#                         # https://qgis.org/pyqgis/3.2/core/Layer/QgsLayerTreeGroup.html
#                         # Therefore we need to remove the child from the group itself.
#                         # Correction. using group.addLayer will not work properly 
#                         self.instance.removeMapLayers(layer_keys)
#                         qgis_group.layertreegroup.removeChildNode(l)
#                     except:
#                         print(f"Could not remove {self.id} from project")                     

#             #addlayer returns QgsLayerTreeLayer.
#             self.instance.addMapLayer(self.layer_base, False)
#             layertreelayer = qgis_group.layertreegroup.addLayer(self.layer_base) 
#             #We need the QgsMapLayer for styles so we access that here.
#             self.layer = layertreelayer.layer()
#             self.add_styles()




# for child in qgis_group.layertreegroup.children():
#     if isinstance(child, QgsLayerTreeLayer):
#         print(child)
#         QgsProject.instance().removeMapLayer(child.layerId())
