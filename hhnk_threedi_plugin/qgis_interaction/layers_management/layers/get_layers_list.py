from ..groups.layer_groups_structure import QgisLayerStructure
import os
import re
from ..groups.project_groups_dicts import build_groups_dict
from ..layers.build_layer_names_dict import build_layer_dicts
from ..layers.layer_variable import layerVariables
from ..layers.build_layer_styles_dict import build_layer_styles_dict
from ..layers.layer_types_definition import VECTOR, VIRTUAL, RASTER


from hhnk_research_tools.variables import file_types_dict, GPKG, TIF
from hhnk_threedi_tools.variables.sqlite import primary_col


def create_source_path(output_dict, file_name_key, extension=GPKG):
    return os.path.join(
        output_dict["layer_path"],
        f"{output_dict[file_name_key]}{file_types_dict[extension]}",
    )


def create_virtual_layer_query(source_layer, condition):
    return f"SELECT * from {source_layer} WHERE {condition}"


def get_sqlite_tests_layers_dict(plugin_dir, chosen_tests, output_dict, groups_dict):
    layer_names_dict = build_layer_dicts(1)
    styles_dict = build_layer_styles_dict(plugin_path=plugin_dir, type=1)
    layers_dict = {}
    if chosen_tests == None or "isolated_channels_chk" in chosen_tests:
        layer = layerVariables(
            layer_name=layer_names_dict["isolated_channels_layer_name"],
            layer_group=groups_dict["sqlite_checks"],
            layer_style=styles_dict["isolated_channels_style"],
            layer_type=VECTOR,
            layer_source=create_source_path(output_dict, "isolated_channels_filename"),
        )
        layers_dict["isolated_channels_layer_vars"] = layer
    if chosen_tests == None or "controlled_structs_chk" in chosen_tests:
        layer = layerVariables(
            layer_name=layer_names_dict["controlled_structs_layer_name"],
            layer_group=groups_dict["sqlite_checks"],
            layer_style=styles_dict["controlled_structs_style"],
            layer_type=VECTOR,
            layer_source=create_source_path(output_dict, "controlled_structs_filename"),
        )
        layers_dict["controlled_structs_layer_vars"] = layer
    if chosen_tests == None or "structs_channel_chk" in chosen_tests:
        layer = layerVariables(
            layer_name=layer_names_dict["structs_channel_layer_name"],
            layer_group=groups_dict["sqlite_checks"],
            layer_style=styles_dict["structs_channels_style"],
            layer_type=VECTOR,
            layer_source=create_source_path(output_dict, "structs_channel_filename"),
        )
        layers_dict["structs_channel_layer_vars"] = layer
    if chosen_tests == None or "weir_height_chk" in chosen_tests:
        layer = layerVariables(
            layer_name=layer_names_dict["weir_height_layer_name"],
            layer_group=groups_dict["sqlite_checks"],
            layer_style=styles_dict["weir_height_style"],
            layer_type=VECTOR,
            layer_source=create_source_path(output_dict, "weir_heights_filename"),
        )
        layers_dict["weir_height_layer_vars"] = layer
    if chosen_tests == None or "profiles_used_chk" in chosen_tests:
        layer_width_all = layerVariables(
            layer_name=layer_names_dict["profiles_used_channel_width_layer_name"],
            layer_group=groups_dict["used_profiles_all"],
            layer_style=styles_dict["profiles_used_width_style"],
            layer_type=VECTOR,
            layer_source=create_source_path(output_dict, "profiles_used_filename"),
        )
        layer_depth_all = layerVariables(
            layer_name=layer_names_dict["profiles_used_channel_depth_layer_name"],
            layer_group=groups_dict["used_profiles_all"],
            layer_style=styles_dict["profiles_used_depth_style"],
            layer_type=VECTOR,
            layer_source=create_source_path(output_dict, "profiles_used_filename"),
        )
        layer_width_primary = layerVariables(
            layer_name=layer_names_dict["profiles_used_channel_width_layer_name"],
            layer_group=groups_dict["used_profiles_primary"],
            layer_style=styles_dict["profiles_used_width_style"],
            layer_type=VIRTUAL,
            query=create_virtual_layer_query(
                source_layer=layer_names_dict["profiles_used_channel_width_layer_name"],
                condition=f"{primary_col} = True",
            ),
        )
        layer_depth_primary = layerVariables(
            layer_name=layer_names_dict["profiles_used_channel_depth_layer_name"],
            layer_group=groups_dict["used_profiles_primary"],
            layer_style=styles_dict["profiles_used_depth_style"],
            layer_type=VIRTUAL,
            query=create_virtual_layer_query(
                source_layer=layer_names_dict["profiles_used_channel_depth_layer_name"],
                condition=f"{primary_col} = True",
            ),
        )
        layers_dict["profiles_used_width_all_layer_vars"] = layer_width_all
        layers_dict["profiles_used_depth_all_layer_vars"] = layer_depth_all
        layers_dict["profiles_used_width_primary_layer_vars"] = layer_width_primary
        layers_dict["profiles_used_depth_primary_layer_vars"] = layer_depth_primary
    if chosen_tests == None or "dewatering_depth_chk" in chosen_tests:
        layer = layerVariables(
            layer_name=layer_names_dict["dewatering_depth_layer_name"],
            layer_group=groups_dict["sqlite_checks"],
            layer_style=styles_dict["dewatering_depth_style"],
            layer_type=RASTER,
            layer_source=create_source_path(output_dict, "dewatering_filename", TIF),
        )
        layers_dict["dewatering_layer_vars"] = layer
    if chosen_tests == None or "watersurface_area_chk" in chosen_tests:
        layer = layerVariables(
            layer_name=layer_names_dict["watersurface_area_layer_name"],
            layer_group=groups_dict["sqlite_checks"],
            layer_style=styles_dict["watersurface_area_style"],
            layer_type=VECTOR,
            layer_source=create_source_path(output_dict, "water_surface_filename"),
        )
        layers_dict["watersurface_area_layer_vars"] = layer
    return layers_dict


