import os

from hhnk_threedi_plugin.dependencies import DEPENDENCY_DIR, THREEDI_DIR
from hhnk_threedi_plugin.dependencies import OUR_DIR as HHNK_THREEDI_PLUGIN_DIR
import hhnk_threedi_plugin.local_settings as local_settings
from pathlib import Path
from qgis.PyQt.QtWidgets import QAction, QMessageBox

from hhnk_threedi_tools.utils.notebooks.run import create_command_bat_file
import hhnk_threedi_tools as htt

class NotebookWidget():
    """Class to interact with the notebook widget."""
    def __init__(self, caller, parent):

        self.caller = caller
        self.parent= parent
        self.api_file = os.path.join(HHNK_THREEDI_PLUGIN_DIR, 'api_key.txt')

        self.load_api_key()


    def read_api_file(self):
        if os.path.exists(self.api_file):
            with open(self.api_file, "r") as f:
                api_key = f.readline()
            return api_key
        else:
            return None


    def load_api_key(self):
        """Load api_key from file and update textbox"""
        api_key = self.read_api_file()
        if api_key:
            self.parent.lizard_api_key_textbox.setText(api_key)


    def _check_api_key_valid(self, api_key):
        """Lizard API keys are 41 characters and have a dot in the name"""
        if len(api_key) == 41 and "." in api_key:
            return True
        else:
            return False


    def generate_notebook_valid(self):
        api_key = self.parent.lizard_api_key_textbox.text()
        if api_key == "Vul hier je Lizard API key in!":
            if os.path.exists(self.api_file):
                api_key = self.read_api_file()
                
                if api_key != '':
                    return api_key
                
            QMessageBox.warning(
                    None,
                    "Starting Jupyter server",
                    "Vul de lizard api key in, deze is niet ingevuld! Heb je deze niet? Ga naar: \nhttps://hhnk.lizard.net/management/#/personal_api_keys",
                    )
            return None
        else:
            if self._check_api_key_valid(api_key):
                # copy to api directory
                output_file = Path(self.api_file)

                if output_file.parents[2].exists(): #Does plugin dir exist.
                    if not output_file.parent.exists(): #Does api_key dir exist
                        os.mkdir(output_file.parent)
                    with open(self.api_file, "w") as f:
                        f.write(api_key)
                else:
                    print(f"{output_file.parents[2]} niet gevonden")
                    # logger.warning(f"{output_file.parents[2]} niet gevonden") # TODO hebben we een logger?
                return api_key

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
                "lizard_api_key_path": self.api_file,            
            },
        )

        notebook_paths = [str(THREEDI_DIR),str(DEPENDENCY_DIR)]
        if local_settings.hhnk_threedi_tools_path not in [None, '']:
            notebook_paths.append(local_settings.hhnk_threedi_tools_path)
        htt.add_notebook_paths(notebook_paths)
        
    def start_server(self):
        api_key = self.generate_notebook_valid()
        if not api_key:
            return
        
        self.generate_notebook_folder(api_key)
        htt.open_server(directory=self.polder_notebooks, location="user", use="run")