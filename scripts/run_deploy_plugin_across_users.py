# %%
import os
from pathlib import Path

from deploy_plugin_across_users import deploy, get_users

PLUGINS_DIR = r"c://Users//{user}//AppData//Roaming//3Di//QGIS3//profiles//default//python//plugins"  # noqa
plugins_dir = PLUGINS_DIR
# from pathlib import Path


def select_users(plugin_name="hhnk_threedi_plugin"):
    """Get users that have a plugin installed."""
    users = get_users()
    selected_users = []

    for user in users:
        try:
            print(f"checking user '{user}'")
            user_plugins_dir = Path(plugins_dir.format(user=user))
            if user_plugins_dir.parent.is_dir():
                if len([i for i in user_plugins_dir.glob(f"*{plugin_name}")]) == 1:
                    selected_users.append(user)
        except:
            pass
    return selected_users


# %% HHNK-THREEDI-PLUGIN %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

selected_users = select_users("hhnk_threedi_plugin")

print("\nSelected users:")
print(selected_users)


# %%
deploy(
    admin_user="wvangerwen",
    plugins=[
        "hhnk_threedi_plugin",
        "threedi_results_analysis",
        "threedi_models_and_simulations",
        "threedi_schematisation_editor",
    ],
    users=selected_users,
    users_ignored=[],
    files_ignored=["local_settings.py", "api_key.txt"],
)


# %% LEGGERTOOL %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

selected_users = select_users("legger")
print(selected_users)

# %%

deploy(
    admin_user="wvangerwen",
    plugins=[
        "legger",
    ],
    users=selected_users,
    users_ignored=[],
    files_ignored=["local_settings.py", "api_key.txt"],
)