def get_zero_d_one_d_layers_dict(plugin_dir, output_dict, groups_dict):
    layers_dict = {}
    layer_names_dict = build_layer_dicts(2)
    styles_dict = build_layer_styles_dict(plugin_path=plugin_dir, type=2)
    # ----------------------------------------------------------
    # Kaart 1: Debiet
    # ----------------------------------------------------------
    layer = layerVariables(
        layer_name=layer_names_dict["hidden_hyd_test_channels_layer_name"],
        layer_style=None,
        layer_type=VECTOR,
        layer_source=create_source_path(output_dict, "hyd_test_channels_filename"),
        add_visible=False,
    )
    layers_dict["hidden_channels_layer_vars"] = layer
    layer = layerVariables(
        layer_name=layer_names_dict["hidden_hyd_test_structs_layer_name"],
        layer_style=None,
        layer_type=VECTOR,
        layer_source=create_source_path(output_dict, "hyd_test_structs_filename"),
        add_visible=False,
    )
    layers_dict["hidden_structs_layer_vars"] = layer
    layer = layerVariables(
        layer_name=layer_names_dict["hyd_test_channels_layer_name"],
        layer_group=groups_dict["debit_primary"],
        layer_style=styles_dict["debit_style"],
        layer_type=VIRTUAL,
        query=create_virtual_layer_query(
            source_layer=layer_names_dict["hidden_hyd_test_channels_layer_name"],
            condition=f"{primary_col} = True",
        ),
    )
    layers_dict["debit_primary_channels_layer_vars"] = layer
    layer = layerVariables(
        layer_name=layer_names_dict["hyd_test_channels_layer_name"],
        layer_group=groups_dict["debit_secondary"],
        layer_style=styles_dict["debit_style"],
        layer_type=VIRTUAL,
        query=create_virtual_layer_query(
            source_layer=layer_names_dict["hidden_hyd_test_channels_layer_name"],
            condition=f"{primary_col} = False",
        ),
    )
    layers_dict["debit_secondary_channels_layer_vars"] = layer
    layer = layerVariables(
        layer_name=layer_names_dict["hyd_test_structs_layer_name"],
        layer_group=groups_dict["debit_primary"],
        layer_style=styles_dict["debit_style"],
        layer_type=VIRTUAL,
        query=create_virtual_layer_query(
            source_layer=layer_names_dict["hidden_hyd_test_structs_layer_name"],
            condition=f"{primary_col} = True",
        ),
    )
    layers_dict["debit_primary_structs_layer_vars"] = layer
    layer = layerVariables(
        layer_name=layer_names_dict["hyd_test_structs_layer_name"],
        layer_group=groups_dict["debit_secondary"],
        layer_style=styles_dict["debit_style"],
        layer_type=VIRTUAL,
        query=create_virtual_layer_query(
            source_layer=layer_names_dict["hidden_hyd_test_structs_layer_name"],
            condition=f"{primary_col} = False",
        ),
    )
    layers_dict["debit_secondary_structs_layer_vars"] = layer
    # ----------------------------------------------------------
    # Kaart 2: Uitzakking initieel peil
    # ----------------------------------------------------------
    layer = layerVariables(
        layer_name=layer_names_dict["waterlevel_start_rain_vs_start_sum_layer_name"],
        layer_group=groups_dict["sagging_initial_level"],
        layer_style=styles_dict["waterlevel_start_rain_vs_start_sum_style"],
        layer_type=VECTOR,
        layer_source=create_source_path(output_dict, "zero_d_one_d_filename"),
    )
    layers_dict["waterlevel_start_rain_vs_start_sum_layer_vars"] = layer
    # ----------------------------------------------------------
    # Kaart 3: Streefpeilhandhaving
    # ----------------------------------------------------------
    layer = layerVariables(
        layer_name=layer_names_dict["waterlevel_end_rain_vs_start_rain_layer_name"],
        layer_group=groups_dict["lvl_maintained"],
        layer_style=styles_dict["waterlevel_end_rain_vs_start_rain_style"],
        layer_type=VECTOR,
        layer_source=create_source_path(output_dict, "zero_d_one_d_filename"),
    )
    layers_dict["waterlevel_end_rain_vs_start_rain_layer_vars"] = layer
    # ----------------------------------------------------------
    # Kaart 4: Verhang en opstuwing
    # ----------------------------------------------------------
    layer = layerVariables(
        layer_name=layer_names_dict["hyd_test_channels_layer_name"],
        layer_group=groups_dict["slope_impoundment_channels_primary"],
        layer_style=styles_dict["slope_impoundment_channel_style"],
        layer_type=VIRTUAL,
        query=create_virtual_layer_query(
            source_layer=layer_names_dict["hidden_hyd_test_channels_layer_name"],
            condition=f"{primary_col} = True",
        ),
    )
    layers_dict["slope_impoundment_channels_primary_layer_vars"] = layer
    layer = layerVariables(
        layer_name=layer_names_dict["hyd_test_channels_layer_name"],
        layer_group=groups_dict["slope_impoundment_channels_secondary"],
        layer_style=styles_dict["slope_impoundment_channel_style"],
        layer_type=VIRTUAL,
        query=create_virtual_layer_query(
            source_layer=layer_names_dict["hidden_hyd_test_channels_layer_name"],
            condition=f"{primary_col} = False",
        ),
    )
    layers_dict["slope_impoundment_channels_secondary_layer_vars"] = layer
    layer = layerVariables(
        layer_name=layer_names_dict["hyd_test_structs_layer_name"],
        layer_group=groups_dict["slope_impoundment_structs_primary"],
        layer_style=styles_dict["slope_impoundment_struct_style"],
        layer_type=VIRTUAL,
        query=create_virtual_layer_query(
            source_layer=layer_names_dict["hidden_hyd_test_structs_layer_name"],
            condition=f"{primary_col} = True",
        ),
    )
    layers_dict["slope_impoundment_structs_primary_layer_vars"] = layer
    layer = layerVariables(
        layer_name=layer_names_dict["hyd_test_structs_layer_name"],
        layer_group=groups_dict["slope_impoundment_structs_secondary"],
        layer_style=styles_dict["slope_impoundment_struct_style"],
        layer_type=VIRTUAL,
        query=create_virtual_layer_query(
            source_layer=layer_names_dict["hidden_hyd_test_structs_layer_name"],
            condition=f"{primary_col} = False",
        ),
    )
    layers_dict["slope_impoundment_structs_secondary_layer_vars"] = layer
    # ----------------------------------------------------------
    # Kaart 5: Stabiele waterstandsverhoging einde regen
    # ----------------------------------------------------------
    layer = layerVariables(
        layer_name=layer_names_dict[
            "waterlevel_end_rain_vs_end_rain_min_one_layer_name"
        ],
        layer_group=groups_dict["stable_lvl_increase"],
        layer_style=styles_dict["waterlevel_end_rain_vs_end_rain_min_one_style"],
        layer_type=VECTOR,
        layer_source=create_source_path(output_dict, "zero_d_one_d_filename"),
    )
    layers_dict["waterlevel_end_rain_vs_end_rain_min_one_layer_vars"] = layer
    # ----------------------------------------------------------
    # Kaart 6: Herstel streefpeil
    # ----------------------------------------------------------
    layer = layerVariables(
        layer_name=layer_names_dict["waterlevel_end_sum_vs_start_sum_layer_name"],
        layer_group=groups_dict["lvl_recovery"],
        layer_style=styles_dict["waterlevel_end_sum_vs_start_sum_style"],
        layer_type=VECTOR,
        layer_source=create_source_path(output_dict, "zero_d_one_d_filename"),
    )
    layers_dict["waterlevel_end_sum_vs_start_sum_layer_vars"] = layer
    return layers_dict


