# %%
from deploy_plugin_across_users import deploy, get_users

# PLUGINS_DIR = r"c://Users//{user}//AppData//Roaming//3Di//QGIS3//profiles//default//python//plugins" # noqa
# plugins_dir = PLUGINS_DIR
# from pathlib import Path
# users = get_users()
# for user in users:
#         print(f"checking user '{user}'")
#         user_plugins_dir = Path(plugins_dir.format(user=user))
#         if user_plugins_dir.parent.is_dir():
#                 print(user)
deploy(admin_user="wvangerwen",
        plugins = ["hhnk_threedi_plugin", "ThreeDiToolbox", "valuetool", "pdokservicesplugin"], 
        users = [],
        users_ignored = [],
        files_ignored = ["local_settings.py", "api_key.txt"],
        )
        

