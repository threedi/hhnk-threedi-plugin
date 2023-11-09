from PyQt5.QtWidgets import QApplication


def update_button_background(button, color=None):
    if color is None:
        # reset button to default style
        button.setStyleSheet(f"QPushButton")
    else:
        button.setStyleSheet(f"QPushButton {'{'}background-color: {color}; color:black{'}'}")
    QApplication.processEvents()
