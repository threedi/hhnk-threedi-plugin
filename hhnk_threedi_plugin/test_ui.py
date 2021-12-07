from hhnk_threedi_tools.folder_structure_and_paths import build_base_paths_dict as p

a = p.build_base_paths_dict(
    r"G:\\02_Werkplaatsen\\06_HYD\\Projecten\\HKC16015 Wateropgave 2.0\\07.Poldermodellen_nieuwe_stijl\\model_test1"
)


from gui.load_layers_popup import loadLayersDialog
from PyQt5.QtWidgets import QMenu, QApplication, QWidget, QVBoxLayout
import sys


def main():
    app = QApplication(sys.argv)
    w = loadLayersDialog(None, None)
    w.show()
    w.set_current_paths()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()


print("hi")
