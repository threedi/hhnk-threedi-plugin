## ONLY MAKE USE OF QGIS NATIVE AND THREEDI RELATED PACKAGES FOR LOCAL RUN

import sys
from pathlib import Path
from dataclasses import dataclass
import platform
import logging
root_logger = logging.getLogger()
for handler in root_logger.handlers[:]:
    root_logger.removeHandler(handler)

logging.basicConfig(
    level=logging.INFO,
    stream=sys.stdout,   # force logging to QGIS console
    format="%(levelname)s - %(message)s"
)
logger = logging.getLogger()
import geopandas as gpd
import pkg_resources
import os
import pyogrio

# import fiona
from typing import Optional,Tuple, Union
import shutil
from shapely import Point
import pandas as pd
from osgeo import ogr
from PyQt5.QtWidgets import QMessageBox, QPlainTextEdit, QToolBar
from qgis.core import QgsProject, QgsVectorLayer
from qgis.utils import iface
from datetime import datetime

# Add the plugins directory to sys.path if needed
if platform.system() == "Windows":
    plugins_path = (
        Path.home()
        / "AppData"
        / "Roaming"
        / "3Di"
        / "QGIS3"
        / "profiles"
        / "default"
        / "python"
        / "plugins"
    )
else:
    plugins_path = (
        Path.home()
        / ".local"
        / "share"
        / "3Di"
        / "QGIS3"
        / "profiles"
        / "default"
        / "python"
        / "plugins"
    )

if not plugins_path.exists():
    raise FileNotFoundError(f"Plugin path does not exist: {plugins_path}")

if plugins_path not in sys.path:
    sys.path.append(str(plugins_path))

# Import the plugin class from the package
import threedi_schematisation_editor.data_models as dm
from threedi_schematisation_editor import ThreediSchematisationEditorPlugin
from threedi_schematisation_editor import ImportStructuresDialog, ImportFeaturesDialog, ImportCrossSectionDataDialog, ImportCrossSectionLocationDialog

BASE_FOLDER = Path(__file__).parent.parent.absolute() / "data"
RESOURCES_FOLDER = BASE_FOLDER / "resources"
MODEL_FOLDER = BASE_FOLDER / "model"

def create_and_populate_output_folders():
    output_folder = MODEL_FOLDER / f"{Path(__file__).stem}_{datetime.now().strftime("%y%m%d_%H%M%S")}"
    output_folder.mkdir(parents=True, exist_ok=True)

    config_folder = output_folder / "00_config"    
    config_folder.mkdir(parents=True, exist_ok=True)
    json_templates = list(RESOURCES_FOLDER.glob("*.json"))
    for json_template in json_templates:
        shutil.copy2(json_template, config_folder)

    source_data_folder = output_folder / "01_source_data"
    source_data_folder.mkdir(parents=True, exist_ok=True)
    shutil.copy2(RESOURCES_FOLDER / "DAMO.gpkg", source_data_folder)
    shutil.copy2(RESOURCES_FOLDER / "HyDAMO.gpkg", source_data_folder)
    
    schematisation_folder = output_folder / "02_schematisation" / "00_basis"
    schematisation_folder.mkdir(parents=True, exist_ok=True)
    shutil.copy2(RESOURCES_FOLDER / "empty_schematisation.gpkg", schematisation_folder / "3Di_schematisation.gpkg")

    threedi_results_folder = output_folder / "03_3di_results"
    threedi_results_folder.mkdir(parents=True, exist_ok=True)
    test_results_folder = output_folder / "04_test_results"
    test_results_folder.mkdir(parents=True, exist_ok=True)

    return output_folder

class ObjectType:
    FEATURE = "feature"
    STRUCTURE = "structure"
    class CrossSection:
        DATA = "cross_section_data"
        LOCATION = "cross_section_location"

