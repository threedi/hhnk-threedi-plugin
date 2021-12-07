<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis simplifyLocal="1" readOnly="0" labelsEnabled="0" styleCategories="AllStyleCategories" simplifyAlgorithm="0" hasScaleBasedVisibilityFlag="1" minScale="25000" simplifyMaxScale="1" version="3.16.11-Hannover" maxScale="1" simplifyDrawingTol="1" simplifyDrawingHints="0">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <temporal fixedDuration="0" enabled="0" endField="" durationField="" accumulate="0" startField="" durationUnit="min" startExpression="" mode="0" endExpression="">
    <fixedRange>
      <start></start>
      <end></end>
    </fixedRange>
  </temporal>
  <renderer-v2 symbollevels="0" forceraster="0" type="RuleRenderer" enableorderby="0">
    <rules key="{a0ba2603-be68-498f-bb2b-0ac962b9e640}">
      <rule symbol="0" scalemaxdenom="25000" key="{c5fa7c39-73dc-42b0-8624-b3b0b5452bff}" scalemindenom="1" label="Secundair, vast" filter="concat(&quot;DAMO_W.Stuw.WS_CATEGORIE&quot;,',',&quot;DAMO_W.Stuw.SOORTREGELBAARHEID&quot;) = '2,1'"/>
      <rule symbol="1" scalemaxdenom="25000" key="{cc1000b8-cb52-4521-a8a4-417dde33885f}" scalemindenom="1" label="Secundair, vast" filter="concat(&quot;DAMO_W.Stuw.WS_CATEGORIE&quot;,',',&quot;DAMO_W.Stuw.SOORTREGELBAARHEID&quot;) = '2,&lt;Null>'"/>
      <rule symbol="2" scalemaxdenom="25000" key="{ac7dc44d-fd90-4006-9f44-5f452ed30422}" scalemindenom="1" label="Secundair, afsluitbaar" filter="concat(&quot;DAMO_W.Stuw.WS_CATEGORIE&quot;,',',&quot;DAMO_W.Stuw.SOORTREGELBAARHEID&quot;) = '2,2'"/>
      <rule symbol="3" scalemaxdenom="25000" key="{c617e82f-4163-4211-a7ac-382f4e6128aa}" scalemindenom="1" label="Secundair, afsluitbaar" filter="concat(&quot;DAMO_W.Stuw.WS_CATEGORIE&quot;,',',&quot;DAMO_W.Stuw.SOORTREGELBAARHEID&quot;) = '2,4'"/>
      <rule symbol="4" scalemaxdenom="25000" key="{febb183d-3496-44f7-a67b-270e50efb7fa}" scalemindenom="1" label="Secundair, afsluitbaar" filter="concat(&quot;DAMO_W.Stuw.WS_CATEGORIE&quot;,',',&quot;DAMO_W.Stuw.SOORTREGELBAARHEID&quot;) = '2,3'"/>
      <rule symbol="5" scalemaxdenom="50000" key="{87eeda13-843f-46cb-b120-41d0fedd080b}" scalemindenom="1" label="Primair, vast" filter="concat(&quot;DAMO_W.Stuw.WS_CATEGORIE&quot;,',',&quot;DAMO_W.Stuw.SOORTREGELBAARHEID&quot;) = '1,1'"/>
      <rule symbol="6" scalemaxdenom="50000" key="{daebca81-d3cf-4225-8847-4e0b92e20823}" scalemindenom="1" label="Primair, niet automatisch" filter="concat(&quot;DAMO_W.Stuw.WS_CATEGORIE&quot;,',',&quot;DAMO_W.Stuw.SOORTREGELBAARHEID&quot;) = '1,2'"/>
      <rule symbol="7" scalemaxdenom="50000" key="{17076ee4-0181-41c8-9000-07b0bbf31f85}" scalemindenom="1" label="Primair, niet automatisch" filter="concat(&quot;DAMO_W.Stuw.WS_CATEGORIE&quot;,',',&quot;DAMO_W.Stuw.SOORTREGELBAARHEID&quot;) = '1,4'"/>
      <rule symbol="8" scalemaxdenom="50000" key="{39b52f76-9a24-4b95-8769-9d7ccd64735c}" scalemindenom="1" label="Primair, automatisch" filter="concat(&quot;DAMO_W.Stuw.WS_CATEGORIE&quot;,',',&quot;DAMO_W.Stuw.SOORTREGELBAARHEID&quot;) = '1,3'"/>
    </rules>
    <symbols>
      <symbol type="marker" name="0" alpha="1" clip_to_extent="1" force_rhr="0">
        <layer enabled="1" pass="0" class="RasterMarker" locked="0">
          <prop v="1" k="alpha"/>
          <prop v="0" k="angle"/>
          <prop v="0.0833333" k="fixedAspectRatio"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="base64:iVBORw0KGgoAAAANSUhEUgAAABAAAAACCAYAAABR7VzxAAAAAXNSR0IB2cksfwAAAAlwSFlzAAAOxAAADsQBlSsOGwAAAChJREFUCJljYYCATQwMDEoMpIHTDAwMiSxQjhIDA4MGiQa8ZGBgYAAAzPkDPMUR6EUAAAAASUVORK5CYII=" k="imageFile"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="Point" k="offset_unit"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="12" k="size"/>
          <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
          <prop v="Point" k="size_unit"/>
          <prop v="1" k="vertical_anchor_point"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol type="marker" name="1" alpha="1" clip_to_extent="1" force_rhr="0">
        <layer enabled="1" pass="0" class="RasterMarker" locked="0">
          <prop v="1" k="alpha"/>
          <prop v="0" k="angle"/>
          <prop v="0.0833333" k="fixedAspectRatio"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="base64:iVBORw0KGgoAAAANSUhEUgAAABAAAAACCAYAAABR7VzxAAAAAXNSR0IB2cksfwAAAAlwSFlzAAAOxAAADsQBlSsOGwAAAChJREFUCJljYYCATQwMDEoMpIHTDAwMiSxQjhIDA4MGiQa8ZGBgYAAAzPkDPMUR6EUAAAAASUVORK5CYII=" k="imageFile"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="Point" k="offset_unit"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="12" k="size"/>
          <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
          <prop v="Point" k="size_unit"/>
          <prop v="1" k="vertical_anchor_point"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol type="marker" name="2" alpha="1" clip_to_extent="1" force_rhr="0">
        <layer enabled="1" pass="0" class="RasterMarker" locked="0">
          <prop v="1" k="alpha"/>
          <prop v="0" k="angle"/>
          <prop v="0.333333" k="fixedAspectRatio"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="base64:iVBORw0KGgoAAAANSUhEUgAAABAAAAAGCAYAAADKfB7nAAAAAXNSR0IB2cksfwAAAAlwSFlzAAAOxAAADsQBlSsOGwAAAGpJREFUGJWVj6ENwzAURB+wdFIsBVgG3aBrBHWIqEM12cijFBkEVUHHSpzwf+yBe7pLAJJetmcCkXTYbmnwDjwjAtsNWNKAD1AjAuALcC2owCMoOG+BpLft0AWgAVsCyDmvwBRpl1J+vXf+AZgbg1xN2rcAAAAASUVORK5CYII=" k="imageFile"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="Point" k="offset_unit"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="12" k="size"/>
          <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
          <prop v="Point" k="size_unit"/>
          <prop v="1" k="vertical_anchor_point"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol type="marker" name="3" alpha="1" clip_to_extent="1" force_rhr="0">
        <layer enabled="1" pass="0" class="RasterMarker" locked="0">
          <prop v="1" k="alpha"/>
          <prop v="0" k="angle"/>
          <prop v="0.333333" k="fixedAspectRatio"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="base64:iVBORw0KGgoAAAANSUhEUgAAABAAAAAGCAYAAADKfB7nAAAAAXNSR0IB2cksfwAAAAlwSFlzAAAOxAAADsQBlSsOGwAAAGpJREFUGJWVj6ENwzAURB+wdFIsBVgG3aBrBHWIqEM12cijFBkEVUHHSpzwf+yBe7pLAJJetmcCkXTYbmnwDjwjAtsNWNKAD1AjAuALcC2owCMoOG+BpLft0AWgAVsCyDmvwBRpl1J+vXf+AZgbg1xN2rcAAAAASUVORK5CYII=" k="imageFile"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="Point" k="offset_unit"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="12" k="size"/>
          <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
          <prop v="Point" k="size_unit"/>
          <prop v="1" k="vertical_anchor_point"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol type="marker" name="4" alpha="1" clip_to_extent="1" force_rhr="0">
        <layer enabled="1" pass="0" class="RasterMarker" locked="0">
          <prop v="1" k="alpha"/>
          <prop v="0" k="angle"/>
          <prop v="0.333333" k="fixedAspectRatio"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="base64:iVBORw0KGgoAAAANSUhEUgAAABAAAAAGCAYAAADKfB7nAAAAAXNSR0IB2cksfwAAAAlwSFlzAAAOxAAADsQBlSsOGwAAAGpJREFUGJWVj6ENwzAURB+wdFIsBVgG3aBrBHWIqEM12cijFBkEVUHHSpzwf+yBe7pLAJJetmcCkXTYbmnwDjwjAtsNWNKAD1AjAuALcC2owCMoOG+BpLft0AWgAVsCyDmvwBRpl1J+vXf+AZgbg1xN2rcAAAAASUVORK5CYII=" k="imageFile"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="Point" k="offset_unit"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="12" k="size"/>
          <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
          <prop v="Point" k="size_unit"/>
          <prop v="1" k="vertical_anchor_point"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol type="marker" name="5" alpha="1" clip_to_extent="1" force_rhr="0">
        <layer enabled="1" pass="0" class="RasterMarker" locked="0">
          <prop v="1" k="alpha"/>
          <prop v="0" k="angle"/>
          <prop v="0.294118" k="fixedAspectRatio"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="base64:iVBORw0KGgoAAAANSUhEUgAAABcAAAAHCAYAAADj/NY7AAAAAXNSR0IB2cksfwAAAAlwSFlzAAAOxAAADsQBlSsOGwAAAMRJREFUKJGdziFKRFEUBuAPHLiCIMMFw4uuwWDR2YDFYBJcgztwBwbbgFgMoskpGtyDmMRkErlBvNrkmCwzMsob5unfzvnhO6enPQvYRZrRfyfnfFdrvW3rei27hHNsz4Oh1vqBHVzPw5dwiTXs47ODv44R9nAxC+/jCqtN0wxKKfddPscwpfQUEWdYxvFvfAU34wObpZTHjjCIiAO8Yjg+cDiNb6WUFiNiA89/gadyhDec/MBzzg+11gFe/glPcor3yfAFJecx1NXHzQkAAAAASUVORK5CYII=" k="imageFile"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="Point" k="offset_unit"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="17" k="size"/>
          <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
          <prop v="Point" k="size_unit"/>
          <prop v="1" k="vertical_anchor_point"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol type="marker" name="6" alpha="1" clip_to_extent="1" force_rhr="0">
        <layer enabled="1" pass="0" class="RasterMarker" locked="0">
          <prop v="1" k="alpha"/>
          <prop v="0" k="angle"/>
          <prop v="0.294118" k="fixedAspectRatio"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="base64:iVBORw0KGgoAAAANSUhEUgAAABcAAAAHCAYAAADj/NY7AAAAAXNSR0IB2cksfwAAAAlwSFlzAAAOxAAADsQBlSsOGwAAAMFJREFUKJGd0CFLQwEQwPGfbHADsbxmEmyrAz+DTKvN7DewWU3WFU0iLBhtluWBxSBiVVSwyMPyhGsLPkXGG3vsH+/gx3FdCyqKYqeqqvVF+98y8xGfTbtuw2wtIs7KsjxeBte9YB9Py/Aexpm5ixN8t8D3MI2Ig8ycNOEb2MQV+jjEfcvLb3CRmbc4wgTv//EhrvGB04gYYNASl5lTvOISW/OXb/v52RBvmdnWne8Bz+j84RFxl5nn+FpVrRupXwIzew03Ja+yAwQAAAAASUVORK5CYII=" k="imageFile"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="Point" k="offset_unit"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="17" k="size"/>
          <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
          <prop v="Point" k="size_unit"/>
          <prop v="1" k="vertical_anchor_point"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol type="marker" name="7" alpha="1" clip_to_extent="1" force_rhr="0">
        <layer enabled="1" pass="0" class="RasterMarker" locked="0">
          <prop v="1" k="alpha"/>
          <prop v="0" k="angle"/>
          <prop v="0.294118" k="fixedAspectRatio"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="base64:iVBORw0KGgoAAAANSUhEUgAAABcAAAAHCAYAAADj/NY7AAAAAXNSR0IB2cksfwAAAAlwSFlzAAAOxAAADsQBlSsOGwAAAMFJREFUKJGd0CFLQwEQwPGfbHADsbxmEmyrAz+DTKvN7DewWU3WFU0iLBhtluWBxSBiVVSwyMPyhGsLPkXGG3vsH+/gx3FdCyqKYqeqqvVF+98y8xGfTbtuw2wtIs7KsjxeBte9YB9Py/Aexpm5ixN8t8D3MI2Ig8ycNOEb2MQV+jjEfcvLb3CRmbc4wgTv//EhrvGB04gYYNASl5lTvOISW/OXb/v52RBvmdnWne8Bz+j84RFxl5nn+FpVrRupXwIzew03Ja+yAwQAAAAASUVORK5CYII=" k="imageFile"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="Point" k="offset_unit"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="17" k="size"/>
          <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
          <prop v="Point" k="size_unit"/>
          <prop v="1" k="vertical_anchor_point"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol type="marker" name="8" alpha="1" clip_to_extent="1" force_rhr="0">
        <layer enabled="1" pass="0" class="RasterMarker" locked="0">
          <prop v="1" k="alpha"/>
          <prop v="0" k="angle"/>
          <prop v="0.294118" k="fixedAspectRatio"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="base64:iVBORw0KGgoAAAANSUhEUgAAABcAAAAHCAYAAADj/NY7AAAAAXNSR0IB2cksfwAAAAlwSFlzAAAOxAAADsQBlSsOGwAAALVJREFUKJGd0L0uhGEQBtBTbDJ+EhIJrbgNrWoTDZ1GQaOzl0I0q1HIBhFRKlwAN6MiWzydxssmPvHxdDOTOZnMQHcWcYLVH+azmeCuazDo6C3jAZs9YNjGAS5/w1fwWFULSTbw0gPfxwXmcf4Nr6qtJIfYgyRXVTXqebkkU4wxrqrTJKNPPMl6g3GLtyRzfXFcf+wvJTnGF441PGGI1z+gsznCLm5ao73lOckZpv+EW+6x04p3cZYypYQRlEYAAAAASUVORK5CYII=" k="imageFile"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="Point" k="offset_unit"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="17" k="size"/>
          <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
          <prop v="Point" k="size_unit"/>
          <prop v="1" k="vertical_anchor_point"/>
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
    <DiagramCategory penColor="#000000" scaleBasedVisibility="0" spacingUnitScale="3x:0,0,0,0,0,0" backgroundAlpha="255" diagramOrientation="Up" penWidth="0" backgroundColor="#ffffff" direction="1" barWidth="5" opacity="1" lineSizeScale="3x:0,0,0,0,0,0" labelPlacementMethod="XHeight" sizeType="MM" spacingUnit="MM" enabled="0" penAlpha="255" height="15" minimumSize="0" spacing="0" width="15" rotationOffset="270" lineSizeType="MM" showAxis="0" sizeScale="3x:0,0,0,0,0,0" minScaleDenominator="500" scaleDependency="Area" maxScaleDenominator="1e+08">
      <fontProperties description="MS Shell Dlg 2,8.25,-1,5,50,0,0,0,0,0" style=""/>
      <attribute color="#000000" label="" field=""/>
      <axisSymbol>
        <symbol type="line" name="" alpha="1" clip_to_extent="1" force_rhr="0">
          <layer enabled="1" pass="0" class="SimpleLine" locked="0">
            <prop v="0" k="align_dash_pattern"/>
            <prop v="square" k="capstyle"/>
            <prop v="5;2" k="customdash"/>
            <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
            <prop v="MM" k="customdash_unit"/>
            <prop v="0" k="dash_pattern_offset"/>
            <prop v="3x:0,0,0,0,0,0" k="dash_pattern_offset_map_unit_scale"/>
            <prop v="MM" k="dash_pattern_offset_unit"/>
            <prop v="0" k="draw_inside_polygon"/>
            <prop v="bevel" k="joinstyle"/>
            <prop v="35,35,35,255" k="line_color"/>
            <prop v="solid" k="line_style"/>
            <prop v="0.26" k="line_width"/>
            <prop v="MM" k="line_width_unit"/>
            <prop v="0" k="offset"/>
            <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
            <prop v="MM" k="offset_unit"/>
            <prop v="0" k="ring_filter"/>
            <prop v="0" k="tweak_dash_pattern_on_corners"/>
            <prop v="0" k="use_custom_dash"/>
            <prop v="3x:0,0,0,0,0,0" k="width_map_unit_scale"/>
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
  <DiagramLayerSettings obstacle="0" zIndex="0" showAll="1" priority="0" dist="0" placement="0" linePlacementFlags="18">
    <properties>
      <Option type="Map">
        <Option type="QString" name="name" value=""/>
        <Option name="properties"/>
        <Option type="QString" name="type" value="collection"/>
      </Option>
    </properties>
  </DiagramLayerSettings>
  <geometryOptions removeDuplicateNodes="0" geometryPrecision="0">
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
      <column width="-1" type="field" name="DAMO_W.Stuw.OBJECTID" hidden="0"/>
      <column width="-1" type="field" name="DAMO_W.Stuw.CODE" hidden="0"/>
      <column width="-1" type="field" name="DAMO_W.Stuw.NAAM" hidden="0"/>
      <column width="-1" type="field" name="DAMO_W.Stuw.HYPERLINK" hidden="0"/>
      <column width="-1" type="field" name="DAMO_W.Stuw.OPMERKING" hidden="0"/>
      <column width="-1" type="field" name="DAMO_W.Stuw.INDICATIEWATERKEREND" hidden="0"/>
      <column width="-1" type="field" name="DAMO_W.Stuw.SOORTSTUW" hidden="0"/>
      <column width="-1" type="field" name="DAMO_W.Stuw.DOORSTROOMBREEDTE" hidden="0"/>
      <column width="-1" type="field" name="DAMO_W.Stuw.LAAGSTEDOORSTROOMHOOGTE" hidden="0"/>
      <column width="-1" type="field" name="DAMO_W.Stuw.HOOGSTEDOORSTROOMHOOGTE" hidden="0"/>
      <column width="-1" type="field" name="DAMO_W.Stuw.SOORTREGELBAARHEID" hidden="0"/>
      <column width="-1" type="field" name="DAMO_W.Stuw.WS_CATEGORIE" hidden="0"/>
      <column width="-1" type="field" name="DAMO_W.Stuw.WS_KRUINVORM" hidden="0"/>
      <column width="-1" type="field" name="DAMO_W.Stuw.WS_OP_AFSTAND_BEHEERD" hidden="0"/>
      <column width="-1" type="field" name="DAMO_W.Stuw.WS_BRON" hidden="0"/>
      <column width="-1" type="field" name="DAMO_W.Stuw.WS_INWINNINGSWIJZE" hidden="0"/>
      <column width="-1" type="field" name="DAMO_W.Stuw.WS_INWINNINGSDATUM" hidden="0"/>
      <column width="-1" type="field" name="DAMO_W.Stuw.WS_INWINNINGSWIJZE_ADMIN" hidden="0"/>
      <column width="-1" type="field" name="DAMO_W.Stuw.WS_INWINNINGSDATUM_ADMIN" hidden="0"/>
      <column width="-1" type="field" name="DAMO_W.Stuw.WS_VOLLEDIGHEID_DATASET" hidden="0"/>
      <column width="-1" type="field" name="DAMO_W.Stuw.WS_KWALITEITSSCORE" hidden="0"/>
      <column width="-1" type="field" name="DAMO_W.Stuw.WS_FUNCTIESTUW" hidden="0"/>
      <column width="-1" type="field" name="DAMO_W.Stuw.WS_OHPLICHT_KWK" hidden="0"/>
      <column width="-1" type="field" name="DAMO_W.Stuw.WS_INFORCODE" hidden="0"/>
      <column width="-1" type="field" name="DAMO_W.Stuw.GISOBJID" hidden="0"/>
      <column width="-1" type="field" name="kunstwerkxy.coordinaten" hidden="0"/>
      <column width="-1" type="field" name="DAMO_W.WS_OHPLICHT_KWK.WS_OHPLICHT_CONSTRUCTIE" hidden="0"/>
      <column width="-1" type="field" name="DAMO_W.WS_OHPLICHT_KWK.WS_OHPLICHT_AFVAL" hidden="0"/>
      <column width="-1" type="field" name="DAMO_W.WS_OHPLICHT_KWK.WS_OHPLICHT_NAT" hidden="0"/>
      <column width="-1" type="field" name="DAMO_W.WS_OHPLICHT_KWK.WS_OHPLICHT_DROOG" hidden="0"/>
      <column width="-1" type="actions" hidden="1"/>
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
    <field name="DAMO_W.Stuw.CODE" editable="1"/>
    <field name="DAMO_W.Stuw.DOORSTROOMBREEDTE" editable="1"/>
    <field name="DAMO_W.Stuw.GISOBJID" editable="1"/>
    <field name="DAMO_W.Stuw.HOOGSTEDOORSTROOMHOOGTE" editable="1"/>
    <field name="DAMO_W.Stuw.HYPERLINK" editable="1"/>
    <field name="DAMO_W.Stuw.INDICATIEWATERKEREND" editable="1"/>
    <field name="DAMO_W.Stuw.LAAGSTEDOORSTROOMHOOGTE" editable="1"/>
    <field name="DAMO_W.Stuw.NAAM" editable="1"/>
    <field name="DAMO_W.Stuw.OBJECTID" editable="1"/>
    <field name="DAMO_W.Stuw.OPMERKING" editable="1"/>
    <field name="DAMO_W.Stuw.SOORTREGELBAARHEID" editable="1"/>
    <field name="DAMO_W.Stuw.SOORTSTUW" editable="1"/>
    <field name="DAMO_W.Stuw.WS_BRON" editable="1"/>
    <field name="DAMO_W.Stuw.WS_CATEGORIE" editable="1"/>
    <field name="DAMO_W.Stuw.WS_FUNCTIESTUW" editable="1"/>
    <field name="DAMO_W.Stuw.WS_INFORCODE" editable="1"/>
    <field name="DAMO_W.Stuw.WS_INWINNINGSDATUM" editable="1"/>
    <field name="DAMO_W.Stuw.WS_INWINNINGSDATUM_ADMIN" editable="1"/>
    <field name="DAMO_W.Stuw.WS_INWINNINGSWIJZE" editable="1"/>
    <field name="DAMO_W.Stuw.WS_INWINNINGSWIJZE_ADMIN" editable="1"/>
    <field name="DAMO_W.Stuw.WS_KRUINVORM" editable="1"/>
    <field name="DAMO_W.Stuw.WS_KWALITEITSSCORE" editable="1"/>
    <field name="DAMO_W.Stuw.WS_OHPLICHT_KWK" editable="1"/>
    <field name="DAMO_W.Stuw.WS_OP_AFSTAND_BEHEERD" editable="1"/>
    <field name="DAMO_W.Stuw.WS_VOLLEDIGHEID_DATASET" editable="1"/>
    <field name="DAMO_W.WS_OHPLICHT_KWK.WS_OHPLICHT_AFVAL" editable="1"/>
    <field name="DAMO_W.WS_OHPLICHT_KWK.WS_OHPLICHT_CONSTRUCTIE" editable="1"/>
    <field name="DAMO_W.WS_OHPLICHT_KWK.WS_OHPLICHT_DROOG" editable="1"/>
    <field name="DAMO_W.WS_OHPLICHT_KWK.WS_OHPLICHT_NAT" editable="1"/>
    <field name="kunstwerkxy.coordinaten" editable="1"/>
  </editable>
  <labelOnTop>
    <field name="DAMO_W.Stuw.CODE" labelOnTop="0"/>
    <field name="DAMO_W.Stuw.DOORSTROOMBREEDTE" labelOnTop="0"/>
    <field name="DAMO_W.Stuw.GISOBJID" labelOnTop="0"/>
    <field name="DAMO_W.Stuw.HOOGSTEDOORSTROOMHOOGTE" labelOnTop="0"/>
    <field name="DAMO_W.Stuw.HYPERLINK" labelOnTop="0"/>
    <field name="DAMO_W.Stuw.INDICATIEWATERKEREND" labelOnTop="0"/>
    <field name="DAMO_W.Stuw.LAAGSTEDOORSTROOMHOOGTE" labelOnTop="0"/>
    <field name="DAMO_W.Stuw.NAAM" labelOnTop="0"/>
    <field name="DAMO_W.Stuw.OBJECTID" labelOnTop="0"/>
    <field name="DAMO_W.Stuw.OPMERKING" labelOnTop="0"/>
    <field name="DAMO_W.Stuw.SOORTREGELBAARHEID" labelOnTop="0"/>
    <field name="DAMO_W.Stuw.SOORTSTUW" labelOnTop="0"/>
    <field name="DAMO_W.Stuw.WS_BRON" labelOnTop="0"/>
    <field name="DAMO_W.Stuw.WS_CATEGORIE" labelOnTop="0"/>
    <field name="DAMO_W.Stuw.WS_FUNCTIESTUW" labelOnTop="0"/>
    <field name="DAMO_W.Stuw.WS_INFORCODE" labelOnTop="0"/>
    <field name="DAMO_W.Stuw.WS_INWINNINGSDATUM" labelOnTop="0"/>
    <field name="DAMO_W.Stuw.WS_INWINNINGSDATUM_ADMIN" labelOnTop="0"/>
    <field name="DAMO_W.Stuw.WS_INWINNINGSWIJZE" labelOnTop="0"/>
    <field name="DAMO_W.Stuw.WS_INWINNINGSWIJZE_ADMIN" labelOnTop="0"/>
    <field name="DAMO_W.Stuw.WS_KRUINVORM" labelOnTop="0"/>
    <field name="DAMO_W.Stuw.WS_KWALITEITSSCORE" labelOnTop="0"/>
    <field name="DAMO_W.Stuw.WS_OHPLICHT_KWK" labelOnTop="0"/>
    <field name="DAMO_W.Stuw.WS_OP_AFSTAND_BEHEERD" labelOnTop="0"/>
    <field name="DAMO_W.Stuw.WS_VOLLEDIGHEID_DATASET" labelOnTop="0"/>
    <field name="DAMO_W.WS_OHPLICHT_KWK.WS_OHPLICHT_AFVAL" labelOnTop="0"/>
    <field name="DAMO_W.WS_OHPLICHT_KWK.WS_OHPLICHT_CONSTRUCTIE" labelOnTop="0"/>
    <field name="DAMO_W.WS_OHPLICHT_KWK.WS_OHPLICHT_DROOG" labelOnTop="0"/>
    <field name="DAMO_W.WS_OHPLICHT_KWK.WS_OHPLICHT_NAT" labelOnTop="0"/>
    <field name="kunstwerkxy.coordinaten" labelOnTop="0"/>
  </labelOnTop>
  <dataDefinedFieldProperties/>
  <widgets/>
  <previewExpression>DAMO_W.Stuw.OBJECTID</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>0</layerGeometryType>
</qgis>
