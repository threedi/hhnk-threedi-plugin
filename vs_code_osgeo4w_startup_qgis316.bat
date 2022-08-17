@echo off

REM Vul hier het pad naar de OSGeo4W installatie in
set OSGEO4W_ROOT=C:\OSGeo4W64

REM Vul hier het pad naar de visual studio code executable in
set VSCODE="C:\Program Files\Microsoft VS Code Insiders\Code - Insiders.exe"

call "%OSGEO4W_ROOT%\bin\o4w_env.bat"
call "%OSGEO4W_ROOT%\bin\qt5_env.bat"
call "%OSGEO4W_ROOT%\bin\py3_env.bat"

path %OSGEO4W_ROOT%\apps\qgis-ltr\bin;%PATH%
path C:\Program Files\7-Zip;%PATH% 
set QGIS_PREFIX_PATH=%OSGEO4W_ROOT%\apps\qgis-ltr

set GDAL_FILENAME_IS_UTF8=YES

set VSI_CACHE=TRUE
set VSI_CACHE_SIZE=1000000
set QT_PLUGIN_PATH=%OSGEO4W_ROOT%\apps\qgis-ltr\qtplugins;%OSGEO4W_ROOT%\apps\Qt5\plugins

set PYTHONHOME=%OSGEO4W_ROOT%\apps\Python37

set PYTHONPATH=%appdata%\QGIS\QGIS3\profiles\default\python
set PYTHONPATH=%appdata%\QGIS\QGIS3\profiles\default\python\plugins\hhnk_threedi_toolbox\external-dependencies;%PYTHONPATH%
set PYTHONPATH=%OSGEO4W_ROOT%\apps\Python37\Scripts;%PYTHONPATH%
set PYTHONPATH=%OSGEO4W_ROOT%\apps\qgis-ltr\python;%PYTHONPATH%

set QT_QPA_PLATFORM_PLUGIN_PATH=%OSGEO4W_ROOT%\apps\Qt5\plugins\platforms

start "VSCode aware of QGIS" /B %VSCODE% %*
