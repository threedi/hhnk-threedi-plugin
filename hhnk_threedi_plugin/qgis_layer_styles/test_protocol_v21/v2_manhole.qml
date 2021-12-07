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
    <field configurationFlags="None" name="shape">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option type="QString" name="00: square" value="00"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="01: round" value="01"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="02: rectangle" value="02"/>
              </Option>
            </Option>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="width">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="length">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="manhole_indicator">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option type="QString" name="0: inspection" value="0"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="1: outlet" value="1"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="2: pumpstation" value="2"/>
              </Option>
            </Option>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="calculation_type">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option type="QString" name="0: embedded" value="0"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="1: isolated" value="1"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="2: connected" value="2"/>
              </Option>
            </Option>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="bottom_level">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="surface_level">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="drain_level">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="sediment_level">
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
  </fieldConfiguration>
  <aliases>
    <alias field="id" name="" index="0"/>
    <alias field="display_name" name="" index="1"/>
    <alias field="code" name="" index="2"/>
    <alias field="connection_node_id" name="" index="3"/>
    <alias field="shape" name="" index="4"/>
    <alias field="width" name="" index="5"/>
    <alias field="length" name="" index="6"/>
    <alias field="manhole_indicator" name="" index="7"/>
    <alias field="calculation_type" name="" index="8"/>
    <alias field="bottom_level" name="" index="9"/>
    <alias field="surface_level" name="" index="10"/>
    <alias field="drain_level" name="" index="11"/>
    <alias field="sediment_level" name="" index="12"/>
    <alias field="zoom_category" name="" index="13"/>
  </aliases>
  <defaults>
    <default applyOnUpdate="0" field="id" expression="if(maximum(id) is null,1, maximum(id)+1)"/>
    <default applyOnUpdate="0" field="display_name" expression="'new'"/>
    <default applyOnUpdate="0" field="code" expression="'new'"/>
    <default applyOnUpdate="0" field="connection_node_id" expression=""/>
    <default applyOnUpdate="0" field="shape" expression=""/>
    <default applyOnUpdate="0" field="width" expression=""/>
    <default applyOnUpdate="0" field="length" expression=""/>
    <default applyOnUpdate="0" field="manhole_indicator" expression="0"/>
    <default applyOnUpdate="0" field="calculation_type" expression=""/>
    <default applyOnUpdate="0" field="bottom_level" expression=""/>
    <default applyOnUpdate="0" field="surface_level" expression=""/>
    <default applyOnUpdate="0" field="drain_level" expression=""/>
    <default applyOnUpdate="0" field="sediment_level" expression=""/>
    <default applyOnUpdate="0" field="zoom_category" expression="1"/>
  </defaults>
  <constraints>
    <constraint unique_strength="1" constraints="3" field="id" exp_strength="0" notnull_strength="1"/>
    <constraint unique_strength="0" constraints="1" field="display_name" exp_strength="0" notnull_strength="1"/>
    <constraint unique_strength="0" constraints="1" field="code" exp_strength="0" notnull_strength="1"/>
    <constraint unique_strength="1" constraints="3" field="connection_node_id" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="0" field="shape" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="width" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="length" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="1" field="manhole_indicator" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="1" field="calculation_type" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="1" field="bottom_level" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="1" field="surface_level" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="0" field="drain_level" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="sediment_level" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="zoom_category" exp_strength="0" notnull_strength="0"/>
  </constraints>
  <constraintExpressions>
    <constraint field="id" exp="" desc=""/>
    <constraint field="display_name" exp="" desc=""/>
    <constraint field="code" exp="" desc=""/>
    <constraint field="connection_node_id" exp="" desc=""/>
    <constraint field="shape" exp="" desc=""/>
    <constraint field="width" exp="" desc=""/>
    <constraint field="length" exp="" desc=""/>
    <constraint field="manhole_indicator" exp="" desc=""/>
    <constraint field="calculation_type" exp="" desc=""/>
    <constraint field="bottom_level" exp="" desc=""/>
    <constraint field="surface_level" exp="" desc=""/>
    <constraint field="drain_level" exp="" desc=""/>
    <constraint field="sediment_level" exp="" desc=""/>
    <constraint field="zoom_category" exp="" desc=""/>
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
      <column type="field" name="connection_node_id" width="-1" hidden="0"/>
      <column type="field" name="shape" width="-1" hidden="0"/>
      <column type="field" name="width" width="-1" hidden="0"/>
      <column type="field" name="length" width="-1" hidden="0"/>
      <column type="field" name="manhole_indicator" width="-1" hidden="0"/>
      <column type="field" name="calculation_type" width="-1" hidden="0"/>
      <column type="field" name="bottom_level" width="-1" hidden="0"/>
      <column type="field" name="surface_level" width="-1" hidden="0"/>
      <column type="field" name="drain_level" width="-1" hidden="0"/>
      <column type="field" name="sediment_level" width="-1" hidden="0"/>
      <column type="field" name="zoom_category" width="-1" hidden="0"/>
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
    <attributeEditorContainer columnCount="1" name="Manhole" groupBox="0" showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="">
      <attributeEditorContainer columnCount="1" name="General" groupBox="1" showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="">
        <attributeEditorField name="id" showLabel="1" index="0"/>
        <attributeEditorField name="display_name" showLabel="1" index="1"/>
        <attributeEditorField name="code" showLabel="1" index="2"/>
        <attributeEditorField name="connection_node_id" showLabel="1" index="3"/>
        <attributeEditorField name="calculation_type" showLabel="1" index="8"/>
      </attributeEditorContainer>
      <attributeEditorContainer columnCount="1" name="Characteristics" groupBox="1" showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="">
        <attributeEditorField name="shape" showLabel="1" index="4"/>
        <attributeEditorField name="width" showLabel="1" index="5"/>
        <attributeEditorField name="length" showLabel="1" index="6"/>
        <attributeEditorField name="surface_level" showLabel="1" index="10"/>
        <attributeEditorField name="drain_level" showLabel="1" index="11"/>
        <attributeEditorField name="bottom_level" showLabel="1" index="9"/>
      </attributeEditorContainer>
      <attributeEditorContainer columnCount="1" name="Visualization" groupBox="1" showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="">
        <attributeEditorField name="zoom_category" showLabel="1" index="13"/>
        <attributeEditorField name="manhole_indicator" showLabel="1" index="7"/>
      </attributeEditorContainer>
    </attributeEditorContainer>
  </attributeEditorForm>
  <editable>
    <field editable="1" name="bottom_level"/>
    <field editable="1" name="calculation_type"/>
    <field editable="1" name="code"/>
    <field editable="1" name="connection_node_id"/>
    <field editable="1" name="display_name"/>
    <field editable="1" name="drain_level"/>
    <field editable="1" name="id"/>
    <field editable="1" name="length"/>
    <field editable="1" name="manhole_indicator"/>
    <field editable="1" name="sediment_level"/>
    <field editable="1" name="shape"/>
    <field editable="1" name="surface_level"/>
    <field editable="1" name="width"/>
    <field editable="1" name="zoom_category"/>
  </editable>
  <labelOnTop>
    <field labelOnTop="0" name="bottom_level"/>
    <field labelOnTop="0" name="calculation_type"/>
    <field labelOnTop="0" name="code"/>
    <field labelOnTop="0" name="connection_node_id"/>
    <field labelOnTop="0" name="display_name"/>
    <field labelOnTop="0" name="drain_level"/>
    <field labelOnTop="0" name="id"/>
    <field labelOnTop="0" name="length"/>
    <field labelOnTop="0" name="manhole_indicator"/>
    <field labelOnTop="0" name="sediment_level"/>
    <field labelOnTop="0" name="shape"/>
    <field labelOnTop="0" name="surface_level"/>
    <field labelOnTop="0" name="width"/>
    <field labelOnTop="0" name="zoom_category"/>
  </labelOnTop>
  <dataDefinedFieldProperties/>
  <widgets/>
  <previewExpression>id</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>4</layerGeometryType>
</qgis>