def get_bank_levels_layers_dict(plugin_dir, output_dict, groups_dict):
    layer_names_dict = build_layer_dicts(3)
    styles_dict = build_layer_styles_dict(plugin_path=plugin_dir, type=3)
    layers_dict = {}
    layer = layerVariables(
        layer_name=layer_names_dict["flow_1d2d_flowlines_layer_name"],
        layer_group=groups_dict["bank_levels"],
        layer_style=styles_dict["flow_1d2d_flowlines_style"],
        layer_type=VECTOR,
        layer_source=create_source_path(output_dict, "flow_1d2d_flowlines_filename"),
    )
    layers_dict["flow_1d2d_flowlines_layer_vars"] = layer
    layer = layerVariables(
        layer_name=layer_names_dict["flow_1d2d_channels_layer_name"],
        layer_group=groups_dict["bank_levels"],
        layer_style=styles_dict["flow_1d2d_channels_style"],
        layer_type=VECTOR,
        layer_source=create_source_path(output_dict, "flow_1d2d_channels_filename"),
    )
    layers_dict["flow_1d2d_channels_layer_vars"] = layer
    layer = layerVariables(
        layer_name=layer_names_dict["flow_1d2d_manholes_layer_name"],
        layer_group=groups_dict["bank_levels"],
        layer_style=styles_dict["flow_1d2d_manholes_style"],
        layer_type=VECTOR,
        layer_source=create_source_path(output_dict, "flow_1d2d_manholes_filename"),
    )
    layers_dict["flow_1d2d_manholes_layer_vars"] = layer
    layer = layerVariables(
        layer_name=layer_names_dict["flow_1d2d_cross_sections_layer"],
        layer_group=groups_dict["bank_levels"],
        layer_style=styles_dict["flow_1d2d_cross_sections_style"],
        layer_type=VECTOR,
        layer_source=create_source_path(
            output_dict, "flow_1d2d_cross_sections_filename"
        ),
    )
    layers_dict["flow_1d2d_cross_sections_vars"] = layer
    return layers_dict


