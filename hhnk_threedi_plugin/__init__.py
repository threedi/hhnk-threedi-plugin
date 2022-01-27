# -*- coding: utf-8 -*-
"""
/***************************************************************************
 HHNK_toolbox
                                 A QGIS plugin
 Plugin voor watersystemen analyse
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2021-04-02
        copyright            : (C) 2021 by Laure Ravier, HHNK
        email                : L.Ravier@hhnk.nl
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""
from .dependencies import ensure_dependencies


#TODO
#research tools installatie uit osgeo weghalen. Sys path append hier van de github repo. 

# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load HHNK_toolbox class from file HHNK_toolbox.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    ensure_dependencies()
    from .hhnk_toolbox import HHNK_toolbox

    return HHNK_toolbox(iface)

import sys
sys.path.append('.')