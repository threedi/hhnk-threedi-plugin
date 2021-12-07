<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis maxScale="0" version="3.16.11-Hannover" hasScaleBasedVisibilityFlag="0" minScale="1e+08" styleCategories="AllStyleCategories">
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
    <property key="identify/format" value="Undefined"/>
  </customproperties>
  <pipe>
    <provider>
      <resampling enabled="false" zoomedInResamplingMethod="nearestNeighbour" maxOversampling="2" zoomedOutResamplingMethod="nearestNeighbour"/>
    </provider>
    <rasterrenderer type="singlebandcolordata" alphaBand="-1" opacity="1" nodataColor="" band="1">
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
    <maplayer maxScale="0" refreshOnNotifyEnabled="0" type="raster" hasScaleBasedVisibilityFlag="0" autoRefreshEnabled="0" autoRefreshTime="0" minScale="1e+08" styleCategories="AllStyleCategories" refreshOnNotifyMessage="">
      <extent>
        <xmin>-370406.0832773745059967</xmin>
        <ymin>5180.78219399723457173</ymin>
        <xmax>680410.16862535197287798</xmax>
        <ymax>925274.94854621356353164</ymax>
      </extent>
      <id>Luchtfoto_Actueel_Ortho_25cm_RGB20190220111749895</id>
      <datasource>tileMatrixSet=EPSG:28992&amp;crs=EPSG:28992&amp;layers=Actueel_ortho25&amp;styles=default&amp;format=image/jpeg&amp;url=https://geodata.nationaalgeoregister.nl/luchtfoto/rgb/wmts?request%3DGetCapabilities%26service%3DWMTS</datasource>
      <keywordList>
        <value/>
      </keywordList>
      <layername>Luchtfoto Actueel Ortho 25cm RGB</layername>
      <srs>
        <spatialrefsys>
          <wkt>PROJCRS["Amersfoort / RD New",BASEGEOGCRS["Amersfoort",DATUM["Amersfoort",ELLIPSOID["Bessel 1841",6377397.155,299.1528128,LENGTHUNIT["metre",1]]],PRIMEM["Greenwich",0,ANGLEUNIT["degree",0.0174532925199433]],ID["EPSG",4289]],CONVERSION["RD New",METHOD["Oblique Stereographic",ID["EPSG",9809]],PARAMETER["Latitude of natural origin",52.1561605555556,ANGLEUNIT["degree",0.0174532925199433],ID["EPSG",8801]],PARAMETER["Longitude of natural origin",5.38763888888889,ANGLEUNIT["degree",0.0174532925199433],ID["EPSG",8802]],PARAMETER["Scale factor at natural origin",0.9999079,SCALEUNIT["unity",1],ID["EPSG",8805]],PARAMETER["False easting",155000,LENGTHUNIT["metre",1],ID["EPSG",8806]],PARAMETER["False northing",463000,LENGTHUNIT["metre",1],ID["EPSG",8807]]],CS[Cartesian,2],AXIS["easting (X)",east,ORDER[1],LENGTHUNIT["metre",1]],AXIS["northing (Y)",north,ORDER[2],LENGTHUNIT["metre",1]],USAGE[SCOPE["unknown"],AREA["Netherlands - onshore"],BBOX[50.75,3.2,53.7,7.22]],ID["EPSG",28992]]</wkt>
          <proj4>+proj=sterea +lat_0=52.1561605555556 +lon_0=5.38763888888889 +k=0.9999079 +x_0=155000 +y_0=463000 +ellps=bessel +towgs84=565.2369,50.0087,465.658,-0.406857330322398,0.350732676542563,-1.8703473836068,4.0812 +units=m +no_defs</proj4>
          <srsid>2517</srsid>
          <srid>28992</srid>
          <authid>EPSG:28992</authid>
          <description>Amersfoort / RD New</description>
          <projectionacronym>sterea</projectionacronym>
          <ellipsoidacronym>EPSG:7004</ellipsoidacronym>
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
            <wkt/>
            <proj4/>
            <srsid>0</srsid>
            <srid>0</srid>
            <authid/>
            <description/>
            <projectionacronym/>
            <ellipsoidacronym/>
            <geographicflag>false</geographicflag>
          </spatialrefsys>
        </crs>
        <extent/>
      </resourceMetadata>
      <provider>wms</provider>
      <noData>
        <noDataList bandNo="1" useSrcNoData="0"/>
      </noData>
      <map-layer-style-manager current="standaard">
        <map-layer-style name="standaard"/>
      </map-layer-style-manager>
      <flags>
        <Identifiable>1</Identifiable>
        <Removable>1</Removable>
        <Searchable>1</Searchable>
      </flags>
      <temporal mode="0" fetchMode="0" enabled="0">
        <fixedRange>
          <start/>
          <end/>
        </fixedRange>
      </temporal>
      <customproperties>
        <property key="identify/format" value="Undefined"/>
      </customproperties>
      <pipe>
        <provider>
          <resampling enabled="false" maxOversampling="2" zoomedInResamplingMethod="nearestNeighbour" zoomedOutResamplingMethod="nearestNeighbour"/>
        </provider>
        <rasterrenderer alphaBand="-1" type="singlebandcolordata" nodataColor="" opacity="1" band="1">
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
      <blendMode>0</blendMode>
    </maplayer>
  </originalStyle>
  <blendMode>0</blendMode>
</qgis>
