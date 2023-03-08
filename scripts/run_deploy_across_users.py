# %%
from deploy_across_users import deploy


deploy(admin_user="wvangerwen",
        plugins = ["hhnk_threedi_plugin", "ThreeDiToolbox", "valuetool", "pdokservicesplugin"], 
        users = ["wvanesse"],
        users_ignored = [],
        files_ignored = ["local_settings.py", "api_key.txt"],
        )
        

