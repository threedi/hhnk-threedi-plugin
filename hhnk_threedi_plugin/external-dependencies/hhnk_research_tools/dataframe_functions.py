import geopandas as gpd
from shapely import wkt
import os
from hhnk_research_tools.variables import WKT, GPKG_DRIVER
from hhnk_research_tools.variables import (
    DEF_GEOMETRY_COL,
    DEF_SRC_CRS,
    DEF_TRGT_CRS,
    DEF_DELIMITER,
    DEF_ENCODING,
)
from hhnk_research_tools.variables import file_types_dict, GPKG, CSV
from hhnk_research_tools.general_functions import ensure_file_path

# Conversion
def _set_geometry_by_type(df, geom_col_type, col=DEF_GEOMETRY_COL):
    """
    Converts geometry if necessary, depending on geometry column type

        _set_geometry_by_type(
            df (pandas DataFrame),
            geom_col_type (string: type of geometry)
            col -> 'geometry' (string: name of column containing geometry in df)

    replaces geometry column with converted values
    """
    if geom_col_type == WKT:
        try:
            df[col] = df[col].apply(wkt.loads)
        except Exception as e:
            raise e from None


# TODO convert_df_to_gdf en create_gdf_from_df zijn geworden; convert_df_to_gdf
# TODO make this more logical, it now handles two types of geometry_cols under the same variable.
def df_convert_to_gdf(
    df,
    geom_col_type=WKT,
    geometry_col=DEF_GEOMETRY_COL,
    src_crs=DEF_SRC_CRS,
    trgt_crs=DEF_TRGT_CRS,
):
    """
    Convert a pandas DataFrame to a geopandas GeoDataFrame

    geometry_col can both be a column name or a pd.Series.
    When a pandas series is provided it already needs to be shapely geometry type


        df_convert_to_gdf(
            df (original pandas dataframe)
            geom_col_type -> WKT (type of geometry column to make sure geometry is interpreted correctly)
            geometry_col -> 'geometry' (string: name of column in df to be used as geometry)
            src_crs -> 4326 (original projection geometry)
            trgt_crs -> 28992 (crs to convert geometry to)
            )
    """
    src_epsg = f"EPSG:{src_crs}"
    try:
        if type(geometry_col) == str:
            _set_geometry_by_type(df, geom_col_type, geometry_col)
        gdf = gpd.GeoDataFrame(df, geometry=geometry_col, crs=src_epsg)
        gdf.to_crs(epsg=trgt_crs, inplace=True)
        return gdf
    except Exception as e:
        raise e from None


def df_add_geometry_to_gdf(df, geometry_col, crs=DEF_TRGT_CRS) -> gpd.GeoDataFrame:
    """
    Creates geopandas GeoDataFrame from pandas DataFrame

        df_add_geometry_to_gdf(
                df (pandas DataFrame)
                geometry_col (Geometry column for GeoDataFrame)
                crs (projection) -> 28992
            )

    return value: GeoDataFrame with df as data, geometry_col as geometry and crs as crs
    """
    trgt_crs = f"EPSG:{crs}"
    try:
        gdf = gpd.GeoDataFrame(df, geometry=geometry_col, crs=trgt_crs)
        return gdf
    except Exception as e:
        raise e from None


# Saving
def gdf_write_to_geopackage(gdf, path=None, filename=None, filepath=None, driver=GPKG_DRIVER, index=False):
    """
    Functions outputs DataFrame of GeoDataFrame to .gpkg document

        gdf_write_to_csv(
            gdf (DataFrame, to be written to .gpkg file)
            path (string, folder to create new file in)
            filename (string, name of file to be created, without extension (.csv)
            driver -> 'GPKG' (driver to be used by .to_file function of gdf)
            index -> False (given as index parameter to .to_file function of gdf (Write row names or not)

    Return value: file path (path + filename + extension) if gdf is not empty, else None
    """
    ext = file_types_dict[GPKG]
    if filepath is None:
        filepath = os.path.join(path, filename + ext)
        
    try:
        if os.path.exists(filepath):
            os.remove(filepath)
        if not gdf.empty:
            ensure_file_path(filepath)
            if filename is None:
                gdf.to_file(filepath, driver=driver, index=index)
            else:
                gdf.to_file(filepath, layer=filename, driver=driver, index=index)

            return filepath
        return None
    except Exception as e:
        raise e from None


def gdf_write_to_csv(gdf, path=None, filename=None, filepath=None, mode="w", cols=None, index=False):
    """
    Functions outputs DataFrame of GeoDataFrame to .csv document

        gdf_write_to_csv(
            gdf (DataFrame, to be written to .csv file)
            path (string, folder to create new file in)
            filename (string, name of file to be created, without extension (.csv)
            mode -> 'w' (optional specification of write mode)
            cols -> None (specify columns to write to output)
            index -> False (given as index parameter to .to_csv function of gdf (Write row names or not)

    Return value: file path (path + filename + extension) if gdf is not empty, else None
    """
    ext = file_types_dict[CSV]
    if filepath is None:
        filepath = os.path.join(path, filename + ext)
    try:
        if filename:
            ensure_file_path(filename)
        if os.path.exists(filepath):
            os.remove(filepath)
        if not gdf.empty:
            ensure_file_path(filepath)
            gdf.to_csv(
                filepath,
                sep=DEF_DELIMITER,
                encoding=DEF_ENCODING,
                columns=cols,
                mode=mode,
                index=index,
            )
            return filepath
        else:
            return None
    except Exception as e:
        raise e from None
