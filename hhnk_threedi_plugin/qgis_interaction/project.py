# %%
# # -*- coding: utf-8 -*-
"""
#TODO:
    2. Add printcomposers

"""

import logging
from pathlib import Path
from typing import Union

import hhnk_threedi_tools as htt
from hhnk_threedi_tools.qgis import layer_structure
from qgis.core import (
    QgsLayoutExporter,
    QgsMapLayerStyle,
    QgsMapThemeCollection,
    QgsPrintLayout,
    QgsProject,
    QgsRasterLayer,
    QgsReadWriteContext,
    QgsRenderContext,
    QgsVectorLayer,
)
from qgis.PyQt.QtXml import QDomDocument
from qgis.utils import iface

logger = logging.getLogger(__name__)


class QgisLayer:
    """class used for multiple qgis layer:
    QgsVectorLayer
    QgsRasterLayer
    """

    def __init__(
        self,
        settings: htt.QgisLayerSettings,
    ):
        """
        Parameters
        ----------
        settings : htt.QgisLayerSettings
        """

        self.settings = settings
        self.instance = QgsProject.instance()
        self._layer = None
        self._layertreelayer = None

    def get_qgis_layer(self):
        """
        create a qgis layer instance based on settings.

        Do not make this an attribute of QgisLayer! When removing the layer
        the id will remain the same and weird errors will occur.
        """
        if self.settings.ftype in ["ogr", "arcgisfeatureserver"]:
            return QgsVectorLayer(self.settings.source, self.settings.name, self.settings.ftype)
        elif self.settings.ftype in ["gdal", "wms", "arcgismapserver"]:
            return QgsRasterLayer(self.settings.source, self.settings.name, self.settings.ftype)
        else:
            print(f"ERROR: Layer {self.settings.name} has unknown ftype: {self.settings.ftype}")

    @property
    def name(self):
        return self.settings.name

    @property
    def id(self):
        return self.settings.id

    @property
    def layer(self):
        if self._layer is None:
            self._layer = self.get_layer()
        return self._layer

    def add_styles(self):
        """
        Add styles to layer in project. Can add multiple styles.
        """
        style = QgsMapLayerStyle()
        style.readFromLayer(self.layer)  # doesnt seem to work.
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
        qgis_layer = self.get_qgis_layer()  # dont set this as attribute. id must change when its removed.
        if self.is_valid(qgis_layer):
            # Find index of layer in avalailable layers in group
            # print(self.id)
            layer_keys = [l.layerId() for l in qgis_group.layer_list if self.name == l.name()]
            if layer_keys:
                # Break loop if no reload required
                if not reload:
                    pass
                # remove all layers with name in group.
                else:
                    try:
                        # for l in layer_keys:
                        # Note that using removeMapLayers does not work because the
                        # group has ownership of the layer. See addLayer in;
                        # https://qgis.org/pyqgis/3.2/core/Layer/QgsLayerTreeGroup.html
                        # Therefore we need to remove the child from the group itself.
                        # Correction. using group.addLayer will not work properly
                        self.instance.removeMapLayers(layer_keys)
                        self._layer = None
                    #                        for l in layer_keys:
                    #                            qgis_group.layertreegroup.removeChildNode(l)
                    #                            print(l)
                    except:
                        print(f"Could not remove {self.id} from project")
                        raise

            # We also need to add the layer to the instance, otherwise the group
            # gets ownership over the layer, which will break some other things with
            # styling and removing the layer.
            self.instance.addMapLayer(qgis_layer, False)
            self._layertreelayer = qgis_group.layertreegroup.addLayer(qgis_layer)  # returns QgsLayerTreeLayer.
            # We need the QgsMapLayer for styles so we access that here.
            self._layer = self._layertreelayer.layer()
            self.add_styles()

            # Set visibility (defaults to off)
            self._layertreelayer.setItemVisibilityChecked(False)
            self._layertreelayer.setExpanded(False)

    def is_valid(self, qgis_layer) -> bool:
        """Check if layer is valid, checked before adding to project"""

        qml_valid = True
        for qml_path in self.settings.qml_lst:
            if not qml_path.exists():
                print(f"Layer styling does not exist: {qml_path}")
                qml_valid = False
            else:
                qml_valid = all((qml_valid, True))

        # check layer
        try:
            layer_valid = qgis_layer.isValid()

            if not layer_valid:
                if not Path(qgis_layer.source().exists()):
                    print(f"Layer source does not exist: {qgis_layer.source()}")

        except Exception:
            layer_valid = False
            print(f"Layer {self.id} not valid. Please check data-source: {self.settings.file}")

        return all((qml_valid, layer_valid))

    def get_group(self):
        """find group recursively"""
        group = self.instance.layerTreeRoot()
        for group_name in self.settings.group_lst:
            group = group.findGroup(group_name)
            if group is None:
                return None
        return group

    def get_layer(self) -> Union[QgsVectorLayer, QgsRasterLayer]:
        """Return the QGIS layer the self.name

        Returns
        -------
        Union[QgsVectorLayer, QgsRasterLayer]
            QGIS Layer
        """
        group = None
        if self.settings.group_lst:
            group = self.get_group()
            if group:  # find layer in group, if None, layer has been removed.
                layer = next((child.layer() for child in group.children() if child.name() == self.name), None)
            else:  # Group does not exist, so layer has been removed.
                layer = None
        else:  # No groups in QGIS instance.
            layer = self.instance.mapLayersByName(self.name)

        return layer

    def zoom_to_layer(self):
        """Set canvas extent in qgis to layer extent."""
        if self.layer is None:
            print(f"Layer invalid, not setting extent: {self.id}")
            return

        canvas = iface.mapCanvas()
        extent = self.layer.extent()
        print("Setting extent to", extent)
        print("Canvas", canvas)
        canvas.setExtent(extent)
        canvas.setExtent(extent)


