<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis maxScale="0" simplifyMaxScale="1" version="3.16.11-Hannover" hasScaleBasedVisibilityFlag="0" simplifyDrawingHints="1" simplifyDrawingTol="1" simplifyAlgorithm="0" readOnly="0" labelsEnabled="1" minScale="0" styleCategories="AllStyleCategories" simplifyLocal="1">
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
        <layer enabled="1" class="ArrowLine" locked="0" pass="0">
          <prop k="arrow_start_width" v="1"/>
          <prop k="arrow_start_width_unit" v="MM"/>
          <prop k="arrow_start_width_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="arrow_type" v="0"/>
          <prop k="arrow_width" v="1"/>
          <prop k="arrow_width_unit" v="MM"/>
          <prop k="arrow_width_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="head_length" v="1.5"/>
          <prop k="head_length_unit" v="MM"/>
          <prop k="head_length_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="head_thickness" v="1.5"/>
          <prop k="head_thickness_unit" v="MM"/>
          <prop k="head_thickness_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="head_type" v="0"/>
          <prop k="is_curved" v="1"/>
          <prop k="is_repeated" v="1"/>
          <prop k="offset" v="0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="offset_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="ring_filter" v="0"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
          <symbol type="fill" name="@0@0" clip_to_extent="1" force_rhr="0" alpha="1">
            <layer enabled="1" class="SimpleFill" locked="0" pass="0">
              <prop k="border_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="color" v="255,174,0,255"/>
              <prop k="joinstyle" v="bevel"/>
              <prop k="offset" v="0,0"/>
              <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="outline_color" v="213,180,60,255"/>
              <prop k="outline_style" v="solid"/>
              <prop k="outline_width" v="0.26"/>
              <prop k="outline_width_unit" v="MM"/>
              <prop k="style" v="solid"/>
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
  <labeling type="simple">
    <settings calloutType="simple">
      <text-style multilineHeight="1" isExpression="1" fontStrikeout="0" fontSize="8.25" textOrientation="horizontal" fontSizeUnit="Point" fontLetterSpacing="0" previewBkgrdColor="255,255,255,255" namedStyle="Standaard" fontSizeMapUnitScale="3x:0,0,0,0,0,0" textColor="0,0,0,255" allowHtml="0" capitalization="0" fontItalic="0" blendMode="0" fontWeight="50" textOpacity="1" useSubstitutions="0" fieldName=" &quot;code&quot;  || '\n' || 'start: ' ||  &quot;start_action_value&quot; || '\n' ||&#xd;&#xa;  'min: ' || &quot;min_action_value&quot; ||&#xd;&#xa;  '\n' || 'max: ' || &quot;max_action_value&quot; || '\n'" fontUnderline="0" fontKerning="1" fontFamily="MS Shell Dlg 2" fontWordSpacing="0">
        <text-buffer bufferBlendMode="0" bufferColor="255,255,255,255" bufferJoinStyle="128" bufferDraw="1" bufferOpacity="1" bufferSizeUnits="MM" bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferSize="1" bufferNoFill="1"/>
        <text-mask maskSize="1.5" maskSizeUnits="MM" maskType="0" maskEnabled="0" maskOpacity="1" maskJoinStyle="128" maskedSymbolLayers="" maskSizeMapUnitScale="3x:0,0,0,0,0,0"/>
        <background shapeSizeUnit="MM" shapeJoinStyle="64" shapeSizeY="0" shapeRadiiX="0" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeOffsetX="0" shapeSizeX="0" shapeBorderColor="128,128,128,255" shapeBlendMode="0" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeFillColor="255,255,255,255" shapeOffsetY="0" shapeSVGFile="" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeBorderWidthUnit="MM" shapeRotation="0" shapeType="0" shapeRadiiY="0" shapeOpacity="1" shapeBorderWidth="0" shapeSizeType="0" shapeRotationType="0" shapeDraw="0" shapeOffsetUnit="MM" shapeRadiiUnit="MM">
          <symbol type="marker" name="markerSymbol" clip_to_extent="1" force_rhr="0" alpha="1">
            <layer enabled="1" class="SimpleMarker" locked="0" pass="0">
              <prop k="angle" v="0"/>
              <prop k="color" v="196,60,57,255"/>
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
        </background>
        <shadow shadowOffsetGlobal="1" shadowDraw="0" shadowRadiusUnit="MM" shadowOpacity="0.7" shadowRadiusAlphaOnly="0" shadowOffsetAngle="135" shadowOffsetDist="1" shadowOffsetUnit="MM" shadowScale="100" shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowColor="0,0,0,255" shadowBlendMode="6" shadowUnder="0" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowRadius="1.5"/>
        <dd_properties>
          <Option type="Map">
            <Option type="QString" name="name" value=""/>
            <Option name="properties"/>
            <Option type="QString" name="type" value="collection"/>
          </Option>
        </dd_properties>
        <substitutions/>
      </text-style>
      <text-format addDirectionSymbol="0" leftDirectionSymbol="&lt;" rightDirectionSymbol=">" reverseDirectionSymbol="0" plussign="0" decimals="3" wrapChar="" multilineAlign="0" autoWrapLength="0" placeDirectionSymbol="0" formatNumbers="0" useMaxLineLengthForAutoWrap="1"/>
      <placement xOffset="0" overrunDistanceMapUnitScale="3x:0,0,0,0,0,0" placementFlags="10" overrunDistanceUnit="MM" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" preserveRotation="1" layerType="LineGeometry" lineAnchorType="0" distMapUnitScale="3x:0,0,0,0,0,0" priority="5" overrunDistance="0" geometryGeneratorType="PointGeometry" distUnits="MM" rotationAngle="0" repeatDistanceUnits="MM" geometryGenerator="" dist="0" maxCurvedCharAngleIn="25" fitInPolygonOnly="0" centroidInside="0" maxCurvedCharAngleOut="-25" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" centroidWhole="0" geometryGeneratorEnabled="0" offsetUnits="MM" polygonPlacementFlags="2" placement="2" lineAnchorPercent="0.5" offsetType="0" repeatDistance="0" yOffset="0" quadOffset="4"/>
      <rendering displayAll="1" obstacleType="1" zIndex="0" labelPerPart="0" fontLimitPixelSize="0" minFeatureSize="0" fontMinPixelSize="3" fontMaxPixelSize="10000" obstacle="1" upsidedownLabels="0" scaleMax="41486" obstacleFactor="1" drawLabels="1" maxNumLabels="2000" limitNumLabels="0" mergeLines="1" scaleMin="0" scaleVisibility="1"/>
      <dd_properties>
        <Option type="Map">
          <Option type="QString" name="name" value=""/>
          <Option name="properties"/>
          <Option type="QString" name="type" value="collection"/>
        </Option>
      </dd_properties>
      <callout type="simple">
        <Option type="Map">
          <Option type="QString" name="anchorPoint" value="pole_of_inaccessibility"/>
          <Option type="Map" name="ddProperties">
            <Option type="QString" name="name" value=""/>
            <Option name="properties"/>
            <Option type="QString" name="type" value="collection"/>
          </Option>
          <Option type="bool" name="drawToAllParts" value="false"/>
          <Option type="QString" name="enabled" value="0"/>
          <Option type="QString" name="labelAnchorPoint" value="point_on_exterior"/>
          <Option type="QString" name="lineSymbol" value="&lt;symbol type=&quot;line&quot; name=&quot;symbol&quot; clip_to_extent=&quot;1&quot; force_rhr=&quot;0&quot; alpha=&quot;1&quot;>&lt;layer enabled=&quot;1&quot; class=&quot;SimpleLine&quot; locked=&quot;0&quot; pass=&quot;0&quot;>&lt;prop k=&quot;align_dash_pattern&quot; v=&quot;0&quot;/>&lt;prop k=&quot;capstyle&quot; v=&quot;square&quot;/>&lt;prop k=&quot;customdash&quot; v=&quot;5;2&quot;/>&lt;prop k=&quot;customdash_map_unit_scale&quot; v=&quot;3x:0,0,0,0,0,0&quot;/>&lt;prop k=&quot;customdash_unit&quot; v=&quot;MM&quot;/>&lt;prop k=&quot;dash_pattern_offset&quot; v=&quot;0&quot;/>&lt;prop k=&quot;dash_pattern_offset_map_unit_scale&quot; v=&quot;3x:0,0,0,0,0,0&quot;/>&lt;prop k=&quot;dash_pattern_offset_unit&quot; v=&quot;MM&quot;/>&lt;prop k=&quot;draw_inside_polygon&quot; v=&quot;0&quot;/>&lt;prop k=&quot;joinstyle&quot; v=&quot;bevel&quot;/>&lt;prop k=&quot;line_color&quot; v=&quot;60,60,60,255&quot;/>&lt;prop k=&quot;line_style&quot; v=&quot;solid&quot;/>&lt;prop k=&quot;line_width&quot; v=&quot;0.3&quot;/>&lt;prop k=&quot;line_width_unit&quot; v=&quot;MM&quot;/>&lt;prop k=&quot;offset&quot; v=&quot;0&quot;/>&lt;prop k=&quot;offset_map_unit_scale&quot; v=&quot;3x:0,0,0,0,0,0&quot;/>&lt;prop k=&quot;offset_unit&quot; v=&quot;MM&quot;/>&lt;prop k=&quot;ring_filter&quot; v=&quot;0&quot;/>&lt;prop k=&quot;tweak_dash_pattern_on_corners&quot; v=&quot;0&quot;/>&lt;prop k=&quot;use_custom_dash&quot; v=&quot;0&quot;/>&lt;prop k=&quot;width_map_unit_scale&quot; v=&quot;3x:0,0,0,0,0,0&quot;/>&lt;data_defined_properties>&lt;Option type=&quot;Map&quot;>&lt;Option type=&quot;QString&quot; name=&quot;name&quot; value=&quot;&quot;/>&lt;Option name=&quot;properties&quot;/>&lt;Option type=&quot;QString&quot; name=&quot;type&quot; value=&quot;collection&quot;/>&lt;/Option>&lt;/data_defined_properties>&lt;/layer>&lt;/symbol>"/>
          <Option type="double" name="minLength" value="0"/>
          <Option type="QString" name="minLengthMapUnitScale" value="3x:0,0,0,0,0,0"/>
          <Option type="QString" name="minLengthUnit" value="MM"/>
          <Option type="double" name="offsetFromAnchor" value="0"/>
          <Option type="QString" name="offsetFromAnchorMapUnitScale" value="3x:0,0,0,0,0,0"/>
          <Option type="QString" name="offsetFromAnchorUnit" value="MM"/>
          <Option type="double" name="offsetFromLabel" value="0"/>
          <Option type="QString" name="offsetFromLabelMapUnitScale" value="3x:0,0,0,0,0,0"/>
          <Option type="QString" name="offsetFromLabelUnit" value="MM"/>
        </Option>
      </callout>
    </settings>
  </labeling>
  <customproperties/>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <geometryOptions geometryPrecision="0" removeDuplicateNodes="0">
    <activeChecks/>
    <checkConfiguration/>
  </geometryOptions>
  <legend type="default-vector"/>
  <referencedLayers/>
  <fieldConfiguration>
    <field configurationFlags="None" name="fid">
      <editWidget type="">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="control_id">
      <editWidget type="">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="action_table">
      <editWidget type="">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="target_type">
      <editWidget type="">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="target_id">
      <editWidget type="">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="code">
      <editWidget type="">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="start_action_value">
      <editWidget type="">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="min_action_value">
      <editWidget type="">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="max_action_value">
      <editWidget type="">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="hdb_streefpeil">
      <editWidget type="">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="hdb_kruin_min">
      <editWidget type="">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="hdb_kruin_max">
      <editWidget type="">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
  </fieldConfiguration>
  <aliases>
    <alias field="fid" name="" index="0"/>
    <alias field="control_id" name="" index="1"/>
    <alias field="action_table" name="" index="2"/>
    <alias field="target_type" name="" index="3"/>
    <alias field="target_id" name="" index="4"/>
    <alias field="code" name="" index="5"/>
    <alias field="start_action_value" name="" index="6"/>
    <alias field="min_action_value" name="" index="7"/>
    <alias field="max_action_value" name="" index="8"/>
    <alias field="hdb_streefpeil" name="" index="9"/>
    <alias field="hdb_kruin_min" name="" index="10"/>
    <alias field="hdb_kruin_max" name="" index="11"/>
  </aliases>
  <defaults>
    <default applyOnUpdate="0" field="fid" expression=""/>
    <default applyOnUpdate="0" field="control_id" expression=""/>
    <default applyOnUpdate="0" field="action_table" expression=""/>
    <default applyOnUpdate="0" field="target_type" expression=""/>
    <default applyOnUpdate="0" field="target_id" expression=""/>
    <default applyOnUpdate="0" field="code" expression=""/>
    <default applyOnUpdate="0" field="start_action_value" expression=""/>
    <default applyOnUpdate="0" field="min_action_value" expression=""/>
    <default applyOnUpdate="0" field="max_action_value" expression=""/>
    <default applyOnUpdate="0" field="hdb_streefpeil" expression=""/>
    <default applyOnUpdate="0" field="hdb_kruin_min" expression=""/>
    <default applyOnUpdate="0" field="hdb_kruin_max" expression=""/>
  </defaults>
  <constraints>
    <constraint unique_strength="1" constraints="3" field="fid" exp_strength="0" notnull_strength="1"/>
    <constraint unique_strength="0" constraints="0" field="control_id" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="action_table" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="target_type" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="target_id" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="code" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="start_action_value" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="min_action_value" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="max_action_value" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="hdb_streefpeil" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="hdb_kruin_min" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="hdb_kruin_max" exp_strength="0" notnull_strength="0"/>
  </constraints>
  <constraintExpressions>
    <constraint field="fid" exp="" desc=""/>
    <constraint field="control_id" exp="" desc=""/>
    <constraint field="action_table" exp="" desc=""/>
    <constraint field="target_type" exp="" desc=""/>
    <constraint field="target_id" exp="" desc=""/>
    <constraint field="code" exp="" desc=""/>
    <constraint field="start_action_value" exp="" desc=""/>
    <constraint field="min_action_value" exp="" desc=""/>
    <constraint field="max_action_value" exp="" desc=""/>
    <constraint field="hdb_streefpeil" exp="" desc=""/>
    <constraint field="hdb_kruin_min" exp="" desc=""/>
    <constraint field="hdb_kruin_max" exp="" desc=""/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction key="Canvas" value="{00000000-0000-0000-0000-000000000000}"/>
  </attributeactions>
  <attributetableconfig actionWidgetStyle="dropDown" sortExpression="" sortOrder="0">
    <columns/>
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
  <editforminitcode><![CDATA[]]></editforminitcode>
  <featformsuppress>0</featformsuppress>
  <editorlayout>generatedlayout</editorlayout>
  <editable/>
  <labelOnTop/>
  <dataDefinedFieldProperties/>
  <widgets/>
  <previewExpression></previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>1</layerGeometryType>
</qgis>
