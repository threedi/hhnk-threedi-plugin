<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis maxScale="inf" version="3.16.11-Hannover" hasScaleBasedVisibilityFlag="0" minScale="1e+08" styleCategories="AllStyleCategories">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <temporal mode="0" enabled="0" fetchMode="0">
    <fixedRange>
      <start></start>
      <end></end>
    </fixedRange>
  </temporal>
  <customproperties>
    <property key="embeddedWidgets/count" value="0"/>
    <property key="identify/format" value="Value"/>
  </customproperties>
  <pipe>
    <provider>
      <resampling enabled="false" zoomedInResamplingMethod="nearestNeighbour" maxOversampling="2" zoomedOutResamplingMethod="nearestNeighbour"/>
    </provider>
    <rasterrenderer type="hillshade" alphaBand="0" azimuth="315" opacity="0.298039" nodataColor="" angle="45" zfactor="10" multidirection="0" band="1">
      <rasterTransparency/>
      <minMaxOrigin>
        <limits>None</limits>
        <extent>WholeRaster</extent>
        <statAccuracy>Estimated</statAccuracy>
        <cumulativeCutLower>0.02</cumulativeCutLower>
        <cumulativeCutUpper>0.98</cumulativeCutUpper>
        <stdDevFactor>2</stdDevFactor>
      </minMaxOrigin>
    </rasterrenderer>
    <brightnesscontrast gamma="1" contrast="0" brightness="0"/>
    <huesaturation colorizeGreen="128" colorizeOn="0" colorizeBlue="128" colorizeStrength="100" colorizeRed="255" saturation="0" grayscaleMode="0"/>
    <rasterresampler maxOversampling="2"/>
    <resamplingStage>resamplingFilter</resamplingStage>
  </pipe>
  <originalStyle>
    <maplayer maxScale="inf" refreshOnNotifyEnabled="0" type="raster" hasScaleBasedVisibilityFlag="0" autoRefreshEnabled="0" autoRefreshTime="0" minScale="1e+08" styleCategories="AllStyleCategories" refreshOnNotifyMessage="">
      <id>dem_Marken20190520161434272</id>
      <datasource>../02. Sqlite modeldatabase/rasters/dem_waterland.tif</datasource>
      <keywordList>
        <value/>
      </keywordList>
      <layername>dem hillshade</layername>
      <srs>
        <spatialrefsys>
          <proj4>+proj=sterea +lat_0=52.15616055555555 +lon_0=5.38763888888889 +k=0.9999079 +x_0=155000 +y_0=463000 +ellps=bessel +towgs84=565.2369,50.0087,465.658,-0.406857,0.350733,-1.87035,4.0812 +units=m +no_defs</proj4>
          <srsid>2517</srsid>
          <srid>28992</srid>
          <authid>EPSG:28992</authid>
          <description>Amersfoort / RD New</description>
          <projectionacronym>sterea</projectionacronym>
          <ellipsoidacronym>bessel</ellipsoidacronym>
          <geographicflag>false</geographicflag>
        </spatialrefsys>
      </srs>
      <resourceMetadata>
        <identifier/>
        <parentidentifier/>
        <language/>
        <type/>
        <title/>
        <abstract/>
        <links/>
        <fees/>
        <encoding/>
        <crs>
          <spatialrefsys>
            <proj4/>
            <srsid>0</srsid>
            <srid>0</srid>
            <authid/>
            <description/>
            <projectionacronym/>
            <ellipsoidacronym/>
            <geographicflag>true</geographicflag>
          </spatialrefsys>
        </crs>
        <extent/>
      </resourceMetadata>
      <provider>gdal</provider>
      <noData>
        <noDataList bandNo="1" useSrcNoData="1">
          <noDataRange min="10" max="10"/>
        </noDataList>
      </noData>
      <map-layer-style-manager current="standaard">
        <map-layer-style name="standaard"/>
      </map-layer-style-manager>
      <flags>
        <Identifiable>1</Identifiable>
        <Removable>1</Removable>
        <Searchable>1</Searchable>
      </flags>
      <customproperties>
        <property key="embeddedWidgets/count" value="0"/>
        <property key="identify/format" value="Value"/>
      </customproperties>
      <pipe>
        <rasterrenderer azimuth="315" alphaBand="0" type="hillshade" opacity="0.298039" angle="45" multidirection="0" zfactor="10" band="1">
          <rasterTransparency/>
          <minMaxOrigin>
            <limits>None</limits>
            <extent>WholeRaster</extent>
            <statAccuracy>Estimated</statAccuracy>
            <cumulativeCutLower>0.02</cumulativeCutLower>
            <cumulativeCutUpper>0.98</cumulativeCutUpper>
            <stdDevFactor>2</stdDevFactor>
          </minMaxOrigin>
        </rasterrenderer>
        <brightnesscontrast contrast="0" brightness="0"/>
        <huesaturation colorizeGreen="128" colorizeOn="0" colorizeBlue="128" colorizeStrength="100" colorizeRed="255" saturation="0" grayscaleMode="0"/>
        <rasterresampler maxOversampling="2"/>
      </pipe>
      <blendMode>0</blendMode>
    </maplayer>
  </originalStyle>
  <blendMode>0</blendMode>
</qgis>
