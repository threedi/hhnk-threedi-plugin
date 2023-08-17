

from doctest import OutputChecker
from hhnk_threedi_plugin.tasks.sqlite_test_tasks.base_sqlite_test_task import BaseSqliteTask
import copy
from PyQt5.QtCore import pyqtSignal
from qgis.core import QgsTask, Qgis
from qgis.utils import QgsMessageLog, iface
from hhnk_threedi_plugin.gui.checks.sqlite_test_widgets.impervious_surface_result import create_impervious_surface_widget
from hhnk_threedi_plugin.gui.checks.sqlite_test_widgets.profiles_used_result import create_profiles_used_widget
from hhnk_threedi_plugin.gui.checks.sqlite_test_widgets.controlled_structs_result import create_controlled_structs_widget
from hhnk_threedi_plugin.gui.checks.sqlite_test_widgets.weir_height_result import create_weir_height_widget
from hhnk_threedi_plugin.gui.checks.sqlite_test_widgets.geometries_result import create_geometries_result_widget
from hhnk_threedi_plugin.gui.checks.sqlite_test_widgets.structs_channels_result import create_structs_channels_result_widget
from hhnk_threedi_plugin.gui.checks.sqlite_test_widgets.general_checks_result import create_general_checks_result_widget
from hhnk_threedi_plugin.gui.checks.sqlite_test_widgets.isolated_channels_result import create_isolated_channels_result_widget
from hhnk_threedi_plugin.gui.checks.sqlite_test_widgets.dem_max_val_result import create_dem_max_val_result_widget
from hhnk_threedi_plugin.gui.checks.sqlite_test_widgets.watersurface_area_result import create_watersurface_area_result_widget
from hhnk_threedi_plugin.gui.checks.sqlite_test_widgets.cross_section_warning_result import cross_section_duplicate_widget
from hhnk_threedi_plugin.gui.checks.sqlite_test_widgets.cross_section_vertex_result import cross_section_no_vertex_widget

import hhnk_research_tools as hrt
import geopandas as gpd


class impSurfaceTask(BaseSqliteTask):
    def __init__(self, folder):
        super().__init__(folder, mutex=None, wait_cond=None)
        self.description="bereken ondoorlatend oppervlak model en polder"

    def run(self):
        QgsMessageLog.logMessage(f"Taak gestart {self.description}", level=Qgis.Info)
        try:
            self.result_text = self.sqlite_test.run_imp_surface_area()
            return True
        except Exception as e:
            self.exception = e
            return False


    def finished_custom(self):
        title, widget = create_impervious_surface_widget(result_text=self.result_text)
        return title, widget


class profilesUsedTask(BaseSqliteTask):
    def __init__(self, folder):
        super().__init__(folder)
        self.description="bepalen gebruikte profielen watergangen"
        self.layer_source = self.folder.output.sqlite_tests.gebruikte_profielen.path

    def run_custom(self):
        if self.os_retry is None:
            self.gdf = self.sqlite_test.run_used_profiles()

        self.gdf.to_file(self.layer_source, index=False, driver='GPKG')

    
    def finished_custom(self):
        # add_layers(self.layers_list, self.test_env.group_structure) #TODO
        title, widget = create_profiles_used_widget(layer_source=self.layer_source)
        return title, widget


class controlledStructsTask(BaseSqliteTask):
    def __init__(self, folder):
        super().__init__(folder)
        self.description="gestuurde kunstwerken overzicht aanmaken"
        self.layer_source = self.folder.output.sqlite_tests.gestuurde_kunstwerken.path

    def run_custom(self):
        if self.os_retry is None:
            self.sqlite_test.run_controlled_structures(overwrite=False)
        return True

    def finished_custom(self):
        # add_layers(self.layers_list, self.test_env.group_structure) #TODO

        title, widget = create_controlled_structs_widget(layer_source=self.layer_source)
        return title, widget


class weirHeightTask(BaseSqliteTask):
    def __init__(self, folder):
        super().__init__(folder)
        self.description="stuw hoogtes en bodemhoogtes vergelijken"
        self.layer_source = self.folder.output.sqlite_tests.bodemhoogte_stuw.path

    def run_custom(self):
        if self.os_retry is None:
            self.gdf, self.update_query = self.sqlite_test.run_weir_floor_level()

        self.gdf.to_file(self.layer_source, index=False, driver='GPKG')
        return True

    def finished_custom(self):
        # add_layers(self.layers_list, self.test_env.group_structure) #TODO

        title, widget = create_weir_height_widget(
                            layer_source=self.layer_source,
                            gdf=self.gdf,
                            model_path=self.folder.model.schema_base.database.path,
                        )

        return title, widget


class geometriesTask(BaseSqliteTask):
    def __init__(self, folder):
        super().__init__(folder)
        self.description="nakijken geometrie"
        self.layer_source = self.folder.output.sqlite_tests.geometry_check.path

    def run_custom(self):
        if self.os_retry is None:
            self.gdf = self.sqlite_test.run_geometry_checks()

        self.csv_path = hrt.gdf_write_to_csv(
            self.gdf,
            filepath=self.layer_source
        )
        return True

    def finished_custom(self):
        # add_layers(self.layers_list, self.test_env.group_structure) #TODO

        title, widget = create_geometries_result_widget(csv_path=self.layer_source)

        return title, widget


