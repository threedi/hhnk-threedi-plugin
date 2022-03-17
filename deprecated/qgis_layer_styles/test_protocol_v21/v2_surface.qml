<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis maxScale="0" simplifyMaxScale="1" version="3.16.11-Hannover" hasScaleBasedVisibilityFlag="0" simplifyDrawingHints="1" simplifyDrawingTol="1" simplifyAlgorithm="0" readOnly="0" labelsEnabled="0" minScale="100000000" styleCategories="AllStyleCategories" simplifyLocal="1">
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
      <symbol type="fill" name="0" clip_to_extent="1" force_rhr="0" alpha="1">
        <layer enabled="1" class="SimpleFill" locked="0" pass="0">
          <prop k="border_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="color" v="244,198,119,255"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="133,112,8,255"/>
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
  <customproperties>
    <property key="embeddedWidgets/count" value="0"/>
    <property key="variableNames"/>
    <property key="variableValues"/>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>0.9</layerOpacity>
  <SingleCategoryDiagramRenderer attributeLegend="1" diagramType="Histogram">
    <DiagramCategory lineSizeType="MM" height="15" opacity="1" enabled="0" penAlpha="255" sizeScale="3x:0,0,0,0,0,0" minScaleDenominator="0" spacing="0" spacingUnit="MM" scaleBasedVisibility="0" backgroundAlpha="255" maxScaleDenominator="1e+08" labelPlacementMethod="XHeight" penWidth="0" scaleDependency="Area" direction="1" penColor="#000000" backgroundColor="#ffffff" spacingUnitScale="3x:0,0,0,0,0,0" width="15" minimumSize="0" diagramOrientation="Up" lineSizeScale="3x:0,0,0,0,0,0" showAxis="0" sizeType="MM" rotationOffset="270" barWidth="5">
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
    <field configurationFlags="None" name="id">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="display_name">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="code">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="zoom_category">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
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
    <field configurationFlags="None" name="nr_of_inhabitants">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="dry_weather_flow">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="function">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="area">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="surface_parameters_id">
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
    <alias field="id" name="" index="0"/>
    <alias field="display_name" name="" index="1"/>
    <alias field="code" name="" index="2"/>
    <alias field="zoom_category" name="" index="3"/>
    <alias field="nr_of_inhabitants" name="" index="4"/>
    <alias field="dry_weather_flow" name="" index="5"/>
    <alias field="function" name="" index="6"/>
    <alias field="area" name="" index="7"/>
    <alias field="surface_parameters_id" name="" index="8"/>
  </aliases>
  <defaults>
    <default applyOnUpdate="0" field="id" expression="if(maximum(id) is null,1, maximum(id)+1)"/>
    <default applyOnUpdate="0" field="display_name" expression="'new'"/>
    <default applyOnUpdate="0" field="code" expression="'new'"/>
    <default applyOnUpdate="0" field="zoom_category" expression="-1"/>
    <default applyOnUpdate="0" field="nr_of_inhabitants" expression=""/>
    <default applyOnUpdate="0" field="dry_weather_flow" expression=""/>
    <default applyOnUpdate="0" field="function" expression=""/>
    <default applyOnUpdate="0" field="area" expression="$area"/>
    <default applyOnUpdate="0" field="surface_parameters_id" expression=""/>
  </defaults>
  <constraints>
    <constraint unique_strength="1" constraints="3" field="id" exp_strength="0" notnull_strength="1"/>
    <constraint unique_strength="0" constraints="1" field="display_name" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="1" field="code" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="1" field="zoom_category" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="0" field="nr_of_inhabitants" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="dry_weather_flow" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="function" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="1" field="area" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="1" field="surface_parameters_id" exp_strength="0" notnull_strength="2"/>
  </constraints>
  <constraintExpressions>
    <constraint field="id" exp="" desc=""/>
    <constraint field="display_name" exp="" desc=""/>
    <constraint field="code" exp="" desc=""/>
    <constraint field="zoom_category" exp="" desc=""/>
    <constraint field="nr_of_inhabitants" exp="" desc=""/>
    <constraint field="dry_weather_flow" exp="" desc=""/>
    <constraint field="function" exp="" desc=""/>
    <constraint field="area" exp="" desc=""/>
    <constraint field="surface_parameters_id" exp="" desc=""/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction key="Canvas" value="{00000000-0000-0000-0000-000000000000}"/>
  </attributeactions>
  <attributetableconfig actionWidgetStyle="dropDown" sortExpression="" sortOrder="0">
    <columns>
      <column type="field" name="id" width="-1" hidden="0"/>
      <column type="field" name="display_name" width="-1" hidden="0"/>
      <column type="field" name="code" width="-1" hidden="0"/>
      <column type="field" name="zoom_category" width="-1" hidden="0"/>
      <column type="field" name="nr_of_inhabitants" width="-1" hidden="0"/>
      <column type="field" name="dry_weather_flow" width="-1" hidden="0"/>
      <column type="field" name="function" width="-1" hidden="0"/>
      <column type="field" name="area" width="-1" hidden="0"/>
      <column type="field" name="surface_parameters_id" width="-1" hidden="0"/>
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
  <editorlayout>tablayout</editorlayout>
  <attributeEditorForm>
    <attributeEditorContainer columnCount="1" name="Surface" groupBox="0" showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="">
      <attributeEditorContainer columnCount="1" name="General" groupBox="1" showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="">
        <attributeEditorField name="id" showLabel="1" index="0"/>
        <attributeEditorField name="display_name" showLabel="1" index="1"/>
        <attributeEditorField name="code" showLabel="1" index="2"/>
      </attributeEditorContainer>
      <attributeEditorContainer columnCount="1" name="Characteristics" groupBox="1" showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="">
        <attributeEditorContainer columnCount="1" name="Rain water" groupBox="1" showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="">
          <attributeEditorField name="surface_parameters_id" showLabel="1" index="8"/>
          <attributeEditorField name="area" showLabel="1" index="7"/>
        </attributeEditorContainer>
        <attributeEditorContainer columnCount="1" name="Municipal water" groupBox="1" showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="">
          <attributeEditorField name="nr_of_inhabitants" showLabel="1" index="4"/>
          <attributeEditorField name="dry_weather_flow" showLabel="1" index="5"/>
        </attributeEditorContainer>
      </attributeEditorContainer>
      <attributeEditorContainer columnCount="1" name="Visualization" groupBox="1" showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="">
        <attributeEditorField name="zoom_category" showLabel="1" index="3"/>
        <attributeEditorField name="function" showLabel="1" index="6"/>
      </attributeEditorContainer>
    </attributeEditorContainer>
  </attributeEditorForm>
  <editable>
    <field editable="1" name="area"/>
    <field editable="1" name="code"/>
    <field editable="1" name="display_name"/>
    <field editable="1" name="dry_weather_flow"/>
    <field editable="1" name="function"/>
    <field editable="1" name="id"/>
    <field editable="1" name="nr_of_inhabitants"/>
    <field editable="1" name="surface_parameters_id"/>
    <field editable="1" name="zoom_category"/>
  </editable>
  <labelOnTop>
    <field labelOnTop="0" name="area"/>
    <field labelOnTop="0" name="code"/>
    <field labelOnTop="0" name="display_name"/>
    <field labelOnTop="0" name="dry_weather_flow"/>
    <field labelOnTop="0" name="function"/>
    <field labelOnTop="0" name="id"/>
    <field labelOnTop="0" name="nr_of_inhabitants"/>
    <field labelOnTop="0" name="surface_parameters_id"/>
    <field labelOnTop="0" name="zoom_category"/>
  </labelOnTop>
  <dataDefinedFieldProperties/>
  <widgets/>
  <previewExpression>display_name</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>2</layerGeometryType>
</qgis>
