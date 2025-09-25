import hhnk_research_tools as hrt
from hhnk_threedi_tools.utils.queries import create_update_reference_level_query
from hhnk_threedi_tools.variables.database_aliases import a_weir_cross_loc_id
from hhnk_threedi_tools.variables.database_variables import reference_level_col
from hhnk_threedi_tools.variables.weirs import new_ref_lvl
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QLabel, QPushButton, QTextEdit, QVBoxLayout, QWidget
from qgis.utils import Qgis, QgsMessageBar

from hhnk_threedi_plugin.gui.general_objects import (
    create_layer_added_label,
    create_no_errors_label,
    create_view_layer_attributes_button,
)
from hhnk_threedi_plugin.gui.sql_preview.model_changes_preview import (
    modelChangesPreview,
)

controlled_structs_titel = "Bodemhoogte stuw"


class refLevelUpdateDialog(QWidget):
    query_executed = pyqtSignal(str)

    def __init__(self, gdf, model_path):
        super(refLevelUpdateDialog, self).__init__()
        self.setWindowTitle("Voorgestelde aanpassingen")
        layout = QVBoxLayout()
        self.results = QTextEdit()
        self.results.setHidden(True)
        self.results.setReadOnly(True)
        self.model_path = model_path
        self.message_bar = QgsMessageBar()
        self.accept_button = QPushButton()
        self.accept_button.setText("Aanpassingen uitvoeren")
        self.accept_button.clicked.connect(self.make_changes)
        self.changes_preview = modelChangesPreview(
            window_title="Voorgestelde aanpassingen",
            description="Waarden in rood worden aangepast naar waarden in groen",
            df=gdf,
            id_col=a_weir_cross_loc_id,
            old_col=reference_level_col,
            new_col=new_ref_lvl,
            new_col_editable=True,
            searchable=True,
            rows_selectable=True,
        )
        layout.addWidget(self.message_bar)
        layout.addWidget(self.changes_preview)
        layout.addWidget(self.results)
        layout.addWidget(self.accept_button)
        self.setLayout(layout)

    def make_changes(self):
        try:
            self.changes_preview.return_changed_value_rows()
            query = create_update_reference_level_query(
                self.changes_preview.df, self.changes_preview.protected_ids_list
            )
            hrt.execute_sql_changes(query=query, database=self.model_path)
            self.results.setText("<br>".join(query.splitlines()))
            self.query_executed.emit(query)
            self.accept_button.deleteLater()
            self.changes_preview.deleteLater()
            self.setWindowTitle("Uitgevoerde aanpassingen aan model")
            self.results.setHidden(False)
        except Exception as e:
            self.message_bar.pushMessage("Changes could not be completed: " + str(e), Qgis.Critical)


class weirHeightWidget(QWidget):
    def __init__(self, layer_source, gdf, model_path):
        super(weirHeightWidget, self).__init__()
        self.setWindowTitle("Voorgestelde aanpassingen reference level")
        self.dialog = refLevelUpdateDialog(gdf=gdf, model_path=model_path)
        layout = QVBoxLayout()
        layer_label = create_layer_added_label()
        layer_button = create_view_layer_attributes_button(layer_source)
        self.dialog_button = QPushButton("Bekijk voorgestelde aanpassingen")
        self.dialog_button.clicked.connect(self.dialog.show)
        self.dialog.query_executed.connect(lambda: self.dialog_button.setText("Bekijk uitgevoerde aanpassingen"))
        layout.addWidget(layer_label)
        layout.addWidget(layer_button)
        layout.addWidget(self.dialog_button)
        self.setLayout(layout)


def create_weir_height_widget(layer_source, gdf, model_path):
    if not gdf.empty:
        widget = weirHeightWidget(layer_source=layer_source, gdf=gdf, model_path=model_path)
    else:
        widget = QWidget()
        layout = QVBoxLayout()
        label = create_no_errors_label()
        layout.addWidget(label)
        widget.setLayout(layout)
    return controlled_structs_titel, widget
