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
    <field configurationFlags="None" name="interflow_type">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option type="QString" name="0: No interflow" value="0"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="1: Porosity is rescaled per computational cell with respect to the deepest surface level in that cell. (Defining the porosity_layer_thickness is mandatory)" value="1"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="2: Porosity is rescaled per computational cell with respect to the deepest surface level in the 2D surface domain. (Defining the porosity_layer_thickness is mandatory)" value="2"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="3: The impervious layer thickness is uniform in the 2D surface domain and is based on the impervious_layer_elevation and the deepest surface level in that cell." value="3"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="4: The impervious layer thickness is non-uniform in the 2D surface domain and is based on the impervious_layer_elevation with respect to the deepest surface level in the 2D surface domain." value="4"/>
              </Option>
            </Option>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="porosity">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="porosity_file">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="porosity_layer_thickness">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="impervious_layer_elevation">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="hydraulic_conductivity">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="hydraulic_conductivity_file">
      <editWidget type="TextEdit">
        <config>
          <Option/>
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
    <alias field="interflow_type" name="" index="1"/>
    <alias field="porosity" name="" index="2"/>
    <alias field="porosity_file" name="" index="3"/>
    <alias field="porosity_layer_thickness" name="" index="4"/>
    <alias field="impervious_layer_elevation" name="" index="5"/>
    <alias field="hydraulic_conductivity" name="" index="6"/>
    <alias field="hydraulic_conductivity_file" name="" index="7"/>
    <alias field="display_name" name="" index="8"/>
  </aliases>
  <defaults>
    <default applyOnUpdate="0" field="id" expression="if(maximum(id) is null,1, maximum(id)+1)"/>
    <default applyOnUpdate="0" field="interflow_type" expression=""/>
    <default applyOnUpdate="0" field="porosity" expression=""/>
    <default applyOnUpdate="0" field="porosity_file" expression=""/>
    <default applyOnUpdate="0" field="porosity_layer_thickness" expression=""/>
    <default applyOnUpdate="0" field="impervious_layer_elevation" expression=""/>
    <default applyOnUpdate="0" field="hydraulic_conductivity" expression=""/>
    <default applyOnUpdate="0" field="hydraulic_conductivity_file" expression=""/>
    <default applyOnUpdate="0" field="display_name" expression=""/>
  </defaults>
  <constraints>
    <constraint unique_strength="1" constraints="3" field="id" exp_strength="0" notnull_strength="1"/>
    <constraint unique_strength="0" constraints="1" field="interflow_type" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="0" field="porosity" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="porosity_file" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="porosity_layer_thickness" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="impervious_layer_elevation" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="hydraulic_conductivity" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="hydraulic_conductivity_file" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="1" field="display_name" exp_strength="0" notnull_strength="2"/>
  </constraints>
  <constraintExpressions>
    <constraint field="id" exp="" desc=""/>
    <constraint field="interflow_type" exp="" desc=""/>
    <constraint field="porosity" exp="" desc=""/>
    <constraint field="porosity_file" exp="" desc=""/>
    <constraint field="porosity_layer_thickness" exp="" desc=""/>
    <constraint field="impervious_layer_elevation" exp="" desc=""/>
    <constraint field="hydraulic_conductivity" exp="" desc=""/>
    <constraint field="hydraulic_conductivity_file" exp="" desc=""/>
    <constraint field="display_name" exp="" desc=""/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction key="Canvas" value="{00000000-0000-0000-0000-000000000000}"/>
  </attributeactions>
  <attributetableconfig actionWidgetStyle="dropDown" sortExpression="" sortOrder="0">
    <columns>
      <column type="field" name="id" width="-1" hidden="0"/>
      <column type="field" name="interflow_type" width="-1" hidden="0"/>
      <column type="field" name="porosity" width="-1" hidden="0"/>
      <column type="field" name="porosity_file" width="-1" hidden="0"/>
      <column type="field" name="porosity_layer_thickness" width="-1" hidden="0"/>
      <column type="field" name="impervious_layer_elevation" width="-1" hidden="0"/>
      <column type="field" name="hydraulic_conductivity" width="-1" hidden="0"/>
      <column type="field" name="hydraulic_conductivity_file" width="-1" hidden="0"/>
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
      <attributeEditorField name="display_name" showLabel="1" index="8"/>
      <attributeEditorField name="interflow_type" showLabel="1" index="1"/>
    </attributeEditorContainer>
    <attributeEditorContainer columnCount="1" name="Porosity" groupBox="0" showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="">
      <attributeEditorField name="porosity" showLabel="1" index="2"/>
      <attributeEditorField name="porosity_file" showLabel="1" index="3"/>
      <attributeEditorField name="porosity_layer_thickness" showLabel="1" index="4"/>
    </attributeEditorContainer>
    <attributeEditorContainer columnCount="1" name="Hydraulic conductivity" groupBox="0" showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="">
      <attributeEditorField name="hydraulic_conductivity_file" showLabel="1" index="7"/>
      <attributeEditorField name="hydraulic_conductivity" showLabel="1" index="6"/>
    </attributeEditorContainer>
    <attributeEditorContainer columnCount="1" name="Impervious layer" groupBox="0" showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="">
      <attributeEditorField name="impervious_layer_elevation" showLabel="1" index="5"/>
    </attributeEditorContainer>
  </attributeEditorForm>
  <editable>
    <field editable="1" name="display_name"/>
    <field editable="1" name="hydraulic_conductivity"/>
    <field editable="1" name="hydraulic_conductivity_file"/>
    <field editable="1" name="id"/>
    <field editable="1" name="impervious_layer_elevation"/>
    <field editable="1" name="interflow_type"/>
    <field editable="1" name="porosity"/>
    <field editable="1" name="porosity_file"/>
    <field editable="1" name="porosity_layer_thickness"/>
  </editable>
  <labelOnTop>
    <field labelOnTop="0" name="display_name"/>
    <field labelOnTop="0" name="hydraulic_conductivity"/>
    <field labelOnTop="0" name="hydraulic_conductivity_file"/>
    <field labelOnTop="0" name="id"/>
    <field labelOnTop="0" name="impervious_layer_elevation"/>
    <field labelOnTop="0" name="interflow_type"/>
    <field labelOnTop="0" name="porosity"/>
    <field labelOnTop="0" name="porosity_file"/>
    <field labelOnTop="0" name="porosity_layer_thickness"/>
  </labelOnTop>
  <dataDefinedFieldProperties/>
  <widgets/>
  <previewExpression>id</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>4</layerGeometryType>
</qgis>
