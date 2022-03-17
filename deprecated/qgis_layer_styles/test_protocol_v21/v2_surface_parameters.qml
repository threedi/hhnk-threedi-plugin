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
    <field configurationFlags="None" name="outflow_delay">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="surface_layer_thickness">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="infiltration">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="max_infiltration_capacity">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="min_infiltration_capacity">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="infiltration_decay_constant">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="infiltration_recovery_constant">
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
    <alias field="outflow_delay" name="" index="1"/>
    <alias field="surface_layer_thickness" name="" index="2"/>
    <alias field="infiltration" name="" index="3"/>
    <alias field="max_infiltration_capacity" name="" index="4"/>
    <alias field="min_infiltration_capacity" name="" index="5"/>
    <alias field="infiltration_decay_constant" name="" index="6"/>
    <alias field="infiltration_recovery_constant" name="" index="7"/>
  </aliases>
  <defaults>
    <default applyOnUpdate="0" field="id" expression="if(maximum(id) is null,1, maximum(id)+1)"/>
    <default applyOnUpdate="0" field="outflow_delay" expression=""/>
    <default applyOnUpdate="0" field="surface_layer_thickness" expression=""/>
    <default applyOnUpdate="0" field="infiltration" expression=""/>
    <default applyOnUpdate="0" field="max_infiltration_capacity" expression=""/>
    <default applyOnUpdate="0" field="min_infiltration_capacity" expression=""/>
    <default applyOnUpdate="0" field="infiltration_decay_constant" expression=""/>
    <default applyOnUpdate="0" field="infiltration_recovery_constant" expression=""/>
  </defaults>
  <constraints>
    <constraint unique_strength="1" constraints="3" field="id" exp_strength="0" notnull_strength="1"/>
    <constraint unique_strength="0" constraints="1" field="outflow_delay" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="1" field="surface_layer_thickness" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="1" field="infiltration" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="1" field="max_infiltration_capacity" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="1" field="min_infiltration_capacity" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="1" field="infiltration_decay_constant" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="1" field="infiltration_recovery_constant" exp_strength="0" notnull_strength="2"/>
  </constraints>
  <constraintExpressions>
    <constraint field="id" exp="" desc=""/>
    <constraint field="outflow_delay" exp="" desc=""/>
    <constraint field="surface_layer_thickness" exp="" desc=""/>
    <constraint field="infiltration" exp="" desc=""/>
    <constraint field="max_infiltration_capacity" exp="" desc=""/>
    <constraint field="min_infiltration_capacity" exp="" desc=""/>
    <constraint field="infiltration_decay_constant" exp="" desc=""/>
    <constraint field="infiltration_recovery_constant" exp="" desc=""/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction key="Canvas" value="{00000000-0000-0000-0000-000000000000}"/>
  </attributeactions>
  <attributetableconfig actionWidgetStyle="dropDown" sortExpression="" sortOrder="0">
    <columns>
      <column type="field" name="id" width="-1" hidden="0"/>
      <column type="field" name="outflow_delay" width="-1" hidden="0"/>
      <column type="field" name="surface_layer_thickness" width="-1" hidden="0"/>
      <column type="field" name="infiltration" width="-1" hidden="0"/>
      <column type="field" name="max_infiltration_capacity" width="-1" hidden="0"/>
      <column type="field" name="min_infiltration_capacity" width="-1" hidden="0"/>
      <column type="field" name="infiltration_decay_constant" width="-1" hidden="0"/>
      <column type="field" name="infiltration_recovery_constant" width="-1" hidden="0"/>
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
      <attributeEditorField name="id" showLabel="1" index="0"/>
      <attributeEditorField name="infiltration" showLabel="1" index="3"/>
      <attributeEditorField name="max_infiltration_capacity" showLabel="1" index="4"/>
      <attributeEditorField name="min_infiltration_capacity" showLabel="1" index="5"/>
      <attributeEditorField name="infiltration_decay_constant" showLabel="1" index="6"/>
      <attributeEditorField name="infiltration_recovery_constant" showLabel="1" index="7"/>
      <attributeEditorField name="surface_layer_thickness" showLabel="1" index="2"/>
      <attributeEditorField name="outflow_delay" showLabel="1" index="1"/>
    </attributeEditorContainer>
  </attributeEditorForm>
  <editable>
    <field editable="1" name="id"/>
    <field editable="1" name="infiltration"/>
    <field editable="1" name="infiltration_decay_constant"/>
    <field editable="1" name="infiltration_recovery_constant"/>
    <field editable="1" name="max_infiltration_capacity"/>
    <field editable="1" name="min_infiltration_capacity"/>
    <field editable="1" name="outflow_delay"/>
    <field editable="1" name="surface_layer_thickness"/>
  </editable>
  <labelOnTop>
    <field labelOnTop="0" name="id"/>
    <field labelOnTop="0" name="infiltration"/>
    <field labelOnTop="0" name="infiltration_decay_constant"/>
    <field labelOnTop="0" name="infiltration_recovery_constant"/>
    <field labelOnTop="0" name="max_infiltration_capacity"/>
    <field labelOnTop="0" name="min_infiltration_capacity"/>
    <field labelOnTop="0" name="outflow_delay"/>
    <field labelOnTop="0" name="surface_layer_thickness"/>
  </labelOnTop>
  <dataDefinedFieldProperties/>
  <widgets/>
  <previewExpression>id</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>4</layerGeometryType>
</qgis>
