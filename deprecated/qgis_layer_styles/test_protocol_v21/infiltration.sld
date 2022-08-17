<?xml version="1.0" encoding="UTF-8"?>
<StyledLayerDescriptor xmlns="http://www.opengis.net/sld" version="1.0.0" xmlns:sld="http://www.opengis.net/sld" xmlns:gml="http://www.opengis.net/gml" xmlns:ogc="http://www.opengis.net/ogc">
  <UserLayer>
    <sld:LayerFeatureConstraints>
      <sld:FeatureTypeConstraint/>
    </sld:LayerFeatureConstraints>
    <sld:UserStyle>
      <sld:Name>infiltration</sld:Name>
      <sld:FeatureTypeStyle>
        <sld:Rule>
          <sld:RasterSymbolizer>
            <sld:ChannelSelection>
              <sld:GrayChannel>
                <sld:SourceChannelName>1</sld:SourceChannelName>
              </sld:GrayChannel>
            </sld:ChannelSelection>
            <sld:ColorMap type="ramp">
              <sld:ColorMapEntry color="#fafafa" quantity="0" label="0"/>
              <sld:ColorMapEntry color="#dfdfdf" quantity="33.3" label="33.3"/>
              <sld:ColorMapEntry color="#c4c4c4" quantity="66.59999999999999" label="66.6"/>
              <sld:ColorMapEntry color="#a8a8a8" quantity="99.90000000000001" label="99.9"/>
              <sld:ColorMapEntry color="#8d8d8d" quantity="133" label="133"/>
              <sld:ColorMapEntry color="#727272" quantity="166" label="166"/>
              <sld:ColorMapEntry color="#575757" quantity="200" label="200"/>
              <sld:ColorMapEntry color="#3b3b3b" quantity="233" label="233"/>
              <sld:ColorMapEntry color="#202020" quantity="266" label="266"/>
              <sld:ColorMapEntry color="#050505" quantity="300" label="300"/>
            </sld:ColorMap>
          </sld:RasterSymbolizer>
        </sld:Rule>
      </sld:FeatureTypeStyle>
    </sld:UserStyle>
  </UserLayer>
</StyledLayerDescriptor>
