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
    <rasterrenderer classificationMin="0.067" type="singlebandpseudocolor" alphaBand="0" opacity="1" nodataColor="" classificationMax="0.2" band="1">
      <rasterTransparency/>
      <minMaxOrigin>
        <limits>None</limits>
        <extent>WholeRaster</extent>
        <statAccuracy>Exact</statAccuracy>
        <cumulativeCutLower>0.02</cumulativeCutLower>
        <cumulativeCutUpper>0.98</cumulativeCutUpper>
        <stdDevFactor>2</stdDevFactor>
      </minMaxOrigin>
      <rastershader>
        <colorrampshader colorRampType="INTERPOLATED" clip="0" labelPrecision="6" minimumValue="0.067" classificationMode="1" maximumValue="0.2">
          <item color="#fafafa" label="0.067" alpha="255" value="0.067"/>
          <item color="#dfdfdf" label="0.0818" alpha="255" value="0.0818"/>
          <item color="#c4c4c4" label="0.0966" alpha="255" value="0.0966"/>
          <item color="#a8a8a8" label="0.111" alpha="255" value="0.111"/>
          <item color="#8d8d8d" label="0.126" alpha="255" value="0.126"/>
          <item color="#727272" label="0.141" alpha="255" value="0.141"/>
          <item color="#575757" label="0.156" alpha="255" value="0.156"/>
          <item color="#3b3b3b" label="0.17" alpha="255" value="0.17"/>
          <item color="#202020" label="0.185" alpha="255" value="0.185"/>
          <item color="#050505" label="0.2" alpha="255" value="0.2"/>
        </colorrampshader>
      </rastershader>
    </rasterrenderer>
    <brightnesscontrast gamma="1" contrast="0" brightness="0"/>
    <huesaturation colorizeGreen="128" colorizeOn="0" colorizeBlue="128" colorizeStrength="100" colorizeRed="255" saturation="0" grayscaleMode="0"/>
    <rasterresampler zoomedOutResampler="bilinear" maxOversampling="2" zoomedInResampler="cubic"/>
    <resamplingStage>resamplingFilter</resamplingStage>
  </pipe>
  <originalStyle>
    <maplayer maxScale="inf" refreshOnNotifyEnabled="0" type="raster" hasScaleBasedVisibilityFlag="0" autoRefreshEnabled="0" autoRefreshTime="0" minScale="1e+08" styleCategories="AllStyleCategories" refreshOnNotifyMessage="">
      <id>friction_Marken20190520161435661</id>
      <datasource>../02. Sqlite modeldatabase/rasters/friction_waterland.tif</datasource>
      <keywordList>
        <value/>
      </keywordList>
      <layername>friction</layername>
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
        <noDataList bandNo="1" useSrcNoData="1"/>
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
        <rasterrenderer classificationMin="0.067" alphaBand="0" type="singlebandpseudocolor" opacity="1" classificationMax="0.2" band="1">
          <rasterTransparency/>
          <minMaxOrigin>
            <limits>None</limits>
            <extent>WholeRaster</extent>
            <statAccuracy>Exact</statAccuracy>
            <cumulativeCutLower>0.02</cumulativeCutLower>
            <cumulativeCutUpper>0.98</cumulativeCutUpper>
            <stdDevFactor>2</stdDevFactor>
          </minMaxOrigin>
          <rastershader>
            <colorrampshader clip="0" colorRampType="INTERPOLATED" classificationMode="1">
              <item color="#fafafa" label="0.067" alpha="255" value="0.067"/>
              <item color="#dfdfdf" label="0.0818" alpha="255" value="0.0818"/>
              <item color="#c4c4c4" label="0.0966" alpha="255" value="0.0966"/>
              <item color="#a8a8a8" label="0.111" alpha="255" value="0.111"/>
              <item color="#8d8d8d" label="0.126" alpha="255" value="0.126"/>
              <item color="#727272" label="0.141" alpha="255" value="0.141"/>
              <item color="#575757" label="0.156" alpha="255" value="0.156"/>
              <item color="#3b3b3b" label="0.17" alpha="255" value="0.17"/>
              <item color="#202020" label="0.185" alpha="255" value="0.185"/>
              <item color="#050505" label="0.2" alpha="255" value="0.2"/>
            </colorrampshader>
          </rastershader>
        </rasterrenderer>
        <brightnesscontrast contrast="0" brightness="0"/>
        <huesaturation colorizeGreen="128" colorizeOn="0" colorizeBlue="128" colorizeStrength="100" colorizeRed="255" saturation="0" grayscaleMode="0"/>
        <rasterresampler zoomedOutResampler="bilinear" maxOversampling="2" zoomedInResampler="cubic"/>
      </pipe>
      <blendMode>0</blendMode>
    </maplayer>
  </originalStyle>
  <blendMode>0</blendMode>
</qgis>
