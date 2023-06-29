# %%
from deploy_plugin_across_users import deploy, get_users
from pathlib import Path
import os

PLUGINS_DIR = r"c://Users//{user}//AppData//Roaming//3Di//QGIS3//profiles//default//python//plugins" # noqa
plugins_dir = PLUGINS_DIR
# from pathlib import Path
users = get_users()

selected_users = []
for user in users:
        try:
                print(f"checking user '{user}'")
                user_plugins_dir = Path(plugins_dir.format(user=user))
                if user_plugins_dir.parent.is_dir():
                        if len([i for i in user_plugins_dir.glob("*hhnk_threedi_plugin")]) == 1:
                                selected_users.append(user)
        except:
                pass

print("\nSelected users:")
print(selected_users)
# %%
deploy(admin_user="wvangerwen",
        plugins = ["hhnk_threedi_plugin", "ThreeDiToolbox"], 
        users = selected_users,
        users_ignored = [],
        files_ignored = ["local_settings.py", "api_key.txt"],
        )
# %%
