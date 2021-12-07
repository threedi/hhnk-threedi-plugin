from qgis.core import QgsProject, QgsLayerTreeLayer, QgsLayerTreeGroup
from qgis.utils import iface


def is_visible_layer(parent, layer):
    """
    Makes sure we are not removing all layers that share a name with the
    hidden layer we are trying to remove by checking if it's part of the
    Layer Tree
    """
    try:
        for child in parent.children():
            if isinstance(child, QgsLayerTreeGroup):
                if is_visible_layer(child, layer):
                    return True
            elif isinstance(child, QgsLayerTreeLayer) and child.layer() == layer:
                return True
        return False
    except Exception as e:
        raise e from None


def remove_layer_from_root(parent, layer_name, layer_expression):
    try:
        root = QgsProject.instance()
        if layer_name is not None:
            layers_to_remove = [
                child.layerId()
                for child in parent.children()
                if isinstance(child, QgsLayerTreeLayer) and child.name() == layer_name
            ]
            if not layers_to_remove:
                # Means we are dealing with a hidden layer, which HAS to be added to the root of the project
                layers_to_remove = [
                    lyr
                    for lyr in root.mapLayers().values()
                    if lyr.name() == layer_name
                    and not is_visible_layer(QgsProject.instance().layerTreeRoot(), lyr)
                ]
        elif layer_expression is not None:
            layers_to_remove = [
                child.layerId()
                for child in parent.children()
                if isinstance(child, QgsLayerTreeLayer)
                and layer_expression.match(child.name())
            ]
            if not layers_to_remove:
                layers_to_remove = [
                    lyr for lyr in root.mapLayers().values() if lyr.name() == layer_name
                ]
        else:
            layers_to_remove = []
        for layer_id in layers_to_remove:
            root.removeMapLayer(layer_id)
    except Exception as e:
        raise e from None


def remove_layer_from_group(
    parent, current, group_list, layer_name=None, layer_expression=None
):
    """
    Recursively traverses the structure provided in group_list (from highest level to lowest)
    Then removes the layer from that group. It then checks going back up through the group
    list whether a group is now empty. If so, it is removed.

    If a layer or group isn't found, we stop the execution and assume the user has removed or
    renamed the layer or group.
    """
    prj_root = QgsProject.instance()
    if not current:
        return
    if not group_list:
        if layer_name is not None:
            layers_to_remove = [
                child.layerId()
                for child in current.children()
                if child.name() == layer_name
            ]
        elif layer_expression is not None:
            layers_to_remove = [
                child.layerId()
                for child in current.children()
                if layer_expression.match(child.name())
            ]
        else:
            layers_to_remove = []
        for layer_id in layers_to_remove:
            prj_root.removeMapLayer(layer_id)
    else:
        next_parent = current
        next_current = current.findGroup(group_list[0])
        next_grp_lst = group_list[1:]
        remove_layer_from_group(
            parent=next_parent,
            current=next_current,
            group_list=next_grp_lst,
            layer_name=layer_name,
            layer_expression=layer_expression,
        )
    if len(current.children()) == 0:
        parent.removeChildNode(current)


def remove_layer(layer_name=None, layer_expression=None, group_lst=None):
    """
    Removes layers from qgis project. This is neccessary because otherwise we
    can't overwrite their source files.
    """
    try:
        if group_lst is None:
            remove_layer_from_root(
                parent=QgsProject.instance().layerTreeRoot(),
                layer_name=layer_name,
                layer_expression=layer_expression,
            )
        else:
            parent = QgsProject.instance().layerTreeRoot()
            current = parent.findGroup(group_lst[0])
            grp_lst = group_lst[1:]
            if current:
                remove_layer_from_group(
                    parent=parent,
                    current=current,
                    group_list=grp_lst,
                    layer_name=layer_name,
                    layer_expression=layer_expression,
                )
    except Exception as e:
        raise e from None


def remove_layers(layers_list):
    try:
        for layer in layers_list:
            remove_layer(
                layer_name=layer.layer_name,
                layer_expression=layer.layer_expression,
                group_lst=layer.layer_group,
            )
        iface.mapCanvas().refresh()
    except Exception as e:
        raise e from None
