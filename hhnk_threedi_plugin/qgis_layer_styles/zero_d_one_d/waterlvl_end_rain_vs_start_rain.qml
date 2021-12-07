<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis styleCategories="AllStyleCategories" simplifyDrawingTol="1" maxScale="0" simplifyLocal="1" simplifyDrawingHints="0" readOnly="0" labelsEnabled="0" simplifyMaxScale="1" version="3.16.6-Hannover" minScale="100000000" simplifyAlgorithm="0" hasScaleBasedVisibilityFlag="0">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <temporal durationField="" accumulate="0" endExpression="" startExpression="" mode="0" enabled="0" startField="" endField="" fixedDuration="0" durationUnit="min">
    <fixedRange>
      <start></start>
      <end></end>
    </fixedRange>
  </temporal>
  <renderer-v2 forceraster="0" enableorderby="0" symbollevels="0" attr="lvl_rain" graduatedMethod="GraduatedColor" type="graduatedSymbol">
    <ranges>
      <range label="&lt; streefpeil" render="true" symbol="0" lower="-20.000000000000000" upper="-0.050000000000000"/>
      <range label="-0.05 m - 0.1 m" render="false" symbol="1" lower="-0.050000000000000" upper="0.100000000000000"/>
      <range label="0.1 m - 0.25 m" render="true" symbol="2" lower="0.100000000000000" upper="0.250000000000000"/>
      <range label="0.25 m - 0.5 m" render="true" symbol="3" lower="0.250000000000000" upper="0.500000000000000"/>
      <range label="0.5 m - 1 m" render="true" symbol="4" lower="0.500000000000000" upper="1.000000000000000"/>
      <range label="> 1 m" render="true" symbol="5" lower="1.000000000000000" upper="100.000000000000000"/>
    </ranges>
    <symbols>
      <symbol alpha="1" name="0" force_rhr="0" clip_to_extent="1" type="marker">
        <layer locked="0" enabled="1" class="SimpleMarker" pass="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="7,187,255,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="circle"/>
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
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol alpha="1" name="1" force_rhr="0" clip_to_extent="1" type="marker">
        <layer locked="0" enabled="1" class="SimpleMarker" pass="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="33,255,0,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="circle"/>
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
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol alpha="1" name="2" force_rhr="0" clip_to_extent="1" type="marker">
        <layer locked="0" enabled="1" class="SimpleMarker" pass="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="255,228,4,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="circle"/>
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
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol alpha="1" name="3" force_rhr="0" clip_to_extent="1" type="marker">
        <layer locked="0" enabled="1" class="SimpleMarker" pass="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="255,152,4,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="circle"/>
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
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol alpha="1" name="4" force_rhr="0" clip_to_extent="1" type="marker">
        <layer locked="0" enabled="1" class="SimpleMarker" pass="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="255,76,4,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="circle"/>
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
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol alpha="1" name="5" force_rhr="0" clip_to_extent="1" type="marker">
        <layer locked="0" enabled="1" class="SimpleMarker" pass="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="255,0,4,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="circle"/>
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
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </symbols>
    <source-symbol>
      <symbol alpha="1" name="0" force_rhr="0" clip_to_extent="1" type="marker">
        <layer locked="0" enabled="1" class="SimpleMarker" pass="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="70,238,171,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="circle"/>
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
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </source-symbol>
    <colorramp name="[source]" type="gradient">
      <prop k="color1" v="7,187,255,255"/>
      <prop k="color2" v="255,0,4,255"/>
      <prop k="discrete" v="0"/>
      <prop k="rampType" v="gradient"/>
      <prop k="stops" v="0.177885;0,255,0,255:0.344952;255,248,4,255"/>
    </colorramp>
    <classificationMethod id="Jenks">
      <symmetricMode astride="0" enabled="0" symmetrypoint="0"/>
      <labelFormat labelprecision="4" format="%1 - %2" trimtrailingzeroes="1"/>
      <parameters>
        <Option/>
      </parameters>
      <extraInformation/>
    </classificationMethod>
    <rotation/>
    <sizescale/>
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
    <DiagramCategory backgroundColor="#ffffff" spacingUnitScale="3x:0,0,0,0,0,0" height="15" rotationOffset="270" sizeScale="3x:0,0,0,0,0,0" width="15" minScaleDenominator="1000" direction="1" lineSizeType="MM" barWidth="5" backgroundAlpha="255" penWidth="0" sizeType="MM" spacingUnit="MM" diagramOrientation="Up" lineSizeScale="3x:0,0,0,0,0,0" enabled="0" scaleDependency="Area" spacing="0" minimumSize="0" maxScaleDenominator="1e+08" scaleBasedVisibility="0" penAlpha="255" labelPlacementMethod="XHeight" showAxis="0" penColor="#000000" opacity="1">
      <fontProperties description="MS Shell Dlg 2,8.25,-1,5,50,0,0,0,0,0" style=""/>
      <attribute label="" field="" color="#000000"/>
      <axisSymbol>
        <symbol alpha="1" name="" force_rhr="0" clip_to_extent="1" type="line">
          <layer locked="0" enabled="1" class="SimpleLine" pass="0">
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
                <Option name="name" value="" type="QString"/>
                <Option name="properties"/>
                <Option name="type" value="collection" type="QString"/>
              </Option>
            </data_defined_properties>
          </layer>
        </symbol>
      </axisSymbol>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings obstacle="0" linePlacementFlags="2" placement="0" zIndex="0" showAll="1" dist="0" priority="0">
    <properties>
      <Option type="Map">
        <Option name="name" value="" type="QString"/>
        <Option name="properties"/>
        <Option name="type" value="collection" type="QString"/>
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
    <field configurationFlags="None" name="fid">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="lvl_end">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="lvl_end_rain">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="lvl_rain">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="lvl_start">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="wlvl_t_end_sum">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="wlvlv_t_end_rain">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="wvlv_t_end_rain_min_one">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="wlvl_t_start_rain">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="wlvlv_t_0">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="t_end_sum">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="t_end_rain">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="t_end_rain_min_one">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="t_start_rain">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="t_0">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
  </fieldConfiguration>
  <aliases>
    <alias name="" field="fid" index="0"/>
    <alias name="" field="lvl_end" index="1"/>
    <alias name="" field="lvl_end_rain" index="2"/>
    <alias name="" field="lvl_rain" index="3"/>
    <alias name="" field="lvl_start" index="4"/>
    <alias name="" field="wlvl_t_end_sum" index="5"/>
    <alias name="" field="wlvlv_t_end_rain" index="6"/>
    <alias name="" field="wvlv_t_end_rain_min_one" index="7"/>
    <alias name="" field="wlvl_t_start_rain" index="8"/>
    <alias name="" field="wlvlv_t_0" index="9"/>
    <alias name="" field="t_end_sum" index="10"/>
    <alias name="" field="t_end_rain" index="11"/>
    <alias name="" field="t_end_rain_min_one" index="12"/>
    <alias name="" field="t_start_rain" index="13"/>
    <alias name="" field="t_0" index="14"/>
  </aliases>
  <defaults>
    <default applyOnUpdate="0" field="fid" expression=""/>
    <default applyOnUpdate="0" field="lvl_end" expression=""/>
    <default applyOnUpdate="0" field="lvl_end_rain" expression=""/>
    <default applyOnUpdate="0" field="lvl_rain" expression=""/>
    <default applyOnUpdate="0" field="lvl_start" expression=""/>
    <default applyOnUpdate="0" field="wlvl_t_end_sum" expression=""/>
    <default applyOnUpdate="0" field="wlvlv_t_end_rain" expression=""/>
    <default applyOnUpdate="0" field="wvlv_t_end_rain_min_one" expression=""/>
    <default applyOnUpdate="0" field="wlvl_t_start_rain" expression=""/>
    <default applyOnUpdate="0" field="wlvlv_t_0" expression=""/>
    <default applyOnUpdate="0" field="t_end_sum" expression=""/>
    <default applyOnUpdate="0" field="t_end_rain" expression=""/>
    <default applyOnUpdate="0" field="t_end_rain_min_one" expression=""/>
    <default applyOnUpdate="0" field="t_start_rain" expression=""/>
    <default applyOnUpdate="0" field="t_0" expression=""/>
  </defaults>
  <constraints>
    <constraint constraints="3" unique_strength="1" exp_strength="0" notnull_strength="1" field="fid"/>
    <constraint constraints="0" unique_strength="0" exp_strength="0" notnull_strength="0" field="lvl_end"/>
    <constraint constraints="0" unique_strength="0" exp_strength="0" notnull_strength="0" field="lvl_end_rain"/>
    <constraint constraints="0" unique_strength="0" exp_strength="0" notnull_strength="0" field="lvl_rain"/>
    <constraint constraints="0" unique_strength="0" exp_strength="0" notnull_strength="0" field="lvl_start"/>
    <constraint constraints="0" unique_strength="0" exp_strength="0" notnull_strength="0" field="wlvl_t_end_sum"/>
    <constraint constraints="0" unique_strength="0" exp_strength="0" notnull_strength="0" field="wlvlv_t_end_rain"/>
    <constraint constraints="0" unique_strength="0" exp_strength="0" notnull_strength="0" field="wvlv_t_end_rain_min_one"/>
    <constraint constraints="0" unique_strength="0" exp_strength="0" notnull_strength="0" field="wlvl_t_start_rain"/>
    <constraint constraints="0" unique_strength="0" exp_strength="0" notnull_strength="0" field="wlvlv_t_0"/>
    <constraint constraints="0" unique_strength="0" exp_strength="0" notnull_strength="0" field="t_end_sum"/>
    <constraint constraints="0" unique_strength="0" exp_strength="0" notnull_strength="0" field="t_end_rain"/>
    <constraint constraints="0" unique_strength="0" exp_strength="0" notnull_strength="0" field="t_end_rain_min_one"/>
    <constraint constraints="0" unique_strength="0" exp_strength="0" notnull_strength="0" field="t_start_rain"/>
    <constraint constraints="0" unique_strength="0" exp_strength="0" notnull_strength="0" field="t_0"/>
  </constraints>
  <constraintExpressions>
    <constraint desc="" exp="" field="fid"/>
    <constraint desc="" exp="" field="lvl_end"/>
    <constraint desc="" exp="" field="lvl_end_rain"/>
    <constraint desc="" exp="" field="lvl_rain"/>
    <constraint desc="" exp="" field="lvl_start"/>
    <constraint desc="" exp="" field="wlvl_t_end_sum"/>
    <constraint desc="" exp="" field="wlvlv_t_end_rain"/>
    <constraint desc="" exp="" field="wvlv_t_end_rain_min_one"/>
    <constraint desc="" exp="" field="wlvl_t_start_rain"/>
    <constraint desc="" exp="" field="wlvlv_t_0"/>
    <constraint desc="" exp="" field="t_end_sum"/>
    <constraint desc="" exp="" field="t_end_rain"/>
    <constraint desc="" exp="" field="t_end_rain_min_one"/>
    <constraint desc="" exp="" field="t_start_rain"/>
    <constraint desc="" exp="" field="t_0"/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction key="Canvas" value="{00000000-0000-0000-0000-000000000000}"/>
  </attributeactions>
  <attributetableconfig actionWidgetStyle="dropDown" sortOrder="1" sortExpression="&quot;dPeil_einde_regen&quot;">
    <columns>
      <column hidden="1" width="-1" type="actions"/>
      <column name="fid" hidden="0" width="-1" type="field"/>
      <column name="lvl_end" hidden="0" width="-1" type="field"/>
      <column name="lvl_end_rain" hidden="0" width="-1" type="field"/>
      <column name="lvl_rain" hidden="0" width="-1" type="field"/>
      <column name="lvl_start" hidden="0" width="-1" type="field"/>
      <column name="wlvl_t_end_sum" hidden="0" width="-1" type="field"/>
      <column name="wlvlv_t_end_rain" hidden="0" width="-1" type="field"/>
      <column name="wvlv_t_end_rain_min_one" hidden="0" width="-1" type="field"/>
      <column name="wlvl_t_start_rain" hidden="0" width="-1" type="field"/>
      <column name="wlvlv_t_0" hidden="0" width="-1" type="field"/>
      <column name="t_end_sum" hidden="0" width="-1" type="field"/>
      <column name="t_end_rain" hidden="0" width="-1" type="field"/>
      <column name="t_end_rain_min_one" hidden="0" width="-1" type="field"/>
      <column name="t_start_rain" hidden="0" width="-1" type="field"/>
      <column name="t_0" hidden="0" width="-1" type="field"/>
    </columns>
  </attributetableconfig>
  <conditionalstyles>
    <rowstyles/>
    <fieldstyles/>
  </conditionalstyles>
  <storedexpressions/>
  <editform tolerant="1">//srv57d1/geo_info/02_Werkplaatsen/06_HYD/Projecten/HKC16015 Wateropgave 2.0/07. Poldermodellen/28.Waterland/04. Werksessie 1 - Hydraulische toets</editform>
  <editforminit/>
  <editforminitcodesource>0</editforminitcodesource>
  <editforminitfilepath>//srv57d1/geo_info/02_Werkplaatsen/06_HYD/Projecten/HKC16015 Wateropgave 2.0/07. Poldermodellen/28.Waterland/04. Werksessie 1 - Hydraulische toets</editforminitfilepath>
  <editforminitcode><![CDATA[# -*- coding: utf-8 -*-
"""
QGIS forms can have a Python function that is called when the form is
opened.

Use this function to add extra logic to your forms.

Enter the name of the function in the "Python Init function"
field.
An example follows:
"""
from qgis.PyQt.QtWidgets import QWidget

def my_form_open(dialog, layer, feature):
	geom = feature.geometry()
	control = dialog.findChild(QWidget, "MyLineEdit")
]]></editforminitcode>
  <featformsuppress>0</featformsuppress>
  <editorlayout>generatedlayout</editorlayout>
  <editable>
    <field editable="1" name="fid"/>
    <field editable="1" name="lvl_end"/>
    <field editable="1" name="lvl_end_rain"/>
    <field editable="1" name="lvl_rain"/>
    <field editable="1" name="lvl_start"/>
    <field editable="1" name="t_0"/>
    <field editable="1" name="t_end_rain"/>
    <field editable="1" name="t_end_rain_min_one"/>
    <field editable="1" name="t_end_sum"/>
    <field editable="1" name="t_start_rain"/>
    <field editable="1" name="wlvl_t_end_sum"/>
    <field editable="1" name="wlvl_t_start_rain"/>
    <field editable="1" name="wlvlv_t_0"/>
    <field editable="1" name="wlvlv_t_end_rain"/>
    <field editable="1" name="wvlv_t_end_rain_min_one"/>
  </editable>
  <labelOnTop>
    <field name="fid" labelOnTop="0"/>
    <field name="lvl_end" labelOnTop="0"/>
    <field name="lvl_end_rain" labelOnTop="0"/>
    <field name="lvl_rain" labelOnTop="0"/>
    <field name="lvl_start" labelOnTop="0"/>
    <field name="t_0" labelOnTop="0"/>
    <field name="t_end_rain" labelOnTop="0"/>
    <field name="t_end_rain_min_one" labelOnTop="0"/>
    <field name="t_end_sum" labelOnTop="0"/>
    <field name="t_start_rain" labelOnTop="0"/>
    <field name="wlvl_t_end_sum" labelOnTop="0"/>
    <field name="wlvl_t_start_rain" labelOnTop="0"/>
    <field name="wlvlv_t_0" labelOnTop="0"/>
    <field name="wlvlv_t_end_rain" labelOnTop="0"/>
    <field name="wvlv_t_end_rain_min_one" labelOnTop="0"/>
  </labelOnTop>
  <dataDefinedFieldProperties/>
  <widgets/>
  <previewExpression>COALESCE( "T0_wlvl", '&lt;NULL>' )</previewExpression>
  <mapTip>T0_wlvl</mapTip>
  <layerGeometryType>0</layerGeometryType>
</qgis>
