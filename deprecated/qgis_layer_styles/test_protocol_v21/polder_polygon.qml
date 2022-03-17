<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis maxScale="0" simplifyMaxScale="1" version="3.16.11-Hannover" hasScaleBasedVisibilityFlag="0" simplifyDrawingHints="1" simplifyDrawingTol="1" simplifyAlgorithm="0" readOnly="0" labelsEnabled="1" minScale="100000000" styleCategories="AllStyleCategories" simplifyLocal="1">
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
  <renderer-v2 type="invertedPolygonRenderer" forceraster="0" enableorderby="0" preprocessing="0">
    <renderer-v2 type="singleSymbol" forceraster="0" enableorderby="0" symbollevels="0">
      <symbols>
        <symbol type="fill" name="0" clip_to_extent="1" force_rhr="0" alpha="1">
          <layer enabled="1" class="SimpleFill" locked="0" pass="0">
            <prop k="border_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
            <prop k="color" v="0,0,0,255"/>
            <prop k="joinstyle" v="bevel"/>
            <prop k="offset" v="0,0"/>
            <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
            <prop k="offset_unit" v="MM"/>
            <prop k="outline_color" v="0,0,0,255"/>
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
      </symbols>
      <rotation/>
      <sizescale/>
    </renderer-v2>
  </renderer-v2>
  <customproperties>
    <property key="embeddedWidgets/count" value="0"/>
    <property key="variableNames"/>
    <property key="variableValues"/>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>0.4</layerOpacity>
  <SingleCategoryDiagramRenderer attributeLegend="1" diagramType="Histogram">
    <DiagramCategory lineSizeType="MM" height="15" opacity="1" enabled="0" penAlpha="255" sizeScale="3x:0,0,0,0,0,0" minScaleDenominator="inf" spacing="0" spacingUnit="MM" scaleBasedVisibility="0" backgroundAlpha="255" maxScaleDenominator="1e+08" labelPlacementMethod="XHeight" penWidth="0" scaleDependency="Area" direction="1" penColor="#000000" backgroundColor="#ffffff" spacingUnitScale="3x:0,0,0,0,0,0" width="15" minimumSize="0" diagramOrientation="Up" lineSizeScale="3x:0,0,0,0,0,0" showAxis="0" sizeType="MM" rotationOffset="270" barWidth="5">
      <fontProperties style="" description="MS Shell Dlg 2,7.5,-1,5,50,0,0,0,0,0"/>
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
  <DiagramLayerSettings zIndex="0" showAll="1" obstacle="0" priority="0" placement="0" linePlacementFlags="10" dist="0">
    <properties>
      <Option type="Map">
        <Option type="QString" name="name" value=""/>
        <Option type="Map" name="properties">
          <Option type="Map" name="show">
            <Option type="bool" name="active" value="true"/>
            <Option type="QString" name="field" value="polder_id"/>
            <Option type="int" name="type" value="2"/>
          </Option>
        </Option>
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
    <field configurationFlags="None" name="polder_id">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="polder_typ">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="cnt_afvrkw">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="name">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="type">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="cnt_pump_e">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="cnt_pump_1">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="cnt_culver">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="cnt_culv_1">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="cnt_weirs_">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="cnt_weirs1">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="cnt_kruisi">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="cnt_krui_1">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="prct_loose">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="prct_noway">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="prct_pump_">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="prct_pump1">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="prct_culve">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="prct_cul_1">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="prct_weirs">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="prct_wei_1">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="prct_kruis">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="prct_kru_1">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="SHAPE_Leng">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="SHAPE_Area">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
  </fieldConfiguration>
  <aliases>
    <alias field="polder_id" name="" index="0"/>
    <alias field="polder_typ" name="" index="1"/>
    <alias field="cnt_afvrkw" name="" index="2"/>
    <alias field="name" name="" index="3"/>
    <alias field="type" name="" index="4"/>
    <alias field="cnt_pump_e" name="" index="5"/>
    <alias field="cnt_pump_1" name="" index="6"/>
    <alias field="cnt_culver" name="" index="7"/>
    <alias field="cnt_culv_1" name="" index="8"/>
    <alias field="cnt_weirs_" name="" index="9"/>
    <alias field="cnt_weirs1" name="" index="10"/>
    <alias field="cnt_kruisi" name="" index="11"/>
    <alias field="cnt_krui_1" name="" index="12"/>
    <alias field="prct_loose" name="" index="13"/>
    <alias field="prct_noway" name="" index="14"/>
    <alias field="prct_pump_" name="" index="15"/>
    <alias field="prct_pump1" name="" index="16"/>
    <alias field="prct_culve" name="" index="17"/>
    <alias field="prct_cul_1" name="" index="18"/>
    <alias field="prct_weirs" name="" index="19"/>
    <alias field="prct_wei_1" name="" index="20"/>
    <alias field="prct_kruis" name="" index="21"/>
    <alias field="prct_kru_1" name="" index="22"/>
    <alias field="SHAPE_Leng" name="" index="23"/>
    <alias field="SHAPE_Area" name="" index="24"/>
  </aliases>
  <defaults>
    <default applyOnUpdate="0" field="polder_id" expression=""/>
    <default applyOnUpdate="0" field="polder_typ" expression=""/>
    <default applyOnUpdate="0" field="cnt_afvrkw" expression=""/>
    <default applyOnUpdate="0" field="name" expression=""/>
    <default applyOnUpdate="0" field="type" expression=""/>
    <default applyOnUpdate="0" field="cnt_pump_e" expression=""/>
    <default applyOnUpdate="0" field="cnt_pump_1" expression=""/>
    <default applyOnUpdate="0" field="cnt_culver" expression=""/>
    <default applyOnUpdate="0" field="cnt_culv_1" expression=""/>
    <default applyOnUpdate="0" field="cnt_weirs_" expression=""/>
    <default applyOnUpdate="0" field="cnt_weirs1" expression=""/>
    <default applyOnUpdate="0" field="cnt_kruisi" expression=""/>
    <default applyOnUpdate="0" field="cnt_krui_1" expression=""/>
    <default applyOnUpdate="0" field="prct_loose" expression=""/>
    <default applyOnUpdate="0" field="prct_noway" expression=""/>
    <default applyOnUpdate="0" field="prct_pump_" expression=""/>
    <default applyOnUpdate="0" field="prct_pump1" expression=""/>
    <default applyOnUpdate="0" field="prct_culve" expression=""/>
    <default applyOnUpdate="0" field="prct_cul_1" expression=""/>
    <default applyOnUpdate="0" field="prct_weirs" expression=""/>
    <default applyOnUpdate="0" field="prct_wei_1" expression=""/>
    <default applyOnUpdate="0" field="prct_kruis" expression=""/>
    <default applyOnUpdate="0" field="prct_kru_1" expression=""/>
    <default applyOnUpdate="0" field="SHAPE_Leng" expression=""/>
    <default applyOnUpdate="0" field="SHAPE_Area" expression=""/>
  </defaults>
  <constraints>
    <constraint unique_strength="0" constraints="0" field="polder_id" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="polder_typ" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="cnt_afvrkw" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="name" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="type" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="cnt_pump_e" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="cnt_pump_1" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="cnt_culver" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="cnt_culv_1" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="cnt_weirs_" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="cnt_weirs1" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="cnt_kruisi" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="cnt_krui_1" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="prct_loose" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="prct_noway" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="prct_pump_" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="prct_pump1" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="prct_culve" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="prct_cul_1" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="prct_weirs" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="prct_wei_1" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="prct_kruis" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="prct_kru_1" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="SHAPE_Leng" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="SHAPE_Area" exp_strength="0" notnull_strength="0"/>
  </constraints>
  <constraintExpressions>
    <constraint field="polder_id" exp="" desc=""/>
    <constraint field="polder_typ" exp="" desc=""/>
    <constraint field="cnt_afvrkw" exp="" desc=""/>
    <constraint field="name" exp="" desc=""/>
    <constraint field="type" exp="" desc=""/>
    <constraint field="cnt_pump_e" exp="" desc=""/>
    <constraint field="cnt_pump_1" exp="" desc=""/>
    <constraint field="cnt_culver" exp="" desc=""/>
    <constraint field="cnt_culv_1" exp="" desc=""/>
    <constraint field="cnt_weirs_" exp="" desc=""/>
    <constraint field="cnt_weirs1" exp="" desc=""/>
    <constraint field="cnt_kruisi" exp="" desc=""/>
    <constraint field="cnt_krui_1" exp="" desc=""/>
    <constraint field="prct_loose" exp="" desc=""/>
    <constraint field="prct_noway" exp="" desc=""/>
    <constraint field="prct_pump_" exp="" desc=""/>
    <constraint field="prct_pump1" exp="" desc=""/>
    <constraint field="prct_culve" exp="" desc=""/>
    <constraint field="prct_cul_1" exp="" desc=""/>
    <constraint field="prct_weirs" exp="" desc=""/>
    <constraint field="prct_wei_1" exp="" desc=""/>
    <constraint field="prct_kruis" exp="" desc=""/>
    <constraint field="prct_kru_1" exp="" desc=""/>
    <constraint field="SHAPE_Leng" exp="" desc=""/>
    <constraint field="SHAPE_Area" exp="" desc=""/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions/>
  <attributetableconfig actionWidgetStyle="dropDown" sortExpression="" sortOrder="0">
    <columns>
      <column type="field" name="polder_id" width="-1" hidden="0"/>
      <column type="field" name="polder_typ" width="-1" hidden="0"/>
      <column type="field" name="cnt_afvrkw" width="-1" hidden="0"/>
      <column type="field" name="name" width="-1" hidden="0"/>
      <column type="field" name="type" width="-1" hidden="0"/>
      <column type="field" name="cnt_pump_e" width="-1" hidden="0"/>
      <column type="field" name="cnt_pump_1" width="-1" hidden="0"/>
      <column type="field" name="cnt_culver" width="-1" hidden="0"/>
      <column type="field" name="cnt_culv_1" width="-1" hidden="0"/>
      <column type="field" name="cnt_weirs_" width="-1" hidden="0"/>
      <column type="field" name="cnt_weirs1" width="-1" hidden="0"/>
      <column type="field" name="cnt_kruisi" width="-1" hidden="0"/>
      <column type="field" name="cnt_krui_1" width="-1" hidden="0"/>
      <column type="field" name="prct_loose" width="-1" hidden="0"/>
      <column type="field" name="prct_noway" width="-1" hidden="0"/>
      <column type="field" name="prct_pump_" width="-1" hidden="0"/>
      <column type="field" name="prct_pump1" width="-1" hidden="0"/>
      <column type="field" name="prct_culve" width="-1" hidden="0"/>
      <column type="field" name="prct_cul_1" width="-1" hidden="0"/>
      <column type="field" name="prct_weirs" width="-1" hidden="0"/>
      <column type="field" name="prct_wei_1" width="-1" hidden="0"/>
      <column type="field" name="prct_kruis" width="-1" hidden="0"/>
      <column type="field" name="prct_kru_1" width="-1" hidden="0"/>
      <column type="field" name="SHAPE_Leng" width="-1" hidden="0"/>
      <column type="field" name="SHAPE_Area" width="-1" hidden="0"/>
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
from qgis.PyQt.QtWidgets import QWidget

def my_form_open(dialog, layer, feature):
	geom = feature.geometry()
	control = dialog.findChild(QWidget, "MyLineEdit")
]]></editforminitcode>
  <featformsuppress>0</featformsuppress>
  <editorlayout>generatedlayout</editorlayout>
  <editable/>
  <labelOnTop/>
  <dataDefinedFieldProperties/>
  <widgets/>
  <previewExpression>COALESCE( "name", '&lt;NULL>' )</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>2</layerGeometryType>
</qgis>
