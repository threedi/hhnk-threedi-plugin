# %%
import os
import json
import numpy as np

if __name__ =='__main__':
    import sys
    from pathlib import Path
    sys.path.append(str(Path(os.getcwd()).parent.parent))
from hhnk_threedi_plugin.dependencies import DEPENDENCY_DIR, THREEDI_DEPENDENCY_DIR
from hhnk_threedi_plugin.dependencies import OUR_DIR as HHNK_THREEDI_PLUGIN_DIR
try: 
    import hhnk_threedi_plugin.local_settings as local_settings
except ModuleNotFoundError:
    import hhnk_threedi_plugin.local_settings_default as local_settings
from pathlib import Path
from qgis.PyQt.QtWidgets import QAction, QMessageBox

from hhnk_threedi_tools.utils.notebooks.run import create_command_bat_file
from hhnk_research_tools.threedi.read_api_file import read_api_file
import hhnk_threedi_tools as htt


# %%
class NotebookWidget():
    """Class to interact with the notebook widget."""
    def __init__(self, caller, parent):

        self.caller = caller
        self.parent= parent
        self.api_file = os.path.join(HHNK_THREEDI_PLUGIN_DIR, 'api_key.txt')

        self.load_api_key()

    def notebook_paths(self):
        notebook_paths = [str(THREEDI_DEPENDENCY_DIR),str(DEPENDENCY_DIR)]
        if local_settings.hhnk_threedi_tools_path not in [None, '']:
            notebook_paths.append(local_settings.hhnk_threedi_tools_path)
        try:     
            if local_settings.hhnk_research_tools_path not in [None, '']:
                notebook_paths.append(local_settings.hhnk_research_tools_path)
        except:
            pass
        return notebook_paths

    def load_api_key(self):
        """Load api_key from file and update textbox"""
        api_keys = read_api_file(self.api_file)
        if api_keys['lizard']:
            self.parent.lizard_api_key_textbox.setText(api_keys['lizard'])
            
        if api_keys['threedi']:
            self.parent.threedi_api_key_textbox.setText(api_keys['threedi'])

    def _check_api_key_valid(self, api_keys):
        """Lizard API keys are 41 characters and have a dot in the name"""
        return_value=[]
        for key in api_keys:
            if len(api_keys[key]) == 41 and "." in api_keys[key]:
                return_value.append(True)
            else:
                return_value.append(False)

        if np.all(return_value):
            return True
        else:
            return False


    def generate_notebook_valid(self):
        api_keys = {}
        api_keys['lizard'] = self.parent.lizard_api_key_textbox.text()
        api_keys['threedi'] = self.parent.threedi_api_key_textbox.text()

        if api_keys['lizard'] == "Vul hier je Lizard API key in!" or api_keys['threedi'] == "Vul hier je Threedi API key in!":
            if os.path.exists(self.api_file):
                api_keys = read_api_file(self.api_file)
                
                if api_keys['lizard'] != '' and api_keys['threedi'] != '':
                    return api_keys
                
            QMessageBox.warning(
                    None,
                    "Starting Jupyter server",
                    "Vul de lizard api key in, deze is niet ingevuld! Heb je deze niet? Ga naar: \nhttps://hhnk.lizard.net/management/#/personal_api_keys",
                    )
            return None
        else:
            if self._check_api_key_valid(api_keys):
                # copy to api directory
                output_file = Path(self.api_file)

                if output_file.parents[2].exists(): #Does plugin dir exist.
                    if not output_file.parent.exists(): #Does api_key dir exist
                        os.mkdir(output_file.parent)
                    with open(self.api_file, "w") as f:
                        f.write(json.dumps(api_keys))
                else:
                    print(f"{output_file.parents[2]} niet gevonden")
                    # logger.warning(f"{output_file.parents[2]} niet gevonden") # TODO hebben we een logger?
                return api_keys

            else:
                QMessageBox.warning(
                    None,
                    "Starting Jupyter server",
                    "Er is geen correcte API key ingevuld. Heb je deze niet? Ga naar: \nhttps://hhnk.lizard.net/management/#/personal_api_keys",
                    )
                return None
        

    def generate_notebook_folder(self, api_key):
        """retrieves the polder folder and loads the"""
        self.polder_notebooks = os.path.join(self.caller.polder_folder, "Notebooks")
        server_bat_file = os.path.join(self.polder_notebooks, "start_server.bat")
        htt.copy_notebooks(self.polder_notebooks)
        create_command_bat_file(server_bat_file, "user")
        htt.write_notebook_json(
            self.polder_notebooks,
            {
                "polder_folder": self.caller.polder_folder,
                "api_keys_path": self.api_file,            
            },
        )

        htt.add_notebook_paths(self.notebook_paths())
        
    def start_server(self):
        api_key = self.generate_notebook_valid()
        if not api_key:
            return
        
        self.generate_notebook_folder(api_key)
        htt.open_server(
            directory=self.polder_notebooks,
            location="user",
            use="run",
            notebook_paths=self.notebook_paths()
            )