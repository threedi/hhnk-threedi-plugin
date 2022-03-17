<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis maxScale="0" version="3.16.11-Hannover" hasScaleBasedVisibilityFlag="0" readOnly="0" minScale="1e+08" styleCategories="AllStyleCategories">
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
  <customproperties>
    <property key="dualview/previewExpressions" value="var_name"/>
    <property key="embeddedWidgets/count" value="0"/>
    <property key="variableNames"/>
    <property key="variableValues"/>
  </customproperties>
  <geometryOptions geometryPrecision="0" removeDuplicateNodes="0">
    <activeChecks/>
    <checkConfiguration/>
  </geometryOptions>
  <legend type="default-vector"/>
  <referencedLayers/>
  <fieldConfiguration>
    <field configurationFlags="None" name="global_settings_id">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="timestep">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="var_name">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="aggregation_in_space">
      <editWidget type="Hidden">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="aggregation_method">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option type="QString" name="average" value="avg"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="minimum" value="min"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="maximum" value="max"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="cumulative" value="cum"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="median" value="med"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="cumulative negative" value="cum_negative"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="cumulative positive" value="cum_positive"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="current" value="current"/>
              </Option>
            </Option>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="flow_variable">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option type="QString" name="discharge" value="discharge"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="flow velocity" value="flow_velocity"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="pump discharge" value="pump_discharge"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="rain" value="rain"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="waterlevel" value="waterlevel"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="wet cross section" value="wet_cross-section"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="wet surface" value="wet_surface"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="lateral discharge" value="lateral_discharge"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="volume" value="volume"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="infiltration" value="simple_infiltration"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="leakage" value="leakage"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="interception" value="interception"/>
              </Option>
            </Option>
          </Option>
        </config>
      </editWidget>
    </field>
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
  </fieldConfiguration>
  <aliases>
    <alias field="global_settings_id" name="" index="0"/>
    <alias field="timestep" name="" index="1"/>
    <alias field="var_name" name="" index="2"/>
    <alias field="aggregation_in_space" name="" index="3"/>
    <alias field="aggregation_method" name="" index="4"/>
    <alias field="flow_variable" name="" index="5"/>
    <alias field="id" name="" index="6"/>
  </aliases>
  <defaults>
    <default applyOnUpdate="0" field="global_settings_id" expression=""/>
    <default applyOnUpdate="0" field="timestep" expression=""/>
    <default applyOnUpdate="0" field="var_name" expression=""/>
    <default applyOnUpdate="0" field="aggregation_in_space" expression="0"/>
    <default applyOnUpdate="0" field="aggregation_method" expression=""/>
    <default applyOnUpdate="0" field="flow_variable" expression=""/>
    <default applyOnUpdate="0" field="id" expression="if(maximum(id) is null,1, maximum(id)+1)"/>
  </defaults>
  <constraints>
    <constraint unique_strength="0" constraints="0" field="global_settings_id" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="1" field="timestep" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="1" field="var_name" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="1" field="aggregation_in_space" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="1" field="aggregation_method" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="1" field="flow_variable" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="1" constraints="3" field="id" exp_strength="0" notnull_strength="1"/>
  </constraints>
  <constraintExpressions>
    <constraint field="global_settings_id" exp="" desc=""/>
    <constraint field="timestep" exp="" desc=""/>
    <constraint field="var_name" exp="" desc=""/>
    <constraint field="aggregation_in_space" exp="" desc=""/>
    <constraint field="aggregation_method" exp="" desc=""/>
    <constraint field="flow_variable" exp="" desc=""/>
    <constraint field="id" exp="" desc=""/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction key="Canvas" value="{00000000-0000-0000-0000-000000000000}"/>
  </attributeactions>
  <attributetableconfig actionWidgetStyle="dropDown" sortExpression="" sortOrder="0">
    <columns>
      <column type="field" name="timestep" width="214" hidden="0"/>
      <column type="field" name="var_name" width="207" hidden="0"/>
      <column type="field" name="global_settings_id" width="123" hidden="0"/>
      <column type="field" name="aggregation_in_space" width="168" hidden="0"/>
      <column type="field" name="aggregation_method" width="-1" hidden="0"/>
      <column type="field" name="flow_variable" width="-1" hidden="0"/>
      <column type="field" name="id" width="-1" hidden="0"/>
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
    <attributeEditorContainer columnCount="1" name="General" groupBox="0" showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="">
      <attributeEditorField name="id" showLabel="1" index="6"/>
      <attributeEditorField name="flow_variable" showLabel="1" index="5"/>
      <attributeEditorField name="aggregation_method" showLabel="1" index="4"/>
      <attributeEditorField name="timestep" showLabel="1" index="1"/>
      <attributeEditorField name="var_name" showLabel="1" index="2"/>
      <attributeEditorField name="global_settings_id" showLabel="1" index="0"/>
    </attributeEditorContainer>
  </attributeEditorForm>
  <editable>
    <field editable="1" name="aggregation_in_space"/>
    <field editable="1" name="aggregation_method"/>
    <field editable="1" name="flow_variable"/>
    <field editable="1" name="global_settings_id"/>
    <field editable="1" name="id"/>
    <field editable="1" name="timestep"/>
    <field editable="1" name="var_name"/>
  </editable>
  <labelOnTop>
    <field labelOnTop="0" name="aggregation_in_space"/>
    <field labelOnTop="0" name="aggregation_method"/>
    <field labelOnTop="0" name="flow_variable"/>
    <field labelOnTop="0" name="global_settings_id"/>
    <field labelOnTop="0" name="id"/>
    <field labelOnTop="0" name="timestep"/>
    <field labelOnTop="0" name="var_name"/>
  </labelOnTop>
  <dataDefinedFieldProperties/>
  <widgets/>
  <previewExpression>var_name</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>4</layerGeometryType>
</qgis>
