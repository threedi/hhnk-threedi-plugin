import os
import shutil

this_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(this_dir)
home_dir = os.path.expanduser("~")
dest_dir_plug = os.path.join(
    home_dir,
    "AppData",
    "Roaming",
    "3Di",
    "QGIS3",
    "profiles",
    "default",
    "python",
    "plugins",
    "hhnk_threedi_plugin",
)
src_dir_plug = os.path.join(parent_dir, "hhnk_threedi_plugin")
print(f"Deploying {src_dir_plug } to {dest_dir_plug}")
try:
    shutil.rmtree(dest_dir_plug)
except OSError:
    pass  # directory not present at all
shutil.copytree(src_dir_plug, dest_dir_plug)