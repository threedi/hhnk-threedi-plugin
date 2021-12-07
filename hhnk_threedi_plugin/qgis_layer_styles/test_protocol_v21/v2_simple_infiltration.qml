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
    <property key="dualview/previewExpressions" value="id"/>
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
    <field configurationFlags="None" name="infiltration_rate">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="infiltration_rate_file">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="infiltration_surface_option">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="max_infiltration_capacity_file">
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
  </fieldConfiguration>
  <aliases>
    <alias field="id" name="" index="0"/>
    <alias field="infiltration_rate" name="" index="1"/>
    <alias field="infiltration_rate_file" name="" index="2"/>
    <alias field="infiltration_surface_option" name="" index="3"/>
    <alias field="max_infiltration_capacity_file" name="" index="4"/>
    <alias field="display_name" name="" index="5"/>
  </aliases>
  <defaults>
    <default applyOnUpdate="0" field="id" expression="if(maximum(id) is null,1,maximum(id)+1)"/>
    <default applyOnUpdate="0" field="infiltration_rate" expression=""/>
    <default applyOnUpdate="0" field="infiltration_rate_file" expression=""/>
    <default applyOnUpdate="0" field="infiltration_surface_option" expression="0"/>
    <default applyOnUpdate="0" field="max_infiltration_capacity_file" expression=""/>
    <default applyOnUpdate="0" field="display_name" expression="'new'"/>
  </defaults>
  <constraints>
    <constraint unique_strength="1" constraints="3" field="id" exp_strength="0" notnull_strength="1"/>
    <constraint unique_strength="0" constraints="1" field="infiltration_rate" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="0" field="infiltration_rate_file" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="infiltration_surface_option" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="max_infiltration_capacity_file" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="1" field="display_name" exp_strength="0" notnull_strength="2"/>
  </constraints>
  <constraintExpressions>
    <constraint field="id" exp="" desc=""/>
    <constraint field="infiltration_rate" exp="" desc=""/>
    <constraint field="infiltration_rate_file" exp="" desc=""/>
    <constraint field="infiltration_surface_option" exp="" desc=""/>
    <constraint field="max_infiltration_capacity_file" exp="" desc=""/>
    <constraint field="display_name" exp="" desc=""/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction key="Canvas" value="{00000000-0000-0000-0000-000000000000}"/>
  </attributeactions>
  <attributetableconfig actionWidgetStyle="dropDown" sortExpression="" sortOrder="0">
    <columns>
      <column type="field" name="id" width="-1" hidden="0"/>
      <column type="field" name="infiltration_rate" width="-1" hidden="0"/>
      <column type="field" name="infiltration_rate_file" width="-1" hidden="0"/>
      <column type="field" name="infiltration_surface_option" width="-1" hidden="0"/>
      <column type="field" name="max_infiltration_capacity_file" width="-1" hidden="0"/>
      <column type="field" name="display_name" width="-1" hidden="0"/>
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
      <attributeEditorField name="display_name" showLabel="1" index="5"/>
      <attributeEditorField name="infiltration_rate" showLabel="1" index="1"/>
      <attributeEditorField name="infiltration_rate_file" showLabel="1" index="2"/>
      <attributeEditorField name="max_infiltration_capacity_file" showLabel="1" index="4"/>
      <attributeEditorField name="infiltration_surface_option" showLabel="1" index="3"/>
    </attributeEditorContainer>
  </attributeEditorForm>
  <editable>
    <field editable="1" name="display_name"/>
    <field editable="1" name="id"/>
    <field editable="1" name="infiltration_rate"/>
    <field editable="1" name="infiltration_rate_file"/>
    <field editable="1" name="infiltration_surface_option"/>
    <field editable="1" name="max_infiltration_capacity_file"/>
  </editable>
  <labelOnTop>
    <field labelOnTop="0" name="display_name"/>
    <field labelOnTop="0" name="id"/>
    <field labelOnTop="0" name="infiltration_rate"/>
    <field labelOnTop="0" name="infiltration_rate_file"/>
    <field labelOnTop="0" name="infiltration_surface_option"/>
    <field labelOnTop="0" name="max_infiltration_capacity_file"/>
  </labelOnTop>
  <dataDefinedFieldProperties/>
  <widgets/>
  <previewExpression>id</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>4</layerGeometryType>
</qgis>
