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
    <property key="dualview/previewExpressions" value="width"/>
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
    <field configurationFlags="None" name="shape">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option type="QString" name="1: rectangle" value="1"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="2: round" value="2"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="3: egg" value="3"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="5: tabulated rectangle" value="5"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="6: tabulated trapezium" value="6"/>
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
    <field configurationFlags="None" name="height">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
  </fieldConfiguration>
  <aliases>
    <alias field="width" name="" index="0"/>
    <alias field="shape" name="" index="1"/>
    <alias field="code" name="" index="2"/>
    <alias field="id" name="" index="3"/>
    <alias field="height" name="" index="4"/>
  </aliases>
  <defaults>
    <default applyOnUpdate="0" field="width" expression=""/>
    <default applyOnUpdate="0" field="shape" expression=""/>
    <default applyOnUpdate="0" field="code" expression="'new'"/>
    <default applyOnUpdate="0" field="id" expression="if(maximum(id) is null,1, maximum(id)+1)"/>
    <default applyOnUpdate="0" field="height" expression=""/>
  </defaults>
  <constraints>
    <constraint unique_strength="0" constraints="5" field="width" exp_strength="2" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="1" field="shape" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="1" field="code" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="1" constraints="3" field="id" exp_strength="0" notnull_strength="1"/>
    <constraint unique_strength="0" constraints="4" field="height" exp_strength="2" notnull_strength="0"/>
  </constraints>
  <constraintExpressions>
    <constraint field="width" exp="regexp_match(&quot;width&quot;,'^(-?\\d+(\\.\\d+)?)(\\s-?\\d+(\\.\\d+)?)*$')" desc=""/>
    <constraint field="shape" exp="" desc=""/>
    <constraint field="code" exp="" desc=""/>
    <constraint field="id" exp="" desc=""/>
    <constraint field="height" exp="regexp_match(&quot;height&quot;,'^(-?\\d+(\\.\\d+)?)(\\s-?\\d+(\\.\\d+)?)*$') or &quot;height&quot;is null" desc=""/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction key="Canvas" value="{00000000-0000-0000-0000-000000000000}"/>
  </attributeactions>
  <attributetableconfig actionWidgetStyle="dropDown" sortExpression="" sortOrder="0">
    <columns>
      <column type="field" name="width" width="-1" hidden="0"/>
      <column type="field" name="shape" width="-1" hidden="0"/>
      <column type="field" name="code" width="-1" hidden="0"/>
      <column type="field" name="id" width="-1" hidden="0"/>
      <column type="field" name="height" width="-1" hidden="0"/>
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
      <attributeEditorField name="id" showLabel="1" index="3"/>
      <attributeEditorField name="code" showLabel="1" index="2"/>
      <attributeEditorField name="shape" showLabel="1" index="1"/>
      <attributeEditorField name="width" showLabel="1" index="0"/>
      <attributeEditorField name="height" showLabel="1" index="4"/>
    </attributeEditorContainer>
  </attributeEditorForm>
  <editable>
    <field editable="1" name="code"/>
    <field editable="1" name="height"/>
    <field editable="1" name="id"/>
    <field editable="1" name="shape"/>
    <field editable="1" name="width"/>
  </editable>
  <labelOnTop>
    <field labelOnTop="0" name="code"/>
    <field labelOnTop="0" name="height"/>
    <field labelOnTop="0" name="id"/>
    <field labelOnTop="0" name="shape"/>
    <field labelOnTop="0" name="width"/>
  </labelOnTop>
  <dataDefinedFieldProperties/>
  <widgets/>
  <previewExpression>width</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>4</layerGeometryType>
</qgis>
