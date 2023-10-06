
from qgis.core import QgsProject



# Loop through all layers in the project
def remove_layers(files: list):
    """Remove layers from QGIS that lock a file in a list of files."""

    # Get the current project instance
    instance = QgsProject.instance()

    for layer_id, layer in instance.mapLayers().items():
        if any(i in layer.source() for i in files):
            instance.removeMapLayer(layer_id)