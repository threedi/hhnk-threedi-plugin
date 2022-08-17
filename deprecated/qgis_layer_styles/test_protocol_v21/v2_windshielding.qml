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
    <field configurationFlags="None" name="channel_id">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="north">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="northeast">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="east">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="southeast">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="south">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="southwest">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="west">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="northwest">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="the_geom">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
  </fieldConfiguration>
  <aliases>
    <alias field="id" name="" index="0"/>
    <alias field="channel_id" name="" index="1"/>
    <alias field="north" name="" index="2"/>
    <alias field="northeast" name="" index="3"/>
    <alias field="east" name="" index="4"/>
    <alias field="southeast" name="" index="5"/>
    <alias field="south" name="" index="6"/>
    <alias field="southwest" name="" index="7"/>
    <alias field="west" name="" index="8"/>
    <alias field="northwest" name="" index="9"/>
    <alias field="the_geom" name="" index="10"/>
  </aliases>
  <defaults>
    <default applyOnUpdate="0" field="id" expression="if(maximum(id) is null,1, maximum(id)+1)"/>
    <default applyOnUpdate="0" field="channel_id" expression=""/>
    <default applyOnUpdate="0" field="north" expression=""/>
    <default applyOnUpdate="0" field="northeast" expression=""/>
    <default applyOnUpdate="0" field="east" expression=""/>
    <default applyOnUpdate="0" field="southeast" expression=""/>
    <default applyOnUpdate="0" field="south" expression=""/>
    <default applyOnUpdate="0" field="southwest" expression=""/>
    <default applyOnUpdate="0" field="west" expression=""/>
    <default applyOnUpdate="0" field="northwest" expression=""/>
    <default applyOnUpdate="0" field="the_geom" expression=""/>
  </defaults>
  <constraints>
    <constraint unique_strength="1" constraints="3" field="id" exp_strength="0" notnull_strength="1"/>
    <constraint unique_strength="0" constraints="0" field="channel_id" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="north" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="northeast" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="east" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="southeast" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="south" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="southwest" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="west" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="northwest" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="the_geom" exp_strength="0" notnull_strength="0"/>
  </constraints>
  <constraintExpressions>
    <constraint field="id" exp="" desc=""/>
    <constraint field="channel_id" exp="" desc=""/>
    <constraint field="north" exp="" desc=""/>
    <constraint field="northeast" exp="" desc=""/>
    <constraint field="east" exp="" desc=""/>
    <constraint field="southeast" exp="" desc=""/>
    <constraint field="south" exp="" desc=""/>
    <constraint field="southwest" exp="" desc=""/>
    <constraint field="west" exp="" desc=""/>
    <constraint field="northwest" exp="" desc=""/>
    <constraint field="the_geom" exp="" desc=""/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction key="Canvas" value="{00000000-0000-0000-0000-000000000000}"/>
  </attributeactions>
  <attributetableconfig actionWidgetStyle="dropDown" sortExpression="" sortOrder="0">
    <columns>
      <column type="field" name="id" width="-1" hidden="0"/>
      <column type="field" name="channel_id" width="-1" hidden="0"/>
      <column type="field" name="north" width="-1" hidden="0"/>
      <column type="field" name="northeast" width="-1" hidden="0"/>
      <column type="field" name="east" width="-1" hidden="0"/>
      <column type="field" name="southeast" width="-1" hidden="0"/>
      <column type="field" name="south" width="-1" hidden="0"/>
      <column type="field" name="southwest" width="-1" hidden="0"/>
      <column type="field" name="west" width="-1" hidden="0"/>
      <column type="field" name="northwest" width="-1" hidden="0"/>
      <column type="field" name="the_geom" width="-1" hidden="0"/>
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
      <attributeEditorField name="channel_id" showLabel="1" index="1"/>
      <attributeEditorField name="north" showLabel="1" index="2"/>
      <attributeEditorField name="northeast" showLabel="1" index="3"/>
      <attributeEditorField name="east" showLabel="1" index="4"/>
      <attributeEditorField name="southeast" showLabel="1" index="5"/>
      <attributeEditorField name="south" showLabel="1" index="6"/>
      <attributeEditorField name="southwest" showLabel="1" index="7"/>
      <attributeEditorField name="west" showLabel="1" index="8"/>
      <attributeEditorField name="northwest" showLabel="1" index="9"/>
      <attributeEditorField name="the_geom" showLabel="1" index="10"/>
    </attributeEditorContainer>
  </attributeEditorForm>
  <editable>
    <field editable="1" name="channel_id"/>
    <field editable="1" name="east"/>
    <field editable="1" name="id"/>
    <field editable="1" name="north"/>
    <field editable="1" name="northeast"/>
    <field editable="1" name="northwest"/>
    <field editable="1" name="south"/>
    <field editable="1" name="southeast"/>
    <field editable="1" name="southwest"/>
    <field editable="1" name="the_geom"/>
    <field editable="1" name="west"/>
  </editable>
  <labelOnTop>
    <field labelOnTop="0" name="channel_id"/>
    <field labelOnTop="0" name="east"/>
    <field labelOnTop="0" name="id"/>
    <field labelOnTop="0" name="north"/>
    <field labelOnTop="0" name="northeast"/>
    <field labelOnTop="0" name="northwest"/>
    <field labelOnTop="0" name="south"/>
    <field labelOnTop="0" name="southeast"/>
    <field labelOnTop="0" name="southwest"/>
    <field labelOnTop="0" name="the_geom"/>
    <field labelOnTop="0" name="west"/>
  </labelOnTop>
  <dataDefinedFieldProperties/>
  <widgets/>
  <previewExpression>id</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>4</layerGeometryType>
</qgis>
