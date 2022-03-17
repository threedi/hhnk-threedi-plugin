<?xml version="1.0" encoding="UTF-8"?>
<StyledLayerDescriptor xmlns="http://www.opengis.net/sld" version="1.0.0" xmlns:sld="http://www.opengis.net/sld" xmlns:gml="http://www.opengis.net/gml" xmlns:ogc="http://www.opengis.net/ogc">
  <UserLayer>
    <sld:LayerFeatureConstraints>
      <sld:FeatureTypeConstraint/>
    </sld:LayerFeatureConstraints>
    <sld:UserStyle>
      <sld:Name>dem</sld:Name>
      <sld:FeatureTypeStyle>
        <sld:Rule>
          <sld:RasterSymbolizer>
            <sld:ChannelSelection>
              <sld:GrayChannel>
                <sld:SourceChannelName>1</sld:SourceChannelName>
              </sld:GrayChannel>
            </sld:ChannelSelection>
            <sld:ColorMap type="ramp">
              <sld:ColorMapEntry color="#050603" quantity="-5" label="-5"/>
              <sld:ColorMapEntry color="#373724" quantity="-4" label="-4"/>
              <sld:ColorMapEntry color="#183e29" quantity="-3" label="-3"/>
              <sld:ColorMapEntry color="#346945" quantity="-2" label="-2"/>
              <sld:ColorMapEntry color="#3e8a59" quantity="-1" label="-1"/>
              <sld:ColorMapEntry color="#6ca363" quantity="0" label="0"/>
              <sld:ColorMapEntry color="#a5ba6f" quantity="1" label="1"/>
              <sld:ColorMapEntry color="#e7d57a" quantity="2" label="2"/>
              <sld:ColorMapEntry color="#c7a75c" quantity="3" label="3"/>
              <sld:ColorMapEntry color="#b0783a" quantity="4" label="4"/>
              <sld:ColorMapEntry color="#d77f3f" quantity="5" label="5"/>
              <sld:ColorMapEntry color="#103f5f" quantity="10" label="10"/>
            </sld:ColorMap>
          </sld:RasterSymbolizer>
        </sld:Rule>
      </sld:FeatureTypeStyle>
    </sld:UserStyle>
  </UserLayer>
</StyledLayerDescriptor>
