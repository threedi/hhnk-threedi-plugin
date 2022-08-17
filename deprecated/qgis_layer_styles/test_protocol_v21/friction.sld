<?xml version="1.0" encoding="UTF-8"?>
<StyledLayerDescriptor xmlns="http://www.opengis.net/sld" version="1.0.0" xmlns:sld="http://www.opengis.net/sld" xmlns:gml="http://www.opengis.net/gml" xmlns:ogc="http://www.opengis.net/ogc">
  <UserLayer>
    <sld:LayerFeatureConstraints>
      <sld:FeatureTypeConstraint/>
    </sld:LayerFeatureConstraints>
    <sld:UserStyle>
      <sld:Name>friction</sld:Name>
      <sld:FeatureTypeStyle>
        <sld:Rule>
          <sld:RasterSymbolizer>
            <sld:ChannelSelection>
              <sld:GrayChannel>
                <sld:SourceChannelName>1</sld:SourceChannelName>
              </sld:GrayChannel>
            </sld:ChannelSelection>
            <sld:ColorMap type="ramp">
              <sld:ColorMapEntry color="#fafafa" quantity="0.067" label="0.067"/>
              <sld:ColorMapEntry color="#dfdfdf" quantity="0.0818" label="0.0818"/>
              <sld:ColorMapEntry color="#c4c4c4" quantity="0.09660000000000001" label="0.0966"/>
              <sld:ColorMapEntry color="#a8a8a8" quantity="0.111" label="0.111"/>
              <sld:ColorMapEntry color="#8d8d8d" quantity="0.126" label="0.126"/>
              <sld:ColorMapEntry color="#727272" quantity="0.141" label="0.141"/>
              <sld:ColorMapEntry color="#575757" quantity="0.156" label="0.156"/>
              <sld:ColorMapEntry color="#3b3b3b" quantity="0.17" label="0.17"/>
              <sld:ColorMapEntry color="#202020" quantity="0.185" label="0.185"/>
              <sld:ColorMapEntry color="#050505" quantity="0.2" label="0.2"/>
            </sld:ColorMap>
          </sld:RasterSymbolizer>
        </sld:Rule>
      </sld:FeatureTypeStyle>
    </sld:UserStyle>
  </UserLayer>
</StyledLayerDescriptor>
