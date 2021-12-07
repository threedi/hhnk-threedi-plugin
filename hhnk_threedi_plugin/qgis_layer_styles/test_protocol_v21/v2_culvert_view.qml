<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis maxScale="-4.65661e-10" simplifyMaxScale="1" version="3.16.11-Hannover" hasScaleBasedVisibilityFlag="0" simplifyDrawingHints="1" simplifyDrawingTol="1" simplifyAlgorithm="0" readOnly="0" labelsEnabled="0" minScale="100000000" styleCategories="AllStyleCategories" simplifyLocal="1">
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
  <renderer-v2 type="singleSymbol" forceraster="0" enableorderby="0" symbollevels="0">
    <symbols>
      <symbol type="line" name="0" clip_to_extent="1" force_rhr="0" alpha="1">
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
          <prop k="line_color" v="101,101,101,255"/>
          <prop k="line_style" v="solid"/>
          <prop k="line_width" v="0.66"/>
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
        <layer enabled="1" class="MarkerLine" locked="0" pass="0">
          <prop k="average_angle_length" v="4"/>
          <prop k="average_angle_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="average_angle_unit" v="MM"/>
          <prop k="interval" v="3"/>
          <prop k="interval_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="interval_unit" v="MM"/>
          <prop k="offset" v="0"/>
          <prop k="offset_along_line" v="0"/>
          <prop k="offset_along_line_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_along_line_unit" v="RenderMetersInMapUnits"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="placement" v="firstvertex"/>
          <prop k="ring_filter" v="0"/>
          <prop k="rotate" v="1"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option type="Map" name="properties">
                <Option type="Map" name="enabled">
                  <Option type="bool" name="active" value="true"/>
                  <Option type="QString" name="expression" value="coalesce(cul_discharge_coefficient_positive, 0) = 0"/>
                  <Option type="int" name="type" value="3"/>
                </Option>
                <Option type="Map" name="offsetAlongLine">
                  <Option type="bool" name="active" value="true"/>
                  <Option type="QString" name="expression" value="0.6667*$length"/>
                  <Option type="int" name="type" value="3"/>
                </Option>
              </Option>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
          <symbol type="marker" name="@0@1" clip_to_extent="1" force_rhr="0" alpha="1">
            <layer enabled="1" class="SimpleMarker" locked="0" pass="0">
              <prop k="angle" v="180"/>
              <prop k="color" v="255,0,0,255"/>
              <prop k="horizontal_anchor_point" v="1"/>
              <prop k="joinstyle" v="bevel"/>
              <prop k="name" v="line"/>
              <prop k="offset" v="0,0"/>
              <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="outline_color" v="101,101,101,255"/>
              <prop k="outline_style" v="solid"/>
              <prop k="outline_width" v="0.8"/>
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
        </layer>
        <layer enabled="1" class="MarkerLine" locked="0" pass="0">
          <prop k="average_angle_length" v="4"/>
          <prop k="average_angle_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="average_angle_unit" v="MM"/>
          <prop k="interval" v="3"/>
          <prop k="interval_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="interval_unit" v="MM"/>
          <prop k="offset" v="0"/>
          <prop k="offset_along_line" v="0"/>
          <prop k="offset_along_line_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_along_line_unit" v="RenderMetersInMapUnits"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="placement" v="firstvertex"/>
          <prop k="ring_filter" v="0"/>
          <prop k="rotate" v="1"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option type="Map" name="properties">
                <Option type="Map" name="enabled">
                  <Option type="bool" name="active" value="true"/>
                  <Option type="QString" name="expression" value="coalesce(cul_discharge_coefficient_negative,0) > 0&#xd;&#xa;AND coalesce(cul_discharge_coefficient_positive,0) = 0"/>
                  <Option type="int" name="type" value="3"/>
                </Option>
                <Option type="Map" name="offsetAlongLine">
                  <Option type="bool" name="active" value="true"/>
                  <Option type="QString" name="expression" value="0.3333*$length"/>
                  <Option type="int" name="type" value="3"/>
                </Option>
              </Option>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
          <symbol type="marker" name="@0@2" clip_to_extent="1" force_rhr="0" alpha="1">
            <layer enabled="1" class="SimpleMarker" locked="0" pass="0">
              <prop k="angle" v="180"/>
              <prop k="color" v="255,0,0,255"/>
              <prop k="horizontal_anchor_point" v="1"/>
              <prop k="joinstyle" v="bevel"/>
              <prop k="name" v="arrowhead"/>
              <prop k="offset" v="0,0"/>
              <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="outline_color" v="101,101,101,255"/>
              <prop k="outline_style" v="solid"/>
              <prop k="outline_width" v="0.8"/>
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
        </layer>
        <layer enabled="1" class="MarkerLine" locked="0" pass="0">
          <prop k="average_angle_length" v="4"/>
          <prop k="average_angle_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="average_angle_unit" v="MM"/>
          <prop k="interval" v="3"/>
          <prop k="interval_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="interval_unit" v="MM"/>
          <prop k="offset" v="0"/>
          <prop k="offset_along_line" v="0"/>
          <prop k="offset_along_line_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_along_line_unit" v="RenderMetersInMapUnits"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="placement" v="firstvertex"/>
          <prop k="ring_filter" v="0"/>
          <prop k="rotate" v="1"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option type="Map" name="properties">
                <Option type="Map" name="enabled">
                  <Option type="bool" name="active" value="true"/>
                  <Option type="QString" name="expression" value="COALESCE(cul_discharge_coefficient_negative, 0) = 0"/>
                  <Option type="int" name="type" value="3"/>
                </Option>
                <Option type="Map" name="offsetAlongLine">
                  <Option type="bool" name="active" value="true"/>
                  <Option type="QString" name="expression" value="0.3333*$length"/>
                  <Option type="int" name="type" value="3"/>
                </Option>
              </Option>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
          <symbol type="marker" name="@0@3" clip_to_extent="1" force_rhr="0" alpha="1">
            <layer enabled="1" class="SimpleMarker" locked="0" pass="0">
              <prop k="angle" v="0"/>
              <prop k="color" v="255,0,0,255"/>
              <prop k="horizontal_anchor_point" v="1"/>
              <prop k="joinstyle" v="bevel"/>
              <prop k="name" v="line"/>
              <prop k="offset" v="0,0"/>
              <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="outline_color" v="101,101,101,255"/>
              <prop k="outline_style" v="solid"/>
              <prop k="outline_width" v="0.8"/>
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
        </layer>
        <layer enabled="1" class="MarkerLine" locked="0" pass="0">
          <prop k="average_angle_length" v="4"/>
          <prop k="average_angle_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="average_angle_unit" v="MM"/>
          <prop k="interval" v="3"/>
          <prop k="interval_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="interval_unit" v="MM"/>
          <prop k="offset" v="0"/>
          <prop k="offset_along_line" v="0"/>
          <prop k="offset_along_line_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_along_line_unit" v="RenderMetersInMapUnits"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="placement" v="firstvertex"/>
          <prop k="ring_filter" v="0"/>
          <prop k="rotate" v="1"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option type="Map" name="properties">
                <Option type="Map" name="enabled">
                  <Option type="bool" name="active" value="true"/>
                  <Option type="QString" name="expression" value="COALESCE(cul_discharge_coefficient_positive, 0) > 0&#xd;&#xa;AND COALESCE(cul_discharge_coefficient_negative) = 0"/>
                  <Option type="int" name="type" value="3"/>
                </Option>
                <Option type="Map" name="offsetAlongLine">
                  <Option type="bool" name="active" value="true"/>
                  <Option type="QString" name="expression" value="0.66667*$length"/>
                  <Option type="int" name="type" value="3"/>
                </Option>
              </Option>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
          <symbol type="marker" name="@0@4" clip_to_extent="1" force_rhr="0" alpha="1">
            <layer enabled="1" class="SimpleMarker" locked="0" pass="0">
              <prop k="angle" v="0"/>
              <prop k="color" v="255,0,0,255"/>
              <prop k="horizontal_anchor_point" v="1"/>
              <prop k="joinstyle" v="bevel"/>
              <prop k="name" v="arrowhead"/>
              <prop k="offset" v="0,0"/>
              <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="outline_color" v="101,101,101,255"/>
              <prop k="outline_style" v="solid"/>
              <prop k="outline_width" v="0.8"/>
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
        </layer>
        <layer enabled="1" class="MarkerLine" locked="0" pass="0">
          <prop k="average_angle_length" v="4"/>
          <prop k="average_angle_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="average_angle_unit" v="MM"/>
          <prop k="interval" v="3"/>
          <prop k="interval_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="interval_unit" v="MM"/>
          <prop k="offset" v="0"/>
          <prop k="offset_along_line" v="0"/>
          <prop k="offset_along_line_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_along_line_unit" v="MM"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="placement" v="centralpoint"/>
          <prop k="ring_filter" v="0"/>
          <prop k="rotate" v="1"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
          <symbol type="marker" name="@0@5" clip_to_extent="1" force_rhr="0" alpha="1">
            <layer enabled="1" class="SimpleMarker" locked="0" pass="0">
              <prop k="angle" v="0"/>
              <prop k="color" v="101,101,101,255"/>
              <prop k="horizontal_anchor_point" v="1"/>
              <prop k="joinstyle" v="bevel"/>
              <prop k="name" v="circle"/>
              <prop k="offset" v="0,0"/>
              <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="outline_color" v="35,35,35,255"/>
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
        </layer>
      </symbol>
    </symbols>
    <rotation/>
    <sizescale/>
  </renderer-v2>
  <customproperties>
    <property key="dualview/previewExpressions" value="&quot;ROWID&quot;"/>
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
  <DiagramLayerSettings zIndex="0" showAll="1" obstacle="0" priority="0" placement="2" linePlacementFlags="2" dist="0">
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
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="cul_id">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="cul_display_name">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="cul_code">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="cul_calculation_type">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option type="QString" name="100: embedded" value="100"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="101: isolated" value="101"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="102: connected" value="102"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="105: double connected" value="105"/>
              </Option>
            </Option>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="cul_friction_value">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="cul_friction_type">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option type="QString" name="1: Chèzy" value="1"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="2: Manning" value="2"/>
              </Option>
            </Option>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="cul_dist_calc_points">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="cul_zoom_category">
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
    <field configurationFlags="None" name="cul_cross_section_definition_id">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="cul_discharge_coefficient_positive">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="cul_discharge_coefficient_negative">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="cul_invert_level_start_point">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="cul_invert_level_end_point">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="cul_connection_node_start_id">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="cul_connection_node_end_id">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="def_id">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="def_shape">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option type="QString" name="1: rectangle" value="1"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="2: round" value="2"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="3: egg" value="3"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="5: tabulated rectangle" value="5"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="6: tabulated trapezium" value="6"/>
              </Option>
            </Option>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="def_width">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="def_height">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="def_code">
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
    <alias field="cul_id" name="id" index="1"/>
    <alias field="cul_display_name" name="display_name" index="2"/>
    <alias field="cul_code" name="code" index="3"/>
    <alias field="cul_calculation_type" name="calculation_type" index="4"/>
    <alias field="cul_friction_value" name="friction_value" index="5"/>
    <alias field="cul_friction_type" name="friction_type" index="6"/>
    <alias field="cul_dist_calc_points" name="dist_calc_points" index="7"/>
    <alias field="cul_zoom_category" name="zoom_category" index="8"/>
    <alias field="cul_cross_section_definition_id" name="cross_section_definition_id" index="9"/>
    <alias field="cul_discharge_coefficient_positive" name="discharge_coefficient_positive" index="10"/>
    <alias field="cul_discharge_coefficient_negative" name="discharge_coefficient_negative" index="11"/>
    <alias field="cul_invert_level_start_point" name="invert_level_start_point" index="12"/>
    <alias field="cul_invert_level_end_point" name="invert_level_end_point" index="13"/>
    <alias field="cul_connection_node_start_id" name="connection_node_start_id" index="14"/>
    <alias field="cul_connection_node_end_id" name="connection_node_end_id" index="15"/>
    <alias field="def_id" name="id" index="16"/>
    <alias field="def_shape" name="shape" index="17"/>
    <alias field="def_width" name="width" index="18"/>
    <alias field="def_height" name="height" index="19"/>
    <alias field="def_code" name="code" index="20"/>
  </aliases>
  <defaults>
    <default applyOnUpdate="0" field="ROWID" expression=""/>
    <default applyOnUpdate="0" field="cul_id" expression="if(maximum(cul_id) is null,1, maximum(cul_id)+1)"/>
    <default applyOnUpdate="0" field="cul_display_name" expression="'new'"/>
    <default applyOnUpdate="0" field="cul_code" expression="'new'"/>
    <default applyOnUpdate="0" field="cul_calculation_type" expression="101"/>
    <default applyOnUpdate="0" field="cul_friction_value" expression=""/>
    <default applyOnUpdate="0" field="cul_friction_type" expression="2"/>
    <default applyOnUpdate="0" field="cul_dist_calc_points" expression="10000"/>
    <default applyOnUpdate="0" field="cul_zoom_category" expression="3"/>
    <default applyOnUpdate="0" field="cul_cross_section_definition_id" expression=""/>
    <default applyOnUpdate="0" field="cul_discharge_coefficient_positive" expression="0.8"/>
    <default applyOnUpdate="0" field="cul_discharge_coefficient_negative" expression="0.8"/>
    <default applyOnUpdate="0" field="cul_invert_level_start_point" expression="aggregate('v2_manhole_view','min',&quot;bottom_level&quot;, intersects($geometry,start_point(geometry(@parent)))) "/>
    <default applyOnUpdate="0" field="cul_invert_level_end_point" expression="aggregate('v2_manhole_view','min',&quot;bottom_level&quot;, intersects($geometry,end_point(geometry(@parent)))) "/>
    <default applyOnUpdate="0" field="cul_connection_node_start_id" expression="if(aggregate('v2_connection_nodes','min',&quot;id&quot;, intersects($geometry,start_point(geometry(@parent)))) is null, 'Created automatically',aggregate('v2_connection_nodes','min',&quot;id&quot;, intersects($geometry,start_point(geometry(@parent)))))"/>
    <default applyOnUpdate="0" field="cul_connection_node_end_id" expression="if(aggregate('v2_connection_nodes','min',&quot;id&quot;, intersects($geometry,end_point(geometry(@parent)))) is null, 'Created automatically',aggregate('v2_connection_nodes','min',&quot;id&quot;, intersects($geometry,end_point(geometry(@parent)))))"/>
    <default applyOnUpdate="0" field="def_id" expression=""/>
    <default applyOnUpdate="0" field="def_shape" expression=""/>
    <default applyOnUpdate="0" field="def_width" expression=""/>
    <default applyOnUpdate="0" field="def_height" expression=""/>
    <default applyOnUpdate="0" field="def_code" expression=""/>
  </defaults>
  <constraints>
    <constraint unique_strength="0" constraints="0" field="ROWID" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="1" field="cul_id" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="1" field="cul_display_name" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="1" field="cul_code" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="1" field="cul_calculation_type" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="1" field="cul_friction_value" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="1" field="cul_friction_type" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="1" field="cul_dist_calc_points" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="1" field="cul_zoom_category" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="1" field="cul_cross_section_definition_id" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="1" field="cul_discharge_coefficient_positive" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="1" field="cul_discharge_coefficient_negative" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="1" field="cul_invert_level_start_point" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="1" field="cul_invert_level_end_point" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="0" field="cul_connection_node_start_id" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="cul_connection_node_end_id" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="1" field="def_id" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="0" field="def_shape" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="def_width" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="def_height" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="def_code" exp_strength="0" notnull_strength="0"/>
  </constraints>
  <constraintExpressions>
    <constraint field="ROWID" exp="" desc=""/>
    <constraint field="cul_id" exp="" desc=""/>
    <constraint field="cul_display_name" exp="" desc=""/>
    <constraint field="cul_code" exp="" desc=""/>
    <constraint field="cul_calculation_type" exp="" desc=""/>
    <constraint field="cul_friction_value" exp="" desc=""/>
    <constraint field="cul_friction_type" exp="" desc=""/>
    <constraint field="cul_dist_calc_points" exp="" desc=""/>
    <constraint field="cul_zoom_category" exp="" desc=""/>
    <constraint field="cul_cross_section_definition_id" exp="" desc=""/>
    <constraint field="cul_discharge_coefficient_positive" exp="" desc=""/>
    <constraint field="cul_discharge_coefficient_negative" exp="" desc=""/>
    <constraint field="cul_invert_level_start_point" exp="" desc=""/>
    <constraint field="cul_invert_level_end_point" exp="" desc=""/>
    <constraint field="cul_connection_node_start_id" exp="" desc=""/>
    <constraint field="cul_connection_node_end_id" exp="" desc=""/>
    <constraint field="def_id" exp="" desc=""/>
    <constraint field="def_shape" exp="" desc=""/>
    <constraint field="def_width" exp="" desc=""/>
    <constraint field="def_height" exp="" desc=""/>
    <constraint field="def_code" exp="" desc=""/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction key="Canvas" value="{00000000-0000-0000-0000-000000000000}"/>
  </attributeactions>
  <attributetableconfig actionWidgetStyle="dropDown" sortExpression="" sortOrder="0">
    <columns>
      <column type="field" name="ROWID" width="-1" hidden="0"/>
      <column type="field" name="cul_id" width="-1" hidden="0"/>
      <column type="field" name="cul_display_name" width="-1" hidden="0"/>
      <column type="field" name="cul_code" width="-1" hidden="0"/>
      <column type="field" name="cul_calculation_type" width="-1" hidden="0"/>
      <column type="field" name="cul_friction_value" width="-1" hidden="0"/>
      <column type="field" name="cul_friction_type" width="-1" hidden="0"/>
      <column type="field" name="cul_dist_calc_points" width="-1" hidden="0"/>
      <column type="field" name="cul_zoom_category" width="-1" hidden="0"/>
      <column type="field" name="cul_cross_section_definition_id" width="-1" hidden="0"/>
      <column type="field" name="cul_discharge_coefficient_positive" width="-1" hidden="0"/>
      <column type="field" name="cul_discharge_coefficient_negative" width="-1" hidden="0"/>
      <column type="field" name="cul_invert_level_start_point" width="-1" hidden="0"/>
      <column type="field" name="cul_invert_level_end_point" width="-1" hidden="0"/>
      <column type="field" name="cul_connection_node_start_id" width="-1" hidden="0"/>
      <column type="field" name="cul_connection_node_end_id" width="-1" hidden="0"/>
      <column type="field" name="def_id" width="-1" hidden="0"/>
      <column type="field" name="def_shape" width="-1" hidden="0"/>
      <column type="field" name="def_width" width="-1" hidden="0"/>
      <column type="field" name="def_height" width="-1" hidden="0"/>
      <column type="field" name="def_code" width="-1" hidden="0"/>
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
    <attributeEditorContainer columnCount="1" name="Culvert view" groupBox="0" showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="">
      <attributeEditorContainer columnCount="1" name="General" groupBox="1" showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="">
        <attributeEditorField name="cul_id" showLabel="1" index="1"/>
        <attributeEditorField name="cul_display_name" showLabel="1" index="2"/>
        <attributeEditorField name="cul_code" showLabel="1" index="3"/>
        <attributeEditorField name="cul_calculation_type" showLabel="1" index="4"/>
        <attributeEditorField name="cul_dist_calc_points" showLabel="1" index="7"/>
      </attributeEditorContainer>
      <attributeEditorContainer columnCount="1" name="Characteristics" groupBox="1" showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="">
        <attributeEditorField name="cul_invert_level_start_point" showLabel="1" index="12"/>
        <attributeEditorField name="cul_invert_level_end_point" showLabel="1" index="13"/>
        <attributeEditorField name="cul_friction_type" showLabel="1" index="6"/>
        <attributeEditorField name="cul_friction_value" showLabel="1" index="5"/>
        <attributeEditorField name="cul_discharge_coefficient_positive" showLabel="1" index="10"/>
        <attributeEditorField name="cul_discharge_coefficient_negative" showLabel="1" index="11"/>
      </attributeEditorContainer>
      <attributeEditorContainer columnCount="1" name="Cross section definition" groupBox="1" showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="">
        <attributeEditorField name="cul_cross_section_definition_id" showLabel="1" index="9"/>
        <attributeEditorField name="def_code" showLabel="1" index="20"/>
        <attributeEditorField name="def_shape" showLabel="1" index="17"/>
        <attributeEditorField name="def_width" showLabel="1" index="18"/>
        <attributeEditorField name="def_height" showLabel="1" index="19"/>
      </attributeEditorContainer>
      <attributeEditorContainer columnCount="1" name="Visualization" groupBox="1" showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="">
        <attributeEditorField name="cul_zoom_category" showLabel="1" index="8"/>
      </attributeEditorContainer>
      <attributeEditorContainer columnCount="1" name="Connection nodes" groupBox="1" showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="">
        <attributeEditorField name="cul_connection_node_start_id" showLabel="1" index="14"/>
        <attributeEditorField name="cul_connection_node_end_id" showLabel="1" index="15"/>
      </attributeEditorContainer>
    </attributeEditorContainer>
  </attributeEditorForm>
  <editable>
    <field editable="1" name="ROWID"/>
    <field editable="1" name="cul_calculation_type"/>
    <field editable="1" name="cul_code"/>
    <field editable="0" name="cul_connection_node_end_id"/>
    <field editable="0" name="cul_connection_node_start_id"/>
    <field editable="1" name="cul_cross_section_definition_id"/>
    <field editable="1" name="cul_discharge_coefficient_negative"/>
    <field editable="1" name="cul_discharge_coefficient_positive"/>
    <field editable="1" name="cul_display_name"/>
    <field editable="1" name="cul_dist_calc_points"/>
    <field editable="1" name="cul_friction_type"/>
    <field editable="1" name="cul_friction_value"/>
    <field editable="1" name="cul_id"/>
    <field editable="1" name="cul_invert_level_end_point"/>
    <field editable="1" name="cul_invert_level_start_point"/>
    <field editable="1" name="cul_zoom_category"/>
    <field editable="0" name="def_code"/>
    <field editable="0" name="def_height"/>
    <field editable="0" name="def_id"/>
    <field editable="0" name="def_shape"/>
    <field editable="0" name="def_width"/>
  </editable>
  <labelOnTop>
    <field labelOnTop="0" name="ROWID"/>
    <field labelOnTop="0" name="cul_calculation_type"/>
    <field labelOnTop="0" name="cul_code"/>
    <field labelOnTop="0" name="cul_connection_node_end_id"/>
    <field labelOnTop="0" name="cul_connection_node_start_id"/>
    <field labelOnTop="0" name="cul_cross_section_definition_id"/>
    <field labelOnTop="0" name="cul_discharge_coefficient_negative"/>
    <field labelOnTop="0" name="cul_discharge_coefficient_positive"/>
    <field labelOnTop="0" name="cul_display_name"/>
    <field labelOnTop="0" name="cul_dist_calc_points"/>
    <field labelOnTop="0" name="cul_friction_type"/>
    <field labelOnTop="0" name="cul_friction_value"/>
    <field labelOnTop="0" name="cul_id"/>
    <field labelOnTop="0" name="cul_invert_level_end_point"/>
    <field labelOnTop="0" name="cul_invert_level_start_point"/>
    <field labelOnTop="0" name="cul_zoom_category"/>
    <field labelOnTop="0" name="def_code"/>
    <field labelOnTop="0" name="def_height"/>
    <field labelOnTop="0" name="def_id"/>
    <field labelOnTop="0" name="def_shape"/>
    <field labelOnTop="0" name="def_width"/>
  </labelOnTop>
  <dataDefinedFieldProperties/>
  <widgets/>
  <previewExpression>"ROWID"</previewExpression>
  <mapTip>display_name</mapTip>
  <layerGeometryType>1</layerGeometryType>
</qgis>
