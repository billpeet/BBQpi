# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'graph_window.ui'
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
        MainWindow.resize(942, 675)
        MainWindow.setStyleSheet(_fromUtf8("#tempLayout, #tempdisplay, #otherdetails {\n"
"background-color: #eeeeee\n"
"}\n"
"\n"
"QLabel {\n"
"font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"QLineEdit {\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 2px solid gray;\n"
"border-radius: 8px;\n"
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
"font-size: 10px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"min-width: 50px;\n"
"max-width: 50px;\n"
"min-height: 13px;\n"
"max-height: 13px;\n"
"}\n"
"\n"
""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.btnModifySettings = QtGui.QToolButton(self.centralwidget)
        self.btnModifySettings.setObjectName(_fromUtf8("btnModifySettings"))
        self.verticalLayout.addWidget(self.btnModifySettings)
        self.tempLayout = QtGui.QHBoxLayout()
        self.tempLayout.setObjectName(_fromUtf8("tempLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.tempLayout.addItem(spacerItem)
        self.otherdetails = QtGui.QWidget(self.centralwidget)
        self.otherdetails.setObjectName(_fromUtf8("otherdetails"))
        self.gridLayout_2 = QtGui.QGridLayout(self.otherdetails)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_11 = QtGui.QLabel(self.otherdetails)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_2.addWidget(self.label_11, 1, 3, 1, 1)
        self.label_3 = QtGui.QLabel(self.otherdetails)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 0, 2, 1, 1)
        self.dLabel = QtGui.QLabel(self.otherdetails)
        self.dLabel.setObjectName(_fromUtf8("dLabel"))
        self.gridLayout_2.addWidget(self.dLabel, 0, 5, 1, 1)
        self.label_9 = QtGui.QLabel(self.otherdetails)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_2.addWidget(self.label_9, 1, 0, 1, 1)
        self.iLabel = QtGui.QLabel(self.otherdetails)
        self.iLabel.setObjectName(_fromUtf8("iLabel"))
        self.gridLayout_2.addWidget(self.iLabel, 0, 3, 1, 1)
        self.pLabel = QtGui.QLabel(self.otherdetails)
        self.pLabel.setObjectName(_fromUtf8("pLabel"))
        self.gridLayout_2.addWidget(self.pLabel, 0, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.otherdetails)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_2.addWidget(self.label_6, 0, 4, 1, 1)
        self.label = QtGui.QLabel(self.otherdetails)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.outputLabel = QtGui.QLabel(self.otherdetails)
        self.outputLabel.setObjectName(_fromUtf8("outputLabel"))
        self.gridLayout_2.addWidget(self.outputLabel, 1, 4, 1, 2)
        self.setpointLabel = QtGui.QLabel(self.otherdetails)
        self.setpointLabel.setObjectName(_fromUtf8("setpointLabel"))
        self.gridLayout_2.addWidget(self.setpointLabel, 1, 1, 1, 1)
        self.tempLayout.addWidget(self.otherdetails)
        self.tempdisplay = QtGui.QWidget(self.centralwidget)
        self.tempdisplay.setObjectName(_fromUtf8("tempdisplay"))
        self.gridLayout = QtGui.QGridLayout(self.tempdisplay)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_5 = QtGui.QLabel(self.tempdisplay)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.pitTempDisplay = QtGui.QLabel(self.tempdisplay)
        self.pitTempDisplay.setObjectName(_fromUtf8("pitTempDisplay"))
        self.gridLayout.addWidget(self.pitTempDisplay, 0, 1, 1, 1)
        self.label_7 = QtGui.QLabel(self.tempdisplay)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 1)
        self.pitMeatDisplay = QtGui.QLabel(self.tempdisplay)
        self.pitMeatDisplay.setObjectName(_fromUtf8("pitMeatDisplay"))
        self.gridLayout.addWidget(self.pitMeatDisplay, 1, 1, 1, 1)
        self.tempLayout.addWidget(self.tempdisplay)
        self.verticalLayout.addLayout(self.tempLayout)
        self.canvasWidget = QtGui.QWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.canvasWidget.sizePolicy().hasHeightForWidth())
        self.canvasWidget.setSizePolicy(sizePolicy)
        self.canvasWidget.setAutoFillBackground(False)
        self.canvasWidget.setStyleSheet(_fromUtf8(""))
        self.canvasWidget.setObjectName(_fromUtf8("canvasWidget"))
        self.canvasLayout = QtGui.QVBoxLayout(self.canvasWidget)
        self.canvasLayout.setMargin(0)
        self.canvasLayout.setObjectName(_fromUtf8("canvasLayout"))
        self.verticalLayout.addWidget(self.canvasWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 942, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.btnModifySettings.setText(_translate("MainWindow", "Modify Settings", None))
        self.label_11.setText(_translate("MainWindow", "Output:", None))
        self.label_3.setText(_translate("MainWindow", "I:", None))
        self.dLabel.setText(_translate("MainWindow", "0.001", None))
        self.label_9.setText(_translate("MainWindow", "Setpoint:", None))
        self.iLabel.setText(_translate("MainWindow", "1.0", None))
        self.pLabel.setText(_translate("MainWindow", "1.56", None))
        self.label_6.setText(_translate("MainWindow", "D:", None))
        self.label.setText(_translate("MainWindow", "P:", None))
        self.outputLabel.setText(_translate("MainWindow", "50%", None))
        self.setpointLabel.setText(_translate("MainWindow", "100", None))
        self.label_5.setText(_translate("MainWindow", "Pit Temp:", None))
        self.pitTempDisplay.setText(_translate("MainWindow", "180°C", None))
        self.label_7.setText(_translate("MainWindow", "Meat Temp:", None))
        self.pitMeatDisplay.setText(_translate("MainWindow", "180°C", None))

