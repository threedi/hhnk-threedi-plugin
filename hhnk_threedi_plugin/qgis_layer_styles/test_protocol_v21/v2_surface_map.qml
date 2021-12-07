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
    <field configurationFlags="None" name="surface_type">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option type="QString" name="v2_surface" value="v2_surface"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="v2_impervious_surface" value="v2_impervious_surface"/>
              </Option>
            </Option>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="surface_id">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="connection_node_id">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="percentage">
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
    <alias field="surface_type" name="" index="1"/>
    <alias field="surface_id" name="" index="2"/>
    <alias field="connection_node_id" name="" index="3"/>
    <alias field="percentage" name="" index="4"/>
  </aliases>
  <defaults>
    <default applyOnUpdate="0" field="id" expression="if(maximum(id) is null,1, maximum(id)+1)"/>
    <default applyOnUpdate="0" field="surface_type" expression=""/>
    <default applyOnUpdate="0" field="surface_id" expression=""/>
    <default applyOnUpdate="0" field="connection_node_id" expression=""/>
    <default applyOnUpdate="0" field="percentage" expression=""/>
  </defaults>
  <constraints>
    <constraint unique_strength="1" constraints="3" field="id" exp_strength="0" notnull_strength="1"/>
    <constraint unique_strength="0" constraints="1" field="surface_type" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="1" field="surface_id" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="1" field="connection_node_id" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="1" field="percentage" exp_strength="0" notnull_strength="2"/>
  </constraints>
  <constraintExpressions>
    <constraint field="id" exp="" desc=""/>
    <constraint field="surface_type" exp="" desc=""/>
    <constraint field="surface_id" exp="" desc=""/>
    <constraint field="connection_node_id" exp="" desc=""/>
    <constraint field="percentage" exp="" desc=""/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction key="Canvas" value="{00000000-0000-0000-0000-000000000000}"/>
  </attributeactions>
  <attributetableconfig actionWidgetStyle="dropDown" sortExpression="" sortOrder="0">
    <columns>
      <column type="field" name="id" width="-1" hidden="0"/>
      <column type="field" name="surface_type" width="-1" hidden="0"/>
      <column type="field" name="surface_id" width="-1" hidden="0"/>
      <column type="field" name="connection_node_id" width="-1" hidden="0"/>
      <column type="field" name="percentage" width="-1" hidden="0"/>
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
      <attributeEditorField name="surface_type" showLabel="1" index="1"/>
      <attributeEditorField name="surface_id" showLabel="1" index="2"/>
      <attributeEditorField name="connection_node_id" showLabel="1" index="3"/>
      <attributeEditorField name="percentage" showLabel="1" index="4"/>
    </attributeEditorContainer>
  </attributeEditorForm>
  <editable>
    <field editable="1" name="connection_node_id"/>
    <field editable="1" name="id"/>
    <field editable="1" name="percentage"/>
    <field editable="1" name="surface_id"/>
    <field editable="1" name="surface_type"/>
  </editable>
  <labelOnTop>
    <field labelOnTop="0" name="connection_node_id"/>
    <field labelOnTop="0" name="id"/>
    <field labelOnTop="0" name="percentage"/>
    <field labelOnTop="0" name="surface_id"/>
    <field labelOnTop="0" name="surface_type"/>
  </labelOnTop>
  <dataDefinedFieldProperties/>
  <widgets/>
  <previewExpression>id</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>4</layerGeometryType>
</qgis>
