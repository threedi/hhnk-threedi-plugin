@echo off

REM Vul hier het pad naar de OSGeo4W installatie in
@REM set OSGEO4W_ROOT=C:\OSGeo4W
set OSGEO4W_ROOT=%ProgramFiles%\3DiModellerInterface 3.34

REM Vul hier het pad naar de visual studio code executable in
set VSCODE="C:\Program Files\Microsoft VS Code Insiders\Code - Insiders.exe"

call "%OSGEO4W_ROOT%\bin\o4w_env.bat"
REM call "%~dp0\o4w_env.bat"

@REM path %OSGEO4W_ROOT%\apps\qgis-ltr\bin;%PATH% 
path %ProgramFiles%\7-Zip;%PATH% 

set QGIS_PREFIX_PATH=%OSGEO4W_ROOT:\=/%/apps/qgis-ltr
set GDAL_FILENAME_IS_UTF8=YES
set USE_PATH_FOR_GDAL_PYTHON=YES

rem Set VSI cache to be used as buffer, see #6448
set VSI_CACHE=TRUE
set VSI_CACHE_SIZE=1000000
set QT_PLUGIN_PATH=%OSGEO4W_ROOT%\apps\qgis-ltr\qtplugins;%OSGEO4W_ROOT%\apps\qt5\plugins


@REM set PYTHONHOME=%OSGEO4W_ROOT%\apps\Python39
@REM set PYTHONPATH=%PYTHONHOME%;%PYTHONHOME%\Scripts
set PYTHONPATH=%PYTHONPATH%;%OSGEO4W_ROOT%\bin
set PYTHONPATH=%PYTHONPATH%;%PYTHONHOME%\DLLs

set QGIS_APPDATA_DIR=3Di
set PYTHONPATH=%PYTHONPATH%;%appdata%\%QGIS_APPDATA_DIR%\QGIS3\profiles\default\python
set PYTHONPATH=%PYTHONPATH%;%appdata%\%QGIS_APPDATA_DIR%\QGIS3\profiles\default\python\plugins\hhnk_threedi_plugin\external-dependencies
@REM set PYTHONPATH=%PYTHONPATH%;%OSGEO4W_ROOT%\apps\qgis-ltr\python
set PYTHONPATH=%PYTHONPATH%;%appdata%\%QGIS_APPDATA_DIR%\QGIS3\profiles\default\python\plugins\threedi_results_analysis\deps
set PYTHONPATH=%PYTHONPATH%;%appdata%\Python\Python39
set PYTHONPATH=%PYTHONPATH%;%appdata%\Python\Python39\Scripts

path %PATH%;%PYTHONPATH%

REM below is called in from o4w_env.bat - "C:\Program Files\3DiModellerInterface 3.22\etc\ini\qt5.bat"
@REM path %OSGEO4W_ROOT%\apps\qt5\bin;%PATH%

@REM set O4W_QT_PREFIX=%OSGEO4W_ROOT:\=/%/apps/Qt5
@REM set O4W_QT_BINARIES=%OSGEO4W_ROOT:\=/%/apps/Qt5/bin
@REM set O4W_QT_PLUGINS=%OSGEO4W_ROOT:\=/%/apps/Qt5/plugins
@REM set O4W_QT_LIBRARIES=%OSGEO4W_ROOT:\=/%/apps/Qt5/lib
@REM set O4W_QT_TRANSLATIONS=%OSGEO4W_ROOT:\=/%/apps/Qt5/translations
@REM set O4W_QT_HEADERS=%OSGEO4W_ROOT:\=/%/apps/Qt5/include
@REM set O4W_QT_DOC=%OSGEO4W_ROOT:\=/%/apps/Qt5/doc

set QT_QPA_PLATFORM_PLUGIN_PATH=%OSGEO4W_ROOT%\apps\Qt5\plugins\platforms


start "VSCode aware of QGIS" /B %VSCODE% %*



