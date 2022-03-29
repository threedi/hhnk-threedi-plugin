import numpy as np
from shapely.geometry import Point, LineString


def coordinates_to_points(nodes):
    """Input is r.nodes"""
    res_crds = nodes.coordinates
    crds_lst = np.vstack(res_crds.T)
    # convert to shapely format so we can create a geodataframe
    crds = [Point(crd) for crd in crds_lst]
    return crds


def line_geometries_to_coords(lines):
    """
    Coordinates read from threedi results netcdf can't be used as is in geodataframe
    Usage: lines = results.lines.channels.line_geometries where results = GridH5ResultAdmin object
    """
    coords = []
    for line in lines:
        if len(line) >= 4:
            x_coords = line[: int(line.size / 2)].tolist()
            y_coords = line[int(line.size / 2) :].tolist()
        else:
            # Fill in dummy coords
            x_coords = [0.0, 25000]
            y_coords = [0.0, 25000]
        line_list = []
        for x, y in zip(x_coords, y_coords):
            line_list.append([x, y])
        # Creates set of ([x1, y1], [x2, y2] ...., [xn, yn])
        coords.append(LineString(line_list))
    return coords


def extract_boundary_from_polygon(polygon, df_geo_col):
    """Extract the boundaries from a multipolygon.
    This way the intersection with the boundaries can be found."""
    try:
        lines_gdf = polygon.explode()
        lines_gdf[df_geo_col] = lines_gdf[df_geo_col].boundary
    except Exception as e:
        raise e from None
    return lines_gdf


def point_geometries_to_wkt(points):
    coords = []
    for point_x, point_y in zip(points[0], points[1]):
        coords.append(Point([point_x, point_y]))
    return coords