def get_one_d_two_d_layers_dict(plugin_dir, output_dict, groups_dict):
    layers_dict = {}
    layer_names_dict = build_layer_dicts(4)
    styles_dict = build_layer_styles_dict(plugin_path=plugin_dir, type=4)
    # ----------------------------------------------------------
    # Root
    # ----------------------------------------------------------
    layer = layerVariables(
        layer_name=layer_names_dict["grid_nodes_2d_layer_name"],
        layer_group=groups_dict["1d2d_tests"],
        layer_style=styles_dict["grid_nodes_2d_style"],
        layer_type=VECTOR,
        layer_source=create_source_path(output_dict, "grid_nodes_2d_filename"),
    )
    layers_dict["grid_nodes_2d_layer_vars"] = layer
    # ----------------------------------------------------------
    # Kaart 1: Debiet
    # ----------------------------------------------------------
    layer = layerVariables(
        layer_name=layer_names_dict["flow_dry_before_layer_name"],
        layer_group=groups_dict["debit"],
        layer_style=styles_dict["flow_dry_cat_style"],
        layer_type=VECTOR,
        layer_source=create_source_path(output_dict, "1d2d_all_flowlines_filename"),
    )
    layers_dict["flow_dry_before_layer_vars"] = layer
    layer = layerVariables(
        layer_name=layer_names_dict["flow_end_peak_layer_name"],
        layer_group=groups_dict["debit"],
        layer_style=styles_dict["flow_amount_style"],
        layer_type=VECTOR,
        layer_source=create_source_path(output_dict, "1d2d_all_flowlines_filename"),
    )
    layers_dict["flow_end_peak_layer_vars"] = layer
    layer = layerVariables(
        layer_name=layer_names_dict["1d2d_flow_end_peak_layer_name"],
        layer_group=groups_dict["debit"],
        layer_style=styles_dict["flow_amount_style"],
        layer_type=VIRTUAL,
        query=create_virtual_layer_query(
            source_layer=layer_names_dict["flow_end_peak_layer_name"],
            condition="kcu in (51, 52)",
        ),
    )
    layers_dict["1d2d_flow_end_peak_layer_vars"] = layer
    layer = layerVariables(
        layer_name=layer_names_dict["1d2d_flow_end_peak_layer_name"],
        layer_group=groups_dict["debit"],
        layer_style=styles_dict["flow_amount_style"],
        layer_type=VECTOR,
        layer_source=create_source_path(output_dict, "1d2d_all_flowlines_filename"),
    )
    layers_dict["1d2d_flow_end_peak_layer_vars"] = layer
    # ----------------------------------------------------------
    # Kaart 2: Waterdiepte
    # ----------------------------------------------------------
    layer = layerVariables(
        layer_name_format_string=layer_names_dict["water_depth_layer_name_template"],
        layer_group=groups_dict["waterdepth"],
        layer_style=styles_dict["water_depth_style"],
        layer_type=RASTER,
        layer_expression=re.compile(
            layer_names_dict["water_depth_layer_name_template"].format("[0-9]+")
        ),
    )  #'waterdiepte_T[0-9]+_hours'))
    layers_dict["waterdept_layer_vars_template"] = layer
    # ----------------------------------------------------------
    # Kaart 3: Waterstand
    # ----------------------------------------------------------
    layer = layerVariables(
        layer_name_format_string=layer_names_dict["water_level_layer_name_template"],
        layer_group=groups_dict["waterlevel"],
        layer_style=styles_dict["water_level_style"],
        layer_type=RASTER,
        layer_expression=re.compile(
            layer_names_dict["water_level_layer_name_template"].format("[0-9]+")
        ),
    )  #'waterdiepte_T[0-9]+_hours'))
    layers_dict["waterlevel_layer_vars_template"] = layer
    return layers_dict


