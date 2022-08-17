<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis maxScale="0" simplifyMaxScale="1" version="3.16.11-Hannover" hasScaleBasedVisibilityFlag="0" simplifyDrawingHints="1" simplifyDrawingTol="1" simplifyAlgorithm="0" readOnly="0" labelsEnabled="1" minScale="100000000" styleCategories="AllStyleCategories" simplifyLocal="1">
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
  <renderer-v2 type="RuleRenderer" forceraster="0" enableorderby="0" symbollevels="0">
    <rules key="{bef43233-0619-423c-900d-bfeb0a8a73cf}">
      <rule symbol="0" key="{99131f69-5bbf-405c-a13f-84f7c760625f}" filter="&quot;CATEGORIEOPPWATERLICHAAM&quot; = 1" label="Primair"/>
      <rule symbol="1" key="{c8b99524-7f66-417b-bfea-b87020a0dc90}" scalemaxdenom="25001" filter="&quot;CATEGORIEOPPWATERLICHAAM&quot; = 2" label="Secundair"/>
      <rule symbol="2" key="{de5affb4-df54-4288-92ce-952491b85d83}" scalemaxdenom="25001" filter="&quot;CATEGORIEOPPWATERLICHAAM&quot; IN (3,99)" label="Tertiair/overig"/>
    </rules>
    <symbols>
      <symbol type="line" name="0" clip_to_extent="1" force_rhr="0" alpha="1">
        <layer enabled="1" class="SimpleLine" locked="0" pass="0">
          <prop k="align_dash_pattern" v="0"/>
          <prop k="capstyle" v="square"/>
          <prop k="customdash" v="5;2"/>
          <prop k="customdash_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="customdash_unit" v="MM"/>
          <prop k="dash_pattern_offset" v="0"/>
          <prop k="dash_pattern_offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="dash_pattern_offset_unit" v="MM"/>
          <prop k="draw_inside_polygon" v="0"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="line_color" v="1,13,255,255"/>
          <prop k="line_style" v="solid"/>
          <prop k="line_width" v="0.86"/>
          <prop k="line_width_unit" v="MM"/>
          <prop k="offset" v="0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="ring_filter" v="0"/>
          <prop k="tweak_dash_pattern_on_corners" v="0"/>
          <prop k="use_custom_dash" v="0"/>
          <prop k="width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol type="line" name="1" clip_to_extent="1" force_rhr="0" alpha="1">
        <layer enabled="1" class="SimpleLine" locked="0" pass="0">
          <prop k="align_dash_pattern" v="0"/>
          <prop k="capstyle" v="square"/>
          <prop k="customdash" v="5;2"/>
          <prop k="customdash_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="customdash_unit" v="MM"/>
          <prop k="dash_pattern_offset" v="0"/>
          <prop k="dash_pattern_offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="dash_pattern_offset_unit" v="MM"/>
          <prop k="draw_inside_polygon" v="0"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="line_color" v="51,129,212,255"/>
          <prop k="line_style" v="solid"/>
          <prop k="line_width" v="0.66"/>
          <prop k="line_width_unit" v="MM"/>
          <prop k="offset" v="0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="ring_filter" v="0"/>
          <prop k="tweak_dash_pattern_on_corners" v="0"/>
          <prop k="use_custom_dash" v="0"/>
          <prop k="width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol type="line" name="2" clip_to_extent="1" force_rhr="0" alpha="1">
        <layer enabled="1" class="SimpleLine" locked="0" pass="0">
          <prop k="align_dash_pattern" v="0"/>
          <prop k="capstyle" v="square"/>
          <prop k="customdash" v="5;2"/>
          <prop k="customdash_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="customdash_unit" v="MM"/>
          <prop k="dash_pattern_offset" v="0"/>
          <prop k="dash_pattern_offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="dash_pattern_offset_unit" v="MM"/>
          <prop k="draw_inside_polygon" v="0"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="line_color" v="81,212,125,255"/>
          <prop k="line_style" v="solid"/>
          <prop k="line_width" v="0.26"/>
          <prop k="line_width_unit" v="MM"/>
          <prop k="offset" v="0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="ring_filter" v="0"/>
          <prop k="tweak_dash_pattern_on_corners" v="0"/>
          <prop k="use_custom_dash" v="0"/>
          <prop k="width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </symbols>
  </renderer-v2>
  <customproperties>
    <property key="embeddedWidgets/count" value="0"/>
    <property key="variableNames"/>
    <property key="variableValues"/>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <SingleCategoryDiagramRenderer attributeLegend="1" diagramType="Histogram">
    <DiagramCategory lineSizeType="MM" height="15" opacity="1" enabled="0" penAlpha="255" sizeScale="3x:0,0,0,0,0,0" minScaleDenominator="inf" spacing="0" spacingUnit="MM" scaleBasedVisibility="0" backgroundAlpha="255" maxScaleDenominator="1e+08" labelPlacementMethod="XHeight" penWidth="0" scaleDependency="Area" direction="1" penColor="#000000" backgroundColor="#ffffff" spacingUnitScale="3x:0,0,0,0,0,0" width="15" minimumSize="0" diagramOrientation="Up" lineSizeScale="3x:0,0,0,0,0,0" showAxis="0" sizeType="MM" rotationOffset="270" barWidth="5">
      <fontProperties style="" description="MS Shell Dlg 2,7.5,-1,5,50,0,0,0,0,0"/>
      <attribute color="#000000" field="" label=""/>
      <axisSymbol>
        <symbol type="line" name="" clip_to_extent="1" force_rhr="0" alpha="1">
          <layer enabled="1" class="SimpleLine" locked="0" pass="0">
            <prop k="align_dash_pattern" v="0"/>
            <prop k="capstyle" v="square"/>
            <prop k="customdash" v="5;2"/>
            <prop k="customdash_map_unit_scale" v="3x:0,0,0,0,0,0"/>
            <prop k="customdash_unit" v="MM"/>
            <prop k="dash_pattern_offset" v="0"/>
            <prop k="dash_pattern_offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
            <prop k="dash_pattern_offset_unit" v="MM"/>
            <prop k="draw_inside_polygon" v="0"/>
            <prop k="joinstyle" v="bevel"/>
            <prop k="line_color" v="35,35,35,255"/>
            <prop k="line_style" v="solid"/>
            <prop k="line_width" v="0.26"/>
            <prop k="line_width_unit" v="MM"/>
            <prop k="offset" v="0"/>
            <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
            <prop k="offset_unit" v="MM"/>
            <prop k="ring_filter" v="0"/>
            <prop k="tweak_dash_pattern_on_corners" v="0"/>
            <prop k="use_custom_dash" v="0"/>
            <prop k="width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
            <data_defined_properties>
              <Option type="Map">
                <Option type="QString" name="name" value=""/>
                <Option name="properties"/>
                <Option type="QString" name="type" value="collection"/>
              </Option>
            </data_defined_properties>
          </layer>
        </symbol>
      </axisSymbol>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings zIndex="0" showAll="1" obstacle="0" priority="0" placement="2" linePlacementFlags="10" dist="0">
    <properties>
      <Option type="Map">
        <Option type="QString" name="name" value=""/>
        <Option type="Map" name="properties">
          <Option type="Map" name="show">
            <Option type="bool" name="active" value="true"/>
            <Option type="QString" name="field" value="OBJECTID"/>
            <Option type="int" name="type" value="2"/>
          </Option>
        </Option>
        <Option type="QString" name="type" value="collection"/>
      </Option>
    </properties>
  </DiagramLayerSettings>
  <geometryOptions geometryPrecision="0" removeDuplicateNodes="0">
    <activeChecks/>
    <checkConfiguration/>
  </geometryOptions>
  <legend type="default-vector"/>
  <referencedLayers/>
  <fieldConfiguration>
    <field configurationFlags="None" name="OBJECTID">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="WS_BODEMBREEDTE">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="HydroObject_ID">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="CODE">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="NAAM">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="SOORTOPPWATERKWANTITEIT">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="CATEGORIEOPPWATERLICHAAM">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="WS_BODEMHOOGTE">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="WS_TALUD_LINKS">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="WS_TALUD_RECHTS">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="WS_IN_PEILGEBIED">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="bodemhoogte_NAP">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="breedte_getabuleerd">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="hoogte_getabuleerd">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="keuze_profiel">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field configurationFlags="None" name="SHAPE_Length">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
  </fieldConfiguration>
  <aliases>
    <alias field="OBJECTID" name="" index="0"/>
    <alias field="WS_BODEMBREEDTE" name="" index="1"/>
    <alias field="HydroObject_ID" name="" index="2"/>
    <alias field="CODE" name="" index="3"/>
    <alias field="NAAM" name="" index="4"/>
    <alias field="SOORTOPPWATERKWANTITEIT" name="" index="5"/>
    <alias field="CATEGORIEOPPWATERLICHAAM" name="" index="6"/>
    <alias field="WS_BODEMHOOGTE" name="" index="7"/>
    <alias field="WS_TALUD_LINKS" name="" index="8"/>
    <alias field="WS_TALUD_RECHTS" name="" index="9"/>
    <alias field="WS_IN_PEILGEBIED" name="" index="10"/>
    <alias field="bodemhoogte_NAP" name="" index="11"/>
    <alias field="breedte_getabuleerd" name="" index="12"/>
    <alias field="hoogte_getabuleerd" name="" index="13"/>
    <alias field="keuze_profiel" name="" index="14"/>
    <alias field="SHAPE_Length" name="" index="15"/>
  </aliases>
  <defaults>
    <default applyOnUpdate="0" field="OBJECTID" expression=""/>
    <default applyOnUpdate="0" field="WS_BODEMBREEDTE" expression=""/>
    <default applyOnUpdate="0" field="HydroObject_ID" expression=""/>
    <default applyOnUpdate="0" field="CODE" expression=""/>
    <default applyOnUpdate="0" field="NAAM" expression=""/>
    <default applyOnUpdate="0" field="SOORTOPPWATERKWANTITEIT" expression=""/>
    <default applyOnUpdate="0" field="CATEGORIEOPPWATERLICHAAM" expression=""/>
    <default applyOnUpdate="0" field="WS_BODEMHOOGTE" expression=""/>
    <default applyOnUpdate="0" field="WS_TALUD_LINKS" expression=""/>
    <default applyOnUpdate="0" field="WS_TALUD_RECHTS" expression=""/>
    <default applyOnUpdate="0" field="WS_IN_PEILGEBIED" expression=""/>
    <default applyOnUpdate="0" field="bodemhoogte_NAP" expression=""/>
    <default applyOnUpdate="0" field="breedte_getabuleerd" expression=""/>
    <default applyOnUpdate="0" field="hoogte_getabuleerd" expression=""/>
    <default applyOnUpdate="0" field="keuze_profiel" expression=""/>
    <default applyOnUpdate="0" field="SHAPE_Length" expression=""/>
  </defaults>
  <constraints>
    <constraint unique_strength="1" constraints="3" field="OBJECTID" exp_strength="0" notnull_strength="1"/>
    <constraint unique_strength="0" constraints="0" field="WS_BODEMBREEDTE" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="HydroObject_ID" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="CODE" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="NAAM" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="SOORTOPPWATERKWANTITEIT" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="CATEGORIEOPPWATERLICHAAM" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="WS_BODEMHOOGTE" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="WS_TALUD_LINKS" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="WS_TALUD_RECHTS" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="WS_IN_PEILGEBIED" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="bodemhoogte_NAP" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="breedte_getabuleerd" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="hoogte_getabuleerd" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="keuze_profiel" exp_strength="0" notnull_strength="0"/>
    <constraint unique_strength="0" constraints="0" field="SHAPE_Length" exp_strength="0" notnull_strength="0"/>
  </constraints>
  <constraintExpressions>
    <constraint field="OBJECTID" exp="" desc=""/>
    <constraint field="WS_BODEMBREEDTE" exp="" desc=""/>
    <constraint field="HydroObject_ID" exp="" desc=""/>
    <constraint field="CODE" exp="" desc=""/>
    <constraint field="NAAM" exp="" desc=""/>
    <constraint field="SOORTOPPWATERKWANTITEIT" exp="" desc=""/>
    <constraint field="CATEGORIEOPPWATERLICHAAM" exp="" desc=""/>
    <constraint field="WS_BODEMHOOGTE" exp="" desc=""/>
    <constraint field="WS_TALUD_LINKS" exp="" desc=""/>
    <constraint field="WS_TALUD_RECHTS" exp="" desc=""/>
    <constraint field="WS_IN_PEILGEBIED" exp="" desc=""/>
    <constraint field="bodemhoogte_NAP" exp="" desc=""/>
    <constraint field="breedte_getabuleerd" exp="" desc=""/>
    <constraint field="hoogte_getabuleerd" exp="" desc=""/>
    <constraint field="keuze_profiel" exp="" desc=""/>
    <constraint field="SHAPE_Length" exp="" desc=""/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction key="Canvas" value="{00000000-0000-0000-0000-000000000000}"/>
  </attributeactions>
  <attributetableconfig actionWidgetStyle="dropDown" sortExpression="" sortOrder="0">
    <columns>
      <column type="field" name="OBJECTID" width="-1" hidden="0"/>
      <column type="field" name="CODE" width="-1" hidden="0"/>
      <column type="field" name="SOORTOPPWATERKWANTITEIT" width="-1" hidden="0"/>
      <column type="field" name="CATEGORIEOPPWATERLICHAAM" width="-1" hidden="0"/>
      <column type="field" name="WS_BODEMHOOGTE" width="-1" hidden="0"/>
      <column type="field" name="WS_BODEMBREEDTE" width="-1" hidden="0"/>
      <column type="field" name="WS_TALUD_LINKS" width="-1" hidden="0"/>
      <column type="field" name="WS_TALUD_RECHTS" width="-1" hidden="0"/>
      <column type="field" name="WS_IN_PEILGEBIED" width="-1" hidden="0"/>
      <column type="field" name="SHAPE_Length" width="-1" hidden="0"/>
      <column type="actions" width="-1" hidden="1"/>
    </columns>
  </attributetableconfig>
  <conditionalstyles>
    <rowstyles/>
    <fieldstyles/>
  </conditionalstyles>
  <storedexpressions/>
  <editform tolerant="1">C:/Users/chris.kerklaan/Downloads/test_protocol_v21</editform>
  <editforminit/>
  <editforminitcodesource>0</editforminitcodesource>
  <editforminitfilepath>C:/Users/chris.kerklaan/Downloads/test_protocol_v21</editforminitfilepath>
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
  <editorlayout>generatedlayout</editorlayout>
  <editable/>
  <labelOnTop/>
  <dataDefinedFieldProperties/>
  <widgets/>
  <previewExpression>COALESCE( "OBJECTID", '&lt;NULL>' )</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>1</layerGeometryType>
</qgis>
