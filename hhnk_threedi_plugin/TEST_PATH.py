# %%


osgeo_path= ['', 'C:\\PROGRA~1\\3DIMOD~1.22\\bin\\python39.zip', 'C:\\PROGRA~1\\3DIMOD~1.22\\apps\\Python39\\DLLs', 'C:\\PROGRA~1\\3DIMOD~1.22\\apps\\Python39\\lib', 'C:\\PROGRA~1\\3DIMOD~1.22\\bin', 'C:\\PROGRA~1\\3DIMOD~1.22\\apps\\Python39', 'C:\\PROGRA~1\\3DIMOD~1.22\\apps\\Python39\\lib\\site-packages', 'C:\\PROGRA~1\\3DIMOD~1.22\\apps\\Python39\\lib\\site-packages\\GDAL-3.4.3-py3.9-win-amd64.egg', 'C:\\PROGRA~1\\3DIMOD~1.22\\apps\\Python39\\lib\\site-packages\\win32', 'C:\\PROGRA~1\\3DIMOD~1.22\\apps\\Python39\\lib\\site-packages\\win32\\lib', 'C:\\PROGRA~1\\3DIMOD~1.22\\apps\\Python39\\lib\\site-packages\\Pythonwin']

local_path = ['', 'C:\\PROGRA~1\\3DIMOD~1.22\\apps\\Python39', 'C:\\PROGRA~1\\3DIMOD~1.22\\apps\\Python39\\Scripts', 'C:\\Users\\wvangerwen\\AppData\\Roaming\\3Di\\QGIS3\\profiles\\default\\python', 'C:\\Users\\wvangerwen\\AppData\\Roaming\\3Di\\QGIS3\\profiles\\default\\python\\plugins\\hhnk_threedi_plugin\\external-dependencies', 'C:\\PROGRA~1\\3DIMOD~1.22\\apps\\qgis-ltr\\python', 'C:\\Users\\wvangerwen\\AppData\\Roaming\\3Di\\QGIS3\\profiles\\default\\python\\plugins\\ThreeDiToolbox\\deps', 'C:\\Users\\wvangerwen\\AppData\\Roaming\\Python\\Python39', 'C:\\Users\\wvangerwen\\AppData\\Roaming\\Python\\Python39\\Scripts', 'C:\\PROGRA~1\\3DIMOD~1.22\\apps\\Python39\\python39.zip', 'C:\\PROGRA~1\\3DIMOD~1.22\\apps\\Python39\\DLLs', 'C:\\PROGRA~1\\3DIMOD~1.22\\apps\\Python39\\lib', 'C:\\PROGRA~1\\3DIMOD~1.22\\apps\\Python39\\lib\\site-packages', 'C:\\PROGRA~1\\3DIMOD~1.22\\apps\\Python39\\lib\\site-packages\\GDAL-3.4.3-py3.9-win-amd64.egg', 'C:\\PROGRA~1\\3DIMOD~1.22\\apps\\Python39\\lib\\site-packages\\win32', 'C:\\PROGRA~1\\3DIMOD~1.22\\apps\\Python39\\lib\\site-packages\\win32\\lib', 'C:\\PROGRA~1\\3DIMOD~1.22\\apps\\Python39\\lib\\site-packages\\Pythonwin']


for o in osgeo_path:
    if o not in local_path:
        print(o)

# %%