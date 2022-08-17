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
    <field configurationFlags="None" name="maximum_sim_time_step">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="nr_timesteps">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="dem_file">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="minimum_sim_time_step">
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
    <field configurationFlags="None" name="table_step_size_volume_2d">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="frict_coef_file">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="initial_groundwater_level_file">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="initial_waterlevel">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="epsg_code">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="numerical_settings_id">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="dem_obstacle_detection">
      <editWidget type="CheckBox">
        <config>
          <Option type="Map">
            <Option type="QString" name="CheckedState" value="1"/>
            <Option type="QString" name="UncheckedState" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="frict_avg">
      <editWidget type="CheckBox">
        <config>
          <Option type="Map">
            <Option type="QString" name="CheckedState" value="1"/>
            <Option type="QString" name="UncheckedState" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="initial_groundwater_level_type">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option type="QString" name="max" value="0"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="min" value="1"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="average" value="2"/>
              </Option>
            </Option>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="water_level_ini_type">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option type="QString" name="max" value="0"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="min" value="1"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="average" value="2"/>
              </Option>
            </Option>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="grid_space">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="advection_2d">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option type="QString" name="0: Do not use advection 2d" value="0"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="1: Use advection 2d" value="1"/>
              </Option>
            </Option>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="embedded_cutoff_threshold">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="dist_calc_points">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="start_date">
      <editWidget type="DateTime">
        <config>
          <Option type="Map">
            <Option type="bool" name="allow_null" value="true"/>
            <Option type="bool" name="calendar_popup" value="true"/>
            <Option type="QString" name="display_format" value="yyyy-MM-dd"/>
            <Option type="QString" name="field_format" value="yyyy-MM-dd"/>
            <Option type="bool" name="field_iso_format" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="max_interception_file">
      <editWidget type="">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="output_time_step">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="interflow_settings_id">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="table_step_size">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="use_1d_flow">
      <editWidget type="CheckBox">
        <config>
          <Option type="Map">
            <Option type="QString" name="CheckedState" value="1"/>
            <Option type="QString" name="UncheckedState" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="start_time">
      <editWidget type="DateTime">
        <config>
          <Option type="Map">
            <Option type="bool" name="allow_null" value="true"/>
            <Option type="bool" name="calendar_popup" value="true"/>
            <Option type="QString" name="display_format" value="yyyy-MM-dd HH:mm:ss"/>
            <Option type="QString" name="field_format" value="yyyy-MM-dd HH:mm:ss"/>
            <Option type="bool" name="field_iso_format" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="use_2d_rain">
      <editWidget type="CheckBox">
        <config>
          <Option type="Map">
            <Option type="QString" name="CheckedState" value="1"/>
            <Option type="QString" name="UncheckedState" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="initial_groundwater_level">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="kmax">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="initial_waterlevel_file">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="sim_time_step">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="frict_coef">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="guess_dams">
      <editWidget type="CheckBox">
        <config>
          <Option type="Map">
            <Option type="QString" name="CheckedState" value="1"/>
            <Option type="QString" name="UncheckedState" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="control_group_id">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="dem_obstacle_height">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="timestep_plus">
      <editWidget type="CheckBox">
        <config>
          <Option type="Map">
            <Option type="QString" name="CheckedState" value="1"/>
            <Option type="QString" name="UncheckedState" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="name">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="flooding_threshold">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="frict_type">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option type="QString" name="1: Chèzy" value="1"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="2: Manning" value="2"/>
              </Option>
            </Option>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="use_2d_flow">
      <editWidget type="CheckBox">
        <config>
          <Option type="Map">
            <Option type="QString" name="CheckedState" value="1"/>
            <Option type="QString" name="UncheckedState" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="max_interception">
      <editWidget type="">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="max_angle_1d_advection">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="advection_1d">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option type="QString" name="0: Do not use advection 1d" value="0"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="1: Use advection 1d" value="1"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="2: Experimental advection 1d" value="2"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="3: Experimental advection 1d" value="3"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="4: Experimental advection 1d" value="4"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="5: Experimental advection 1d" value="5"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="6: Experimental advection 1d" value="6"/>
              </Option>
            </Option>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="wind_shielding_file">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="simple_infiltration_settings_id">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="groundwater_settings_id">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="manhole_storage_area">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="bool" name="IsMultiline" value="false"/>
            <Option type="bool" name="UseHtml" value="false"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="use_0d_inflow">
      <editWidget type="ValueMap">
        <config>
          <Option type="Map">
            <Option type="List" name="map">
              <Option type="Map">
                <Option type="QString" name="0: do not use 0d inflow" value="0"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="1: use v2_impervious_surface" value="1"/>
              </Option>
              <Option type="Map">
                <Option type="QString" name="2: use v2_surface" value="2"/>
              </Option>
            </Option>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="table_step_size_1d">
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
    <alias field="maximum_sim_time_step" name="" index="0"/>
    <alias field="nr_timesteps" name="" index="1"/>
    <alias field="dem_file" name="" index="2"/>
    <alias field="minimum_sim_time_step" name="" index="3"/>
    <alias field="id" name="" index="4"/>
    <alias field="table_step_size_volume_2d" name="" index="5"/>
    <alias field="frict_coef_file" name="" index="6"/>
    <alias field="initial_groundwater_level_file" name="" index="7"/>
    <alias field="initial_waterlevel" name="" index="8"/>
    <alias field="epsg_code" name="" index="9"/>
    <alias field="numerical_settings_id" name="" index="10"/>
    <alias field="dem_obstacle_detection" name="" index="11"/>
    <alias field="frict_avg" name="" index="12"/>
    <alias field="initial_groundwater_level_type" name="" index="13"/>
    <alias field="water_level_ini_type" name="" index="14"/>
    <alias field="grid_space" name="" index="15"/>
    <alias field="advection_2d" name="" index="16"/>
    <alias field="embedded_cutoff_threshold" name="" index="17"/>
    <alias field="dist_calc_points" name="" index="18"/>
    <alias field="start_date" name="" index="19"/>
    <alias field="max_interception_file" name="" index="20"/>
    <alias field="output_time_step" name="" index="21"/>
    <alias field="interflow_settings_id" name="" index="22"/>
    <alias field="table_step_size" name="" index="23"/>
    <alias field="use_1d_flow" name="" index="24"/>
    <alias field="start_time" name="" index="25"/>
    <alias field="use_2d_rain" name="" index="26"/>
    <alias field="initial_groundwater_level" name="" index="27"/>
    <alias field="kmax" name="" index="28"/>
    <alias field="initial_waterlevel_file" name="" index="29"/>
    <alias field="sim_time_step" name="" index="30"/>
    <alias field="frict_coef" name="" index="31"/>
    <alias field="guess_dams" name="" index="32"/>
    <alias field="control_group_id" name="" index="33"/>
    <alias field="dem_obstacle_height" name="" index="34"/>
    <alias field="timestep_plus" name="" index="35"/>
    <alias field="name" name="" index="36"/>
    <alias field="flooding_threshold" name="" index="37"/>
    <alias field="frict_type" name="" index="38"/>
    <alias field="use_2d_flow" name="" index="39"/>
    <alias field="max_interception" name="" index="40"/>
    <alias field="max_angle_1d_advection" name="" index="41"/>
    <alias field="advection_1d" name="" index="42"/>
    <alias field="wind_shielding_file" name="" index="43"/>
    <alias field="simple_infiltration_settings_id" name="" index="44"/>
    <alias field="groundwater_settings_id" name="" index="45"/>
    <alias field="manhole_storage_area" name="" index="46"/>
    <alias field="use_0d_inflow" name="" index="47"/>
    <alias field="table_step_size_1d" name="" index="48"/>
  </aliases>
  <defaults>
    <default applyOnUpdate="0" field="maximum_sim_time_step" expression=""/>
    <default applyOnUpdate="0" field="nr_timesteps" expression=""/>
    <default applyOnUpdate="0" field="dem_file" expression=""/>
    <default applyOnUpdate="0" field="minimum_sim_time_step" expression=""/>
    <default applyOnUpdate="0" field="id" expression="if(maximum(id) is null,1, maximum(id)+1)"/>
    <default applyOnUpdate="0" field="table_step_size_volume_2d" expression=""/>
    <default applyOnUpdate="0" field="frict_coef_file" expression=""/>
    <default applyOnUpdate="0" field="initial_groundwater_level_file" expression=""/>
    <default applyOnUpdate="0" field="initial_waterlevel" expression=""/>
    <default applyOnUpdate="0" field="epsg_code" expression=""/>
    <default applyOnUpdate="0" field="numerical_settings_id" expression="1"/>
    <default applyOnUpdate="0" field="dem_obstacle_detection" expression="0"/>
    <default applyOnUpdate="0" field="frict_avg" expression="0"/>
    <default applyOnUpdate="0" field="initial_groundwater_level_type" expression=""/>
    <default applyOnUpdate="0" field="water_level_ini_type" expression=""/>
    <default applyOnUpdate="0" field="grid_space" expression=""/>
    <default applyOnUpdate="0" field="advection_2d" expression=""/>
    <default applyOnUpdate="0" field="embedded_cutoff_threshold" expression=""/>
    <default applyOnUpdate="0" field="dist_calc_points" expression="10000"/>
    <default applyOnUpdate="0" field="start_date" expression=" to_date(now() )"/>
    <default applyOnUpdate="0" field="max_interception_file" expression=""/>
    <default applyOnUpdate="0" field="output_time_step" expression=""/>
    <default applyOnUpdate="0" field="interflow_settings_id" expression=""/>
    <default applyOnUpdate="0" field="table_step_size" expression="0.01"/>
    <default applyOnUpdate="0" field="use_1d_flow" expression=""/>
    <default applyOnUpdate="0" field="start_time" expression=" to_date( now() ) ||  ' 00:00:00'"/>
    <default applyOnUpdate="0" field="use_2d_rain" expression=""/>
    <default applyOnUpdate="0" field="initial_groundwater_level" expression=""/>
    <default applyOnUpdate="0" field="kmax" expression=""/>
    <default applyOnUpdate="0" field="initial_waterlevel_file" expression=""/>
    <default applyOnUpdate="0" field="sim_time_step" expression=""/>
    <default applyOnUpdate="0" field="frict_coef" expression=""/>
    <default applyOnUpdate="0" field="guess_dams" expression="0"/>
    <default applyOnUpdate="0" field="control_group_id" expression=""/>
    <default applyOnUpdate="0" field="dem_obstacle_height" expression=""/>
    <default applyOnUpdate="0" field="timestep_plus" expression="0"/>
    <default applyOnUpdate="0" field="name" expression=""/>
    <default applyOnUpdate="0" field="flooding_threshold" expression="0.001"/>
    <default applyOnUpdate="0" field="frict_type" expression="2"/>
    <default applyOnUpdate="0" field="use_2d_flow" expression=""/>
    <default applyOnUpdate="0" field="max_interception" expression=""/>
    <default applyOnUpdate="0" field="max_angle_1d_advection" expression=""/>
    <default applyOnUpdate="0" field="advection_1d" expression=""/>
    <default applyOnUpdate="0" field="wind_shielding_file" expression=""/>
    <default applyOnUpdate="0" field="simple_infiltration_settings_id" expression=""/>
    <default applyOnUpdate="0" field="groundwater_settings_id" expression=""/>
    <default applyOnUpdate="0" field="manhole_storage_area" expression=""/>
    <default applyOnUpdate="0" field="use_0d_inflow" expression=""/>
    <default applyOnUpdate="0" field="table_step_size_1d" expression=""/>
  </defaults>
  <constraints>
    <constraint unique_strength="0" constraints="0" field="maximum_sim_time_step" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="1" field="nr_timesteps" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="0" field="dem_file" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="4" field="minimum_sim_time_step" exp_strength="2" notnull_strength="0"/>
    <constraint unique_strength="1" constraints="3" field="id" exp_strength="0" notnull_strength="1"/>
    <constraint unique_strength="0" constraints="0" field="table_step_size_volume_2d" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="frict_coef_file" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="initial_groundwater_level_file" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="1" field="initial_waterlevel" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="1" field="epsg_code" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="1" field="numerical_settings_id" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="1" field="dem_obstacle_detection" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="1" field="frict_avg" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="0" field="initial_groundwater_level_type" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="water_level_ini_type" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="1" field="grid_space" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="1" field="advection_2d" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="0" field="embedded_cutoff_threshold" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="1" field="dist_calc_points" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="5" field="start_date" exp_strength="2" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="0" field="max_interception_file" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="1" field="output_time_step" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="0" field="interflow_settings_id" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="1" field="table_step_size" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="1" field="use_1d_flow" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="5" field="start_time" exp_strength="2" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="1" field="use_2d_rain" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="0" field="initial_groundwater_level" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="1" field="kmax" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="0" field="initial_waterlevel_file" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="1" field="sim_time_step" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="1" field="frict_coef" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="0" field="guess_dams" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="control_group_id" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="dem_obstacle_height" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="1" field="timestep_plus" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="1" constraints="3" field="name" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="1" field="flooding_threshold" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="0" field="frict_type" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="1" field="use_2d_flow" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="0" field="max_interception" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="max_angle_1d_advection" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="1" field="advection_1d" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="0" field="wind_shielding_file" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="simple_infiltration_settings_id" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="groundwater_settings_id" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="manhole_storage_area" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="1" field="use_0d_inflow" exp_strength="0" notnull_strength="2"/>
    <constraint unique_strength="0" constraints="0" field="table_step_size_1d" exp_strength="0" notnull_strength="0"/>
  </constraints>
  <constraintExpressions>
    <constraint field="maximum_sim_time_step" exp="" desc=""/>
    <constraint field="nr_timesteps" exp="" desc=""/>
    <constraint field="dem_file" exp="" desc=""/>
    <constraint field="minimum_sim_time_step" exp=" &quot;minimum_sim_time_step&quot; &lt; &quot;sim_time_step&quot; " desc=""/>
    <constraint field="id" exp="" desc=""/>
    <constraint field="table_step_size_volume_2d" exp="" desc=""/>
    <constraint field="frict_coef_file" exp="" desc=""/>
    <constraint field="initial_groundwater_level_file" exp="" desc=""/>
    <constraint field="initial_waterlevel" exp="" desc=""/>
    <constraint field="epsg_code" exp="" desc=""/>
    <constraint field="numerical_settings_id" exp="" desc=""/>
    <constraint field="dem_obstacle_detection" exp="" desc=""/>
    <constraint field="frict_avg" exp="" desc=""/>
    <constraint field="initial_groundwater_level_type" exp="" desc=""/>
    <constraint field="water_level_ini_type" exp="" desc=""/>
    <constraint field="grid_space" exp="" desc=""/>
    <constraint field="advection_2d" exp="" desc=""/>
    <constraint field="embedded_cutoff_threshold" exp="" desc=""/>
    <constraint field="dist_calc_points" exp="" desc=""/>
    <constraint field="start_date" exp="&quot;start_date&quot; is not null" desc=""/>
    <constraint field="max_interception_file" exp="" desc=""/>
    <constraint field="output_time_step" exp="" desc=""/>
    <constraint field="interflow_settings_id" exp="" desc=""/>
    <constraint field="table_step_size" exp="" desc=""/>
    <constraint field="use_1d_flow" exp="" desc=""/>
    <constraint field="start_time" exp="&quot;start_time&quot;" desc=""/>
    <constraint field="use_2d_rain" exp="" desc=""/>
    <constraint field="initial_groundwater_level" exp="" desc=""/>
    <constraint field="kmax" exp="" desc=""/>
    <constraint field="initial_waterlevel_file" exp="" desc=""/>
    <constraint field="sim_time_step" exp="" desc=""/>
    <constraint field="frict_coef" exp="" desc=""/>
    <constraint field="guess_dams" exp="" desc=""/>
    <constraint field="control_group_id" exp="" desc=""/>
    <constraint field="dem_obstacle_height" exp="" desc=""/>
    <constraint field="timestep_plus" exp="" desc=""/>
    <constraint field="name" exp="" desc=""/>
    <constraint field="flooding_threshold" exp="" desc=""/>
    <constraint field="frict_type" exp="" desc=""/>
    <constraint field="use_2d_flow" exp="" desc=""/>
    <constraint field="max_interception" exp="" desc=""/>
    <constraint field="max_angle_1d_advection" exp="" desc=""/>
    <constraint field="advection_1d" exp="" desc=""/>
    <constraint field="wind_shielding_file" exp="" desc=""/>
    <constraint field="simple_infiltration_settings_id" exp="" desc=""/>
    <constraint field="groundwater_settings_id" exp="" desc=""/>
    <constraint field="manhole_storage_area" exp="" desc=""/>
    <constraint field="use_0d_inflow" exp="" desc=""/>
    <constraint field="table_step_size_1d" exp="" desc=""/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction key="Canvas" value="{00000000-0000-0000-0000-000000000000}"/>
  </attributeactions>
  <attributetableconfig actionWidgetStyle="dropDown" sortExpression="&quot;maximum_sim_time_step&quot;" sortOrder="0">
    <columns>
      <column type="field" name="maximum_sim_time_step" width="116" hidden="0"/>
      <column type="field" name="nr_timesteps" width="-1" hidden="0"/>
      <column type="field" name="dem_file" width="-1" hidden="0"/>
      <column type="field" name="minimum_sim_time_step" width="-1" hidden="0"/>
      <column type="field" name="id" width="-1" hidden="0"/>
      <column type="field" name="table_step_size_volume_2d" width="-1" hidden="0"/>
      <column type="field" name="frict_coef_file" width="-1" hidden="0"/>
      <column type="field" name="initial_groundwater_level_file" width="-1" hidden="0"/>
      <column type="field" name="initial_waterlevel" width="-1" hidden="0"/>
      <column type="field" name="epsg_code" width="-1" hidden="0"/>
      <column type="field" name="numerical_settings_id" width="-1" hidden="0"/>
      <column type="field" name="dem_obstacle_detection" width="-1" hidden="0"/>
      <column type="field" name="frict_avg" width="-1" hidden="0"/>
      <column type="field" name="initial_groundwater_level_type" width="-1" hidden="0"/>
      <column type="field" name="water_level_ini_type" width="-1" hidden="0"/>
      <column type="field" name="grid_space" width="-1" hidden="0"/>
      <column type="field" name="advection_2d" width="-1" hidden="0"/>
      <column type="field" name="embedded_cutoff_threshold" width="-1" hidden="0"/>
      <column type="field" name="dist_calc_points" width="-1" hidden="0"/>
      <column type="field" name="start_date" width="-1" hidden="0"/>
      <column type="field" name="initial_groundwater_level" width="-1" hidden="0"/>
      <column type="field" name="output_time_step" width="-1" hidden="0"/>
      <column type="field" name="interflow_settings_id" width="-1" hidden="0"/>
      <column type="field" name="table_step_size" width="-1" hidden="0"/>
      <column type="field" name="use_1d_flow" width="-1" hidden="0"/>
      <column type="field" name="start_time" width="-1" hidden="0"/>
      <column type="field" name="use_2d_rain" width="-1" hidden="0"/>
      <column type="field" name="kmax" width="-1" hidden="0"/>
      <column type="field" name="initial_waterlevel_file" width="-1" hidden="0"/>
      <column type="field" name="sim_time_step" width="-1" hidden="0"/>
      <column type="field" name="frict_coef" width="-1" hidden="0"/>
      <column type="field" name="guess_dams" width="-1" hidden="0"/>
      <column type="field" name="control_group_id" width="-1" hidden="0"/>
      <column type="field" name="dem_obstacle_height" width="-1" hidden="0"/>
      <column type="field" name="timestep_plus" width="-1" hidden="0"/>
      <column type="field" name="name" width="-1" hidden="0"/>
      <column type="field" name="flooding_threshold" width="-1" hidden="0"/>
      <column type="field" name="frict_type" width="-1" hidden="0"/>
      <column type="field" name="use_2d_flow" width="-1" hidden="0"/>
      <column type="field" name="max_angle_1d_advection" width="-1" hidden="0"/>
      <column type="field" name="advection_1d" width="-1" hidden="0"/>
      <column type="field" name="wind_shielding_file" width="-1" hidden="0"/>
      <column type="field" name="simple_infiltration_settings_id" width="-1" hidden="0"/>
      <column type="field" name="groundwater_settings_id" width="-1" hidden="0"/>
      <column type="field" name="manhole_storage_area" width="-1" hidden="0"/>
      <column type="field" name="use_0d_inflow" width="-1" hidden="0"/>
      <column type="field" name="table_step_size_1d" width="-1" hidden="0"/>
      <column type="actions" width="-1" hidden="1"/>
      <column type="field" name="interception_global" width="-1" hidden="0"/>
      <column type="field" name="interception_file" width="-1" hidden="0"/>
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
      <attributeEditorField name="id" showLabel="1" index="4"/>
      <attributeEditorField name="name" showLabel="1" index="36"/>
      <attributeEditorField name="use_0d_inflow" showLabel="1" index="47"/>
      <attributeEditorField name="use_1d_flow" showLabel="1" index="24"/>
      <attributeEditorField name="use_2d_rain" showLabel="1" index="26"/>
      <attributeEditorField name="use_2d_flow" showLabel="1" index="39"/>
    </attributeEditorContainer>
    <attributeEditorContainer columnCount="1" name="Grid" groupBox="0" showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="">
      <attributeEditorField name="grid_space" showLabel="1" index="15"/>
      <attributeEditorField name="kmax" showLabel="1" index="28"/>
      <attributeEditorField name="table_step_size" showLabel="1" index="23"/>
    </attributeEditorContainer>
    <attributeEditorContainer columnCount="1" name="Terrain information" groupBox="0" showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="&quot;advection_1d&quot;">
      <attributeEditorContainer columnCount="1" name="DEM" groupBox="1" showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="">
        <attributeEditorField name="dem_file" showLabel="1" index="2"/>
        <attributeEditorField name="epsg_code" showLabel="1" index="9"/>
      </attributeEditorContainer>
      <attributeEditorContainer columnCount="1" name="Friction" groupBox="1" showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="">
        <attributeEditorField name="frict_coef_file" showLabel="1" index="6"/>
        <attributeEditorField name="frict_coef" showLabel="1" index="31"/>
        <attributeEditorField name="frict_type" showLabel="1" index="38"/>
        <attributeEditorField name="frict_avg" showLabel="1" index="12"/>
      </attributeEditorContainer>
      <attributeEditorContainer columnCount="1" name="Groundwater" groupBox="1" showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="">
        <attributeEditorField name="initial_groundwater_level_file" showLabel="1" index="7"/>
        <attributeEditorField name="initial_groundwater_level" showLabel="1" index="27"/>
        <attributeEditorField name="initial_groundwater_level_type" showLabel="1" index="13"/>
      </attributeEditorContainer>
      <attributeEditorContainer columnCount="1" name="Initial waterlevel" groupBox="1" showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="">
        <attributeEditorField name="initial_waterlevel_file" showLabel="1" index="29"/>
        <attributeEditorField name="initial_waterlevel" showLabel="1" index="8"/>
        <attributeEditorField name="water_level_ini_type" showLabel="1" index="14"/>
      </attributeEditorContainer>
      <attributeEditorContainer columnCount="1" name="Interception" groupBox="1" showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="">
        <attributeEditorField name="interception_file" showLabel="1" index="-1"/>
        <attributeEditorField name="interception_global" showLabel="1" index="-1"/>
        <attributeEditorField name="max_interception" showLabel="1" index="40"/>
      </attributeEditorContainer>
      <attributeEditorContainer columnCount="1" name="Wind" groupBox="1" showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="">
        <attributeEditorField name="wind_shielding_file" showLabel="1" index="43"/>
      </attributeEditorContainer>
    </attributeEditorContainer>
    <attributeEditorContainer columnCount="1" name="Time" groupBox="0" showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="">
      <attributeEditorField name="start_date" showLabel="1" index="19"/>
      <attributeEditorField name="start_time" showLabel="1" index="25"/>
      <attributeEditorField name="sim_time_step" showLabel="1" index="30"/>
      <attributeEditorField name="timestep_plus" showLabel="1" index="35"/>
      <attributeEditorField name="minimum_sim_time_step" showLabel="1" index="3"/>
      <attributeEditorField name="maximum_sim_time_step" showLabel="1" index="0"/>
      <attributeEditorField name="nr_timesteps" showLabel="1" index="1"/>
      <attributeEditorField name="output_time_step" showLabel="1" index="21"/>
    </attributeEditorContainer>
    <attributeEditorContainer columnCount="1" name="Settings id's" groupBox="0" showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="">
      <attributeEditorField name="interflow_settings_id" showLabel="1" index="22"/>
      <attributeEditorField name="groundwater_settings_id" showLabel="1" index="45"/>
      <attributeEditorField name="numerical_settings_id" showLabel="1" index="10"/>
      <attributeEditorField name="simple_infiltration_settings_id" showLabel="1" index="44"/>
      <attributeEditorField name="control_group_id" showLabel="1" index="33"/>
    </attributeEditorContainer>
    <attributeEditorContainer columnCount="1" name="Extra options 1D" groupBox="0" showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="">
      <attributeEditorField name="advection_1d" showLabel="1" index="42"/>
      <attributeEditorField name="dist_calc_points" showLabel="1" index="18"/>
      <attributeEditorField name="manhole_storage_area" showLabel="1" index="46"/>
      <attributeEditorField name="max_angle_1d_advection" showLabel="1" index="41"/>
      <attributeEditorField name="table_step_size_1d" showLabel="1" index="48"/>
    </attributeEditorContainer>
    <attributeEditorContainer columnCount="1" name="Extra options 2D" groupBox="0" showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="">
      <attributeEditorField name="advection_2d" showLabel="1" index="16"/>
      <attributeEditorField name="dem_obstacle_detection" showLabel="1" index="11"/>
      <attributeEditorField name="guess_dams" showLabel="1" index="32"/>
      <attributeEditorField name="dem_obstacle_height" showLabel="1" index="34"/>
      <attributeEditorField name="embedded_cutoff_threshold" showLabel="1" index="17"/>
      <attributeEditorField name="flooding_threshold" showLabel="1" index="37"/>
      <attributeEditorField name="table_step_size_volume_2d" showLabel="1" index="5"/>
    </attributeEditorContainer>
  </attributeEditorForm>
  <editable>
    <field editable="1" name="advection_1d"/>
    <field editable="1" name="advection_2d"/>
    <field editable="1" name="control_group_id"/>
    <field editable="1" name="dem_file"/>
    <field editable="1" name="dem_obstacle_detection"/>
    <field editable="1" name="dem_obstacle_height"/>
    <field editable="1" name="dist_calc_points"/>
    <field editable="1" name="embedded_cutoff_threshold"/>
    <field editable="1" name="epsg_code"/>
    <field editable="1" name="flooding_threshold"/>
    <field editable="1" name="frict_avg"/>
    <field editable="1" name="frict_coef"/>
    <field editable="1" name="frict_coef_file"/>
    <field editable="1" name="frict_type"/>
    <field editable="1" name="grid_space"/>
    <field editable="1" name="groundwater_settings_id"/>
    <field editable="1" name="guess_dams"/>
    <field editable="1" name="id"/>
    <field editable="1" name="initial_groundwater_level"/>
    <field editable="1" name="initial_groundwater_level_file"/>
    <field editable="1" name="initial_groundwater_level_type"/>
    <field editable="1" name="initial_waterlevel"/>
    <field editable="1" name="initial_waterlevel_file"/>
    <field editable="1" name="interception_file"/>
    <field editable="1" name="interception_global"/>
    <field editable="1" name="interflow_settings_id"/>
    <field editable="1" name="kmax"/>
    <field editable="1" name="manhole_storage_area"/>
    <field editable="1" name="max_angle_1d_advection"/>
    <field editable="1" name="max_interception"/>
    <field editable="1" name="max_interception_file"/>
    <field editable="1" name="maximum_sim_time_step"/>
    <field editable="1" name="minimum_sim_time_step"/>
    <field editable="1" name="name"/>
    <field editable="1" name="nr_timesteps"/>
    <field editable="1" name="numerical_settings_id"/>
    <field editable="1" name="output_time_step"/>
    <field editable="1" name="sim_time_step"/>
    <field editable="1" name="simple_infiltration_settings_id"/>
    <field editable="1" name="start_date"/>
    <field editable="1" name="start_time"/>
    <field editable="1" name="table_step_size"/>
    <field editable="1" name="table_step_size_1d"/>
    <field editable="1" name="table_step_size_volume_2d"/>
    <field editable="1" name="timestep_plus"/>
    <field editable="1" name="use_0d_inflow"/>
    <field editable="1" name="use_1d_flow"/>
    <field editable="1" name="use_2d_flow"/>
    <field editable="1" name="use_2d_rain"/>
    <field editable="1" name="water_level_ini_type"/>
    <field editable="1" name="wind_shielding_file"/>
  </editable>
  <labelOnTop>
    <field labelOnTop="0" name="advection_1d"/>
    <field labelOnTop="0" name="advection_2d"/>
    <field labelOnTop="0" name="control_group_id"/>
    <field labelOnTop="0" name="dem_file"/>
    <field labelOnTop="0" name="dem_obstacle_detection"/>
    <field labelOnTop="0" name="dem_obstacle_height"/>
    <field labelOnTop="0" name="dist_calc_points"/>
    <field labelOnTop="0" name="embedded_cutoff_threshold"/>
    <field labelOnTop="0" name="epsg_code"/>
    <field labelOnTop="0" name="flooding_threshold"/>
    <field labelOnTop="0" name="frict_avg"/>
    <field labelOnTop="0" name="frict_coef"/>
    <field labelOnTop="0" name="frict_coef_file"/>
    <field labelOnTop="0" name="frict_type"/>
    <field labelOnTop="0" name="grid_space"/>
    <field labelOnTop="0" name="groundwater_settings_id"/>
    <field labelOnTop="0" name="guess_dams"/>
    <field labelOnTop="0" name="id"/>
    <field labelOnTop="0" name="initial_groundwater_level"/>
    <field labelOnTop="0" name="initial_groundwater_level_file"/>
    <field labelOnTop="0" name="initial_groundwater_level_type"/>
    <field labelOnTop="0" name="initial_waterlevel"/>
    <field labelOnTop="0" name="initial_waterlevel_file"/>
    <field labelOnTop="0" name="interception_file"/>
    <field labelOnTop="0" name="interception_global"/>
    <field labelOnTop="0" name="interflow_settings_id"/>
    <field labelOnTop="0" name="kmax"/>
    <field labelOnTop="0" name="manhole_storage_area"/>
    <field labelOnTop="0" name="max_angle_1d_advection"/>
    <field labelOnTop="0" name="max_interception"/>
    <field labelOnTop="0" name="max_interception_file"/>
    <field labelOnTop="0" name="maximum_sim_time_step"/>
    <field labelOnTop="0" name="minimum_sim_time_step"/>
    <field labelOnTop="0" name="name"/>
    <field labelOnTop="0" name="nr_timesteps"/>
    <field labelOnTop="0" name="numerical_settings_id"/>
    <field labelOnTop="0" name="output_time_step"/>
    <field labelOnTop="0" name="sim_time_step"/>
    <field labelOnTop="0" name="simple_infiltration_settings_id"/>
    <field labelOnTop="0" name="start_date"/>
    <field labelOnTop="0" name="start_time"/>
    <field labelOnTop="0" name="table_step_size"/>
    <field labelOnTop="0" name="table_step_size_1d"/>
    <field labelOnTop="0" name="table_step_size_volume_2d"/>
    <field labelOnTop="0" name="timestep_plus"/>
    <field labelOnTop="0" name="use_0d_inflow"/>
    <field labelOnTop="0" name="use_1d_flow"/>
    <field labelOnTop="0" name="use_2d_flow"/>
    <field labelOnTop="0" name="use_2d_rain"/>
    <field labelOnTop="0" name="water_level_ini_type"/>
    <field labelOnTop="0" name="wind_shielding_file"/>
  </labelOnTop>
  <dataDefinedFieldProperties/>
  <widgets/>
  <previewExpression>id</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>4</layerGeometryType>
</qgis>
