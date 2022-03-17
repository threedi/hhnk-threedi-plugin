<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis maxScale="-4.65661e-10" simplifyMaxScale="1" version="3.16.11-Hannover" hasScaleBasedVisibilityFlag="0" simplifyDrawingHints="0" simplifyDrawingTol="1" simplifyAlgorithm="0" readOnly="0" labelsEnabled="0" minScale="100000000" styleCategories="AllStyleCategories" simplifyLocal="1">
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
    <rules key="{4fbba513-a3b1-4a92-97bc-3d44735ac986}">
      <rule symbol="0" key="{a951db60-faa9-4c95-9eaa-a51d84ff90b1}" scalemaxdenom="5000" filter="manh_manhole_indicator = 0" label="Manhole (inspection)"/>
      <rule symbol="1" key="{c9e7ab73-45d5-45d6-970d-b4e28230c1e5}" scalemaxdenom="15000" filter="manh_manhole_indicator = 1" label="Outlet"/>
      <rule symbol="2" key="{a1d98efc-8098-4201-a75e-93dc7c47f076}" filter="manh_manhole_indicator = 2" label="Pumping station"/>
      <rule symbol="3" key="{1b6d21ed-8a83-4e3f-850e-ca64e766f7da}" scalemaxdenom="5000" filter="ELSE" label="Manhole (unspecified)"/>
    </rules>
    <symbols>
      <symbol type="marker" name="0" clip_to_extent="1" force_rhr="0" alpha="1">
        <layer enabled="1" class="SimpleMarker" locked="0" pass="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="255,255,255,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="square"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="0,0,0,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="2"/>
          <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="size_unit" v="MM"/>
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
        <layer enabled="1" class="SimpleMarker" locked="0" pass="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="63,128,192,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="miter"/>
          <prop k="name" v="square"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="85,170,255,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0.75"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="2.5"/>
          <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="size_unit" v="MM"/>
          <prop k="vertical_anchor_point" v="1"/>
          <effect enabled="0" type="effectStack">
            <effect type="dropShadow">
              <prop k="blend_mode" v="13"/>
              <prop k="blur_level" v="0.5"/>
              <prop k="blur_unit" v="MM"/>
              <prop k="blur_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="color" v="0,0,0,255"/>
              <prop k="draw_mode" v="2"/>
              <prop k="enabled" v="1"/>
              <prop k="offset_angle" v="135"/>
              <prop k="offset_distance" v="0.2"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="offset_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="opacity" v="1"/>
            </effect>
            <effect type="outerGlow">
              <prop k="blend_mode" v="0"/>
              <prop k="blur_level" v="2.645"/>
              <prop k="blur_unit" v="MM"/>
              <prop k="blur_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="color1" v="0,0,255,255"/>
              <prop k="color2" v="0,255,0,255"/>
              <prop k="color_type" v="0"/>
              <prop k="discrete" v="0"/>
              <prop k="draw_mode" v="2"/>
              <prop k="enabled" v="0"/>
              <prop k="opacity" v="0.5"/>
              <prop k="rampType" v="gradient"/>
              <prop k="single_color" v="255,255,255,255"/>
              <prop k="spread" v="2"/>
              <prop k="spread_unit" v="MM"/>
              <prop k="spread_unit_scale" v="3x:0,0,0,0,0,0"/>
            </effect>
            <effect type="drawSource">
              <prop k="blend_mode" v="0"/>
              <prop k="draw_mode" v="2"/>
              <prop k="enabled" v="1"/>
              <prop k="opacity" v="1"/>
            </effect>
            <effect type="innerShadow">
              <prop k="blend_mode" v="13"/>
              <prop k="blur_level" v="2.645"/>
              <prop k="blur_unit" v="MM"/>
              <prop k="blur_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="color" v="0,0,0,255"/>
              <prop k="draw_mode" v="2"/>
              <prop k="enabled" v="0"/>
              <prop k="offset_angle" v="135"/>
              <prop k="offset_distance" v="2"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="offset_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="opacity" v="1"/>
            </effect>
            <effect type="innerGlow">
              <prop k="blend_mode" v="0"/>
              <prop k="blur_level" v="2.645"/>
              <prop k="blur_unit" v="MM"/>
              <prop k="blur_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="color1" v="0,0,255,255"/>
              <prop k="color2" v="0,255,0,255"/>
              <prop k="color_type" v="0"/>
              <prop k="discrete" v="0"/>
              <prop k="draw_mode" v="2"/>
              <prop k="enabled" v="0"/>
              <prop k="opacity" v="0.5"/>
              <prop k="rampType" v="gradient"/>
              <prop k="single_color" v="255,255,255,255"/>
              <prop k="spread" v="2"/>
              <prop k="spread_unit" v="MM"/>
              <prop k="spread_unit_scale" v="3x:0,0,0,0,0,0"/>
            </effect>
          </effect>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option type="Map" name="properties">
                <Option type="Map" name="size">
                  <Option type="bool" name="active" value="true"/>
                  <Option type="QString" name="expression" value="if(@map_scale&lt;10000, 2.5,1.5)"/>
                  <Option type="int" name="type" value="3"/>
                </Option>
              </Option>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol type="marker" name="2" clip_to_extent="1" force_rhr="0" alpha="1">
        <layer enabled="1" class="SimpleMarker" locked="0" pass="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="85,255,127,0"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="pentagon"/>
          <prop k="offset" v="0.10000000000000001,0.10000000000000001"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="0,0,0,183"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0.7"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="4.1"/>
          <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="size_unit" v="MM"/>
          <prop k="vertical_anchor_point" v="1"/>
          <effect enabled="0" type="effectStack">
            <effect type="dropShadow">
              <prop k="blend_mode" v="13"/>
              <prop k="blur_level" v="0.5"/>
              <prop k="blur_unit" v="MM"/>
              <prop k="blur_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="color" v="0,0,0,255"/>
              <prop k="draw_mode" v="2"/>
              <prop k="enabled" v="1"/>
              <prop k="offset_angle" v="135"/>
              <prop k="offset_distance" v="0.2"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="offset_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="opacity" v="1"/>
            </effect>
            <effect type="outerGlow">
              <prop k="blend_mode" v="0"/>
              <prop k="blur_level" v="2.645"/>
              <prop k="blur_unit" v="MM"/>
              <prop k="blur_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="color1" v="0,0,255,255"/>
              <prop k="color2" v="0,255,0,255"/>
              <prop k="color_type" v="0"/>
              <prop k="discrete" v="0"/>
              <prop k="draw_mode" v="2"/>
              <prop k="enabled" v="0"/>
              <prop k="opacity" v="0.5"/>
              <prop k="rampType" v="gradient"/>
              <prop k="single_color" v="255,255,255,255"/>
              <prop k="spread" v="2"/>
              <prop k="spread_unit" v="MM"/>
              <prop k="spread_unit_scale" v="3x:0,0,0,0,0,0"/>
            </effect>
            <effect type="drawSource">
              <prop k="blend_mode" v="0"/>
              <prop k="draw_mode" v="2"/>
              <prop k="enabled" v="1"/>
              <prop k="opacity" v="1"/>
            </effect>
            <effect type="innerShadow">
              <prop k="blend_mode" v="13"/>
              <prop k="blur_level" v="2.645"/>
              <prop k="blur_unit" v="MM"/>
              <prop k="blur_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="color" v="0,0,0,255"/>
              <prop k="draw_mode" v="2"/>
              <prop k="enabled" v="0"/>
              <prop k="offset_angle" v="135"/>
              <prop k="offset_distance" v="2"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="offset_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="opacity" v="1"/>
            </effect>
            <effect type="innerGlow">
              <prop k="blend_mode" v="0"/>
              <prop k="blur_level" v="2.645"/>
              <prop k="blur_unit" v="MM"/>
              <prop k="blur_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="color1" v="0,0,255,255"/>
              <prop k="color2" v="0,255,0,255"/>
              <prop k="color_type" v="0"/>
              <prop k="discrete" v="0"/>
              <prop k="draw_mode" v="2"/>
              <prop k="enabled" v="0"/>
              <prop k="opacity" v="0.5"/>
              <prop k="rampType" v="gradient"/>
              <prop k="single_color" v="255,255,255,255"/>
              <prop k="spread" v="2"/>
              <prop k="spread_unit" v="MM"/>
              <prop k="spread_unit_scale" v="3x:0,0,0,0,0,0"/>
            </effect>
          </effect>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option type="Map" name="properties">
                <Option type="Map" name="size">
                  <Option type="bool" name="active" value="true"/>
                  <Option type="QString" name="expression" value="if(@map_scale&lt;10000, 4.1,3.1)"/>
                  <Option type="int" name="type" value="3"/>
                </Option>
              </Option>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
        <layer enabled="1" class="SimpleMarker" locked="0" pass="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="85,255,127,0"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="pentagon"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="255,127,0,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0.7"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="4"/>
          <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="size_unit" v="MM"/>
          <prop k="vertical_anchor_point" v="1"/>
          <effect enabled="0" type="effectStack">
            <effect type="dropShadow">
              <prop k="blend_mode" v="13"/>
              <prop k="blur_level" v="0.5"/>
              <prop k="blur_unit" v="MM"/>
              <prop k="blur_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="color" v="0,0,0,255"/>
              <prop k="draw_mode" v="2"/>
              <prop k="enabled" v="1"/>
              <prop k="offset_angle" v="135"/>
              <prop k="offset_distance" v="0.2"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="offset_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="opacity" v="1"/>
            </effect>
            <effect type="outerGlow">
              <prop k="blend_mode" v="0"/>
              <prop k="blur_level" v="2.645"/>
              <prop k="blur_unit" v="MM"/>
              <prop k="blur_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="color1" v="0,0,255,255"/>
              <prop k="color2" v="0,255,0,255"/>
              <prop k="color_type" v="0"/>
              <prop k="discrete" v="0"/>
              <prop k="draw_mode" v="2"/>
              <prop k="enabled" v="0"/>
              <prop k="opacity" v="0.5"/>
              <prop k="rampType" v="gradient"/>
              <prop k="single_color" v="255,255,255,255"/>
              <prop k="spread" v="2"/>
              <prop k="spread_unit" v="MM"/>
              <prop k="spread_unit_scale" v="3x:0,0,0,0,0,0"/>
            </effect>
            <effect type="drawSource">
              <prop k="blend_mode" v="0"/>
              <prop k="draw_mode" v="2"/>
              <prop k="enabled" v="1"/>
              <prop k="opacity" v="1"/>
            </effect>
            <effect type="innerShadow">
              <prop k="blend_mode" v="13"/>
              <prop k="blur_level" v="2.645"/>
              <prop k="blur_unit" v="MM"/>
              <prop k="blur_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="color" v="0,0,0,255"/>
              <prop k="draw_mode" v="2"/>
              <prop k="enabled" v="0"/>
              <prop k="offset_angle" v="135"/>
              <prop k="offset_distance" v="2"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="offset_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="opacity" v="1"/>
            </effect>
            <effect type="innerGlow">
              <prop k="blend_mode" v="0"/>
              <prop k="blur_level" v="2.645"/>
              <prop k="blur_unit" v="MM"/>
              <prop k="blur_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="color1" v="0,0,255,255"/>
              <prop k="color2" v="0,255,0,255"/>
              <prop k="color_type" v="0"/>
              <prop k="discrete" v="0"/>
              <prop k="draw_mode" v="2"/>
              <prop k="enabled" v="0"/>
              <prop k="opacity" v="0.5"/>
              <prop k="rampType" v="gradient"/>
              <prop k="single_color" v="255,255,255,255"/>
              <prop k="spread" v="2"/>
              <prop k="spread_unit" v="MM"/>
              <prop k="spread_unit_scale" v="3x:0,0,0,0,0,0"/>
            </effect>
          </effect>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option type="Map" name="properties">
                <Option type="Map" name="size">
                  <Option type="bool" name="active" value="true"/>
                  <Option type="QString" name="expression" value="if(@map_scale&lt;10000, 4,3)"/>
                  <Option type="int" name="type" value="3"/>
                </Option>
              </Option>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol type="marker" name="3" clip_to_extent="1" force_rhr="0" alpha="1">
        <layer enabled="1" class="SimpleMarker" locked="0" pass="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="85,255,127,0"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="square"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="255,9,1,255"/>
          <prop k="outline_style" v="dot"/>
          <prop k="outline_width" v="0.25"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="2"/>
          <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="size_unit" v="MM"/>
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
    <property key="dualview/previewExpressions" value="manh_display_name"/>
    <property key="embeddedWidgets/count" value="0"/>
    <property key="variableNames"/>
    <property key="variableValues"/>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <SingleCategoryDiagramRenderer attributeLegend="1" diagramType="Pie">
    <DiagramCategory lineSizeType="MM" height="15" opacity="1" enabled="0" penAlpha="255" sizeScale="3x:0,0,0,0,0,0" minScaleDenominator="-4.65661e-10" spacing="0" spacingUnit="MM" scaleBasedVisibility="0" backgroundAlpha="255" maxScaleDenominator="1e+08" labelPlacementMethod="XHeight" penWidth="0" scaleDependency="Area" direction="1" penColor="#000000" backgroundColor="#ffffff" spacingUnitScale="3x:0,0,0,0,0,0" width="15" minimumSize="0" diagramOrientation="Up" lineSizeScale="3x:0,0,0,0,0,0" showAxis="0" sizeType="MM" rotationOffset="270" barWidth="5">
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
  <DiagramLayerSettings zIndex="0" showAll="1" obstacle="0" priority="0" placement="0" linePlacementFlags="2" dist="0">
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
  <fieldConfiguration>
    <field configurationFlags="None" name="ROWID">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="manh_id">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="manh_display_name">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="manh_code">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="manh_connection_node_id">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="manh_shape">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option type="QString" name="00: square" value="00"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="01: round" value="01"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="02: rectangle" value="02"/>
              </Option>
            </Option>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="manh_width">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="manh_length">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="manh_manhole_indicator">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option type="QString" name="0: inspection" value="0"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="1: outlet" value="1"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="2: pump" value="2"/>
              </Option>
            </Option>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="manh_calculation_type">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option type="QString" name="0: embedded" value="0"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="1: isolated" value="1"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="2: connected" value="2"/>
              </Option>
            </Option>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="manh_bottom_level">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="manh_surface_level">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="manh_drain_level">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="manh_sediment_level">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="manh_zoom_category">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option type="QString" name="-1" value="-1"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="0" value="0"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="1" value="1"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="2" value="2"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="3" value="3"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="4" value="4"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="5" value="5"/>
              </Option>
            </Option>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="node_id">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="node_storage_area">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="node_initial_waterlevel">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="node_code">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="node_the_geom_linestring">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
  </fieldConfiguration>
  <aliases>
    <alias field="ROWID" name="" index="0"/>
    <alias field="manh_id" name="id" index="1"/>
    <alias field="manh_display_name" name="display_name" index="2"/>
    <alias field="manh_code" name="code" index="3"/>
    <alias field="manh_connection_node_id" name="connection_node_id" index="4"/>
    <alias field="manh_shape" name="shape" index="5"/>
    <alias field="manh_width" name="width" index="6"/>
    <alias field="manh_length" name="length" index="7"/>
    <alias field="manh_manhole_indicator" name="manhole_indicator" index="8"/>
    <alias field="manh_calculation_type" name="calculation_type" index="9"/>
    <alias field="manh_bottom_level" name="bottom_level" index="10"/>
    <alias field="manh_surface_level" name="surface_level" index="11"/>
    <alias field="manh_drain_level" name="drain_level" index="12"/>
    <alias field="manh_sediment_level" name="sediment_level" index="13"/>
    <alias field="manh_zoom_category" name="zoom_category" index="14"/>
    <alias field="node_id" name="" index="15"/>
    <alias field="node_storage_area" name="" index="16"/>
    <alias field="node_initial_waterlevel" name="" index="17"/>
    <alias field="node_code" name="" index="18"/>
    <alias field="node_the_geom_linestring" name="the_geom_linestring" index="19"/>
  </aliases>
  <defaults>
    <default applyOnUpdate="0" field="ROWID" expression=""/>
    <default applyOnUpdate="0" field="manh_id" expression="if(maximum(manh_id) is null,1, maximum(manh_id)+1)"/>
    <default applyOnUpdate="0" field="manh_display_name" expression="'new'"/>
    <default applyOnUpdate="0" field="manh_code" expression="'new'"/>
    <default applyOnUpdate="0" field="manh_connection_node_id" expression="if(aggregate('v2_connection_nodes','min',&quot;id&quot;, intersects($geometry,geometry(@parent))) is null,'Created automatically',aggregate('v2_connection_nodes','min',&quot;id&quot;, intersects($geometry,geometry(@parent))))"/>
    <default applyOnUpdate="0" field="manh_shape" expression=""/>
    <default applyOnUpdate="0" field="manh_width" expression=""/>
    <default applyOnUpdate="0" field="manh_length" expression=""/>
    <default applyOnUpdate="0" field="manh_manhole_indicator" expression="'0'"/>
    <default applyOnUpdate="0" field="manh_calculation_type" expression=""/>
    <default applyOnUpdate="0" field="manh_bottom_level" expression="&quot;manh_bottom_level&quot;&lt;&quot;manh_surface_level&quot;"/>
    <default applyOnUpdate="0" field="manh_surface_level" expression=""/>
    <default applyOnUpdate="0" field="manh_drain_level" expression=""/>
    <default applyOnUpdate="0" field="manh_sediment_level" expression=""/>
    <default applyOnUpdate="0" field="manh_zoom_category" expression="1"/>
    <default applyOnUpdate="0" field="node_id" expression="'filled automatically'"/>
    <default applyOnUpdate="0" field="node_storage_area" expression=""/>
    <default applyOnUpdate="0" field="node_initial_waterlevel" expression=""/>
    <default applyOnUpdate="0" field="node_code" expression="'new'"/>
    <default applyOnUpdate="0" field="node_the_geom_linestring" expression=""/>
  </defaults>
  <constraints>
    <constraint unique_strength="0" constraints="0" field="ROWID" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="manh_id" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="1" field="manh_display_name" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="1" field="manh_code" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="1" field="manh_connection_node_id" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="1" field="manh_shape" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="1" field="manh_width" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="0" field="manh_length" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="1" field="manh_manhole_indicator" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="1" field="manh_calculation_type" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="1" field="manh_bottom_level" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="1" field="manh_surface_level" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="0" field="manh_drain_level" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="manh_sediment_level" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="1" field="manh_zoom_category" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="0" field="node_id" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="node_storage_area" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="node_initial_waterlevel" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="1" field="node_code" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="0" field="node_the_geom_linestring" exp_strength="0" notnull_strength="0"/>
  </constraints>
  <constraintExpressions>
    <constraint field="ROWID" exp="" desc=""/>
    <constraint field="manh_id" exp="" desc=""/>
    <constraint field="manh_display_name" exp="" desc=""/>
    <constraint field="manh_code" exp="" desc=""/>
    <constraint field="manh_connection_node_id" exp="" desc=""/>
    <constraint field="manh_shape" exp="" desc=""/>
    <constraint field="manh_width" exp="" desc=""/>
    <constraint field="manh_length" exp="" desc=""/>
    <constraint field="manh_manhole_indicator" exp="" desc=""/>
    <constraint field="manh_calculation_type" exp="" desc=""/>
    <constraint field="manh_bottom_level" exp="" desc=""/>
    <constraint field="manh_surface_level" exp="" desc=""/>
    <constraint field="manh_drain_level" exp="" desc=""/>
    <constraint field="manh_sediment_level" exp="" desc=""/>
    <constraint field="manh_zoom_category" exp="" desc=""/>
    <constraint field="node_id" exp="" desc=""/>
    <constraint field="node_storage_area" exp="" desc=""/>
    <constraint field="node_initial_waterlevel" exp="" desc=""/>
    <constraint field="node_code" exp="" desc=""/>
    <constraint field="node_the_geom_linestring" exp="" desc=""/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction key="Canvas" value="{00000000-0000-0000-0000-000000000000}"/>
  </attributeactions>
  <attributetableconfig actionWidgetStyle="dropDown" sortExpression="&quot;manh_manhole_indicator&quot;" sortOrder="0">
    <columns>
      <column type="field" name="ROWID" width="-1" hidden="0"/>
      <column type="field" name="manh_id" width="-1" hidden="0"/>
      <column type="field" name="manh_display_name" width="-1" hidden="0"/>
      <column type="field" name="manh_code" width="-1" hidden="0"/>
      <column type="field" name="manh_connection_node_id" width="-1" hidden="0"/>
      <column type="field" name="manh_shape" width="-1" hidden="0"/>
      <column type="field" name="manh_width" width="-1" hidden="0"/>
      <column type="field" name="manh_length" width="-1" hidden="0"/>
      <column type="field" name="manh_manhole_indicator" width="-1" hidden="0"/>
      <column type="field" name="manh_calculation_type" width="-1" hidden="0"/>
      <column type="field" name="manh_bottom_level" width="-1" hidden="0"/>
      <column type="field" name="manh_surface_level" width="-1" hidden="0"/>
      <column type="field" name="manh_drain_level" width="-1" hidden="0"/>
      <column type="field" name="manh_sediment_level" width="-1" hidden="0"/>
      <column type="field" name="manh_zoom_category" width="-1" hidden="0"/>
      <column type="field" name="node_id" width="-1" hidden="0"/>
      <column type="field" name="node_storage_area" width="-1" hidden="0"/>
      <column type="field" name="node_initial_waterlevel" width="-1" hidden="0"/>
      <column type="field" name="node_code" width="-1" hidden="0"/>
      <column type="field" name="node_the_geom_linestring" width="-1" hidden="0"/>
      <column type="actions" width="-1" hidden="1"/>
    </columns>
  </attributetableconfig>
  <conditionalstyles>
    <rowstyles/>
    <fieldstyles/>
  </conditionalstyles>
  <storedexpressions/>
  <editform tolerant="1">C:/Users/chris.kerklaan/Downloads/test_protocol_v21</editform>
  <editforminit/>
  <editforminitcodesource>0</editforminitcodesource>
  <editforminitfilepath>C:/Users/chris.kerklaan/Downloads/test_protocol_v21</editforminitfilepath>
  <editforminitcode><![CDATA[# -*- coding: utf-8 -*-
"""
QGIS forms can have a Python function that is called when the form is
opened.

Use this function to add extra logic to your forms.

Enter the name of the function in the "Python Init function"
field.
An example follows:
"""
from PyQt4.QtGui import QWidget

def my_form_open(dialog, layer, feature):
	geom = feature.geometry()
	control = dialog.findChild(QWidget, "MyLineEdit")
]]></editforminitcode>
  <featformsuppress>0</featformsuppress>
  <editorlayout>tablayout</editorlayout>
  <attributeEditorForm>
    <attributeEditorContainer columnCount="1" name="Manhole_view" groupBox="0" showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="">
      <attributeEditorContainer columnCount="1" name="General" groupBox="1" showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="">
        <attributeEditorField name="manh_id" showLabel="1" index="1"/>
        <attributeEditorField name="manh_display_name" showLabel="1" index="2"/>
        <attributeEditorField name="manh_code" showLabel="1" index="3"/>
        <attributeEditorField name="manh_calculation_type" showLabel="1" index="9"/>
      </attributeEditorContainer>
      <attributeEditorContainer columnCount="1" name="Characteristics" groupBox="1" showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="">
        <attributeEditorField name="manh_shape" showLabel="1" index="5"/>
        <attributeEditorField name="manh_width" showLabel="1" index="6"/>
        <attributeEditorField name="manh_length" showLabel="1" index="7"/>
        <attributeEditorField name="manh_bottom_level" showLabel="1" index="10"/>
        <attributeEditorField name="manh_surface_level" showLabel="1" index="11"/>
        <attributeEditorField name="manh_drain_level" showLabel="1" index="12"/>
      </attributeEditorContainer>
      <attributeEditorContainer columnCount="1" name="Visualisation" groupBox="1" showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="">
        <attributeEditorField name="manh_manhole_indicator" showLabel="1" index="8"/>
        <attributeEditorField name="manh_zoom_category" showLabel="1" index="14"/>
      </attributeEditorContainer>
      <attributeEditorContainer columnCount="1" name="Connection node" groupBox="1" showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="">
        <attributeEditorField name="manh_connection_node_id" showLabel="1" index="4"/>
        <attributeEditorField name="node_code" showLabel="1" index="18"/>
        <attributeEditorField name="node_initial_waterlevel" showLabel="1" index="17"/>
        <attributeEditorField name="node_storage_area" showLabel="1" index="16"/>
      </attributeEditorContainer>
    </attributeEditorContainer>
  </attributeEditorForm>
  <editable>
    <field editable="1" name="ROWID"/>
    <field editable="1" name="manh_bottom_level"/>
    <field editable="1" name="manh_calculation_type"/>
    <field editable="1" name="manh_code"/>
    <field editable="0" name="manh_connection_node_id"/>
    <field editable="1" name="manh_display_name"/>
    <field editable="1" name="manh_drain_level"/>
    <field editable="0" name="manh_id"/>
    <field editable="1" name="manh_length"/>
    <field editable="1" name="manh_manhole_indicator"/>
    <field editable="1" name="manh_sediment_level"/>
    <field editable="1" name="manh_shape"/>
    <field editable="1" name="manh_surface_level"/>
    <field editable="1" name="manh_width"/>
    <field editable="1" name="manh_zoom_category"/>
    <field editable="1" name="node_code"/>
    <field editable="0" name="node_id"/>
    <field editable="1" name="node_initial_waterlevel"/>
    <field editable="1" name="node_storage_area"/>
    <field editable="1" name="node_the_geom_linestring"/>
  </editable>
  <labelOnTop>
    <field labelOnTop="0" name="ROWID"/>
    <field labelOnTop="0" name="manh_bottom_level"/>
    <field labelOnTop="0" name="manh_calculation_type"/>
    <field labelOnTop="0" name="manh_code"/>
    <field labelOnTop="0" name="manh_connection_node_id"/>
    <field labelOnTop="0" name="manh_display_name"/>
    <field labelOnTop="0" name="manh_drain_level"/>
    <field labelOnTop="0" name="manh_id"/>
    <field labelOnTop="0" name="manh_length"/>
    <field labelOnTop="0" name="manh_manhole_indicator"/>
    <field labelOnTop="0" name="manh_sediment_level"/>
    <field labelOnTop="0" name="manh_shape"/>
    <field labelOnTop="0" name="manh_surface_level"/>
    <field labelOnTop="0" name="manh_width"/>
    <field labelOnTop="0" name="manh_zoom_category"/>
    <field labelOnTop="0" name="node_code"/>
    <field labelOnTop="0" name="node_id"/>
    <field labelOnTop="0" name="node_initial_waterlevel"/>
    <field labelOnTop="0" name="node_storage_area"/>
    <field labelOnTop="0" name="node_the_geom_linestring"/>
  </labelOnTop>
  <dataDefinedFieldProperties/>
  <widgets/>
  <previewExpression>"manh_display_name"</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>0</layerGeometryType>
</qgis>
