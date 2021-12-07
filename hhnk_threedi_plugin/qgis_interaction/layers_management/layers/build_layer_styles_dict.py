import os


def build_layer_styles_dict(plugin_path, type):
    """
    builds paths to layer styles
    types:
    1 -> sqlite tests style paths
    2 -> 0d1d tests style paths
    3 -> bank_levels style paths
    4 -> 1d2d tests style paths
    """
    plugin_path_styles_path = os.path.join(plugin_path, "qgis_layer_styles")
    styles_dict = {}
    if type == 1:
        styles_path = os.path.join(plugin_path_styles_path, "sqlite_test")
        styles_dict["isolated_channels_style"] = os.path.join(
            styles_path, "isolated_channels.qml"
        )
        styles_dict["controlled_structs_style"] = os.path.join(
            styles_path, "controlled_structs.qml"
        )
        styles_dict["structs_channels_style"] = os.path.join(
            styles_path, "structs_channel.qml"
        )
        styles_dict["weir_height_style"] = os.path.join(styles_path, "weir_height.qml")
        styles_dict["profiles_used_width_style"] = os.path.join(
            styles_path, "channel_width.qml"
        )
        styles_dict["profiles_used_depth_style"] = os.path.join(
            styles_path, "channel_depth.qml"
        )
        styles_dict["dewatering_depth_style"] = os.path.join(
            styles_path, "dewatering_depth.qml"
        )
        styles_dict["watersurface_area_style"] = os.path.join(
            styles_path, "watersurface_area.qml"
        )

    elif type == 2:
        styles_path = os.path.join(plugin_path_styles_path, "zero_d_one_d")
        styles_dict["debit_style"] = os.path.join(styles_path, "debit.qml")
        styles_dict["slope_impoundment_channel_style"] = os.path.join(
            styles_path, "slope_impoundment_channels.qml"
        )
        styles_dict["slope_impoundment_struct_style"] = os.path.join(
            styles_path, "slope_impoundment_structs.qml"
        )
        styles_dict["waterlevel_start_rain_vs_start_sum_style"] = os.path.join(
            styles_path, "waterlvl_start_rain_vs_start_sum.qml"
        )
        styles_dict["waterlevel_end_rain_vs_start_rain_style"] = os.path.join(
            styles_path, "waterlvl_end_rain_vs_start_rain.qml"
        )
        styles_dict["waterlevel_end_rain_vs_end_rain_min_one_style"] = os.path.join(
            styles_path, "waterlvl_end_rain_vs_end_rain_min_1.qml"
        )
        styles_dict["waterlevel_end_sum_vs_start_sum_style"] = os.path.join(
            styles_path, "waterlvl_end_sum_start_sum.qml"
        )
    elif type == 3:
        styles_path = os.path.join(plugin_path_styles_path, "bank_levels")
        styles_dict["flow_1d2d_flowlines_style"] = os.path.join(
            styles_path, "1d2d_flowlines.qml"
        )
        styles_dict["flow_1d2d_channels_style"] = os.path.join(
            styles_path, "flow_1d2d_channels.qml"
        )
        styles_dict["flow_1d2d_manholes_style"] = os.path.join(
            styles_path, "manholes.qml"
        )
        styles_dict["flow_1d2d_cross_sections_style"] = os.path.join(
            styles_path, "cross_section_locations.qml"
        )

    elif type == 4:
        styles_path = os.path.join(plugin_path_styles_path, "one_d_two_d")
        styles_dict["grid_nodes_2d_style"] = os.path.join(
            styles_path, "grid_nodes_2d.qml"
        )
        styles_dict["flow_amount_style"] = os.path.join(styles_path, "flow_amount.qml")
        styles_dict["flow_dry_cat_style"] = os.path.join(
            styles_path, "flow_dry_category.qml"
        )
        styles_dict["water_depth_style"] = os.path.join(styles_path, "waterdepth.qml")
        styles_dict["water_level_style"] = os.path.join(styles_path, "waterlevel.qml")
    return styles_dict
