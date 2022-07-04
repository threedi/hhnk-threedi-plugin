@echo off

REM Vul hier het pad naar de OSGeo4W installatie in
set OSGEO4W_ROOT=C:\OSGeo4W

REM Vul hier het pad naar de visual studio code executable in
set VSCODE="C:\Program Files\Microsoft VS Code Insiders\Code - Insiders.exe"

call "%OSGEO4W_ROOT%\bin\o4w_env.bat"
REM call "%~dp0\o4w_env.bat"

path %OSGEO4W_ROOT%\apps\qgis-ltr\bin;%PATH%
path C:\Program Files\7-Zip;%PATH% 

set QGIS_PREFIX_PATH=%OSGEO4W_ROOT:\=/%/apps/qgis-ltr
set GDAL_FILENAME_IS_UTF8=YES
set USE_PATH_FOR_GDAL_PYTHON=YES

rem Set VSI cache to be used as buffer, see #6448
set VSI_CACHE=TRUE
set VSI_CACHE_SIZE=1000000
set QT_PLUGIN_PATH=%OSGEO4W_ROOT%\apps\qgis-ltr\qtplugins;%OSGEO4W_ROOT%\apps\qt5\plugins

SET PYTHONHOME=%OSGEO4W_ROOT%\apps\Python39
SET PYTHONPATH=%PYTHONHOME%;%PYTHONHOME%\Scripts
PATH %PYTHONPATH%;%PATH%


set PYTHONPATH=%appdata%\QGIS\QGIS3\profiles\default\python
set PYTHONPATH=%appdata%\QGIS\QGIS3\profiles\default\python\plugins\hhnk_threedi_toolbox\external-dependencies;%PYTHONPATH%
set PYTHONPATH=%OSGEO4W_ROOT%\apps\qgis-ltr\python;%PYTHONPATH%

path %OSGEO4W_ROOT%\apps\qt5\bin;%PATH%

set O4W_QT_PREFIX=%OSGEO4W_ROOT:\=/%/apps/Qt5
set O4W_QT_BINARIES=%OSGEO4W_ROOT:\=/%/apps/Qt5/bin
set O4W_QT_PLUGINS=%OSGEO4W_ROOT:\=/%/apps/Qt5/plugins
set O4W_QT_LIBRARIES=%OSGEO4W_ROOT:\=/%/apps/Qt5/lib
set O4W_QT_TRANSLATIONS=%OSGEO4W_ROOT:\=/%/apps/Qt5/translations
set O4W_QT_HEADERS=%OSGEO4W_ROOT:\=/%/apps/Qt5/include
set O4W_QT_DOC=%OSGEO4W_ROOT:\=/%/apps/Qt5/doc

set QT_QPA_PLATFORM_PLUGIN_PATH=%OSGEO4W_ROOT%\apps\Qt5\plugins\platforms


start "VSCode aware of QGIS" /B %VSCODE% %*



