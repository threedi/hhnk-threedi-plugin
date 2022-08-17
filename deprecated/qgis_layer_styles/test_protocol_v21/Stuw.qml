<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis maxScale="1" simplifyMaxScale="1" version="3.16.11-Hannover" hasScaleBasedVisibilityFlag="1" simplifyDrawingHints="0" simplifyDrawingTol="1" simplifyAlgorithm="0" readOnly="0" labelsEnabled="0" minScale="25000" styleCategories="AllStyleCategories" simplifyLocal="1">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <temporal endField="" mode="0" startField="" startExpression="" enabled="0" durationField="" endExpression="" accumulate="0" fixedDuration="0" durationUnit="min">
    <fixedRange>
      <start></start>
      <end></end>
    </fixedRange>
  </temporal>
  <renderer-v2 type="RuleRenderer" forceraster="0" enableorderby="0" symbollevels="0">
    <rules key="{a0ba2603-be68-498f-bb2b-0ac962b9e640}">
      <rule symbol="0" key="{c5fa7c39-73dc-42b0-8624-b3b0b5452bff}" scalemaxdenom="25000" filter="concat(&quot;DAMO_W.Stuw.WS_CATEGORIE&quot;,',',&quot;DAMO_W.Stuw.SOORTREGELBAARHEID&quot;) = '2,1'" label="Secundair, vast" scalemindenom="1"/>
      <rule symbol="1" key="{cc1000b8-cb52-4521-a8a4-417dde33885f}" scalemaxdenom="25000" filter="concat(&quot;DAMO_W.Stuw.WS_CATEGORIE&quot;,',',&quot;DAMO_W.Stuw.SOORTREGELBAARHEID&quot;) = '2,&lt;Null>'" label="Secundair, vast" scalemindenom="1"/>
      <rule symbol="2" key="{ac7dc44d-fd90-4006-9f44-5f452ed30422}" scalemaxdenom="25000" filter="concat(&quot;DAMO_W.Stuw.WS_CATEGORIE&quot;,',',&quot;DAMO_W.Stuw.SOORTREGELBAARHEID&quot;) = '2,2'" label="Secundair, afsluitbaar" scalemindenom="1"/>
      <rule symbol="3" key="{c617e82f-4163-4211-a7ac-382f4e6128aa}" scalemaxdenom="25000" filter="concat(&quot;DAMO_W.Stuw.WS_CATEGORIE&quot;,',',&quot;DAMO_W.Stuw.SOORTREGELBAARHEID&quot;) = '2,4'" label="Secundair, afsluitbaar" scalemindenom="1"/>
      <rule symbol="4" key="{febb183d-3496-44f7-a67b-270e50efb7fa}" scalemaxdenom="25000" filter="concat(&quot;DAMO_W.Stuw.WS_CATEGORIE&quot;,',',&quot;DAMO_W.Stuw.SOORTREGELBAARHEID&quot;) = '2,3'" label="Secundair, afsluitbaar" scalemindenom="1"/>
      <rule symbol="5" key="{87eeda13-843f-46cb-b120-41d0fedd080b}" scalemaxdenom="50000" filter="concat(&quot;DAMO_W.Stuw.WS_CATEGORIE&quot;,',',&quot;DAMO_W.Stuw.SOORTREGELBAARHEID&quot;) = '1,1'" label="Primair, vast" scalemindenom="1"/>
      <rule symbol="6" key="{daebca81-d3cf-4225-8847-4e0b92e20823}" scalemaxdenom="50000" filter="concat(&quot;DAMO_W.Stuw.WS_CATEGORIE&quot;,',',&quot;DAMO_W.Stuw.SOORTREGELBAARHEID&quot;) = '1,2'" label="Primair, niet automatisch" scalemindenom="1"/>
      <rule symbol="7" key="{17076ee4-0181-41c8-9000-07b0bbf31f85}" scalemaxdenom="50000" filter="concat(&quot;DAMO_W.Stuw.WS_CATEGORIE&quot;,',',&quot;DAMO_W.Stuw.SOORTREGELBAARHEID&quot;) = '1,4'" label="Primair, niet automatisch" scalemindenom="1"/>
      <rule symbol="8" key="{39b52f76-9a24-4b95-8769-9d7ccd64735c}" scalemaxdenom="50000" filter="concat(&quot;DAMO_W.Stuw.WS_CATEGORIE&quot;,',',&quot;DAMO_W.Stuw.SOORTREGELBAARHEID&quot;) = '1,3'" label="Primair, automatisch" scalemindenom="1"/>
    </rules>
    <symbols>
      <symbol type="marker" name="0" clip_to_extent="1" force_rhr="0" alpha="1">
        <layer enabled="1" class="RasterMarker" locked="0" pass="0">
          <prop k="alpha" v="1"/>
          <prop k="angle" v="0"/>
          <prop k="fixedAspectRatio" v="0.0833333"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="imageFile" v="base64:iVBORw0KGgoAAAANSUhEUgAAABAAAAACCAYAAABR7VzxAAAAAXNSR0IB2cksfwAAAAlwSFlzAAAOxAAADsQBlSsOGwAAAChJREFUCJljYYCATQwMDEoMpIHTDAwMiSxQjhIDA4MGiQa8ZGBgYAAAzPkDPMUR6EUAAAAASUVORK5CYII="/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="Point"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="12"/>
          <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="size_unit" v="Point"/>
          <prop k="vertical_anchor_point" v="1"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol type="marker" name="1" clip_to_extent="1" force_rhr="0" alpha="1">
        <layer enabled="1" class="RasterMarker" locked="0" pass="0">
          <prop k="alpha" v="1"/>
          <prop k="angle" v="0"/>
          <prop k="fixedAspectRatio" v="0.0833333"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="imageFile" v="base64:iVBORw0KGgoAAAANSUhEUgAAABAAAAACCAYAAABR7VzxAAAAAXNSR0IB2cksfwAAAAlwSFlzAAAOxAAADsQBlSsOGwAAAChJREFUCJljYYCATQwMDEoMpIHTDAwMiSxQjhIDA4MGiQa8ZGBgYAAAzPkDPMUR6EUAAAAASUVORK5CYII="/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="Point"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="12"/>
          <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="size_unit" v="Point"/>
          <prop k="vertical_anchor_point" v="1"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol type="marker" name="2" clip_to_extent="1" force_rhr="0" alpha="1">
        <layer enabled="1" class="RasterMarker" locked="0" pass="0">
          <prop k="alpha" v="1"/>
          <prop k="angle" v="0"/>
          <prop k="fixedAspectRatio" v="0.333333"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="imageFile" v="base64:iVBORw0KGgoAAAANSUhEUgAAABAAAAAGCAYAAADKfB7nAAAAAXNSR0IB2cksfwAAAAlwSFlzAAAOxAAADsQBlSsOGwAAAGpJREFUGJWVj6ENwzAURB+wdFIsBVgG3aBrBHWIqEM12cijFBkEVUHHSpzwf+yBe7pLAJJetmcCkXTYbmnwDjwjAtsNWNKAD1AjAuALcC2owCMoOG+BpLft0AWgAVsCyDmvwBRpl1J+vXf+AZgbg1xN2rcAAAAASUVORK5CYII="/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="Point"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="12"/>
          <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="size_unit" v="Point"/>
          <prop k="vertical_anchor_point" v="1"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol type="marker" name="3" clip_to_extent="1" force_rhr="0" alpha="1">
        <layer enabled="1" class="RasterMarker" locked="0" pass="0">
          <prop k="alpha" v="1"/>
          <prop k="angle" v="0"/>
          <prop k="fixedAspectRatio" v="0.333333"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="imageFile" v="base64:iVBORw0KGgoAAAANSUhEUgAAABAAAAAGCAYAAADKfB7nAAAAAXNSR0IB2cksfwAAAAlwSFlzAAAOxAAADsQBlSsOGwAAAGpJREFUGJWVj6ENwzAURB+wdFIsBVgG3aBrBHWIqEM12cijFBkEVUHHSpzwf+yBe7pLAJJetmcCkXTYbmnwDjwjAtsNWNKAD1AjAuALcC2owCMoOG+BpLft0AWgAVsCyDmvwBRpl1J+vXf+AZgbg1xN2rcAAAAASUVORK5CYII="/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="Point"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="12"/>
          <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="size_unit" v="Point"/>
          <prop k="vertical_anchor_point" v="1"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol type="marker" name="4" clip_to_extent="1" force_rhr="0" alpha="1">
        <layer enabled="1" class="RasterMarker" locked="0" pass="0">
          <prop k="alpha" v="1"/>
          <prop k="angle" v="0"/>
          <prop k="fixedAspectRatio" v="0.333333"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="imageFile" v="base64:iVBORw0KGgoAAAANSUhEUgAAABAAAAAGCAYAAADKfB7nAAAAAXNSR0IB2cksfwAAAAlwSFlzAAAOxAAADsQBlSsOGwAAAGpJREFUGJWVj6ENwzAURB+wdFIsBVgG3aBrBHWIqEM12cijFBkEVUHHSpzwf+yBe7pLAJJetmcCkXTYbmnwDjwjAtsNWNKAD1AjAuALcC2owCMoOG+BpLft0AWgAVsCyDmvwBRpl1J+vXf+AZgbg1xN2rcAAAAASUVORK5CYII="/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="Point"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="12"/>
          <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="size_unit" v="Point"/>
          <prop k="vertical_anchor_point" v="1"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol type="marker" name="5" clip_to_extent="1" force_rhr="0" alpha="1">
        <layer enabled="1" class="RasterMarker" locked="0" pass="0">
          <prop k="alpha" v="1"/>
          <prop k="angle" v="0"/>
          <prop k="fixedAspectRatio" v="0.294118"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="imageFile" v="base64:iVBORw0KGgoAAAANSUhEUgAAABcAAAAHCAYAAADj/NY7AAAAAXNSR0IB2cksfwAAAAlwSFlzAAAOxAAADsQBlSsOGwAAAMRJREFUKJGdziFKRFEUBuAPHLiCIMMFw4uuwWDR2YDFYBJcgztwBwbbgFgMoskpGtyDmMRkErlBvNrkmCwzMsob5unfzvnhO6enPQvYRZrRfyfnfFdrvW3rei27hHNsz4Oh1vqBHVzPw5dwiTXs47ODv44R9nAxC+/jCqtN0wxKKfddPscwpfQUEWdYxvFvfAU34wObpZTHjjCIiAO8Yjg+cDiNb6WUFiNiA89/gadyhDec/MBzzg+11gFe/glPcor3yfAFJecx1NXHzQkAAAAASUVORK5CYII="/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="Point"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="17"/>
          <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="size_unit" v="Point"/>
          <prop k="vertical_anchor_point" v="1"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol type="marker" name="6" clip_to_extent="1" force_rhr="0" alpha="1">
        <layer enabled="1" class="RasterMarker" locked="0" pass="0">
          <prop k="alpha" v="1"/>
          <prop k="angle" v="0"/>
          <prop k="fixedAspectRatio" v="0.294118"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="imageFile" v="base64:iVBORw0KGgoAAAANSUhEUgAAABcAAAAHCAYAAADj/NY7AAAAAXNSR0IB2cksfwAAAAlwSFlzAAAOxAAADsQBlSsOGwAAAMFJREFUKJGd0CFLQwEQwPGfbHADsbxmEmyrAz+DTKvN7DewWU3WFU0iLBhtluWBxSBiVVSwyMPyhGsLPkXGG3vsH+/gx3FdCyqKYqeqqvVF+98y8xGfTbtuw2wtIs7KsjxeBte9YB9Py/Aexpm5ixN8t8D3MI2Ig8ycNOEb2MQV+jjEfcvLb3CRmbc4wgTv//EhrvGB04gYYNASl5lTvOISW/OXb/v52RBvmdnWne8Bz+j84RFxl5nn+FpVrRupXwIzew03Ja+yAwQAAAAASUVORK5CYII="/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="Point"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="17"/>
          <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="size_unit" v="Point"/>
          <prop k="vertical_anchor_point" v="1"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol type="marker" name="7" clip_to_extent="1" force_rhr="0" alpha="1">
        <layer enabled="1" class="RasterMarker" locked="0" pass="0">
          <prop k="alpha" v="1"/>
          <prop k="angle" v="0"/>
          <prop k="fixedAspectRatio" v="0.294118"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="imageFile" v="base64:iVBORw0KGgoAAAANSUhEUgAAABcAAAAHCAYAAADj/NY7AAAAAXNSR0IB2cksfwAAAAlwSFlzAAAOxAAADsQBlSsOGwAAAMFJREFUKJGd0CFLQwEQwPGfbHADsbxmEmyrAz+DTKvN7DewWU3WFU0iLBhtluWBxSBiVVSwyMPyhGsLPkXGG3vsH+/gx3FdCyqKYqeqqvVF+98y8xGfTbtuw2wtIs7KsjxeBte9YB9Py/Aexpm5ixN8t8D3MI2Ig8ycNOEb2MQV+jjEfcvLb3CRmbc4wgTv//EhrvGB04gYYNASl5lTvOISW/OXb/v52RBvmdnWne8Bz+j84RFxl5nn+FpVrRupXwIzew03Ja+yAwQAAAAASUVORK5CYII="/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="Point"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="17"/>
          <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="size_unit" v="Point"/>
          <prop k="vertical_anchor_point" v="1"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol type="marker" name="8" clip_to_extent="1" force_rhr="0" alpha="1">
        <layer enabled="1" class="RasterMarker" locked="0" pass="0">
          <prop k="alpha" v="1"/>
          <prop k="angle" v="0"/>
          <prop k="fixedAspectRatio" v="0.294118"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="imageFile" v="base64:iVBORw0KGgoAAAANSUhEUgAAABcAAAAHCAYAAADj/NY7AAAAAXNSR0IB2cksfwAAAAlwSFlzAAAOxAAADsQBlSsOGwAAALVJREFUKJGd0L0uhGEQBtBTbDJ+EhIJrbgNrWoTDZ1GQaOzl0I0q1HIBhFRKlwAN6MiWzydxssmPvHxdDOTOZnMQHcWcYLVH+azmeCuazDo6C3jAZs9YNjGAS5/w1fwWFULSTbw0gPfxwXmcf4Nr6qtJIfYgyRXVTXqebkkU4wxrqrTJKNPPMl6g3GLtyRzfXFcf+wvJTnGF441PGGI1z+gsznCLm5ao73lOckZpv+EW+6x04p3cZYypYQRlEYAAAAASUVORK5CYII="/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="Point"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="17"/>
          <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="size_unit" v="Point"/>
          <prop k="vertical_anchor_point" v="1"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </symbols>
  </renderer-v2>
  <customproperties>
    <property key="embeddedWidgets/count" value="0"/>
    <property key="variableNames"/>
    <property key="variableValues"/>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <SingleCategoryDiagramRenderer attributeLegend="1" diagramType="Histogram">
    <DiagramCategory lineSizeType="MM" height="15" opacity="1" enabled="0" penAlpha="255" sizeScale="3x:0,0,0,0,0,0" minScaleDenominator="500" spacing="0" spacingUnit="MM" scaleBasedVisibility="0" backgroundAlpha="255" maxScaleDenominator="1e+08" labelPlacementMethod="XHeight" penWidth="0" scaleDependency="Area" direction="1" penColor="#000000" backgroundColor="#ffffff" spacingUnitScale="3x:0,0,0,0,0,0" width="15" minimumSize="0" diagramOrientation="Up" lineSizeScale="3x:0,0,0,0,0,0" showAxis="0" sizeType="MM" rotationOffset="270" barWidth="5">
      <fontProperties style="" description="MS Shell Dlg 2,8.25,-1,5,50,0,0,0,0,0"/>
      <attribute color="#000000" field="" label=""/>
      <axisSymbol>
        <symbol type="line" name="" clip_to_extent="1" force_rhr="0" alpha="1">
          <layer enabled="1" class="SimpleLine" locked="0" pass="0">
            <prop k="align_dash_pattern" v="0"/>
            <prop k="capstyle" v="square"/>
            <prop k="customdash" v="5;2"/>
            <prop k="customdash_map_unit_scale" v="3x:0,0,0,0,0,0"/>
            <prop k="customdash_unit" v="MM"/>
            <prop k="dash_pattern_offset" v="0"/>
            <prop k="dash_pattern_offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
            <prop k="dash_pattern_offset_unit" v="MM"/>
            <prop k="draw_inside_polygon" v="0"/>
            <prop k="joinstyle" v="bevel"/>
            <prop k="line_color" v="35,35,35,255"/>
            <prop k="line_style" v="solid"/>
            <prop k="line_width" v="0.26"/>
            <prop k="line_width_unit" v="MM"/>
            <prop k="offset" v="0"/>
            <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
            <prop k="offset_unit" v="MM"/>
            <prop k="ring_filter" v="0"/>
            <prop k="tweak_dash_pattern_on_corners" v="0"/>
            <prop k="use_custom_dash" v="0"/>
            <prop k="width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
            <data_defined_properties>
              <Option type="Map">
                <Option type="QString" name="name" value=""/>
                <Option name="properties"/>
                <Option type="QString" name="type" value="collection"/>
              </Option>
            </data_defined_properties>
          </layer>
        </symbol>
      </axisSymbol>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings zIndex="0" showAll="1" obstacle="0" priority="0" placement="0" linePlacementFlags="18" dist="0">
    <properties>
      <Option type="Map">
        <Option type="QString" name="name" value=""/>
        <Option name="properties"/>
        <Option type="QString" name="type" value="collection"/>
      </Option>
    </properties>
  </DiagramLayerSettings>
  <geometryOptions geometryPrecision="0" removeDuplicateNodes="0">
    <activeChecks/>
    <checkConfiguration/>
  </geometryOptions>
  <legend type="default-vector"/>
  <referencedLayers/>
  <fieldConfiguration/>
  <aliases/>
  <defaults/>
  <constraints/>
  <constraintExpressions/>
  <expressionfields/>
  <attributeactions>
    <defaultAction key="Canvas" value="{00000000-0000-0000-0000-000000000000}"/>
  </attributeactions>
  <attributetableconfig actionWidgetStyle="dropDown" sortExpression="" sortOrder="0">
    <columns>
      <column type="field" name="DAMO_W.Stuw.OBJECTID" width="-1" hidden="0"/>
      <column type="field" name="DAMO_W.Stuw.CODE" width="-1" hidden="0"/>
      <column type="field" name="DAMO_W.Stuw.NAAM" width="-1" hidden="0"/>
      <column type="field" name="DAMO_W.Stuw.HYPERLINK" width="-1" hidden="0"/>
      <column type="field" name="DAMO_W.Stuw.OPMERKING" width="-1" hidden="0"/>
      <column type="field" name="DAMO_W.Stuw.INDICATIEWATERKEREND" width="-1" hidden="0"/>
      <column type="field" name="DAMO_W.Stuw.SOORTSTUW" width="-1" hidden="0"/>
      <column type="field" name="DAMO_W.Stuw.DOORSTROOMBREEDTE" width="-1" hidden="0"/>
      <column type="field" name="DAMO_W.Stuw.LAAGSTEDOORSTROOMHOOGTE" width="-1" hidden="0"/>
      <column type="field" name="DAMO_W.Stuw.HOOGSTEDOORSTROOMHOOGTE" width="-1" hidden="0"/>
      <column type="field" name="DAMO_W.Stuw.SOORTREGELBAARHEID" width="-1" hidden="0"/>
      <column type="field" name="DAMO_W.Stuw.WS_CATEGORIE" width="-1" hidden="0"/>
      <column type="field" name="DAMO_W.Stuw.WS_KRUINVORM" width="-1" hidden="0"/>
      <column type="field" name="DAMO_W.Stuw.WS_OP_AFSTAND_BEHEERD" width="-1" hidden="0"/>
      <column type="field" name="DAMO_W.Stuw.WS_BRON" width="-1" hidden="0"/>
      <column type="field" name="DAMO_W.Stuw.WS_INWINNINGSWIJZE" width="-1" hidden="0"/>
      <column type="field" name="DAMO_W.Stuw.WS_INWINNINGSDATUM" width="-1" hidden="0"/>
      <column type="field" name="DAMO_W.Stuw.WS_INWINNINGSWIJZE_ADMIN" width="-1" hidden="0"/>
      <column type="field" name="DAMO_W.Stuw.WS_INWINNINGSDATUM_ADMIN" width="-1" hidden="0"/>
      <column type="field" name="DAMO_W.Stuw.WS_VOLLEDIGHEID_DATASET" width="-1" hidden="0"/>
      <column type="field" name="DAMO_W.Stuw.WS_KWALITEITSSCORE" width="-1" hidden="0"/>
      <column type="field" name="DAMO_W.Stuw.WS_FUNCTIESTUW" width="-1" hidden="0"/>
      <column type="field" name="DAMO_W.Stuw.WS_OHPLICHT_KWK" width="-1" hidden="0"/>
      <column type="field" name="DAMO_W.Stuw.WS_INFORCODE" width="-1" hidden="0"/>
      <column type="field" name="DAMO_W.Stuw.GISOBJID" width="-1" hidden="0"/>
      <column type="field" name="kunstwerkxy.coordinaten" width="-1" hidden="0"/>
      <column type="field" name="DAMO_W.WS_OHPLICHT_KWK.WS_OHPLICHT_CONSTRUCTIE" width="-1" hidden="0"/>
      <column type="field" name="DAMO_W.WS_OHPLICHT_KWK.WS_OHPLICHT_AFVAL" width="-1" hidden="0"/>
      <column type="field" name="DAMO_W.WS_OHPLICHT_KWK.WS_OHPLICHT_NAT" width="-1" hidden="0"/>
      <column type="field" name="DAMO_W.WS_OHPLICHT_KWK.WS_OHPLICHT_DROOG" width="-1" hidden="0"/>
      <column type="actions" width="-1" hidden="1"/>
    </columns>
  </attributetableconfig>
  <conditionalstyles>
    <rowstyles/>
    <fieldstyles/>
  </conditionalstyles>
  <storedexpressions/>
  <editform tolerant="1"></editform>
  <editforminit/>
  <editforminitcodesource>0</editforminitcodesource>
  <editforminitfilepath></editforminitfilepath>
  <editforminitcode><![CDATA[# -*- coding: utf-8 -*-
"""
Formulieren van QGIS kunnen een functie voor Python hebben die wordt aangeroepen wanneer het formulier wordt geopend.

Gebruik deze functie om extra logica aan uw formulieren toe te voegen.

Voer de naam van de functie in in het veld "Python Init function".

Een voorbeeld volgt hieronder:
"""
from qgis.PyQt.QtWidgets import QWidget

def my_form_open(dialog, layer, feature):
	geom = feature.geometry()
	control = dialog.findChild(QWidget, "MyLineEdit")
]]></editforminitcode>
  <featformsuppress>0</featformsuppress>
  <editorlayout>generatedlayout</editorlayout>
  <editable>
    <field editable="1" name="DAMO_W.Stuw.CODE"/>
    <field editable="1" name="DAMO_W.Stuw.DOORSTROOMBREEDTE"/>
    <field editable="1" name="DAMO_W.Stuw.GISOBJID"/>
    <field editable="1" name="DAMO_W.Stuw.HOOGSTEDOORSTROOMHOOGTE"/>
    <field editable="1" name="DAMO_W.Stuw.HYPERLINK"/>
    <field editable="1" name="DAMO_W.Stuw.INDICATIEWATERKEREND"/>
    <field editable="1" name="DAMO_W.Stuw.LAAGSTEDOORSTROOMHOOGTE"/>
    <field editable="1" name="DAMO_W.Stuw.NAAM"/>
    <field editable="1" name="DAMO_W.Stuw.OBJECTID"/>
    <field editable="1" name="DAMO_W.Stuw.OPMERKING"/>
    <field editable="1" name="DAMO_W.Stuw.SOORTREGELBAARHEID"/>
    <field editable="1" name="DAMO_W.Stuw.SOORTSTUW"/>
    <field editable="1" name="DAMO_W.Stuw.WS_BRON"/>
    <field editable="1" name="DAMO_W.Stuw.WS_CATEGORIE"/>
    <field editable="1" name="DAMO_W.Stuw.WS_FUNCTIESTUW"/>
    <field editable="1" name="DAMO_W.Stuw.WS_INFORCODE"/>
    <field editable="1" name="DAMO_W.Stuw.WS_INWINNINGSDATUM"/>
    <field editable="1" name="DAMO_W.Stuw.WS_INWINNINGSDATUM_ADMIN"/>
    <field editable="1" name="DAMO_W.Stuw.WS_INWINNINGSWIJZE"/>
    <field editable="1" name="DAMO_W.Stuw.WS_INWINNINGSWIJZE_ADMIN"/>
    <field editable="1" name="DAMO_W.Stuw.WS_KRUINVORM"/>
    <field editable="1" name="DAMO_W.Stuw.WS_KWALITEITSSCORE"/>
    <field editable="1" name="DAMO_W.Stuw.WS_OHPLICHT_KWK"/>
    <field editable="1" name="DAMO_W.Stuw.WS_OP_AFSTAND_BEHEERD"/>
    <field editable="1" name="DAMO_W.Stuw.WS_VOLLEDIGHEID_DATASET"/>
    <field editable="1" name="DAMO_W.WS_OHPLICHT_KWK.WS_OHPLICHT_AFVAL"/>
    <field editable="1" name="DAMO_W.WS_OHPLICHT_KWK.WS_OHPLICHT_CONSTRUCTIE"/>
    <field editable="1" name="DAMO_W.WS_OHPLICHT_KWK.WS_OHPLICHT_DROOG"/>
    <field editable="1" name="DAMO_W.WS_OHPLICHT_KWK.WS_OHPLICHT_NAT"/>
    <field editable="1" name="kunstwerkxy.coordinaten"/>
  </editable>
  <labelOnTop>
    <field labelOnTop="0" name="DAMO_W.Stuw.CODE"/>
    <field labelOnTop="0" name="DAMO_W.Stuw.DOORSTROOMBREEDTE"/>
    <field labelOnTop="0" name="DAMO_W.Stuw.GISOBJID"/>
    <field labelOnTop="0" name="DAMO_W.Stuw.HOOGSTEDOORSTROOMHOOGTE"/>
    <field labelOnTop="0" name="DAMO_W.Stuw.HYPERLINK"/>
    <field labelOnTop="0" name="DAMO_W.Stuw.INDICATIEWATERKEREND"/>
    <field labelOnTop="0" name="DAMO_W.Stuw.LAAGSTEDOORSTROOMHOOGTE"/>
    <field labelOnTop="0" name="DAMO_W.Stuw.NAAM"/>
    <field labelOnTop="0" name="DAMO_W.Stuw.OBJECTID"/>
    <field labelOnTop="0" name="DAMO_W.Stuw.OPMERKING"/>
    <field labelOnTop="0" name="DAMO_W.Stuw.SOORTREGELBAARHEID"/>
    <field labelOnTop="0" name="DAMO_W.Stuw.SOORTSTUW"/>
    <field labelOnTop="0" name="DAMO_W.Stuw.WS_BRON"/>
    <field labelOnTop="0" name="DAMO_W.Stuw.WS_CATEGORIE"/>
    <field labelOnTop="0" name="DAMO_W.Stuw.WS_FUNCTIESTUW"/>
    <field labelOnTop="0" name="DAMO_W.Stuw.WS_INFORCODE"/>
    <field labelOnTop="0" name="DAMO_W.Stuw.WS_INWINNINGSDATUM"/>
    <field labelOnTop="0" name="DAMO_W.Stuw.WS_INWINNINGSDATUM_ADMIN"/>
    <field labelOnTop="0" name="DAMO_W.Stuw.WS_INWINNINGSWIJZE"/>
    <field labelOnTop="0" name="DAMO_W.Stuw.WS_INWINNINGSWIJZE_ADMIN"/>
    <field labelOnTop="0" name="DAMO_W.Stuw.WS_KRUINVORM"/>
    <field labelOnTop="0" name="DAMO_W.Stuw.WS_KWALITEITSSCORE"/>
    <field labelOnTop="0" name="DAMO_W.Stuw.WS_OHPLICHT_KWK"/>
    <field labelOnTop="0" name="DAMO_W.Stuw.WS_OP_AFSTAND_BEHEERD"/>
    <field labelOnTop="0" name="DAMO_W.Stuw.WS_VOLLEDIGHEID_DATASET"/>
    <field labelOnTop="0" name="DAMO_W.WS_OHPLICHT_KWK.WS_OHPLICHT_AFVAL"/>
    <field labelOnTop="0" name="DAMO_W.WS_OHPLICHT_KWK.WS_OHPLICHT_CONSTRUCTIE"/>
    <field labelOnTop="0" name="DAMO_W.WS_OHPLICHT_KWK.WS_OHPLICHT_DROOG"/>
    <field labelOnTop="0" name="DAMO_W.WS_OHPLICHT_KWK.WS_OHPLICHT_NAT"/>
    <field labelOnTop="0" name="kunstwerkxy.coordinaten"/>
  </labelOnTop>
  <dataDefinedFieldProperties/>
  <widgets/>
  <previewExpression>DAMO_W.Stuw.OBJECTID</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>0</layerGeometryType>
</qgis>
