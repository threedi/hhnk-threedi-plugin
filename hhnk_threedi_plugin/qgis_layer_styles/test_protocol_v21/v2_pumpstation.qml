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
    <property key="dualview/previewExpressions" value="display_name"/>
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
    <field configurationFlags="None" name="upper_stop_level">
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
    <field configurationFlags="None" name="connection_node_end_id">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="classification">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="sewerage">
      <editWidget type="CheckBox">
        <config>
          <Option type="Map">
            <Option type="QString" name="CheckedState" value="1"/>
            <Option type="QString" name="UncheckedState" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="lower_stop_level">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="connection_node_start_id">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="start_level">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="capacity">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="type">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option type="QString" name="1: Pump behaviour is based on water levels on the suction-side of the pump" value="1"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="2: Pump behaviour is based on water levels on the delivery-side of the pump" value="2"/>
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
    <alias field="upper_stop_level" name="" index="0"/>
    <alias field="zoom_category" name="" index="1"/>
    <alias field="code" name="" index="2"/>
    <alias field="display_name" name="" index="3"/>
    <alias field="connection_node_end_id" name="" index="4"/>
    <alias field="classification" name="" index="5"/>
    <alias field="sewerage" name="" index="6"/>
    <alias field="lower_stop_level" name="" index="7"/>
    <alias field="connection_node_start_id" name="" index="8"/>
    <alias field="start_level" name="" index="9"/>
    <alias field="capacity" name="" index="10"/>
    <alias field="type" name="" index="11"/>
    <alias field="id" name="" index="12"/>
  </aliases>
  <defaults>
    <default applyOnUpdate="0" field="upper_stop_level" expression=""/>
    <default applyOnUpdate="0" field="zoom_category" expression="3"/>
    <default applyOnUpdate="0" field="code" expression="'new'"/>
    <default applyOnUpdate="0" field="display_name" expression="'new'"/>
    <default applyOnUpdate="0" field="connection_node_end_id" expression=""/>
    <default applyOnUpdate="0" field="classification" expression=""/>
    <default applyOnUpdate="0" field="sewerage" expression=""/>
    <default applyOnUpdate="0" field="lower_stop_level" expression=""/>
    <default applyOnUpdate="0" field="connection_node_start_id" expression=""/>
    <default applyOnUpdate="0" field="start_level" expression=""/>
    <default applyOnUpdate="0" field="capacity" expression=""/>
    <default applyOnUpdate="0" field="type" expression="1"/>
    <default applyOnUpdate="0" field="id" expression="if(maximum(id) is null,1, maximum(id)+1)"/>
  </defaults>
  <constraints>
    <constraint unique_strength="0" constraints="4" field="upper_stop_level" exp_strength="2" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="1" field="zoom_category" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="1" field="code" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="1" field="display_name" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="1" field="connection_node_end_id" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="0" field="classification" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="1" field="sewerage" exp_strength="0" notnull_strength="1"/>
    <constraint unique_strength="0" constraints="5" field="lower_stop_level" exp_strength="2" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="1" field="connection_node_start_id" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="1" field="start_level" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="5" field="capacity" exp_strength="2" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="1" field="type" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="1" constraints="3" field="id" exp_strength="0" notnull_strength="1"/>
  </constraints>
  <constraintExpressions>
    <constraint field="upper_stop_level" exp="&quot;upper_stop_level&quot;>&quot;start_level&quot; or &quot;upper_stop_level&quot; is null" desc=""/>
    <constraint field="zoom_category" exp="" desc=""/>
    <constraint field="code" exp="" desc=""/>
    <constraint field="display_name" exp="" desc=""/>
    <constraint field="connection_node_end_id" exp="" desc=""/>
    <constraint field="classification" exp="" desc=""/>
    <constraint field="sewerage" exp="" desc=""/>
    <constraint field="lower_stop_level" exp="&quot;lower_stop_level&quot;&lt;&quot;start_level&quot;" desc=""/>
    <constraint field="connection_node_start_id" exp="" desc=""/>
    <constraint field="start_level" exp="" desc=""/>
    <constraint field="capacity" exp="&quot;capacity&quot;>=0" desc=""/>
    <constraint field="type" exp="" desc=""/>
    <constraint field="id" exp="" desc=""/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction key="Canvas" value="{00000000-0000-0000-0000-000000000000}"/>
  </attributeactions>
  <attributetableconfig actionWidgetStyle="dropDown" sortExpression="" sortOrder="0">
    <columns>
      <column type="field" name="upper_stop_level" width="-1" hidden="0"/>
      <column type="field" name="zoom_category" width="-1" hidden="0"/>
      <column type="field" name="code" width="-1" hidden="0"/>
      <column type="field" name="display_name" width="-1" hidden="0"/>
      <column type="field" name="connection_node_end_id" width="-1" hidden="0"/>
      <column type="field" name="classification" width="-1" hidden="0"/>
      <column type="field" name="sewerage" width="-1" hidden="0"/>
      <column type="field" name="lower_stop_level" width="-1" hidden="0"/>
      <column type="field" name="connection_node_start_id" width="-1" hidden="0"/>
      <column type="field" name="start_level" width="-1" hidden="0"/>
      <column type="field" name="capacity" width="-1" hidden="0"/>
      <column type="field" name="type" width="-1" hidden="0"/>
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
    <attributeEditorContainer columnCount="1" name="Pumpstation" groupBox="0" showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="">
      <attributeEditorContainer columnCount="1" name="General" groupBox="1" showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="">
        <attributeEditorField name="id" showLabel="1" index="12"/>
        <attributeEditorField name="display_name" showLabel="1" index="3"/>
        <attributeEditorField name="code" showLabel="1" index="2"/>
      </attributeEditorContainer>
      <attributeEditorContainer columnCount="1" name="Characteristics" groupBox="1" showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="">
        <attributeEditorField name="capacity" showLabel="1" index="10"/>
        <attributeEditorField name="start_level" showLabel="1" index="9"/>
        <attributeEditorField name="lower_stop_level" showLabel="1" index="7"/>
        <attributeEditorField name="upper_stop_level" showLabel="1" index="0"/>
        <attributeEditorField name="type" showLabel="1" index="11"/>
      </attributeEditorContainer>
      <attributeEditorContainer columnCount="1" name="Visualization" groupBox="1" showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="">
        <attributeEditorField name="zoom_category" showLabel="1" index="1"/>
        <attributeEditorField name="sewerage" showLabel="1" index="6"/>
      </attributeEditorContainer>
      <attributeEditorContainer columnCount="1" name="Connection nodes" groupBox="1" showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="">
        <attributeEditorField name="connection_node_start_id" showLabel="1" index="8"/>
        <attributeEditorField name="connection_node_end_id" showLabel="1" index="4"/>
      </attributeEditorContainer>
    </attributeEditorContainer>
  </attributeEditorForm>
  <editable>
    <field editable="1" name="capacity"/>
    <field editable="1" name="classification"/>
    <field editable="1" name="code"/>
    <field editable="1" name="connection_node_end_id"/>
    <field editable="1" name="connection_node_start_id"/>
    <field editable="1" name="display_name"/>
    <field editable="1" name="id"/>
    <field editable="1" name="lower_stop_level"/>
    <field editable="1" name="sewerage"/>
    <field editable="1" name="start_level"/>
    <field editable="1" name="type"/>
    <field editable="1" name="upper_stop_level"/>
    <field editable="1" name="zoom_category"/>
  </editable>
  <labelOnTop>
    <field labelOnTop="0" name="capacity"/>
    <field labelOnTop="0" name="classification"/>
    <field labelOnTop="0" name="code"/>
    <field labelOnTop="0" name="connection_node_end_id"/>
    <field labelOnTop="0" name="connection_node_start_id"/>
    <field labelOnTop="0" name="display_name"/>
    <field labelOnTop="0" name="id"/>
    <field labelOnTop="0" name="lower_stop_level"/>
    <field labelOnTop="0" name="sewerage"/>
    <field labelOnTop="0" name="start_level"/>
    <field labelOnTop="0" name="type"/>
    <field labelOnTop="0" name="upper_stop_level"/>
    <field labelOnTop="0" name="zoom_category"/>
  </labelOnTop>
  <dataDefinedFieldProperties/>
  <widgets/>
  <previewExpression>display_name</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>4</layerGeometryType>
</qgis>
