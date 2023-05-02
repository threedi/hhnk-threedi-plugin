import os
import re
import copy
from .layers.layer_types_definition import VECTOR, VIRTUAL, RASTER
from qgis.core import (
    QgsProject,
    QgsVectorLayer,
    QgsLayerTreeLayer,
    QgsRasterLayer,
    QgsLayerTreeGroup,
    QgsMapThemeCollection,
)
from .groups.group_orders import build_group_order
import re


def update_group_order_list(groups_list, layer_tree):
    # If we are working with the highest level of groups, there may be revision numbers in group names
    # we have to update the groups list (which doesn't know about revision number from previously run
    # tests) to include the full name of the groups. We do this by looking for group names matching the
    # base name (i.e. 05. Hydraulische toets en 0d1d tests) that are in the project. This is only neccessary
    # at the highest level of group names
    groups_in_project = [
        item.name()
        for item in layer_tree.children()
        if isinstance(item, QgsLayerTreeGroup)
    ]
    new_groups_list = []

    def find_partial_in_project(groups_in_project):
        matches = []
        for it in groups_in_project:
            pattern = r"^" + item + r"\s*\[#[0-9]+]"
            if re.match(pattern, it):
                matches.append(it)
        return matches

    for item in groups_list:
        groups_found = find_partial_in_project(groups_in_project)
        if groups_found:
            new_groups_list += groups_found
        else:
            new_groups_list.append(item)
    return new_groups_list


def find_group_index_inner(groups_list, group_name, is_main_group=False):
    """
    Looks up the index of a group based on a list containing the order within its parent. Function finds
    the closest (in index) preceding member of the current groups parent (that is already in the qgis project!)
    and returns that items index + 1. If no preceeding members are found, 0 is returned as the index.
    """
    try:
        found = None
        layer_tree = QgsProject.instance().layerTreeRoot()
        # starting at the index index in the order -1, traverse the order list backward
        # to look for a group that is already part of the project
        if is_main_group:
            groups_list = update_group_order_list(groups_list, layer_tree)
        # Find index of group name in group order list
        group_index = groups_list.index(group_name)
        for i in reversed(range(group_index)):
            found = layer_tree.findGroup(groups_list[i])
            if found is not None:
                # If we find a group that is already in the project, we stop looking
                break
        if found is not None:
            # If a group was found, we look up its index in its respective parent (group or root of project
            # and add 1 to it to get the position to insert the new group at
            for index, child in enumerate(found.parent().children()):
                if child == found:
                    return index + 1
        else:
            # If we didn't find any preceding groups in the project, we just add it as the first group
            return 0
    except Exception as e:
        raise e from None


def find_group_index(group_name, group_structure):
    """
    Certain QGIS layer groups have numbered members (i.e.: Kaart 01 etc) and so do the test layer groups
    (04. Sqlite tesprotocol). In order to preserve the order in which we want them displayed, we check
    whether the group we are adding now is in any of the ordered groups. If so, we look up the appropriate index
    for it. If not, we add it at the zero index.

    Does not handle group name being in multiple group order lists
    """
    try:
        main_group_order, zero_d_group_order, one_d_group_order = build_group_order(
            group_structure
        )
        if group_name in main_group_order:
            index = find_group_index_inner(
                groups_list=main_group_order, group_name=group_name, is_main_group=True
            )
        elif group_name in zero_d_group_order:
            index = find_group_index_inner(
                groups_list=zero_d_group_order, group_name=group_name
            )
        elif group_name in one_d_group_order:
            index = find_group_index_inner(
                groups_list=one_d_group_order, group_name=group_name
            )
        else:
            index = -1
        return index
    except Exception as e:
        raise e from None


def ensure_group(groups, root, group_structure):
    """
    Function takes list of group names, first one has to be top level
    compared to root
    group
        subgroup1
            sub_subgroup
    etc as a list
    """
    try:
        found = False
        if groups:
            for child in root.children():
                if isinstance(child, QgsLayerTreeGroup):
                    # If group exists, go check it's children
                    if child.name() == groups[0]:
                        return ensure_group(groups[1:], child, group_structure)
                        found = True
            if found == False:
                try:
                    index = find_group_index(groups[0], group_structure)
                    group = root.insertGroup(index, groups[0])
                    # When we create a group, set it to collapsed
                    group.setExpanded(False)
                except Exception as e:
                    raise e from None
                return ensure_group(groups[1:], group, group_structure)
        else:
            return root
    except Exception as e:
        raise e from None


def add_layer_to_project(layer, group_structure, group_lst=None, add=True):
    """
    group name has to be list relative to root of project
    root
        group
            subgroup
                subsubgroup for example
    """
    try:
        root = QgsProject.instance().layerTreeRoot()
        QgsProject.instance().addMapLayer(layer, False)
        if add:
            if group_lst is not None:
                group = ensure_group(group_lst, root, group_structure)
                group.addLayer(layer)
            else:
                root.addLayer(layer)
    except Exception as e:
        try:
            # If an error occurred, try and remove the map layer. Otherwise this can cause OSErrors
            QgsProject.instance().removeMapLayer(layer)
        except Exception as e:
            pass
        raise e from None


