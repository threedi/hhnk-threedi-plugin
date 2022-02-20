from PyQt5.QtWidgets import (
    QPushButton,
    QTreeWidget,
    QTreeWidgetItem,
    QVBoxLayout,
    QTreeView,
    QWidget,
)
from PyQt5.QtCore import pyqtSignal


class SectionExpandButton(QPushButton):
    """
    a QPushbutton that can expand or collapse its section
    """

    def __init__(self, item, text="", parent=None):
        super().__init__(text, parent)
        self.setStyleSheet(
            "background-color: #a6a9ad; text-align: left; padding: 5px 10px 5px 10px"
        )
        self.section = item
        self.section.setExpanded(True)
        self.clicked.connect(self.on_clicked)

    def on_clicked(self):
        """
        toggle expand/collapse of section by clicking
        """
        if self.section.isExpanded():
            self.section.setExpanded(False)
        else:
            self.section.setExpanded(True)


class collapsibleTree(QWidget):
    """
    Widget to which collapsible sections can be added
    """

    sections_changed = pyqtSignal()

    def __init__(self, parent=None):
        super(collapsibleTree, self).__init__(parent)
        layout = QVBoxLayout()
        self.tree = QTreeWidget()
        self.tree.setHeaderHidden(True)
        self.tree.setIndentation(0)
        self.tree.setVerticalScrollMode(QTreeView.ScrollPerPixel)
        layout.addWidget(self.tree)
        self.setLayout(layout)
        self.sections = []
        if not self.sections:
            self.setHidden(True)
        self.sections_changed.connect(self.adjust_visibility)

    def adjust_visibility(self):
        if not self.sections:
            self.setHidden(True)
        else:
            self.setHidden(False)

    def add_section(self, title, widget):
        """
        adds collapsible section. Checks if section by the specified title
        already exists and removes is first if so
        """
        self.remove_section(title)
        button1 = self.add_button(title)
        section1 = self.add_widget(button1, widget)
        button1.addChild(section1)
        self.sections_changed.emit()

    def add_button(self, title):
        """creates a QTreeWidgetItem containing a button
        to expand or collapse its section
        """
        item = QTreeWidgetItem()
        self.sections.append((title, item))
        self.tree.addTopLevelItem(item)
        self.tree.setItemWidget(item, 0, SectionExpandButton(item, text=title))
        return item

    def add_widget(self, button, widget):
        """
        creates a QWidgetItem containing the widget,
        as child of the button-QWidgetItem
        """
        section = QTreeWidgetItem(button)
        section.setDisabled(True)
        self.tree.setItemWidget(section, 0, widget)
        return section

    def remove_section(self, title):
        """
        finds section by title and removes it from widget
        and sections
        """
        for item in self.sections:
            if item[0] == title:
                self.tree.takeTopLevelItem(self.tree.indexOfTopLevelItem(item[1]))
                self.sections.remove(item)
                break
        self.sections_changed.emit()
