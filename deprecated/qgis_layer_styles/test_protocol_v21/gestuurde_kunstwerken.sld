<?xml version="1.0" encoding="UTF-8"?>
<StyledLayerDescriptor xmlns="http://www.opengis.net/sld" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" version="1.1.0" xsi:schemaLocation="http://www.opengis.net/sld http://schemas.opengis.net/sld/1.1.0/StyledLayerDescriptor.xsd" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:se="http://www.opengis.net/se" xmlns:ogc="http://www.opengis.net/ogc">
  <NamedLayer>
    <se:Name>gestuurde_kunstwerken</se:Name>
    <UserStyle>
      <se:Name>gestuurde_kunstwerken</se:Name>
      <se:FeatureTypeStyle>
        <se:Rule>
          <se:Name>Single symbol</se:Name>
          <!--SymbolLayerV2 ArrowLine not implemented yet-->
        </se:Rule>
        <se:Rule>
          <se:MinScaleDenominator>0</se:MinScaleDenominator>
          <se:MaxScaleDenominator>41486</se:MaxScaleDenominator>
          <se:TextSymbolizer>
            <se:Label>
              <!--SE Export for code || '\n' || 'start: ' || start_action_value || '\n' || 'min: ' || min_action_value || '\n' || 'max: ' || max_action_value || '\n' not implemented yet-->Placeholder</se:Label>
            <se:Font>
              <se:SvgParameter name="font-family">MS Shell Dlg 2</se:SvgParameter>
              <se:SvgParameter name="font-size">10</se:SvgParameter>
            </se:Font>
            <se:LabelPlacement>
              <se:LinePlacement>
                <se:GeneralizeLine>true</se:GeneralizeLine>
              </se:LinePlacement>
            </se:LabelPlacement>
            <se:Halo>
              <se:Radius>2</se:Radius>
              <se:Fill>
                <se:SvgParameter name="fill">#ffffff</se:SvgParameter>
              </se:Fill>
            </se:Halo>
            <se:Fill>
              <se:SvgParameter name="fill">#000000</se:SvgParameter>
            </se:Fill>
            <se:VendorOption name="conflictResolution">false</se:VendorOption>
            <se:VendorOption name="group">yes</se:VendorOption>
          </se:TextSymbolizer>
        </se:Rule>
      </se:FeatureTypeStyle>
    </UserStyle>
  </NamedLayer>
</StyledLayerDescriptor>
