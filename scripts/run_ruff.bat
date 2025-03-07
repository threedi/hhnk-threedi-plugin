REM force-exclude to make sure it uses the extend-exclude from pyproject.
python -m ruff check ../hhnk_threedi_plugin --select I --fix 
python -m ruff format ../hhnk_threedi_plugin --force-exclude