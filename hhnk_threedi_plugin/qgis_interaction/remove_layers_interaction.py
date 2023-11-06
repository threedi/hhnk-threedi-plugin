from pathlib import Path

from qgis.core import QgsProject


# Loop through all layers in the project
def remove_layers(files: list):
    """Remove layers from QGIS that lock a file in a list of files."""

    # Get the current project instance
    instance = QgsProject.instance()

    # Make sure files have specified format (posix)
    files = [Path(i.absolute().resolve()).as_posix() for i in files]

    for layer_id, layer in instance.mapLayers().items():
        # compare layer.source() in posix format with posix formated files
        if any(i in Path(layer.source()).as_posix() for i in files):
            instance.removeMapLayer(layer_id)
