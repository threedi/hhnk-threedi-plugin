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
    <field configurationFlags="None" name="cfl_strictness_factor_1d">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="cfl_strictness_factor_2d">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="convergence_cg">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="convergence_eps">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="flow_direction_threshold">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="frict_shallow_water_correction">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="general_numerical_threshold">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="integration_method">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="limiter_grad_1d">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="limiter_grad_2d">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="limiter_slope_crossectional_area_2d">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="limiter_slope_friction_2d">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="max_nonlin_iterations">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="max_degree">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option type="QString" name="5: for surface 2D flow only" value="5"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="7: for 1D and 2D flow" value="7"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="70: for surface 1D, 2D surface and groundwater flow or higher" value="70"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="700: for 1D flow" value="700"/>
              </Option>
            </Option>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="minimum_friction_velocity">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="minimum_surface_area">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="precon_cg">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="preissmann_slot">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="pump_implicit_ratio">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="thin_water_layer_definition">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="use_of_cg">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="use_of_nested_newton">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option type="QString" name="0: When the schematisation does not include 1D-elements with closed-profiles" value="0"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="1: When the schematisation  includes 1D-elements with closed-profiles" value="1"/>
              </Option>
            </Option>
          </Option>
        </config>
      </editWidget>
    </field>
  </fieldConfiguration>
  <aliases>
    <alias field="id" name="" index="0"/>
    <alias field="cfl_strictness_factor_1d" name="" index="1"/>
    <alias field="cfl_strictness_factor_2d" name="" index="2"/>
    <alias field="convergence_cg" name="" index="3"/>
    <alias field="convergence_eps" name="" index="4"/>
    <alias field="flow_direction_threshold" name="" index="5"/>
    <alias field="frict_shallow_water_correction" name="" index="6"/>
    <alias field="general_numerical_threshold" name="" index="7"/>
    <alias field="integration_method" name="" index="8"/>
    <alias field="limiter_grad_1d" name="" index="9"/>
    <alias field="limiter_grad_2d" name="" index="10"/>
    <alias field="limiter_slope_crossectional_area_2d" name="" index="11"/>
    <alias field="limiter_slope_friction_2d" name="" index="12"/>
    <alias field="max_nonlin_iterations" name="" index="13"/>
    <alias field="max_degree" name="" index="14"/>
    <alias field="minimum_friction_velocity" name="" index="15"/>
    <alias field="minimum_surface_area" name="" index="16"/>
    <alias field="precon_cg" name="" index="17"/>
    <alias field="preissmann_slot" name="" index="18"/>
    <alias field="pump_implicit_ratio" name="" index="19"/>
    <alias field="thin_water_layer_definition" name="" index="20"/>
    <alias field="use_of_cg" name="" index="21"/>
    <alias field="use_of_nested_newton" name="" index="22"/>
  </aliases>
  <defaults>
    <default applyOnUpdate="0" field="id" expression=" if(maximum(id) is null,1, maximum(id)+1)"/>
    <default applyOnUpdate="0" field="cfl_strictness_factor_1d" expression="1"/>
    <default applyOnUpdate="0" field="cfl_strictness_factor_2d" expression="1"/>
    <default applyOnUpdate="0" field="convergence_cg" expression="0.000000001"/>
    <default applyOnUpdate="0" field="convergence_eps" expression="0.00001"/>
    <default applyOnUpdate="0" field="flow_direction_threshold" expression="0.000001"/>
    <default applyOnUpdate="0" field="frict_shallow_water_correction" expression="0"/>
    <default applyOnUpdate="0" field="general_numerical_threshold" expression="0.00000001"/>
    <default applyOnUpdate="0" field="integration_method" expression="0"/>
    <default applyOnUpdate="0" field="limiter_grad_1d" expression="1"/>
    <default applyOnUpdate="0" field="limiter_grad_2d" expression="0"/>
    <default applyOnUpdate="0" field="limiter_slope_crossectional_area_2d" expression="0"/>
    <default applyOnUpdate="0" field="limiter_slope_friction_2d" expression="0"/>
    <default applyOnUpdate="0" field="max_nonlin_iterations" expression="20"/>
    <default applyOnUpdate="0" field="max_degree" expression=""/>
    <default applyOnUpdate="0" field="minimum_friction_velocity" expression="0.05"/>
    <default applyOnUpdate="0" field="minimum_surface_area" expression="0.00000001"/>
    <default applyOnUpdate="0" field="precon_cg" expression="1"/>
    <default applyOnUpdate="0" field="preissmann_slot" expression="0"/>
    <default applyOnUpdate="0" field="pump_implicit_ratio" expression="1"/>
    <default applyOnUpdate="0" field="thin_water_layer_definition" expression="0.05"/>
    <default applyOnUpdate="0" field="use_of_cg" expression="20"/>
    <default applyOnUpdate="0" field="use_of_nested_newton" expression=""/>
  </defaults>
  <constraints>
    <constraint unique_strength="1" constraints="3" field="id" exp_strength="0" notnull_strength="1"/>
    <constraint unique_strength="0" constraints="0" field="cfl_strictness_factor_1d" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="cfl_strictness_factor_2d" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="convergence_cg" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="1" field="convergence_eps" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="0" field="flow_direction_threshold" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="frict_shallow_water_correction" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="general_numerical_threshold" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="1" field="integration_method" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="0" field="limiter_grad_1d" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="limiter_grad_2d" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="limiter_slope_crossectional_area_2d" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="limiter_slope_friction_2d" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="1" field="max_nonlin_iterations" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="1" field="max_degree" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="0" field="minimum_friction_velocity" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="minimum_surface_area" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="precon_cg" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="preissmann_slot" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="pump_implicit_ratio" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="thin_water_layer_definition" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="1" field="use_of_cg" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="1" field="use_of_nested_newton" exp_strength="0" notnull_strength="2"/>
  </constraints>
  <constraintExpressions>
    <constraint field="id" exp="" desc=""/>
    <constraint field="cfl_strictness_factor_1d" exp="" desc=""/>
    <constraint field="cfl_strictness_factor_2d" exp="" desc=""/>
    <constraint field="convergence_cg" exp="" desc=""/>
    <constraint field="convergence_eps" exp="" desc=""/>
    <constraint field="flow_direction_threshold" exp="" desc=""/>
    <constraint field="frict_shallow_water_correction" exp="" desc=""/>
    <constraint field="general_numerical_threshold" exp="" desc=""/>
    <constraint field="integration_method" exp="" desc=""/>
    <constraint field="limiter_grad_1d" exp="" desc=""/>
    <constraint field="limiter_grad_2d" exp="" desc=""/>
    <constraint field="limiter_slope_crossectional_area_2d" exp="" desc=""/>
    <constraint field="limiter_slope_friction_2d" exp="" desc=""/>
    <constraint field="max_nonlin_iterations" exp="" desc=""/>
    <constraint field="max_degree" exp="" desc=""/>
    <constraint field="minimum_friction_velocity" exp="" desc=""/>
    <constraint field="minimum_surface_area" exp="" desc=""/>
    <constraint field="precon_cg" exp="" desc=""/>
    <constraint field="preissmann_slot" exp="" desc=""/>
    <constraint field="pump_implicit_ratio" exp="" desc=""/>
    <constraint field="thin_water_layer_definition" exp="" desc=""/>
    <constraint field="use_of_cg" exp="" desc=""/>
    <constraint field="use_of_nested_newton" exp="" desc=""/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction key="Canvas" value="{00000000-0000-0000-0000-000000000000}"/>
  </attributeactions>
  <attributetableconfig actionWidgetStyle="dropDown" sortExpression="" sortOrder="0">
    <columns>
      <column type="field" name="id" width="-1" hidden="0"/>
      <column type="field" name="cfl_strictness_factor_1d" width="-1" hidden="0"/>
      <column type="field" name="cfl_strictness_factor_2d" width="-1" hidden="0"/>
      <column type="field" name="convergence_cg" width="-1" hidden="0"/>
      <column type="field" name="convergence_eps" width="-1" hidden="0"/>
      <column type="field" name="flow_direction_threshold" width="-1" hidden="0"/>
      <column type="field" name="frict_shallow_water_correction" width="-1" hidden="0"/>
      <column type="field" name="general_numerical_threshold" width="-1" hidden="0"/>
      <column type="field" name="integration_method" width="-1" hidden="0"/>
      <column type="field" name="limiter_grad_1d" width="-1" hidden="0"/>
      <column type="field" name="limiter_grad_2d" width="-1" hidden="0"/>
      <column type="field" name="limiter_slope_crossectional_area_2d" width="-1" hidden="0"/>
      <column type="field" name="limiter_slope_friction_2d" width="-1" hidden="0"/>
      <column type="field" name="max_nonlin_iterations" width="-1" hidden="0"/>
      <column type="field" name="max_degree" width="-1" hidden="0"/>
      <column type="field" name="minimum_friction_velocity" width="-1" hidden="0"/>
      <column type="field" name="minimum_surface_area" width="-1" hidden="0"/>
      <column type="field" name="precon_cg" width="-1" hidden="0"/>
      <column type="field" name="preissmann_slot" width="-1" hidden="0"/>
      <column type="field" name="pump_implicit_ratio" width="-1" hidden="0"/>
      <column type="field" name="thin_water_layer_definition" width="-1" hidden="0"/>
      <column type="field" name="use_of_cg" width="-1" hidden="0"/>
      <column type="field" name="use_of_nested_newton" width="-1" hidden="0"/>
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
    </attributeEditorContainer>
    <attributeEditorContainer columnCount="1" name="Limiters" groupBox="0" showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="">
      <attributeEditorField name="limiter_grad_1d" showLabel="1" index="9"/>
      <attributeEditorField name="limiter_grad_2d" showLabel="1" index="10"/>
      <attributeEditorField name="limiter_slope_crossectional_area_2d" showLabel="1" index="11"/>
      <attributeEditorField name="limiter_slope_friction_2d" showLabel="1" index="12"/>
    </attributeEditorContainer>
    <attributeEditorContainer columnCount="1" name="Matrix" groupBox="0" showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="">
      <attributeEditorField name="convergence_cg" showLabel="1" index="3"/>
      <attributeEditorField name="convergence_eps" showLabel="1" index="4"/>
      <attributeEditorField name="use_of_cg" showLabel="1" index="21"/>
      <attributeEditorField name="use_of_nested_newton" showLabel="1" index="22"/>
      <attributeEditorField name="max_degree" showLabel="1" index="14"/>
      <attributeEditorField name="max_nonlin_iterations" showLabel="1" index="13"/>
      <attributeEditorField name="precon_cg" showLabel="1" index="17"/>
      <attributeEditorField name="integration_method" showLabel="1" index="8"/>
    </attributeEditorContainer>
    <attributeEditorContainer columnCount="1" name="Thresholds" groupBox="0" showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="">
      <attributeEditorField name="flow_direction_threshold" showLabel="1" index="5"/>
      <attributeEditorField name="general_numerical_threshold" showLabel="1" index="7"/>
      <attributeEditorField name="thin_water_layer_definition" showLabel="1" index="20"/>
      <attributeEditorField name="minimum_friction_velocity" showLabel="1" index="15"/>
      <attributeEditorField name="minimum_surface_area" showLabel="1" index="16"/>
    </attributeEditorContainer>
    <attributeEditorContainer columnCount="1" name="Miscellaneous" groupBox="0" showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="">
      <attributeEditorField name="cfl_strictness_factor_1d" showLabel="1" index="1"/>
      <attributeEditorField name="cfl_strictness_factor_2d" showLabel="1" index="2"/>
      <attributeEditorField name="frict_shallow_water_correction" showLabel="1" index="6"/>
      <attributeEditorField name="pump_implicit_ratio" showLabel="1" index="19"/>
      <attributeEditorField name="preissmann_slot" showLabel="1" index="18"/>
    </attributeEditorContainer>
  </attributeEditorForm>
  <editable>
    <field editable="1" name="cfl_strictness_factor_1d"/>
    <field editable="1" name="cfl_strictness_factor_2d"/>
    <field editable="1" name="convergence_cg"/>
    <field editable="1" name="convergence_eps"/>
    <field editable="1" name="flow_direction_threshold"/>
    <field editable="1" name="frict_shallow_water_correction"/>
    <field editable="1" name="general_numerical_threshold"/>
    <field editable="1" name="id"/>
    <field editable="1" name="integration_method"/>
    <field editable="1" name="limiter_grad_1d"/>
    <field editable="1" name="limiter_grad_2d"/>
    <field editable="1" name="limiter_slope_crossectional_area_2d"/>
    <field editable="1" name="limiter_slope_friction_2d"/>
    <field editable="1" name="max_degree"/>
    <field editable="1" name="max_nonlin_iterations"/>
    <field editable="1" name="minimum_friction_velocity"/>
    <field editable="1" name="minimum_surface_area"/>
    <field editable="1" name="precon_cg"/>
    <field editable="1" name="preissmann_slot"/>
    <field editable="1" name="pump_implicit_ratio"/>
    <field editable="1" name="thin_water_layer_definition"/>
    <field editable="1" name="use_of_cg"/>
    <field editable="1" name="use_of_nested_newton"/>
  </editable>
  <labelOnTop>
    <field labelOnTop="0" name="cfl_strictness_factor_1d"/>
    <field labelOnTop="0" name="cfl_strictness_factor_2d"/>
    <field labelOnTop="0" name="convergence_cg"/>
    <field labelOnTop="0" name="convergence_eps"/>
    <field labelOnTop="0" name="flow_direction_threshold"/>
    <field labelOnTop="0" name="frict_shallow_water_correction"/>
    <field labelOnTop="0" name="general_numerical_threshold"/>
    <field labelOnTop="0" name="id"/>
    <field labelOnTop="0" name="integration_method"/>
    <field labelOnTop="0" name="limiter_grad_1d"/>
    <field labelOnTop="0" name="limiter_grad_2d"/>
    <field labelOnTop="0" name="limiter_slope_crossectional_area_2d"/>
    <field labelOnTop="0" name="limiter_slope_friction_2d"/>
    <field labelOnTop="0" name="max_degree"/>
    <field labelOnTop="0" name="max_nonlin_iterations"/>
    <field labelOnTop="0" name="minimum_friction_velocity"/>
    <field labelOnTop="0" name="minimum_surface_area"/>
    <field labelOnTop="0" name="precon_cg"/>
    <field labelOnTop="0" name="preissmann_slot"/>
    <field labelOnTop="0" name="pump_implicit_ratio"/>
    <field labelOnTop="0" name="thin_water_layer_definition"/>
    <field labelOnTop="0" name="use_of_cg"/>
    <field labelOnTop="0" name="use_of_nested_newton"/>
  </labelOnTop>
  <dataDefinedFieldProperties/>
  <widgets/>
  <previewExpression>id</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>4</layerGeometryType>
</qgis>