class structsChannelsTask(BaseSqliteTask):
    def __init__(self, folder):
        super().__init__(folder)
        self.description="bepalen kunstwerken met referentie level onder bodem niveau"
        self.layer_source = self.folder.output.sqlite_tests.bodemhoogte_kunstwerken.path
        # print(self.layer_source)

    def run_custom(self):
        if self.os_retry is None:
            self.gdf = self.sqlite_test.run_struct_channel_bed_level()

        # print(self.gdf)
        hrt.gdf_write_to_geopackage(self.gdf, filepath=str(self.layer_source))
        return True

    def finished_custom(self):
        # add_layers(self.layers_list, self.test_env.group_structure) #TODO

        title, widget = create_structs_channels_result_widget(self.layer_source)

        return title, widget


class generalChecksTask(BaseSqliteTask):
    def __init__(self, folder):
        super().__init__(folder)
        self.description="algemene model checks"
        self.layer_source = self.folder.output.sqlite_tests.general_sqlite_checks.path

    def run_custom(self):
        if self.os_retry is None:
            self.gdf = self.sqlite_test.run_model_checks()

        hrt.gdf_write_to_csv(self.gdf, filepath=self.layer_source)
        return True

    def finished_custom(self):
        title, widget = create_general_checks_result_widget(csv_path=self.layer_source)
        return title, widget


class isolatedChannelsTask(BaseSqliteTask):
    def __init__(self, folder):
        super().__init__(folder)
        self.description="geïsoleerde watergangen bepalen"
        self.layer_source = self.folder.output.sqlite_tests.geisoleerde_watergangen.path

    def run_custom(self):
        if self.os_retry is None:
            self.gdf, self.result_text = self.sqlite_test.run_isolated_channels()

        hrt.gdf_write_to_csv(self.gdf, filepath=self.layer_source)
        return True

    def finished_custom(self):
        title, widget = create_isolated_channels_result_widget(self.result_text, self.layer_source)
        return title, widget


class demMaxValTask(BaseSqliteTask):
    def __init__(self, folder):
        super().__init__(folder, mutex=None, wait_cond=None)
        self.description="maximale waarde DEM bepalen"

    def run(self):
        QgsMessageLog.logMessage(f"Taak gestart {self.description}", level=Qgis.Info)
        try:
            self.result_text = self.sqlite_test.run_dem_max_value()
            return True
        except Exception as e:
            self.exception = e
            return False


    def finished_custom(self):
        """Add layer so it is seen by the widget"""
        title, widget = create_dem_max_val_result_widget(result_text=self.result_text)
        return title, widget


class dewateringTask(BaseSqliteTask):
    def __init__(self, folder):
        super().__init__(folder, mutex=None, wait_cond=None)
        self.description="bepalen ontwateringsdiepte op basis van DEM hoogtes"

    def run(self):
        QgsMessageLog.logMessage(f"Taak gestart {self.description}", level=Qgis.Info)
        try:
            self.sqlite_test.run_dewatering_depth(overwrite=False)
            return True
        except Exception as e:
            self.exception = e
            return False


    def finished_custom(self):
        """Add layer so it is seen by the widget"""
        # add_layers(self.layers_list, self.test_env.group_structure) #TODO
        return None, None #No widget created.


class watersurfaceAreaTask(BaseSqliteTask):
    def __init__(self, folder):
        super().__init__(folder)
        self.description="wateroppervlak damo/model vergelijken"
        self.layer_source = self.folder.output.sqlite_tests.wateroppervlak.path

    def run_custom(self):
        if self.os_retry is None:
            self.gdf, self.result_text = self.sqlite_test.run_watersurface_area()

        hrt.gdf_write_to_geopackage(self.gdf, filepath=self.layer_source)
        return True

    def finished_custom(self):
                # add_layers(self.layers_list, self.test_env.group_structure) #TODO
        title, widget = create_watersurface_area_result_widget(self.result_text, self.layer_source)
        return title, widget


class gridTask(BaseSqliteTask):
    def __init__(self, folder):
        super().__init__(folder, mutex=None, wait_cond=None)
        self.description="grid genereren"

    def run(self):
        QgsMessageLog.logMessage(f"Taak gestart {self.description}", level=Qgis.Info)
        try:
            self.sqlite_test.create_grid_from_sqlite(sqlite_path=self.folder.model.schema_base.sqlite_paths[0], 
                                                        dem_path=self.folder.model.schema_base.rasters.dem.path, 
                                                        output_folder=self.folder.output.sqlite_tests.path)
            return True
        except Exception as e:
            self.exception = e
            return False

    def finished_custom(self):
        """Add layer so it is seen by the widget"""
        # add_layers(self.layers_list, self.test_env.group_structure) #TODO
        return None, None #No widget created.

class crossSectionDuplicateTask(BaseSqliteTask):
    def __init__(self, folder):
        super().__init__(folder)
        self.description="dubbele cross sections"
        self.layer_source = self.folder.output.sqlite_tests.cross_section_duplicates.path
        self.database =  self.folder.model.schema_base.database

    def run_custom(self):
        if self.os_retry is None:
            self.gdf = self.sqlite_test.run_cross_section_duplicates(database = self.database)

        self.gdf.to_file(self.layer_source, index=False, driver='GPKG')

    
    def finished_custom(self):

        title, widget = cross_section_duplicate_widget(layer_source=self.layer_source)
        return title, widget

class crossSectionNoVertexTask(BaseSqliteTask):
    def __init__(self, folder):
        super().__init__(folder)
        self.description="profielen geen snijpunt in vertex "
        self.database =   self.folder.model.schema_base.database
        self.layer_source = self.folder.output.sqlite_tests.cross_section_no_vertex.path

    def run_custom(self):
        
        if self.os_retry is None:
            self.gdf = self.sqlite_test.run_cross_section_no_vertex(database = self.database)

        self.gdf.to_file(self.layer_source, index=False, driver='GPKG')

    
    def finished_custom(self):

        title, widget = cross_section_no_vertex_widget(layer_source=self.layer_source)
        return title, widget
    