class QgisAllThemes:
    def __init__(self) -> None:
        self.instance = QgsProject.instance()

    @property
    def mapthemecollection(self):
        return self.instance.mapThemeCollection()

    @property
    def theme_structure(self):
        structure = {}
        for theme in self.theme_names:
            layers = self.get_theme_layers(theme)
            structure[theme] = layers
        return structure

    @property
    def theme_names(self):
        return self.mapthemecollection.mapThemes()

    def get_theme(self, theme_name):
        return self.mapthemecollection.mapThemeState(theme_name)

    def get_theme_layers(self, theme_name: str) -> dict:
        """

        Parameters
        ----------
        theme_name (str): name of theme

        Returns
        -------
        dict {QgisVectorLayer.name(): QgisVectorLayer}
        """
        theme = self.get_theme(theme_name)

        layers = {}
        for record in theme.layerRecords():
            layer_record = record.layer()
            layers[layer_record.name()] = layer_record
        return layers

    def add_theme(self, theme_settings, layers, verbose=False):
        """Add a theme to qgis project. If the theme already exists,
        it wil instead add/replace layers.

        Note that themes can be quite tricky if they are edited after they have been edited.
        Therefore we here retrieve the layers in the theme and then remove it before
        creating it again, see issue #143

        Parameters
        ----------
        theme_settings (htt.qgis.QgisThemeSettings): class with name and layerids
        layers (pd.Series): series with QgisLayer entries.
        verbose (bool, optional):
        """
        if verbose:
            print(f"Creating theme: {theme_settings.name}")

        # Bestaande theme verwijderen, eerst layers ophalen. Omdat niet alle layers
        # ook in theme_settings.layer_ids staan, bijvoorbeeld als er eerst een
        # 0d1d_check resultaat is ingeladen van een bepaalde revisie.
        current_theme_layers = self.get_theme_layers(theme_settings.name)
        self.mapthemecollection.removeMapTheme(theme_settings.name)
        theme = self.get_theme(theme_settings.name)

        if verbose:
            print(f"\t\ttheme has layers: {current_theme_layers.keys()}")

        theme_layers = {}

        # Bestaande layers in de visibility preset overnemen. Layername blijft een
        # key en dus uniek. Deze wordt later overschreven als die ook in de theme_settings
        # staat. Als er twee keer een 0d1d_check resultaat wordt ingeladen blijft de meest
        # recent ingeladen group onder het thema hangen.
        for layer_name, layer in current_theme_layers.items():
            theme_layers[layer_name] = QgsMapThemeCollection.MapThemeLayerRecord(layer)

        for layer_id in theme_settings.layer_ids:
            layer = layers[layer_id]

            if layer.layer is not None:
                if verbose:
                    print(f"\tadd layer: {layer.layer}")

                theme_layers[layer.name] = QgsMapThemeCollection.MapThemeLayerRecord(layer.layer)
            else:
                if verbose:
                    print(f"\t--- {layer.name} layer not found")

        theme.setLayerRecords(list(theme_layers.values()))
        self.mapthemecollection.insert(theme_settings.name, theme)


