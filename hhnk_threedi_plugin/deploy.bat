
@REM deploy plugin to appdata
pb_tool compile

SET PLUGIN_PATH=%appdata%\3Di\QGIS3\profiles\default\python\plugins

xcopy . %PLUGIN_PATH%\hhnk_threedi_plugin\ /EXCLUDE:exclude_copy.txt/E/q

copy %PLUGIN_PATH%\api_key\api_key.txt %PLUGIN_PATH%\hhnk_threedi_plugin\api_key.txt

@REM https://stackoverflow.com/questions/35988863/using-command-line-batch-to-switch-to-focus-on-app
@REM  Open qgis (needs to be empty project. Then press ctrl+r to reload.)
@REM cannot seem to find out how wildcards work. So we use a couple options how the window is called.
%@Try%
  call sendkeys.bat "*Untitled" "^r" 
%@EndTry%
:@Catch
  call sendkeys.bat "Untitled" "^r" 
:@EndCatch
:@Catch
  call sendkeys.bat "QGIS" "^r" 
:@EndCatch


