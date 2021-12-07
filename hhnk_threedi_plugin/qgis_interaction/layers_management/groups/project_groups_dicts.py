def build_groups_dict(groups):
    # dictionary to refer to qgis layer groups
    # used to automatically generate and remove layers and layer groups

    qgis_sqlite_groups_dict = {
        "sqlite_checks": groups.sqlite_group.group,
        "used_profiles": groups.sqlite_group.profiles_used.base,
        "used_profiles_primary": groups.sqlite_group.profiles_used.primary,
        "used_profiles_all": groups.sqlite_group.profiles_used.all,
    }

    qgis_0d1d_groups_dict = {
        "0d1d_tests": groups.hyd_test_and_0d1d.group,
        "debit_primary": groups.hyd_test_and_0d1d.debit.primary,
        "debit_secondary": groups.hyd_test_and_0d1d.debit.secondary,
        "slope_impoundment_structs_primary": groups.hyd_test_and_0d1d.slope_impoundment.structs.primary,
        "slope_impoundment_structs_secondary": groups.hyd_test_and_0d1d.slope_impoundment.structs.secondary,
        "slope_impoundment_channels_primary": groups.hyd_test_and_0d1d.slope_impoundment.channels.primary,
        "slope_impoundment_channels_secondary": groups.hyd_test_and_0d1d.slope_impoundment.channels.secondary,
        "sagging_initial_level": groups.hyd_test_and_0d1d.sagging,
        "lvl_maintained": groups.hyd_test_and_0d1d.level_maintaining,
        "stable_lvl_increase": groups.hyd_test_and_0d1d.stable_level_increase,
        "lvl_recovery": groups.hyd_test_and_0d1d.level_recovery,
    }

    qgis_bank_levels_groups_dict = {"bank_levels": groups.bank_levels}

    qgis_1d2d_groups_dict = {
        "1d2d_tests": groups.one_d_two_d.group,
        "debit": groups.one_d_two_d.debit,
        "waterdepth": groups.one_d_two_d.water_depth,
        "waterlevel": groups.one_d_two_d.water_level,
    }
    return (
        qgis_sqlite_groups_dict,
        qgis_0d1d_groups_dict,
        qgis_bank_levels_groups_dict,
        qgis_1d2d_groups_dict,
    )