class QgisAllGroups:
    def __init__(self, settings: htt.qgis.QgisAllGroupsSettings):
        self.settings = settings
        self.instance = QgsProject.instance()
        self.root = self.instance.layerTreeRoot()
        self.groups = {}  # group.id: class QgisGroup
        self.layertreegroups = {}  # group.id: layertreegroup

    def create_groups(self):
        """Create groups recursively. Adds groups to the self.groups dict so we
        can access those later."""
        for group_settings in self.settings.groups.get_all_children():
            # Load parent group layertree

            if group_settings.parent_id == "":
                self.layertreegroups[group_settings.id] = self.root
            else:
                self.layertreegroups[group_settings.id] = self.groups[
                    group_settings.parent_id
                ].parent_layertreegroup.findGroup(group_settings.parent_name)

            if group_settings.id not in self.groups:
                self.groups[group_settings.id] = QgisGroup(
                    settings=group_settings,
                    parent_layertreegroup=self.layertreegroups[group_settings.id],
                )


class QgisGroup:
    """
    QgisGroup instance that can recursively add groups to project

    Parameters:
    settings (htt.QgisGroupSettings):
    parent_layertreegroup ():
    """

    def __init__(self, settings, parent_layertreegroup):
        self.settings = settings
        self.parent_layertreegroup = parent_layertreegroup

        self.layertreegroup = self.get_or_create()

    @property
    def id(self):
        """id of group"""
        return self.settings.id

    @property
    def name(self):
        """name of group"""
        return self.settings.name

    def get_or_create(self):
        """Get the group and create if doesnt exist."""
        layertreegroup = None
        if self.parent_layertreegroup is not None:
            layertreegroup = self.parent_layertreegroup.findGroup(self.name)

        if layertreegroup is None:
            if self.settings.load_group:
                # TODO betere manier om dit bij te houden..
                if self.settings.lvl != 1:
                    group_index = -1
                else:
                    if self.settings.subject in ["achtergrond", "test_protocol"]:
                        group_index = -1
                    else:
                        group_index = 0

                print(f"group:{self.name}. lvl: {self.settings.lvl}. idx: {group_index}")

                layertreegroup = self.parent_layertreegroup.insertGroup(index=group_index, name=self.name)
                layertreegroup.setItemVisibilityChecked(False)
                layertreegroup.setExpanded(False)
        return layertreegroup

    @property
    def layer_list(self) -> list:
        """returns QgsLayerTreeLayer, not QgsVectorLayer
        QgsLayerTreeLayer.layer() returns the QgsVectorLayer which is used for adding
        layer to project.
        """
        # return [j for j in [i.layer() for i in self.layertreegroup.findLayers()] if j is not None]
        return [i for i in self.layertreegroup.findLayers()]


