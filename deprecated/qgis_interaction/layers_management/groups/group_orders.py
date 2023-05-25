from .....hhnk_threedi_plugin.qgis_interaction.layers_management.groups.layer_groups_structure import QgisLayerStructure


def build_group_order(qls):
    zero_d_group = qls.hyd_test_and_0d1d
    one_d_group = qls.one_d_two_d

    main_group_order = [
        qls.sqlite_group.group[0],  # 04. Testprotocol sqlite
        qls.hyd_test_and_0d1d.group[0],  # 05. Hydraulische Toets en 0d1d tests
        qls.bank_levels[0],  # 06. Bank levels
        qls.one_d_two_d.group[0],
    ]  # 07. Testprotocol 1d2d tests

    zero_d_group_order = [
        zero_d_group.debit.base[1],  # Kaart 1: Debiet
        zero_d_group.sagging[1],  # Kaart 2: Uitzakking initieel peil
        zero_d_group.level_maintaining[1],  # Kaart 3: Streefpeilhandhaving
        zero_d_group.slope_impoundment.base[1],  # Kaart 4: Verhang en opstuwing
        zero_d_group.stable_level_increase[
            1
        ],  # Kaart 5: Stabiele waterstandsverhoging einde regen
        zero_d_group.level_recovery[1],
    ]  # Kaart 6: Herstel streefpeil

    one_d_group_order = [
        one_d_group.debit[1],  # Kaart 1: Debiet
        one_d_group.water_depth[1],  # Kaart 2: Waterdiepte
        one_d_group.water_level[1],
    ]  # Kaart 3: Waterstand
    return main_group_order, zero_d_group_order, one_d_group_order