def get_layers_list(
    test_type, plugin_dir, output_dict, group_structure, chosen_tests=None
):
    """
    1 -> sqlite tests
    2 -> 0d1d tests
    3 -> bank_levels
    4 -> 1d2d tests
    Creates templates for lists: initiated with layer group and name
    layer itself is added by functions later
    """

    (
        qgis_sqlite_groups_dict,
        qgis_0d1d_groups_dict,
        qgis_bank_levels_groups_dict,
        qgis_1d2d_groups_dict,
    ) = build_groups_dict(groups=group_structure)

    if test_type == 1:
        layers_dict = get_sqlite_tests_layers_dict(
            plugin_dir=plugin_dir,
            chosen_tests=chosen_tests,
            output_dict=output_dict,
            groups_dict=qgis_sqlite_groups_dict,
        )
    elif test_type == 2:
        layers_dict = get_zero_d_one_d_layers_dict(
            plugin_dir=plugin_dir,
            output_dict=output_dict,
            groups_dict=qgis_0d1d_groups_dict,
        )
    elif test_type == 3:
        layers_dict = get_bank_levels_layers_dict(
            plugin_dir=plugin_dir,
            output_dict=output_dict,
            groups_dict=qgis_bank_levels_groups_dict,
        )
    elif test_type == 4:
        layers_dict = get_one_d_two_d_layers_dict(
            plugin_dir=plugin_dir,
            output_dict=output_dict,
            groups_dict=qgis_1d2d_groups_dict,
        )
    return layers_dict
