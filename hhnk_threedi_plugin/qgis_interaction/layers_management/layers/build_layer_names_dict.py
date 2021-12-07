def build_layer_dicts(type):
    """
    layer names associated with type of test added to dict
    1 -> sqlite tests layer names
    2 -> 0d1d tests layer names
    3 -> bank_levels layer names
    4 -> 1d2d tests layer names
    """
    layer_names_dict = {}
    if type == 1:
        layer_names_dict["isolated_channels_layer_name"] = "geisoleerde_watergangen"
        layer_names_dict["controlled_structs_layer_name"] = "gestuurde_kunstwerken"
        layer_names_dict["structs_channel_layer_name"] = "bodemhoogte_kunstwerken"
        layer_names_dict["weir_height_layer_name"] = "bodemhoogte_stuw"
        layer_names_dict[
            "profiles_used_channel_width_layer_name"
        ] = "watergangen_breedte"
        layer_names_dict[
            "profiles_used_channel_depth_layer_name"
        ] = "watergangen_diepte"
        layer_names_dict["dewatering_depth_layer_name"] = "ontwateringsdiepte"
        layer_names_dict["watersurface_area_layer_name"] = "oppervlaktewater"

    if type == 2:
        layer_names_dict[
            "hidden_hyd_test_channels_layer_name"
        ] = "hd_watergang_segmenten"
        layer_names_dict["hyd_test_channels_layer_name"] = "watergang_segmenten"
        layer_names_dict["hidden_hyd_test_structs_layer_name"] = "hd_kunstwerken"
        layer_names_dict["hyd_test_structs_layer_name"] = "kunstwerken"
        layer_names_dict[
            "waterlevel_start_rain_vs_start_sum_layer_name"
        ] = "waterstand_begin_regen_vs_begin_som"
        layer_names_dict[
            "waterlevel_end_rain_vs_start_rain_layer_name"
        ] = "waterstand_einde_regen_vs_begin_regen"
        layer_names_dict[
            "waterlevel_end_rain_vs_end_rain_min_one_layer_name"
        ] = "waterstand_einde_regen_vs_1_dag_eerder"
        layer_names_dict[
            "waterlevel_end_sum_vs_start_sum_layer_name"
        ] = "waterstand_einde_som_vs_start_som"

    if type == 3:
        layer_names_dict["flow_1d2d_flowlines_layer_name"] = "stroming_1d2d_flowlines"
        layer_names_dict["flow_1d2d_channels_layer_name"] = "stroming_1d2d_watergangen"
        layer_names_dict["flow_1d2d_manholes_layer_name"] = "stroming_1d2d_putten"
        layer_names_dict[
            "flow_1d2d_cross_sections_layer"
        ] = "stroming_1d2d_cross_sections"

    if type == 4:
        # Voor kaarten 2 en 3 (waterdiepte en waterstand) is de naam afhankelijk van tijdstappen. Om die reden
        # zijn deze kaart lagen alleen als template toegevoegd aan de dict
        layer_names_dict["grid_nodes_2d_layer_name"] = "grid_nodes_2d"
        layer_names_dict["water_level_layer_name_template"] = "waterstand_T{}_uur"
        layer_names_dict["water_depth_layer_name_template"] = "waterdiepte_T{}_uur"
        layer_names_dict["flow_dry_before_layer_name"] = "stroming_vooraf_droog"
        layer_names_dict["flow_end_peak_layer_name"] = "stroming_einde_piek"
        layer_names_dict["flow_12hr_after_peak_layer_name"] = "stroming_12_uur_na_piek"
        layer_names_dict["1d2d_flow_end_peak_layer_name"] = "1d2d_stroming_einde_piek"
    return layer_names_dict
