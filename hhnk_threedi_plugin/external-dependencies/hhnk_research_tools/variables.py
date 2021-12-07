from osgeo import gdal

# default_variables
DEF_GEOMETRY_COL = "geometry"
DEF_TRGT_CRS = 28992
DEF_SRC_CRS = 4326
DEF_DELIMITER = ","
DEF_ENCODING = "utf-8"

# Download from http://www.gaia-gis.it/gaia-sins/windows-bin-amd64/ into anaconda installation
# Needs to be added to path before using.
MOD_SPATIALITE_PATH = r"C:\ProgramData\Anaconda3\mod_spatialite-5.0.1-win-amd64"


# definitions
WKT = "wkt"
GPKG_DRIVER = "GPKG"
ESRI_DRIVER = "ESRI Shapefile"
OPEN_FILE_GDB_DRIVER = "OpenFileGDB"

# types
#   Output file types: to prevent typo's and in case of remapping
TIF = "tif"
CSV = "csv"
QML = "qml"
TEXT = "txt"
SHAPE = "shp"
SQL = "sql"
GEOTIFF = "GTiff"
GPKG = "gpkg"
H5 = "h5"
NC = "nc"
SQLITE = "sqlite"
GDB = "gdb"
SHX = "shx"
DBF = "dbf"
PRJ = "prj"
GDAL_DATATYPE = gdal.GDT_Float32
file_types_dict = {
    "csv": ".csv",
    "txt": ".txt",
    "shp": ".shp",
    "sql": ".sql",
    "sqlite": ".sqlite",
    "tif": ".tif",
    "gdb": ".gdb",
    "gpkg": ".gpkg",
    "qml": ".qml",
    "h5": ".h5",
    "nc": ".nc",
    "shx": ".shx",
    "dbf": ".dbf",
    "prj": ".prj",
}
UTF8 = "utf-8"

# Gridadmin variable names
all_1d = "1D_ALL"
all_2d = "2D_ALL"

# rain
t_0_col = "t_0"
t_start_rain_col = "t_start_rain"
t_end_rain_min_one_col = "t_end_rain_min_one"
t_end_rain_col = "t_end_rain"
t_end_sum_col = "t_end_sum"
t_index_col = "value"

# Results
one_d_two_d = "1d2d"


class ThreediInformation:
    """
    Initialization:
    ThreediInformation(result, scenario_df)

    Members:
        result  (GridH5ResultAdmin object)
        scenario_df  (dataframe containing indexes of important timesteps
                        in rain scenario)
    return value: object
    """

    def __init__(self, result, df):
        self.result = result
        self.scenario_df = df
