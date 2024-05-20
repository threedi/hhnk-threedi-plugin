# rename to local_settings.py
import os

DEBUG = False

threeditoolbox_path = os.path.join(
    os.getenv("APPDATA"), r"3Di\QGIS3\profiles\default\python\plugins\threedi_results_analysis\deps"
)

project_path = None
