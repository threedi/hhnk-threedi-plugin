<?xml version="1.0" encoding="UTF-8"?>
<StyledLayerDescriptor xmlns="http://www.opengis.net/sld" version="1.0.0" xmlns:sld="http://www.opengis.net/sld" xmlns:gml="http://www.opengis.net/gml" xmlns:ogc="http://www.opengis.net/ogc">
  <UserLayer>
    <sld:LayerFeatureConstraints>
      <sld:FeatureTypeConstraint/>
    </sld:LayerFeatureConstraints>
    <sld:UserStyle>
      <sld:Name>cw_schade_plas_correctie</sld:Name>
      <sld:FeatureTypeStyle>
        <sld:Rule>
          <sld:RasterSymbolizer>
            <sld:ChannelSelection>
              <sld:GrayChannel>
                <sld:SourceChannelName>1</sld:SourceChannelName>
              </sld:GrayChannel>
            </sld:ChannelSelection>
            <sld:ColorMap type="intervals">
              <sld:ColorMapEntry color="#ffffb2" quantity="10" label="&lt;= 10"/>
              <sld:ColorMapEntry color="#ffd76d" quantity="20" label="10 - 20"/>
              <sld:ColorMapEntry color="#fea649" quantity="30" label="20 - 30"/>
              <sld:ColorMapEntry color="#f86c30" quantity="40" label="30 - 40"/>
              <sld:ColorMapEntry color="#e62f21" quantity="50" label="40 - 50"/>
              <sld:ColorMapEntry color="#bd0026" quantity="inf" label="> 50"/>
            </sld:ColorMap>
          </sld:RasterSymbolizer>
        </sld:Rule>
      </sld:FeatureTypeStyle>
    </sld:UserStyle>
  </UserLayer>
</StyledLayerDescriptor>
