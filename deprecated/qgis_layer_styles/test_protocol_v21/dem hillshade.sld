<?xml version="1.0" encoding="UTF-8"?>
<StyledLayerDescriptor xmlns="http://www.opengis.net/sld" version="1.0.0" xmlns:sld="http://www.opengis.net/sld" xmlns:gml="http://www.opengis.net/gml" xmlns:ogc="http://www.opengis.net/ogc">
  <UserLayer>
    <sld:LayerFeatureConstraints>
      <sld:FeatureTypeConstraint/>
    </sld:LayerFeatureConstraints>
    <sld:UserStyle>
      <sld:Name>dem hillshade</sld:Name>
      <sld:FeatureTypeStyle>
        <sld:Rule>
          <sld:RasterSymbolizer>
            <sld:Opacity>0.298039</sld:Opacity>
            <sld:ShadedRelief>
              <sld:BrightnessOnly>true</sld:BrightnessOnly>
              <sld:ReliefFactor>10</sld:ReliefFactor>
              <sld:VendorOption name="altitude">45</sld:VendorOption>
              <sld:VendorOption name="azimuth">315</sld:VendorOption>
              <sld:VendorOption name="multidirectional">0</sld:VendorOption>
            </sld:ShadedRelief>
          </sld:RasterSymbolizer>
        </sld:Rule>
      </sld:FeatureTypeStyle>
    </sld:UserStyle>
  </UserLayer>
</StyledLayerDescriptor>