HYDAMO_THREEDI_SETTINGS = {
    "hydroobject": {
        "object_name": "channel",
        "object_type": ObjectType.STRUCTURE,
        "model_class": dm.Channel,
    },
    "duikersifonhevel": {
        "object_name": "orifice",
        "object_type": ObjectType.STRUCTURE,
        "model_class": dm.Orifice,
    },
    "gemaal": {
        "object_name": "pump",
        "object_type": ObjectType.STRUCTURE,
        "model_class": dm.Pump,
    },
    "profiellijn": {
        "object_name": "cross_section_location",
        "object_type": ObjectType.CrossSection.LOCATION,
        "model_class": dm.CrossSectionLocation,
    }, 
    "profielpunt": {
        "object_name": "cross_section_data",
        "object_type": ObjectType.CrossSection.DATA,
        "model_class": dm.CrossSectionData,
    }, 
    # "combinatiepeilgebied": {}, 
    # "peilgebiedpraktijk": {}, 
    "STUW": {
        "object_name": "weir",
        "object_type": ObjectType.STRUCTURE,
        "model_class": dm.Weir,
    },
}

DB_LAYERS_MAPPING = {
    "HYDROOBJECT": "aquaprd",
    "DUIKERSIFONHEVEL": "aquaprd",
    "GEMAAL": "aquaprd",
    "PROFIELLIJN": "aquaprd", 
    "PROFIELPUNT": "aquaprd", 
    "COMBINATIEGEBIED": "aquaprd", 
    "PEILGEBIED PRAKTIJK": "aquaprd", 
    "STUW": "aquaprd", 
}

TABLE_NAMES = list(DB_LAYERS_MAPPING.keys())

# Check if the specific duikers layer is in the group
## write a for loop that goes through all the layers and uses the right method/template to convert data
## DUIKERSIFONHEVEL: orifice, orifice.json
## PROFIELLIJN/PROFIELPUNT: cross section, cross_section.json
## HYDROOBJECT: channels, channels.json
## GEMAAL: pump, pump.json ## POMP en GEMAAL zijn aan elkaar gelinkt in HyDAMO (Gemaal voldoende)
## -> Via json expressies toevoegen bijv: aanslagpeil 3cm boven streefpeil
## COMBINATIEGEBIED/PEILGEBIED PRAKTIJK ini waterstand info moet naar connection nodes
## STUW: weir
## -> Kruinpeil via zelfde manier invullen vanaf waterstand
## -> Expressiebuilder proberen in te vullen
## -> Kan achteraf als alles ingeladen is gedaan

