@REM deploy plugin to appdata
pb_tool deploy -y

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