class QgisPrintLayout:
    """Layout manager met voorgedefineerde kaarten.
    Kan templates toevoegen en laden"""

    def __init__(self) -> None:
        self.instance = QgsProject.instance()
        self.layoutmanager = self.instance.layoutManager()

    def get_layout(self, layout_name: str):
        """Get layout bij name"""
        return self.layoutmanager.layoutByName(layout_name)

    def add_from_template(self, template_path, name):
        """Add a layout from template file (.qpt)"""
        layout = self.get_layout(name)

        layout = QgsPrintLayout(self.instance)
        with open(template_path, "r", encoding=None) as f:
            template_content = f.read()
        doc = QDomDocument()
        doc.setContent(template_content)

        # adding to existing items
        items, ok = layout.loadFromTemplate(doc, QgsReadWriteContext(), True)
        print("items", items, "ok", ok)
        layout.setName(name)
        self.instance.layoutManager().addLayout(layout)

    def create_pdf_from_composer(
        self,
        composer_name,
        title,
        subtitle,
        legenda_ids,
        selected_legenda,
        theme,
        output_file,
    ):
        """Create pdf from a print compusing using"""
        layout_item = self.get_layout(composer_name)

        # -------------------------------------------------------------------------------------
        # Change layout settings
        # -------------------------------------------------------------------------------------
        label_item = layout_item.itemById("titel")
        label_item.setText(title)

        label_item = layout_item.itemById("subtitel")
        label_item.setText(subtitle)

        # Hide all legend items, only show selected legend.
        for legenda_id in legenda_ids:
            legenda_item = layout_item.itemById(legenda_id)
            legenda_item.setVisibility(False)
            if legenda_id == selected_legenda:
                legenda_item.setVisibility(True)

        ref_map = layout_item.referenceMap()
        ref_map.setFollowVisibilityPresetName(theme)

        # Poging om extent goed te zetten, maar handmatig is beter.
        # ref_map.setExtent(project.mapcanvas_extent)

        # -------------------------------------------------------------------------------------
        # Export
        # -------------------------------------------------------------------------------------
        pdf_settings = QgsLayoutExporter.PdfExportSettings()
        pdf_settings.textRenderFormat = (
            QgsRenderContext.TextFormatAlwaysText
        )  # If not changed the labels will be ugly in the pdf

        # image_settings = QgsLayoutExporter.ImageExportSettings()

        export = QgsLayoutExporter(layout_item)
        result = export.exportToPdf(output_file, pdf_settings)
        return result


class Project:
    """
    Project instance which loads a layer_structure from file and then
    creates groups, loads layers, generates themes
    """

    def __init__(self, verbose=False):
        self.structure = None  # fill using self.get_structure() or self.run()
        self.groups = None
        self.layers = {}
        self.themes = QgisAllThemes()
        self.layout = QgisPrintLayout()
        self.verbose = verbose

    def get_structure(self, layer_structure_path, subjects, revisions, folder):
        """Load layer structure from file"""
        self.structure = layer_structure.LayerStructure(
            layer_structure_path=layer_structure_path, subjects=subjects, revisions=revisions, folder=folder
        )
        self.structure.run()

    def add_layers(self):
        """Add selected layers to project"""
        for layer in self.structure.layers:
            qgis_layer = QgisLayer(layer)
            if qgis_layer.settings.load_layer:
                qgis_layer.add_to_project(qgis_group=self.groups.groups[qgis_layer.settings.group_id])
            self.layers[qgis_layer.id] = qgis_layer

    def add_themes(self):
        """get themes from settings."""
        for theme_settings in self.structure.themes:
            self.themes.add_theme(theme_settings=theme_settings, layers=self.layers, verbose=self.verbose)

    def run(
        self,
        layer_structure_path=None,
        subjects=None,
        revisions: htt.SelectedRevisions = htt.SelectedRevisions(),
        folder=None,
        **kwargs,
    ):
        """Run project, load layer structure and load selected layers."""
        self.get_structure(layer_structure_path, subjects, revisions, folder, **kwargs)
        self.groups = QgisAllGroups(settings=self.structure.groups)

        self.groups.create_groups()
        self.add_layers()
        self.add_themes()