def convert_to_3Di(
    hydamo_file_path: Path,
    hydamo_layers: list,
    output_schematisation_directory: Path,
    empty_schematisation_file_path: Optional[Path] = None,
) -> None:
    """
    Convert the HyDAMO file to a 3Di schematisation.
    Writing is handled in process_hydroobject_layer.

    Parameters
    ----------
    hydamo_file_path : Union[Path, hrt.SpatialDatabase]
        Path to the HyDAMO file. Will be converted to hrt.SpatialDatabase
    hydamo_layers : list
        Layers in hydamo_file_path to process, e.g. HYDROOBJECT
    output_schematisation_directory : Path
        Path to the directory where the 3Di schematisation will be stored.
    empty_schematisation_file_path : Optional[Path], default is None
        File path containing the empty schematisation. When None, it will load the
        empty_schematisation.gpkg from htt.resources.schematisation_builder
    """   
    def load(layer: Optional[str] = None) -> gpd.GeoDataFrame:
        """Load layer from geodataframe. When no layer provided, use the default / first one."""
        def available_layers():
            """Return available layers in file gdb"""
            ds = ogr.Open(hydamo_file_path)
            if ds is None:
                raise RuntimeError(f"Could not open {hydamo_file_path}")
            return [ds.GetLayerByIndex(i).GetName() for i in range(ds.GetLayerCount())]
            # return fiona.listlayers(hydamo_file_path)
        def view_name_with_parents(parents: int = 0) -> str:
            """Display name of file with number of parents

            parents (int): defaults to 0
                number of parents to show
            """
            parents = min(len(Path(hydamo_file_path).parts) - 2, parents)  # avoids index-error
            return hydamo_file_path.split(Path(hydamo_file_path).parents[parents].as_posix(), maxsplit=1)[-1]
        
        avail_layers = available_layers()
        if layer is None:
            if len(avail_layers) == 1:
                layer = avail_layers[0]
            else:
                layer = input(f"Select layer [{avail_layers}]:")
        if layer not in avail_layers:
            raise ValueError(
                f"Layer {layer} not available in {view_name_with_parents(2)}. Options are: {avail_layers}"
            )
        gdf = gpd.read_file(hydamo_file_path, layer=layer, engine="pyogrio")
        return gdf
    
    def load_all_schematisation_layers(
        empty_schematisation_file_path: Optional[Path] = None,
    ) -> Tuple[dict[str, gpd.GeoDataFrame], Path]:
        """
        Load schematisation layers from an empty schema file into a dictionary.

        Parameters
        ----------
        empty_schematisation_file_path : Path, default is None
            File path containing the empty schematisation. When None, it will load the empty_schematisation.gpkg
            from htt.resources.schematisation_builder

        Returns
        -------
        layers_data : dict[str, gpd.GeoDataFrame]
            Dictionary of GeoDataFrames for each layer
        empty_schematisation_file_path : Path
            Path to empty gpkg, wont be None from here on.
        """
        if empty_schematisation_file_path is None:
            empty_schematisation_file_path = str(RESOURCES_FOLDER / "empty_schematisation.gpkg")

        layers_data = {}
        for layer in SCHEMATISATION_LAYERS:
            layers_data[layer] = gpd.read_file(empty_schematisation_file_path, layer=layer)
        return layers_data, empty_schematisation_file_path
    
    def get_unique_id(layer_gdf: gpd.GeoDataFrame) -> int:
        """Get a unique ID for a layer."""
        return layer_gdf["id"].max() + 1 if not layer_gdf.empty else 1
    
    def process_hydroobject_layer(
        hydroobject: gpd.GeoDataFrame,
        schematisation_layers: dict,
        connection_node_id: int,
        channel_id: int,
        output_path: Path,
        crs: Union[str, int],
    ) -> None:
        """
        Process the hydroobject layer and save connection_node and channel layers.

        Parameters
        ----------
        hydroobject : GeoDataFrame
            The hydroobject layer.
        schematisation_layers : dict
            Dictionary with the schematisation layers.
        connection_node_id : int
            Starting ID for connection nodes.
        channel_id : int
            Starting ID for channels.
        output_path : Path
            Path to save the output layers.
        crs : Union[str, int]
            Coordinate reference system for the GeoDataFrames.

        Writes
        ------
        output_path : Path
            Write 'connection_node' and 'channel' layer to gpkg. Output location comes from input params.
        """
        def find_point_in_points(point, points, tolerance: float = 1e-2):
            """Find an existing point or return None."""
            for pt in points:
                if pt["geometry"].distance(point) < tolerance:
                    return pt["id"]
            return None

        connection_nodes: list[dict] = []
        channels: list[dict] = []

        for _, row in hydroobject.iterrows():
            # Add start and end points of the feature to the connection_node layer
            start_point = Point(row["geometry"].coords[0])
            end_point = Point(row["geometry"].coords[-1])

            # Find or add start point
            connection_node_start_id = find_point_in_points(start_point, connection_nodes)
            if connection_node_start_id is None:
                connection_node_start_id = connection_node_id
                connection_nodes.append({"id": connection_node_id, "geometry": start_point})
                connection_node_id += 1

            # Find or add end point
            connection_node_end_id = find_point_in_points(end_point, connection_nodes)
            if connection_node_end_id is None:
                connection_node_end_id = connection_node_id
                connection_nodes.append({"id": connection_node_id, "geometry": end_point})
                connection_node_id += 1

            # Add the feature to the channel layer
            channels.append(
                {
                    "id": channel_id,
                    "geometry": row["geometry"],
                    "connection_node_id_start": connection_node_start_id,
                    "connection_node_id_end": connection_node_end_id,
                    "exchange_type": 101,
                    "code": row["code"],
                }
            )
            channel_id += 1

        # Get schema templates (empty GeoDataFrames with correct dtypes)
        connection_node_template = schematisation_layers.get("connection_node", gpd.GeoDataFrame()).copy()
        channel_template = schematisation_layers.get("channel", gpd.GeoDataFrame()).copy()

        # Add id column to templates
        connection_node_template["id"] = pd.Series(dtype="int64")
        channel_template["id"] = pd.Series(dtype="int64")

        # Create GeoDataFrame
        connection_node_gdf = gpd.GeoDataFrame(connection_nodes, geometry="geometry", crs=connection_node_template.crs)
        channel_gdf = gpd.GeoDataFrame(channels, geometry="geometry", crs=channel_template.crs)

        # Reindex to match template columns (missing ones will be NaN, extra ones will be dropped)
        connection_node_gdf = connection_node_gdf.reindex(columns=connection_node_template.columns)
        channel_gdf = channel_gdf.reindex(columns=channel_template.columns)

        # Save the layers
        connection_node_gdf.to_file(output_path, layer="connection_node", engine="pyogrio", mode="w")
        channel_gdf.to_file(output_path, layer="channel", engine="pyogrio", mode="w")

    # Load the HyDAMO file layers
    layers_dict = {layer: load(layer=layer) for layer in hydamo_layers}

    # Load the empty schematisation layers
    SCHEMATISATION_LAYERS = ["channel", "connection_node"]
    schematisation_layers, empty_schematisation_file_path = load_all_schematisation_layers(
        empty_schematisation_file_path
    )

    # Create the output directory if it does not exist
    output_schematisation_directory = Path(output_schematisation_directory)
    output_schematisation_directory.mkdir(parents=True, exist_ok=True)
    output_path = output_schematisation_directory / "3Di_schematisation.gpkg"

    # Copy the empty schematisation file to the output path
    shutil.copy2(empty_schematisation_file_path, output_path)

    # Process the hydroobject layer if present
    if "hydroobject" in layers_dict:
        hydroobject = layers_dict["hydroobject"]
        connection_node_id = get_unique_id(layer_gdf=schematisation_layers.get("connection_node", gpd.GeoDataFrame()))
        channel_id = get_unique_id(layer_gdf=schematisation_layers.get("channel", gpd.GeoDataFrame()))
        crs = hydroobject.crs
        process_hydroobject_layer(
            hydroobject=hydroobject,
            schematisation_layers=schematisation_layers,
            connection_node_id=connection_node_id,
            channel_id=channel_id,
            output_path=output_path,
            crs=crs,
        )
    else:
        raise ValueError("No hydroobject layer found in the HyDAMO file.")

