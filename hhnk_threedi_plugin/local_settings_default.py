#rename to local_settings.py
import os 

DEBUG=True

hhnk_threedi_tools_path = None
threeditoolbox_path = os.path.join(os.getenv('APPDATA'), r'3Di\QGIS3\profiles\default\python\plugins\ThreeDiToolbox\deps')

project_path = None