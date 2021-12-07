primary = ["primair"]
secondary = ["secundair"]
structs = ["kunstwerken"]
channels = ["watergangen"]
used_profiles = ["Gebruikte profielen"]
bank_lvls = ["Bank levels"]
wrong_bed_lvls = ["Foutieve bed levels"]
all_name = ["Alle"]


class Sqlite_lvl1:
    def __init__(self, parent):
        self.base = parent
        self.primary = self.base + primary
        self.all = self.base + all_name


class SqliteGroup:
    def __init__(self):
        self.group = ["04. Testprotocol sqlite"]
        self.profiles_used = Sqlite_lvl1(self.group + used_profiles)


class Debit_lvl1:
    def __init__(self, parent):
        self.base = parent
        self.primary = self.base + primary
        self.secondary = self.base + secondary


class SlopeImoundment_lvl2:
    def __init__(self, parent):
        self.base = parent
        self.primary = self.base + primary
        self.secondary = self.base + secondary


class SlopeImpoundment_lvl1:
    def __init__(self, parent):
        self.base = parent
        self.structs = SlopeImoundment_lvl2(self.base + structs)
        self.channels = SlopeImoundment_lvl2(self.base + channels)


class HydToest0d1dGroup:
    def __init__(self, revision):
        self.group = (
            [f"05. Hydraulische Toets en 0d1d tests [#{revision}]"]
            if revision is not None
            else ["05. Hydraulische Toets en 0d1d tests"]
        )
        self.debit = Debit_lvl1(self.group + ["Kaart 1: Debiet"])
        self.sagging = self.group + ["Kaart 2: Uitzakking initieel peil"]
        self.level_maintaining = self.group + ["Kaart 3: Streefpeilhandhaving"]
        self.slope_impoundment = SlopeImpoundment_lvl1(
            self.group + ["Kaart 4: Verhang en opstuwing"]
        )
        self.stable_level_increase = self.group + [
            "Kaart 5: Stabiele waterstandsverhoging einde regen"
        ]
        self.level_recovery = self.group + ["Kaart 6: Herstel streefpeil"]


class OnedTwodGroup:
    def __init__(self, revision):
        self.group = (
            [f"07. Testprotocol 1d2d tests [#{revision}]"]
            if revision is not None
            else ["07. Testprotocol 1d2d tests"]
        )
        self.debit = self.group + ["Kaart 1: Debiet"]
        self.water_depth = self.group + ["Kaart 2: Waterdiepte"]
        self.water_level = self.group + ["Kaart 3: Waterstand"]


class QgisLayerStructure:
    """
    Represents the QGIS project structures main and subgroups
    If, for example, you want to access the name of
    05. Hydraulische Toets en 0d1d tests
        01. Kaart 1: Debiet
            primair
    you would access it like this:
    {class_instance}.hyd_test_and_0d1d.debit.primary
    """

    def __init__(self, zero_d_revision=None, one_d_revision=None):
        self.sqlite_group = SqliteGroup()
        self.hyd_test_and_0d1d = HydToest0d1dGroup(zero_d_revision)
        self.one_d_two_d = OnedTwodGroup(one_d_revision)
        self.bank_levels = ["06. Bank levels"]
