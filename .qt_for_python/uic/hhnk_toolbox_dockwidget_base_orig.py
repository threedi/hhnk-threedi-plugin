# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\github\wvangerwen\hhnk-threedi-plugin\hhnk_threedi_plugin\hhnk_toolbox_dockwidget_base_orig.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HHNK_toolboxDockWidget(object):
    def setupUi(self, HHNK_toolboxDockWidget):
        HHNK_toolboxDockWidget.setObjectName("HHNK_toolboxDockWidget")
        HHNK_toolboxDockWidget.resize(468, 848)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(HHNK_toolboxDockWidget.sizePolicy().hasHeightForWidth())
        HHNK_toolboxDockWidget.setSizePolicy(sizePolicy)
        HHNK_toolboxDockWidget.setMinimumSize(QtCore.QSize(205, 534))
        HHNK_toolboxDockWidget.setMaximumSize(QtCore.QSize(524287, 524287))
        HHNK_toolboxDockWidget.setBaseSize(QtCore.QSize(0, 0))
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setMinimumSize(QtCore.QSize(0, 0))
        self.dockWidgetContents.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.select_polder_label = QtWidgets.QLabel(self.dockWidgetContents)
        self.select_polder_label.setObjectName("select_polder_label")
        self.verticalLayout.addWidget(self.select_polder_label)
        self.polder_selector = QgsFileWidget(self.dockWidgetContents)
        self.polder_selector.setStorageMode(QgsFileWidget.GetDirectory)
        self.polder_selector.setObjectName("polder_selector")
        self.verticalLayout.addWidget(self.polder_selector)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.create_new_project_btn = QtWidgets.QPushButton(self.dockWidgetContents)
        self.create_new_project_btn.setObjectName("create_new_project_btn")
        self.verticalLayout.addWidget(self.create_new_project_btn)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.load_layers_btn = QtWidgets.QPushButton(self.dockWidgetContents)
        self.load_layers_btn.setObjectName("load_layers_btn")
        self.verticalLayout.addWidget(self.load_layers_btn)
        spacerItem2 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem2)
        self.model_state_label = QtWidgets.QLabel(self.dockWidgetContents)
        self.model_state_label.setObjectName("model_state_label")
        self.verticalLayout.addWidget(self.model_state_label)
        self.model_state_show = QtWidgets.QLabel(self.dockWidgetContents)
        self.model_state_show.setObjectName("model_state_show")
        self.verticalLayout.addWidget(self.model_state_show)
        self.model_state_btn = QtWidgets.QPushButton(self.dockWidgetContents)
        self.model_state_btn.setEnabled(False)
        self.model_state_btn.setObjectName("model_state_btn")
        self.verticalLayout.addWidget(self.model_state_btn)
        spacerItem3 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem3)
        self.lizard_api_key_textbox = QtWidgets.QLineEdit(self.dockWidgetContents)
        self.lizard_api_key_textbox.setObjectName("lizard_api_key_textbox")
        self.verticalLayout.addWidget(self.lizard_api_key_textbox)
        self.server_btn = QtWidgets.QPushButton(self.dockWidgetContents)
        self.server_btn.setObjectName("server_btn")
        self.verticalLayout.addWidget(self.server_btn)
        self.tests_toolbox = QtWidgets.QToolBox(self.dockWidgetContents)
        self.tests_toolbox.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tests_toolbox.sizePolicy().hasHeightForWidth())
        self.tests_toolbox.setSizePolicy(sizePolicy)
        self.tests_toolbox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tests_toolbox.setObjectName("tests_toolbox")
        self.sqlite_tests = QtWidgets.QWidget()
        self.sqlite_tests.setGeometry(QtCore.QRect(0, 0, 446, 399))
        self.sqlite_tests.setMinimumSize(QtCore.QSize(125, 0))
        self.sqlite_tests.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.sqlite_tests.setObjectName("sqlite_tests")
        self.gridLayout = QtWidgets.QGridLayout(self.sqlite_tests)
        self.gridLayout.setObjectName("gridLayout")
        self.sqlite_checks_frame = QtWidgets.QFrame(self.sqlite_tests)
        self.sqlite_checks_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.sqlite_checks_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.sqlite_checks_frame.setLineWidth(0)
        self.sqlite_checks_frame.setObjectName("sqlite_checks_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.sqlite_checks_frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.start_sqlite_check = QtWidgets.QPushButton(self.sqlite_checks_frame)
        self.start_sqlite_check.setMaximumSize(QtCore.QSize(16777215, 23))
        self.start_sqlite_check.setObjectName("start_sqlite_check")
        self.verticalLayout_2.addWidget(self.start_sqlite_check)
        self.gridLayout.addWidget(self.sqlite_checks_frame, 0, 0, 1, 1, QtCore.Qt.AlignTop)
        self.tests_toolbox.addItem(self.sqlite_tests, "")
        self.verticalLayout.addWidget(self.tests_toolbox)
        HHNK_toolboxDockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(HHNK_toolboxDockWidget)
        self.tests_toolbox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(HHNK_toolboxDockWidget)

    def retranslateUi(self, HHNK_toolboxDockWidget):
        _translate = QtCore.QCoreApplication.translate
        HHNK_toolboxDockWidget.setWindowTitle(_translate("HHNK_toolboxDockWidget", "HHNK Toolbox"))
        self.select_polder_label.setText(_translate("HHNK_toolboxDockWidget", "Selecteer een polder"))
        self.polder_selector.setDialogTitle(_translate("HHNK_toolboxDockWidget", "Selecteer polder map"))
        self.create_new_project_btn.setText(_translate("HHNK_toolboxDockWidget", "Nieuw project aanmaken"))
        self.load_layers_btn.setText(_translate("HHNK_toolboxDockWidget", "Laad lagen"))
        self.model_state_label.setText(_translate("HHNK_toolboxDockWidget", "Huidige modelstaat:"))
        self.model_state_show.setText(_translate("HHNK_toolboxDockWidget", "Onbekend"))
        self.model_state_btn.setText(_translate("HHNK_toolboxDockWidget", "Modelstaat aanpassen"))
        self.lizard_api_key_textbox.setText(_translate("HHNK_toolboxDockWidget", "Vul hier je Lizard API key in!"))
        self.server_btn.setText(_translate("HHNK_toolboxDockWidget", "Open Jupyter Notebook Server"))
        self.start_sqlite_check.setText(_translate("HHNK_toolboxDockWidget", "Sqlite tests"))
        self.tests_toolbox.setItemText(self.tests_toolbox.indexOf(self.sqlite_tests), _translate("HHNK_toolboxDockWidget", "Sqlite tests"))

from qgsfilewidget import QgsFileWidget