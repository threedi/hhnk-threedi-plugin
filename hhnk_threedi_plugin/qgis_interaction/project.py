# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 09:17:26 2021

@author: chris.kerklaan

#TODO:
    1. Let groups be unique
    2. Add printcomposers
    
"""
import os
from qgis.utils import iface
from qgis.core import (
    QgsProject,
    QgsVectorLayer,
    QgsRasterLayer,
    QgsLayerTreeGroup,
    QgsMapThemeCollection,
)

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
        type: str=None,
        style_path=None,
        subject="HTT",
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

        self.subject = subject

        if style_path is not None:
            self.style = style_path
            # check style
            if not os.path.exists(style_path):
                self.send_message(f"Styling {style_path} does not exist")

        # check layer
        if not self.valid:
            self.send_message(f"Layer {layer_name}  of {source_path} not valid")

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

    def __init__(self, structure={}, subject="HTT"):
        self.instance = QgsProject.instance()
        self.root = self.instance.layerTreeRoot()
        self.mapthemecollection = self.instance.mapThemeCollection()
        self.structure = structure
        self.subject = subject

    def __iter__(self):
        for i in self.root.children():
            yield i

    @property
    def group_structure(self):
        return list(self.structure.keys())

    @property
    def subgroup_structure(self):
        subgroups = []
        for group in self.group_structure:
            if type(self.structure[group]) is dict:
                subs = list(self.structure[group].keys())
                for sub in subs:
                    subgroups.append((sub, group))
        return subgroups
    
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

    def get_group(self, group_name):
        return self.root.findGroup(group_name)

    def get_layer(self, layer_name):
        layer = self.instance.mapLayersByName(layer_name)
        if len(layer) == 0:
            return None
        else:
            return layer[0]
    
    def get_theme(self, theme_name):
        return self.mapthemecollection.mapThemeState(theme_name)        
    
    def get_theme_layers(self, theme_name):
        theme = self.get_theme(theme_name)
        
        names = []
        for record in theme.layerRecords():
            names.append(record.layer().name())
        return names

    def add_layers(self, layers, group_name=None, reverse=False):
        if reverse:
            layers.reversed()

        for layer in layers:
            self.add_layer(layer, group_name)

    def add_layer(self, layer: Layer, group_name=None):
        """Appends a layer to a group, creates a group if not exist"""

        self.instance.addMapLayer(layer.source, False)
        if group_name:
            group = self.add_group(group_name)
            group.addLayer(layer.source)
        else:
            self.root.addLayer(layer.source)

    def add_group(self, group_name):
        """creates a group and appends the group to the root in the right order
            return an existing group if already exists
        """
        group = self.get_group(group_name)
        if group is not None:
            return group

        group = self.root.insertGroup(self.group_index(group_name), group_name)
        group.setExpanded(False)
        return group
    
    def add_subgroup(self, group_name, parent_group_name):
        """ adds a group under a group"""
        parent_group = self.get_group(parent_group_name)
        if parent_group is None:
            parent_group = self.add_group(parent_group_name)
        
        group = self.get_group(group_name)
        if group is not None:
            return group
        
        group = parent_group.addGroup(group_name)
        group.setExpanded(False)
        return group

    def add_theme(self, theme_name, layer_names):
        """theme name is the name of the theme and
        layer names is the name of the layer which is visible
        if layer does not exists it get skipped
        """

        collection = self.instance.mapThemeCollection()
        theme = collection.mapThemeState(theme_name)

        records = []
        for layer_name in layer_names:
            layer = self.get_layer(layer_name)
            if layer:
                records.append(QgsMapThemeCollection.MapThemeLayerRecord(layer))

        theme.setLayerRecords(records)
        collection.insert(theme_name, theme)
        

    def generate_groups(self):
        """ generates all groups and subgroups based on self.structure"""
        for group in self.group_structure:
            self.add_group(group)
        
        for subgroup in self.subgroup_structure:
            self.add_subgroup(*subgroup)
            

    def group_index(self, group_name):
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

    def write_styling(self, path):
        for layer in self.layer_list:
            name = layer.name()
            name = self.standardize(name)
            layer.saveNamedStyle(f"{path}/{name}.qml")
            layer.saveSldStyle(f"{path}/{name}.sld")

    def standardize(self, name):
        """names are edited spaces become _ and are : removed, lowered"""
        return name.replace(" ", "_").replace(":", "").lower()

    def send_message(self, message, level=1, duration=5):
        print(self.subject, message)
        iface.messageBar().pushMessage(
            self.subject, message, level=level, duration=duration
        )


def send_message(message, subject, level=1, duration=5):
    print(subject, message)
    iface.messageBar().pushMessage(subject, message, level=level, duration=duration)


# print("doe iets")

STRUCTURE = {
    "Opmerkingen": [("opmerkingen.shp", "Opmerkingen")],
    # Group                 # Subgroup                    # Layer names
    "Datachecker output": {
        "Kunstwerken niet in model": [
            ("datachecker_output.gdb|layername=channel_loose", "Watergang: channel loose"),
            ("datachecker_output.gdb|layername=channel_nowayout", "Watergang: channel nowayout"),
            ("datachecker_output.gdb|layername=culvert|subset='isusable' = '0'", "Duikers niet in model"),
            ("datachecker_output.gdb|layername=weirs|subset='isusable' = '0'","Stuwen niet in model"),
            ("datachecker_output.gdb|layername=bridge|subset='isusable' = '0'", "Bruggen niet in model"),
            ("datachecker_output.gdb|layername=fixed_dam|subset='isusable' = '0'", "Vaste dammen niet in model"),
            ("datachecker_output.gdb|layername=pumpstation|subset='isusable' = '0'", "Gemaal niet in model"),
            ("datachecker_output.gdb|layername=kruising_zonder_kunstwerk", "KZK"),
            ("datachecker_output.gdb|layername=crosssection|subset='isusable' = '0'", "Gemeten niet in model"),
        ],
        "Kunstwerken met aannames": [
            ("datachecker_output.gdb|layername=culvert|subset='aanname' LIKE ('%width,width%')", "Duiker aanname: doorstroomafmeting"),
            ("datachecker_output.gdb|layername=culvert|subset='aanname' LIKE ('%bed_level_up%')", "Duiker aanname: bob"),
            ("datachecker_output.gdb|layername=levee", "Levee: 30 cm boven max peil"),
            ("datachecker_output.gdb|layername=weirs|subset='aanname' LIKE ('%crest_width%')", "Stuw aanname: breedte"),
            ("datachecker_output.gdb|layername=fixeddrainagelevelarea|subset='streefpeil_bwn2' = -10", "Peilgebied aanname: streefpeil"),
        ],
        "Kunstwerken": [
            ("datachecker_output.gdb|layername=channel", "datachecker_output channel"),
            ("datachecker_output.gdb|layername=weirs|subset='isusable' = '1'", "Stuwen wel in model"),
            ("datachecker_output.gdb|layername=culvert|subset='isusable' = '1'", "Duikers wel in model"),
            ("datachecker_output.gdb|layername=bridge|subset='isusable' = '1'", "Bruggen wel in model"),
            ("datachecker_output.gdb|layername=fixed_dam|subset='isusable' = '1'", "Vaste dammen wel in model"),
            ("datachecker_output.gdb|layername=pumpstation|subset='isusable' = '1'","Gemaal wel in model"),
        ],
    },
}
# project = Project(STRUCTURE)
# project.generate_groups()
# print(project.subgroup_structure)

# import os
# os.chdir(r"C:\Users\chris.kerklaan\Documents\test2")
# layer1 = Layer("geometry1.shp", "g1", "geometry1.qml" , "vector")
# layer2 = Layer("geometry2.shp", "g2", "geometry2.qml" , "vector")
# layer3 = Layer("geometry3.shp", "g3", "geometry2.qml" , "vector")

# project=  Project()
# for group, layer_list in NEW_STRUCTURE.items():
#     for layer_name in layer_list:
#         if layer_name == "g1":
#             layer = layer1
#         elif layer_name == "g2":
#             layer = layer2
#         elif layer_name == "g3":
#             layer = layer3
#         print(layer_name)

#         project.add_layer(layer, group)

# project.add_layer(layer2, "yolo")
# project.add_layer(layer3, "test")

# project.add_layer(layer3, "eerste")

# project.add_layer(layer3, "derde")

# project.add_layer(layer3, "vierde")

# project.add_theme("gones", ["g1"])

# project.write_styling(r"C:\Users\chris.kerklaan\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\hhnk_threedi_plugin\qgis_layer_styles\klimaatsommen")
