# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 16:24:32 2021

@author: chris.kerklaan
"""
import pandas as pd
import numpy as np
import geopandas as gpd
from shapely.geometry import Point
import hhnk_research_tools as hrt
import shapely.wkt as wkt
from shapely.geometry import MultiPoint, Point

from hhnk_research_tools.threedi.variables.results_mapping import one_d_two_d
from hhnk_research_tools.threedi.geometry_functions import point_geometries_to_wkt

from hhnk_research_tools.variables import UTF8, GPKG_DRIVER

DEF_TRGT_CRS = 28992
one_d_node_id_col = "1dnode_id"
node_id_col = "node_id"
node_geometry_col = "node_geometry"
node_type_col = "node_type"
init_wlevel_col = "initial_waterlevel"
storage_area_col = "storage_area"

connection_val = "connection"
added_calc_val = "added_calculation"
one_d_two_d_crosses_levee_val = "1d2d_crosses_levee"
one_d_two_d_crosses_fixed = "1d2d_crosses_fixeddrainage"
levee_id_col = "levee_id"
levee_height_col = "levee_height"

type_col = "type"


def read_1d2d_lines(results):
    """Uitlezen 1d2d lijnelementen
    Alle 1d2d lijnelementen in het model.
    """
    try:
        # Creates geodataframe with geometries of 1d2d subset of nodes in 3di results
        print(type(results))

        coords = hrt.threedi.line_geometries_to_coords(
            results.lines.subset(one_d_two_d).line_geometries
        )
        one_d_two_d_lines_gdf = gpd.GeoDataFrame(
            geometry=coords, crs=f"EPSG:{DEF_TRGT_CRS}"
        )

        # 1d nodes om te bepalen bij welk kunstwerk het hoort
        one_d_two_d_lines_gdf[one_d_node_id_col] = [
            a[1] for a in results.lines.subset(one_d_two_d).line_nodes
        ]
        one_d_two_d_lines_gdf[node_id_col] = results.nodes.filter(
            id__in=one_d_two_d_lines_gdf[one_d_node_id_col].tolist()
        ).content_pk
        one_d_two_d_lines_gdf.index = one_d_two_d_lines_gdf[one_d_node_id_col]

        # Get values corresponding to id's in onetwo_line_geo from results and add to dataframe
        oned_nodes_list = results.nodes.filter(
            id__in=one_d_two_d_lines_gdf[one_d_node_id_col].tolist()
        )
        oned_conn_nodes_id_list = oned_nodes_list.connectionnodes.id.tolist()
        oned_conn_nodes_init_wlvl_list = (
            oned_nodes_list.connectionnodes.initial_waterlevel.tolist()
        )
        oned_conn_nodes_storage_area_list = oned_nodes_list.connectionnodes.storage_area
        oned_added_calculation_nodes_list = (
            oned_nodes_list.added_calculationnodes.id.tolist()
        )

        # Add node geometries
        one_d_two_d_lines_gdf[node_geometry_col] = point_geometries_to_wkt(
            oned_nodes_list.coordinates
        )

        # Add information about node type
        one_d_two_d_lines_gdf.loc[
            one_d_two_d_lines_gdf[one_d_node_id_col].isin(oned_conn_nodes_id_list),
            node_type_col,
        ] = connection_val
        one_d_two_d_lines_gdf.loc[
            one_d_two_d_lines_gdf[one_d_node_id_col].isin(
                oned_added_calculation_nodes_list
            ),
            node_type_col,
        ] = added_calc_val

        # Add initial waterlevel to nodes
        one_d_two_d_lines_gdf.loc[
            one_d_two_d_lines_gdf[one_d_node_id_col].isin(oned_conn_nodes_id_list),
            init_wlevel_col,
        ] = oned_conn_nodes_init_wlvl_list

        # Add storage area from connection nodes to the table
        storage_area_lst = [a.decode(UTF8) for a in oned_conn_nodes_storage_area_list]
        one_d_two_d_lines_gdf.loc[
            one_d_two_d_lines_gdf[one_d_node_id_col].isin(oned_conn_nodes_id_list),
            storage_area_col,
        ] = storage_area_lst
        one_d_two_d_lines_gdf[storage_area_col] = pd.to_numeric(
            one_d_two_d_lines_gdf[storage_area_col]
        )
        return one_d_two_d_lines_gdf
    except Exception as e:
        raise e from None


def import_levees(results):
    def levees_to_linestring(levee_geom):
        try:
            levee_linestr = []
            for line in levee_geom:
                line.FlattenTo2D()  # Er staat nog een hoogte opgeslagen in de levee van 0. Deze wordt verwijderd.
                levee_linestr.append(wkt.loads(line.ExportToWkt()))
            return levee_linestr
        except Exception as e:
            raise e from None

    try:
        levee_line = levees_to_linestring(results.levees.geoms)
        levee_line_geo = gpd.GeoDataFrame(
            geometry=levee_line, crs=f"EPSG:{DEF_TRGT_CRS}"
        )
        levee_line_geo[levee_id_col] = results.levees.id
        levee_line_geo[levee_height_col] = results.levees.crest_level
        levee_line_geo.index = levee_line_geo[levee_id_col]
        return levee_line_geo
    except Exception as e:
        raise e from None


def make_line_geometries(cls, datasource, threedi_datasource):
    """

    create line geometries based on spatialite geometries but with
    segmentized for calculation core line segments
    :return:
    flattened array of line_geometries with length lines
    array[
        [x1, x2, x3, y1, y2, y3],
        [x1, x2, y1, y2]
    ]
    """

    DB_OBJECTS = [threedi_datasource.v2_channels, threedi_datasource.v2_culverts]

    LINE_TYPES = [constants.TYPE_V2_CHANNEL, constants.TYPE_V2_CULVERT]

    line_db_dict = dict(list(zip(LINE_TYPES, DB_OBJECTS)))

    size_array = as_numpy_array(datasource["lik"]).shape[0]
    line_geometries = np.full(size_array, 0, dtype=np.dtype("O"))
    start_x = datasource["line_coords"][0][:]
    start_y = datasource["line_coords"][1][:]
    end_x = datasource["line_coords"][2][:]
    end_y = datasource["line_coords"][3][:]
    kcu = datasource["kcu"][:]
    xys = np.array(list(zip(start_x.T, end_x.T, start_y.T, end_y.T)))
    for i in range(len(line_geometries)):
        line_geometries[i] = np.array(xys[i])

    for line_type, db_objects in line_db_dict.items():
        for db_object in db_objects:
            line_idx = np.where(
                (datasource["content_pk"][:] == db_object.pk)
                & (datasource["content_type"][:] == line_type)
            )[0]
            geom = wkt.loads(db_object.the_geom.wkt)
            line_geometries[line_idx] = _cut_geometries(
                geom,
                start_x[line_idx],
                start_y[line_idx],
                end_x[line_idx],
                end_y[line_idx],
                kcu[line_idx],
            )

    return line_geometries


def _cut_geometries(geom, start_x, start_y, end_x, end_y, kcu_array):
    """
    Segmentize line geometry based on start and end points from calc
    line segments

    :param geom: orginal geometry from the sqlite database
    :param start_x: threedicore x-coordinates for start points
    :param start_y: threedicore y-coordinates for start points
    :param end_x: threedicore x-coordinates for end points
    :param end_y: threedicore y-coordinates for end points
    :kcu_array: corresponding kcu values for threedicore coordinates

    :returns  an array of seperate line geometries for number of
    calc lines on geometry, like so::

        array[
            [x1, x2, x3, y1, y2, y3],
            [x1, x2, y1, y2]
        ]
    """

    cut_geometries = np.zeros((len(start_x),), dtype=np.dtype("O"))
    start_points = MultiPoint(list(zip(start_x, start_y)))
    end_points = MultiPoint(list(zip(end_x, end_y)))

    for piece in range(len(cut_geometries)):
        kcu = kcu_array[piece]
        if kcu == 0:
            start_pnt = geom.interpolate(geom.project(start_points[piece]))
            end_pnt = geom.interpolate(geom.project(end_points[piece]))
        else:
            start_pnt = start_points[piece]
            end_pnt = end_points[piece]
        start_distance = round(geom.project(start_pnt), 3)
        end_distance = round(geom.project(end_pnt), 3)

        # Don't use the z-coordinate
        if geom.has_z:
            coords = [(x, y) for x, y, z in geom.coords]
        else:
            coords = list(geom.coords)
        start_set = False
        # no additional calc points
        if start_distance <= 0.0 and end_distance >= geom.length:
            linestring = np.array(
                [(start_pnt.x, start_pnt.y)] + coords[1:-1] + [(end_pnt.x, end_pnt.y)]
            )
            # "F" means to flatten in column-major (Fortran- style) order
            cut_geometries[piece] = linestring.flatten("F")

        for i, p in enumerate(coords):
            # dist to vertex
            pd = round(geom.project(Point(p)), 3)

            # should not happen but sometimes drawing direction does not
            # correspond with start and endpoints, so flip them
            if start_distance > end_distance:
                # This is not safe!!!!!!
                # TODO: check if this actually can happen
                start_distance, end_distance = end_distance, start_distance
                start_points, end_points = end_points, start_points

            # check for start point
            if (pd == start_distance) and not start_set:
                start_pnt = []
                start_i = i
                start_set = True
            # should not happen but in case pd (point) and first vertex
            # do not have the same position move pd back
            elif (pd > start_distance) and not start_set:
                start_pnt = [(start_pnt.x, start_pnt.y)]
                start_i = i
                start_set = True
            if pd >= end_distance:
                linestring = np.array(
                    start_pnt + coords[start_i:i] + [(end_pnt.x, end_pnt.y)]
                )
                # "F" means to flatten in column-major (Fortran- style)
                # order
                cut_geometries[piece] = linestring.flatten("F")
                break

    return cut_geometries


def as_numpy_array(array):
    if hasattr(array, "value"):
        return array.value
    return array[:]