def create_vector_layer(source_path, layer_name, layer_style, type="ogr"):
    try:
        layer = QgsVectorLayer(source_path, layer_name, type)
        if not layer.isValid():
            raise Exception(f"Layer created is invalid {source_path}")
        layer.loadNamedStyle(layer_style)
        return layer
    except Exception as e:
        raise e from None


def create_raster_layer(source_path, layer_name, layer_style):
    try:
        layer = QgsRasterLayer(source_path, layer_name)
        if not layer.isValid():
            raise Exception(f"Layer created is invalid {source_path}")
        layer.loadNamedStyle(layer_style)
        return layer
    except Exception as e:
        raise e from None


def create_virtual_layer(query, layer_name, layer_style, type="virtual"):
    try:
        layer = QgsVectorLayer(f"?query={query}", layer_name, type)
        if not layer.isValid():
            raise Exception(f"Layer view creation failed")
        layer.loadNamedStyle(layer_style)
    except Exception as e:
        raise e from None
    return layer


def add_layer_to_themes(layer, themes_list):
    """
    Takes a layer and a list of names of mapThemes names. Add layer to all layer themes.
    If a theme doesn't exist yet, it is created first.
    """
    try:
        map_theme_collection = QgsProject.instance().mapThemeCollection()
        map_themes = map_theme_collection.mapThemes()
        for theme in themes_list:
            # Create a new theme and add the layer to it
            new_theme = QgsMapThemeCollection.MapThemeRecord()
            layer_record = QgsMapThemeCollection.MapThemeLayerRecord(layer)
            new_theme.addLayerRecord(layer_record)
            if theme not in map_themes:
                # If the theme in the list doesn't exist, insert it into the themes collection
                map_theme_collection.insert(theme, new_theme)
            else:
                # If the theme in the list doesn exist, copy all of its layer records if there isn't
                # a layer record in the new theme of the corresponding layer,
                # then update (overwrite) the theme in the collection with the new theme
                layer_record_list = map_theme_collection.mapThemeState(
                    theme
                ).layerRecords()
                layers_list = [item.layer() for item in new_theme.layerRecords()]
                for lyr_rec in layer_record_list:
                    if lyr_rec.layer() not in layers_list:
                        new_theme.addLayerRecord(lyr_rec)
                map_theme_collection.update(theme, new_theme)
    except Exception as e:
        raise e from None


def find_tif_layers_and_append(input_folder, layers_list) -> dict:
    """Find rasters that were created with a regular expression. And add
    them to the layers list
    e.g. waterstand_T3_uur, waterstand_T15_uur"""
    for layer in layers_list:
        print(f"layer; {layer.layer_expression}")

        if (
            layer.layer_expression != None
        ):  # waterdept_layer_vars_template, waterlevel_layer_vars_template
            # List files in input_folder
            available_files = [
                i
                for i in os.listdir(input_folder)
                if os.path.isfile(os.path.join(input_folder, i))
            ]
            print(f"expression not none; {layer}")

            # Add files to layers list if not already in dict/list
            for file in available_files:
                print(f"all files; {file}")
                if re.search(layer.layer_expression, file.split(".")[0]):
                    print(file)

                    if file not in [l.layer_name for l in layers_list]:
                        layer_new = copy.copy(layer)
                        layer_new.layer_name = file.split(".")[0]
                        layer_new.layer_source = os.path.join(input_folder, file)
                        layer_new.layer_expression = None
                        layers_list.append(layer_new)
                        print(f"added {file}")
    return layers_list


def add_layers(layers_list, group_structure):
    try:
        for layer_args in layers_list:
            if layer_args.layer_source != None and os.path.exists(
                layer_args.layer_source
            ):
                if layer_args.layer_type == VECTOR:
                    layer = create_vector_layer(
                        source_path=layer_args.layer_source,
                        layer_name=layer_args.layer_name,
                        layer_style=layer_args.layer_style,
                    )
                elif layer_args.layer_type == RASTER:
                    layer = create_raster_layer(
                        source_path=layer_args.layer_source,
                        layer_name=layer_args.layer_name,
                        layer_style=layer_args.layer_style,
                    )
                elif layer_args.layer_type == VIRTUAL:
                    layer = create_virtual_layer(
                        query=layer_args.query,
                        layer_name=layer_args.layer_name,
                        layer_style=layer_args.layer_style,
                    )
                else:
                    raise Exception(
                        f"Error: no layer type specified for layer {layer_args.layer_name}"
                        f"to be created from {layer_args.layer_source}"
                    )
                add_layer_to_project(
                    layer=layer,
                    group_lst=layer_args.layer_group,
                    add=layer_args.add_visible,
                    group_structure=group_structure,
                )
                if layer_args.add_visible:
                    add_layer_to_themes(
                        layer=layer, themes_list=layer_args.layer_themes
                    )
    except Exception as e:
        raise e from None
