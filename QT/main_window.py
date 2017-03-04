# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(_fromUtf8("#centralwidget{\n"
"background-color: #ff9933\n"
"}\n"
"\n"
"#NewProjectWidget, #TemperatureDisplayWidget_2{\n"
"background-color: #ffffff;\n"
"border-style: none;\n"
"border-radius: 7;\n"
"}\n"
"\n"
"#JobNameTitle {\n"
"text-align: right;\n"
"    font: 75 14pt \"Lato\";\n"
"}\n"
"\n"
"QLabel {\n"
"text-align: right;\n"
"font: 10pt \"Lato\";\n"
"}\n"
"\n"
"QDoubleSpinBox {\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 1px solid gray;\n"
"border-radius:4px;\n"
"}\n"
"\n"
"QPushButton {\n"
"color: white;\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #88d, stop: 0.1 #99e, stop: 0.49 #77c, stop: 0.5 #66b, stop: 1 #77c);\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font: \"Lato\";\n"
"font-size: 10px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"min-width: 50px;\n"
"min-height: 13px;\n"
"}\n"
"\n"
"\n"
"\n"
""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.TemperatureDisplayWidget_2 = QtGui.QWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TemperatureDisplayWidget_2.sizePolicy().hasHeightForWidth())
        self.TemperatureDisplayWidget_2.setSizePolicy(sizePolicy)
        self.TemperatureDisplayWidget_2.setMinimumSize(QtCore.QSize(100, 70))
        self.TemperatureDisplayWidget_2.setObjectName(_fromUtf8("TemperatureDisplayWidget_2"))
        self.formLayout = QtGui.QFormLayout(self.TemperatureDisplayWidget_2)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_5 = QtGui.QLabel(self.TemperatureDisplayWidget_2)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_5)
        self.pitTempDisplay = QtGui.QLabel(self.TemperatureDisplayWidget_2)
        self.pitTempDisplay.setObjectName(_fromUtf8("pitTempDisplay"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.pitTempDisplay)
        self.label_7 = QtGui.QLabel(self.TemperatureDisplayWidget_2)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_7)
        self.pitMeatDisplay = QtGui.QLabel(self.TemperatureDisplayWidget_2)
        self.pitMeatDisplay.setObjectName(_fromUtf8("pitMeatDisplay"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.pitMeatDisplay)
        self.gridLayout_2.addWidget(self.TemperatureDisplayWidget_2, 1, 5, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 1, 3, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 3, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 5, 2, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 3, 5, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 1, 4, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(0, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem5, 2, 5, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem6, 3, 1, 1, 1)
        spacerItem7 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem7, 4, 2, 1, 1)
        self.NewProjectWidget = QtGui.QWidget(self.centralwidget)
        self.NewProjectWidget.setMinimumSize(QtCore.QSize(250, 250))
        self.NewProjectWidget.setObjectName(_fromUtf8("NewProjectWidget"))
        self.gridLayout = QtGui.QGridLayout(self.NewProjectWidget)
        self.gridLayout.setContentsMargins(9, -1, -1, -1)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem8)
        self.JobNameTitle = QtGui.QLabel(self.NewProjectWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.JobNameTitle.setFont(font)
        self.JobNameTitle.setObjectName(_fromUtf8("JobNameTitle"))
        self.horizontalLayout.addWidget(self.JobNameTitle)
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem9)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 3)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.btnAdvanced = QtGui.QPushButton(self.NewProjectWidget)
        self.btnAdvanced.setObjectName(_fromUtf8("btnAdvanced"))
        self.verticalLayout.addWidget(self.btnAdvanced)
        self.btnCreate = QtGui.QPushButton(self.NewProjectWidget)
        self.btnCreate.setObjectName(_fromUtf8("btnCreate"))
        self.verticalLayout.addWidget(self.btnCreate)
        self.btnQuit = QtGui.QPushButton(self.NewProjectWidget)
        self.btnQuit.setObjectName(_fromUtf8("btnQuit"))
        self.verticalLayout.addWidget(self.btnQuit)
        self.gridLayout.addLayout(self.verticalLayout, 5, 0, 1, 3)
        self.numMeatTempSetPoint = QtGui.QDoubleSpinBox(self.NewProjectWidget)
        self.numMeatTempSetPoint.setObjectName(_fromUtf8("numMeatTempSetPoint"))
        self.gridLayout.addWidget(self.numMeatTempSetPoint, 4, 1, 1, 2)
        self.label_2 = QtGui.QLabel(self.NewProjectWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.numPitTempSetPoint = QtGui.QDoubleSpinBox(self.NewProjectWidget)
        self.numPitTempSetPoint.setObjectName(_fromUtf8("numPitTempSetPoint"))
        self.gridLayout.addWidget(self.numPitTempSetPoint, 3, 1, 1, 2)
        self.label_4 = QtGui.QLabel(self.NewProjectWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.NewProjectWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.txtJobName = QtGui.QLineEdit(self.NewProjectWidget)
        self.txtJobName.setMinimumSize(QtCore.QSize(200, 0))
        self.txtJobName.setObjectName(_fromUtf8("txtJobName"))
        self.gridLayout.addWidget(self.txtJobName, 1, 1, 1, 2)
        self.gridLayout_2.addWidget(self.NewProjectWidget, 3, 2, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_5.setText(_translate("MainWindow", "Pit Temp:", None))
        self.pitTempDisplay.setText(_translate("MainWindow", "180°C", None))
        self.label_7.setText(_translate("MainWindow", "Meat Temp:", None))
        self.pitMeatDisplay.setText(_translate("MainWindow", "180°C", None))
        self.JobNameTitle.setText(_translate("MainWindow", "Create New Project", None))
        self.btnAdvanced.setText(_translate("MainWindow", "Advanced Settings", None))
        self.btnCreate.setText(_translate("MainWindow", "Create New Project", None))
        self.btnQuit.setText(_translate("MainWindow", "Quit", None))
        self.label_2.setText(_translate("MainWindow", "Job Name:", None))
        self.label_4.setText(_translate("MainWindow", "Meat Temp Set Point:", None))
        self.label_3.setText(_translate("MainWindow", "Pit Temp Set Point:", None))

