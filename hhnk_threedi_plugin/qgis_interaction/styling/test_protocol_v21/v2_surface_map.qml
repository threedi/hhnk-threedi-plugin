<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis readOnly="0" styleCategories="AllStyleCategories" hasScaleBasedVisibilityFlag="0" minScale="1e+08" version="3.16.11-Hannover" maxScale="0">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <temporal fixedDuration="0" enabled="0" endField="" durationField="" accumulate="0" startField="" durationUnit="min" startExpression="" mode="0" endExpression="">
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
  <geometryOptions removeDuplicateNodes="0" geometryPrecision="0">
    <activeChecks/>
    <checkConfiguration/>
  </geometryOptions>
  <legend type="default-vector"/>
  <referencedLayers/>
  <fieldConfiguration>
    <field name="id" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="surface_type" configurationFlags="None">
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
    <field name="surface_id" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="connection_node_id" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="percentage" configurationFlags="None">
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
    <alias name="" index="0" field="id"/>
    <alias name="" index="1" field="surface_type"/>
    <alias name="" index="2" field="surface_id"/>
    <alias name="" index="3" field="connection_node_id"/>
    <alias name="" index="4" field="percentage"/>
  </aliases>
  <defaults>
    <default expression="if(maximum(id) is null,1, maximum(id)+1)" applyOnUpdate="0" field="id"/>
    <default expression="" applyOnUpdate="0" field="surface_type"/>
    <default expression="" applyOnUpdate="0" field="surface_id"/>
    <default expression="" applyOnUpdate="0" field="connection_node_id"/>
    <default expression="" applyOnUpdate="0" field="percentage"/>
  </defaults>
  <constraints>
    <constraint unique_strength="1" exp_strength="0" notnull_strength="1" constraints="3" field="id"/>
    <constraint unique_strength="0" exp_strength="0" notnull_strength="2" constraints="1" field="surface_type"/>
    <constraint unique_strength="0" exp_strength="0" notnull_strength="2" constraints="1" field="surface_id"/>
    <constraint unique_strength="0" exp_strength="0" notnull_strength="2" constraints="1" field="connection_node_id"/>
    <constraint unique_strength="0" exp_strength="0" notnull_strength="2" constraints="1" field="percentage"/>
  </constraints>
  <constraintExpressions>
    <constraint desc="" exp="" field="id"/>
    <constraint desc="" exp="" field="surface_type"/>
    <constraint desc="" exp="" field="surface_id"/>
    <constraint desc="" exp="" field="connection_node_id"/>
    <constraint desc="" exp="" field="percentage"/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction key="Canvas" value="{00000000-0000-0000-0000-000000000000}"/>
  </attributeactions>
  <attributetableconfig actionWidgetStyle="dropDown" sortExpression="" sortOrder="0">
    <columns>
      <column width="-1" type="field" name="id" hidden="0"/>
      <column width="-1" type="field" name="surface_type" hidden="0"/>
      <column width="-1" type="field" name="surface_id" hidden="0"/>
      <column width="-1" type="field" name="connection_node_id" hidden="0"/>
      <column width="-1" type="field" name="percentage" hidden="0"/>
      <column width="-1" type="actions" hidden="1"/>
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
    <attributeEditorContainer columnCount="1" visibilityExpressionEnabled="0" name="General" visibilityExpression="" groupBox="0" showLabel="1">
      <attributeEditorField name="id" showLabel="1" index="0"/>
      <attributeEditorField name="surface_type" showLabel="1" index="1"/>
      <attributeEditorField name="surface_id" showLabel="1" index="2"/>
      <attributeEditorField name="connection_node_id" showLabel="1" index="3"/>
      <attributeEditorField name="percentage" showLabel="1" index="4"/>
    </attributeEditorContainer>
  </attributeEditorForm>
  <editable>
    <field name="connection_node_id" editable="1"/>
    <field name="id" editable="1"/>
    <field name="percentage" editable="1"/>
    <field name="surface_id" editable="1"/>
    <field name="surface_type" editable="1"/>
  </editable>
  <labelOnTop>
    <field name="connection_node_id" labelOnTop="0"/>
    <field name="id" labelOnTop="0"/>
    <field name="percentage" labelOnTop="0"/>
    <field name="surface_id" labelOnTop="0"/>
    <field name="surface_type" labelOnTop="0"/>
  </labelOnTop>
  <dataDefinedFieldProperties/>
  <widgets/>
  <previewExpression>id</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>4</layerGeometryType>
</qgis>
