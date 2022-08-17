<?xml version="1.0" encoding="UTF-8"?>
<StyledLayerDescriptor xmlns="http://www.opengis.net/sld" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" version="1.1.0" xsi:schemaLocation="http://www.opengis.net/sld http://schemas.opengis.net/sld/1.1.0/StyledLayerDescriptor.xsd" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:se="http://www.opengis.net/se" xmlns:ogc="http://www.opengis.net/ogc">
  <NamedLayer>
    <se:Name>Stuw</se:Name>
    <UserStyle>
      <se:Name>Stuw</se:Name>
      <se:FeatureTypeStyle>
        <se:Rule>
          <se:Name>Secundair, vast</se:Name>
          <se:Description>
            <se:Title>Secundair, vast</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:Function name="concat">
                <ogc:PropertyName>DAMO_W.Stuw.WS_CATEGORIE</ogc:PropertyName>
                <ogc:Literal>,</ogc:Literal>
                <ogc:PropertyName>DAMO_W.Stuw.SOORTREGELBAARHEID</ogc:PropertyName>
              </ogc:Function>
              <ogc:Literal>2,1</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>25000</se:MaxScaleDenominator>
          <se:PointSymbolizer>
            <!--QgsMarkerSymbolLayer RasterMarker not implemented yet-->
          </se:PointSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name>Secundair, vast</se:Name>
          <se:Description>
            <se:Title>Secundair, vast</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:Function name="concat">
                <ogc:PropertyName>DAMO_W.Stuw.WS_CATEGORIE</ogc:PropertyName>
                <ogc:Literal>,</ogc:Literal>
                <ogc:PropertyName>DAMO_W.Stuw.SOORTREGELBAARHEID</ogc:PropertyName>
              </ogc:Function>
              <ogc:Literal>2,&lt;Null></ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>25000</se:MaxScaleDenominator>
          <se:PointSymbolizer>
            <!--QgsMarkerSymbolLayer RasterMarker not implemented yet-->
          </se:PointSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name>Secundair, afsluitbaar</se:Name>
          <se:Description>
            <se:Title>Secundair, afsluitbaar</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:Function name="concat">
                <ogc:PropertyName>DAMO_W.Stuw.WS_CATEGORIE</ogc:PropertyName>
                <ogc:Literal>,</ogc:Literal>
                <ogc:PropertyName>DAMO_W.Stuw.SOORTREGELBAARHEID</ogc:PropertyName>
              </ogc:Function>
              <ogc:Literal>2,2</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>25000</se:MaxScaleDenominator>
          <se:PointSymbolizer>
            <!--QgsMarkerSymbolLayer RasterMarker not implemented yet-->
          </se:PointSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name>Secundair, afsluitbaar</se:Name>
          <se:Description>
            <se:Title>Secundair, afsluitbaar</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:Function name="concat">
                <ogc:PropertyName>DAMO_W.Stuw.WS_CATEGORIE</ogc:PropertyName>
                <ogc:Literal>,</ogc:Literal>
                <ogc:PropertyName>DAMO_W.Stuw.SOORTREGELBAARHEID</ogc:PropertyName>
              </ogc:Function>
              <ogc:Literal>2,4</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>25000</se:MaxScaleDenominator>
          <se:PointSymbolizer>
            <!--QgsMarkerSymbolLayer RasterMarker not implemented yet-->
          </se:PointSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name>Secundair, afsluitbaar</se:Name>
          <se:Description>
            <se:Title>Secundair, afsluitbaar</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:Function name="concat">
                <ogc:PropertyName>DAMO_W.Stuw.WS_CATEGORIE</ogc:PropertyName>
                <ogc:Literal>,</ogc:Literal>
                <ogc:PropertyName>DAMO_W.Stuw.SOORTREGELBAARHEID</ogc:PropertyName>
              </ogc:Function>
              <ogc:Literal>2,3</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>25000</se:MaxScaleDenominator>
          <se:PointSymbolizer>
            <!--QgsMarkerSymbolLayer RasterMarker not implemented yet-->
          </se:PointSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name>Primair, vast</se:Name>
          <se:Description>
            <se:Title>Primair, vast</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:Function name="concat">
                <ogc:PropertyName>DAMO_W.Stuw.WS_CATEGORIE</ogc:PropertyName>
                <ogc:Literal>,</ogc:Literal>
                <ogc:PropertyName>DAMO_W.Stuw.SOORTREGELBAARHEID</ogc:PropertyName>
              </ogc:Function>
              <ogc:Literal>1,1</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>25000</se:MaxScaleDenominator>
          <se:PointSymbolizer>
            <!--QgsMarkerSymbolLayer RasterMarker not implemented yet-->
          </se:PointSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name>Primair, niet automatisch</se:Name>
          <se:Description>
            <se:Title>Primair, niet automatisch</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:Function name="concat">
                <ogc:PropertyName>DAMO_W.Stuw.WS_CATEGORIE</ogc:PropertyName>
                <ogc:Literal>,</ogc:Literal>
                <ogc:PropertyName>DAMO_W.Stuw.SOORTREGELBAARHEID</ogc:PropertyName>
              </ogc:Function>
              <ogc:Literal>1,2</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>25000</se:MaxScaleDenominator>
          <se:PointSymbolizer>
            <!--QgsMarkerSymbolLayer RasterMarker not implemented yet-->
          </se:PointSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name>Primair, niet automatisch</se:Name>
          <se:Description>
            <se:Title>Primair, niet automatisch</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:Function name="concat">
                <ogc:PropertyName>DAMO_W.Stuw.WS_CATEGORIE</ogc:PropertyName>
                <ogc:Literal>,</ogc:Literal>
                <ogc:PropertyName>DAMO_W.Stuw.SOORTREGELBAARHEID</ogc:PropertyName>
              </ogc:Function>
              <ogc:Literal>1,4</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>25000</se:MaxScaleDenominator>
          <se:PointSymbolizer>
            <!--QgsMarkerSymbolLayer RasterMarker not implemented yet-->
          </se:PointSymbolizer>
        </se:Rule>
        <se:Rule>
          <se:Name>Primair, automatisch</se:Name>
          <se:Description>
            <se:Title>Primair, automatisch</se:Title>
          </se:Description>
          <ogc:Filter xmlns:ogc="http://www.opengis.net/ogc">
            <ogc:PropertyIsEqualTo>
              <ogc:Function name="concat">
                <ogc:PropertyName>DAMO_W.Stuw.WS_CATEGORIE</ogc:PropertyName>
                <ogc:Literal>,</ogc:Literal>
                <ogc:PropertyName>DAMO_W.Stuw.SOORTREGELBAARHEID</ogc:PropertyName>
              </ogc:Function>
              <ogc:Literal>1,3</ogc:Literal>
            </ogc:PropertyIsEqualTo>
          </ogc:Filter>
          <se:MinScaleDenominator>1</se:MinScaleDenominator>
          <se:MaxScaleDenominator>25000</se:MaxScaleDenominator>
          <se:PointSymbolizer>
            <!--QgsMarkerSymbolLayer RasterMarker not implemented yet-->
          </se:PointSymbolizer>
        </se:Rule>
      </se:FeatureTypeStyle>
    </UserStyle>
  </NamedLayer>
</StyledLayerDescriptor>
