from PyQt5.QtWidgets import QMessageBox


def handle_os_error(error):
    """
    Popup window that informs a user about OSErrors (i.e. file is already open or wrong permissions).

    Created so we can retry creating output rather than throwing an error and having to rerun the
    entire test.

    Returns True if user chose to retry, False if user chose cancel
    """
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setText(f"Error: {error}.\n")
    msgBox.setWindowTitle("OSError")
    msgBox.setStandardButtons(QMessageBox.Retry | QMessageBox.Cancel)
    res = msgBox.exec()
    if res == QMessageBox.Retry:
        return True
    else:
        return False