@dataclass
class SchematisationBuilder:
    """
    All actions in the schematisation_builder tab of the HHNK 3Di Toolbox.

    UI includes:
    - SelectProjectLabel : QLabel
    - SelectProjectComboBox : QComboBox
    - CreateProjectLabel : QLabel
    - CreateProjectPlainTextEdit : QPlainTextEdit
    - CreateProjectPushButton : QPushButton
    - SchematisationBuilderVerticalSpacer : Spacer
    - ProjectTabWidget : QTabWidget
        - tab_status_0 : QWidget
            - SelectPolderLabel : QLabel
            - SelectPolderFileWidget : QgsFileWidget
            - ExportDAMOandHyDAMOPushButton : QPushButton
        - tab_status_1 : QWidget
            - ValidatePushButton : QPushButton
        - tab_status_2 : QWidget
            - ConvertPushButton : QPushButton
    """
    def load_layers_from_geopackage(self, geopackage_path, group_name, layer_to_filter=None):
        """
        Load all layers from a GeoPackage into QGIS and group them under a specified group name.

        Args:
            geopackage_path (str): Path to the GeoPackage file.
            group_name (str): Name of the group under which to load the layers.
        """
        if not Path(geopackage_path).exists():
            raise FileNotFoundError(f"GeoPackage not found: {geopackage_path}")

        # Get the QGIS project instance and create/retrieve the specified group
        project = QgsProject.instance()
        root = project.layerTreeRoot()
        group = root.findGroup(group_name) or root.addGroup(group_name)

        # Use OGR to list layers in the GeoPackage
        data_source = ogr.Open(geopackage_path)
        if not data_source:
            raise ValueError(f"Unable to open GeoPackage: {geopackage_path}")

        layer_name_list = []
        for i in range(data_source.GetLayerCount()):
            layer_name = data_source.GetLayerByIndex(i).GetName()
            if layer_to_filter and layer_to_filter != layer_name:
                continue
            layer_path = f"{geopackage_path}|layername={layer_name}"
            layer = QgsVectorLayer(layer_path, layer_name, "ogr")

            if layer.isValid():
                project.addMapLayer(layer, addToLegend=False)
                group.addLayer(layer)
                layer_name_list.append(layer_name)
            else:
                raise ValueError(f"Failed to load layer: {layer_name}")
        return layer_name_list
    
    def is_layer_in_list(self, layer_name, layer_list):
        """Check if a specific layer is within a given group."""
        # if not group:
        #     QMessageBox.information(None, "Warning", f"Group not found.")

        for layer in layer_list:
            if layer == layer_name:
                return True
        return False

    def convert_project(self):
        """Handle conversion of the project to 3Di schematisation."""
        # Load the HyDAMO layers into QGIS
        group_name = "HyDAMO"       
        hydamo_path = str(OUTPUT_FOLDER / "01_source_data" / "HyDAMO.gpkg")
        damo_path = str(OUTPUT_FOLDER / "01_source_data" / "DAMO.gpkg")
        project = QgsProject.instance()
        root = project.layerTreeRoot()
        group = root.findGroup(group_name) ## make sure HyDAMO group is added        

        if not group:
            logger.warning(f"Group {group_name} will be loaded in project.")
            # Load layers from the GeoPackage into the group if the group does not exist
            layer_name_list = self.load_layers_from_geopackage(
                geopackage_path=hydamo_path,
                group_name=group_name,
            )
        else:
            data_source = ogr.Open(hydamo_path)
            if not data_source:
                raise ValueError(
                    f"Unable to open GeoPackage: {hydamo_path}"
                )

            # Get the layer names from the GeoPackage
            layer_name_list = []
            for i in range(data_source.GetLayerCount()):
                layer_name = data_source.GetLayerByIndex(i).GetName()
                layer_name_list.append(layer_name)

        layer_name_list_no_stuw = layer_name_list[:]
        ## STUW not in HyDAMO, so for now STUW is loaded from DAMO.
        if not root.findGroup("DAMO"):
            logger.warning(f"Group {"DAMO"} will be loaded in project.")
            # Load layers from the GeoPackage into the group if the group does not exist
            layer_name_list.extend(self.load_layers_from_geopackage(
                geopackage_path=damo_path,
                group_name="DAMO",
                layer_to_filter="STUW"
            ))
        else:
            data_source = ogr.Open(damo_path)
            if not data_source:
                raise ValueError(
                    f"Unable to open GeoPackage: {damo_path}"
                )
            # Get the layer names from the GeoPackage
            for i in range(data_source.GetLayerCount()):
                layer_name = data_source.GetLayerByIndex(i).GetName()
                if layer_name != "STUW":
                    continue
                layer_name_list.append(layer_name)

        # CONVERSIONS WITHOUT VECTOR DATA IMPORTER
        # convert_to_3Di(
        #     hydamo_file_path=hydamo_path,
        #     hydamo_layers=layer_name_list_no_stuw,
        #     empty_schematisation_file_path=str(RESOURCES_FOLDER / "empty_schematisation.gpkg"),
        #     output_schematisation_directory=MODEL_FOLDER
        #     / "02_schematisation"
        #     / "00_basis",
        # )

        logger.info("Initial conversion done. Loading into Schematisation Editor.")

        # LOAD BY USING THE SCHEMATISATION EDITOR
        geopackage_path = (
            OUTPUT_FOLDER
            / "02_schematisation"
            / "00_basis"
            / "3Di_schematisation.gpkg"
        )

        if not geopackage_path:
            logger.info(f"Missing 3Di_schematisation.gpkg in {str(OUTPUT_FOLDER)}/02_schematisation/00_basis")
        else:
            # Instantiate the plugin
            plugin_instance = ThreediSchematisationEditorPlugin(iface)
            plugin_instance.initGui()
            plugin_instance.load_schematisation(str(geopackage_path))

            for layer_name in HYDAMO_THREEDI_SETTINGS.keys():
                layer_settings = HYDAMO_THREEDI_SETTINGS.get(layer_name)
                layer_object_name = layer_settings.get("object_name")
                layer_object_type = layer_settings.get("object_type")
                layer_model_class = layer_settings.get("model_class")
                
                match layer_object_type:
                    case ObjectType.FEATURE:
                        import_dlg = ImportFeaturesDialog(
                            import_model_cls=layer_model_class,
                            model_gpkg=plugin_instance.model_gpkg,
                            layer_manager=plugin_instance.layer_manager,
                            uc=plugin_instance.uc,
                        )
                    case ObjectType.STRUCTURE:
                        if layer_model_class == dm.Pump:
                            logger.info(f"Importing {layer_name} through Vector Data Importer is not yet implemented, skipping to next layer...")
                            continue
                        import_dlg = ImportStructuresDialog(
                            import_model_cls=layer_model_class,
                            model_gpkg=plugin_instance.model_gpkg,
                            layer_manager=plugin_instance.layer_manager,
                            uc=plugin_instance.uc,
                        )
                    case ObjectType.CrossSection.DATA:
                        import_dlg = ImportCrossSectionDataDialog(
                            import_model_cls=layer_model_class,
                            model_gpkg=plugin_instance.model_gpkg,
                            layer_manager=plugin_instance.layer_manager,
                            uc=plugin_instance.uc,
                        )
                    case ObjectType.CrossSection.LOCATION:
                        import_dlg = ImportCrossSectionLocationDialog(
                            import_model_cls=layer_model_class,
                            model_gpkg=plugin_instance.model_gpkg,
                            layer_manager=plugin_instance.layer_manager,
                            uc=plugin_instance.uc,
                        )
                    case _:
                        logger.info(f"Importing {layer_name} through Vector Data Importer is not yet implemented, skipping to next layer...")
                        continue
                    
                # CONVERSIONS WITH VECTOR DATA IMPORTER (culverts, orifices, weirs, pipes, manholes)
                logger.info(f"Importing {layer_object_name} through Vector Data Importer...")

                if self.is_layer_in_list(layer_name=layer_name, layer_list=layer_name_list):
                    logger.info(f"Layer {layer_name} is in group {group_name} and will be converted to {layer_object_name}'.")
                    target_layer = QgsProject.instance().mapLayersByName(layer_name)[0]
                    import_dlg.source_layer_cbo.setLayer(target_layer)
                    import_dlg.on_layer_changed(target_layer)
                    logger.info(import_dlg.__str__())
                else:
                    logger.info(f"Layer '{layer_name}' is not in group '{group_name}', skipping to next layer.")
                    continue

                # Load template
                import_config_path = OUTPUT_FOLDER / "00_config" / f"{layer_object_name}.json"
                if not import_config_path:
                    logger.warning(f"Missing {layer_object_name}.json in {str(OUTPUT_FOLDER)}/00_config",)
                else:
                    import_dlg.load_import_settings(template_filepath=import_config_path)
                    # Run the import
                    import_dlg.run_import()  # Trigger the "Run Import" action

if __name__ == "__console__":
    ## Load HYDAMO to QGIS:
    OUTPUT_FOLDER = create_and_populate_output_folders()
    test_schematisation_builder = SchematisationBuilder()
    test_schematisation_builder.convert_project()
