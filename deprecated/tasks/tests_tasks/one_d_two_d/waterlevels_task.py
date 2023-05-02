import copy
from qgis.core import QgsTask, Qgis
from qgis.utils import QgsMessageLog, iface
from deprecated.qgis_interaction.layers_management.adding_layers import add_layers
from hhnk_threedi_plugin.qgis_interaction.layers_management.layers.layer_variable import layerVariables


from hhnk_threedi_tools import OneDTwoDTest

description = "waterstand per tijdstap bepalen"


class waterlevelsTask(QgsTask):
    def __init__(self, test_env):
        super().__init__(description, QgsTask.CanCancel)
        self.description = description
        self.exception = None
        self.test_env = copy.copy(test_env)
        self.waterlevel_layer_template = self.test_env.layers[
            "waterlevel_layer_vars_template"
        ]
        self.waterdepth_layer_template = self.test_env.layers[
            "waterdept_layer_vars_template"
        ]
        self.layers_list = []

    def set_threedi_result(self, result):
        self.test_env.threedi_vars = copy.copy(result)

    def run(self):
        QgsMessageLog.logMessage(f"Taak gestart {self.description}", level=Qgis.Info)
        try:
            one_d_two_d_test = OneDTwoDTest.from_path(
                self.test_env.polder_folder,
                revision=self.test_env.revision_path,
                output_path=self.test_env.output_path,
                dem_path=self.test_env.dem_path,
            )

            (
                timesteps,
                level_names,
                depth_names,
            ) = one_d_two_d_test.run_levels_depths_at_timesteps()

            for time, level_name, depth_name in zip(
                timesteps, level_names, depth_names
            ):
                waterlevel_layer = layerVariables(
                    layer_name=self.waterlevel_layer_template.layer_name_format_string.format(
                        time
                    ),
                    layer_group=self.waterlevel_layer_template.layer_group,
                    layer_style=self.waterlevel_layer_template.layer_style,
                    layer_type=self.waterlevel_layer_template.layer_type,
                    layer_source=level_name,
                )
                self.layers_list.append(waterlevel_layer)
                waterdepth_layer = layerVariables(
                    layer_name=self.waterdepth_layer_template.layer_name_format_string.format(
                        time
                    ),
                    layer_group=self.waterdepth_layer_template.layer_group,
                    layer_style=self.waterdepth_layer_template.layer_style,
                    layer_type=self.waterdepth_layer_template.layer_type,
                    layer_source=depth_name,
                )
                self.layers_list.append(waterdepth_layer)
            return True
        except Exception as e:
            self.exception = e
            return False

    def finished(self, result):
        """
        If result is False, either an exception occured or the task was cancelled.
        If the task completed succesfully, we create the output files, add layers to
        QGIS (if needed) and create the output widget to add to the toolbox
        """
        if not result:
            if self.exception is None:
                iface.messageBar().pushMessage(
                    f"Taak {self.description} onderbroken", level=Qgis.Warning
                )
            else:
                iface.messageBar().pushMessage(
                    f"Taak {self.description} mislukt: zie Message Log",
                    level=Qgis.Critical,
                )
                QgsMessageLog.logMessage(
                    '"{name}" Exception: {exception}'.format(
                        name=self.description, exception=self.exception
                    ),
                    level=Qgis.Critical,
                )
                raise self.exception
        else:
            iface.messageBar().pushMessage(
                f"Taak {self.description} en opslag resultaten succesvol uitgevoerd",
                level=Qgis.Info,
            )
            try:
                add_layers(self.layers_list, self.test_env.group_structure)
            except Exception as e:
                raise e from None
