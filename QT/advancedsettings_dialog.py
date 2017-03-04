# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'advancedsettings_dialog.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 168)
        Dialog.setStyleSheet(_fromUtf8("QLabel {\n"
"text-align: right;\n"
"}\n"
"\n"
"QDoubleSpinBox {\n"
"padding: 1px;\n"
"border-style: solid;\n"
"border: 2px solid gray;\n"
"border-radius: 6px;\n"
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
        self.formLayout = QtGui.QFormLayout(Dialog)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.loggingOn = QtGui.QCheckBox(Dialog)
        self.loggingOn.setObjectName(_fromUtf8("loggingOn"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.loggingOn)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.logFrequency = QtGui.QDoubleSpinBox(Dialog)
        self.logFrequency.setObjectName(_fromUtf8("logFrequency"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.logFrequency)
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.p = QtGui.QDoubleSpinBox(Dialog)
        self.p.setDecimals(3)
        self.p.setObjectName(_fromUtf8("p"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.p)
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.i = QtGui.QDoubleSpinBox(Dialog)
        self.i.setDecimals(3)
        self.i.setObjectName(_fromUtf8("i"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.i)
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_5)
        self.d = QtGui.QDoubleSpinBox(Dialog)
        self.d.setDecimals(3)
        self.d.setObjectName(_fromUtf8("d"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.d)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.SpanningRole, self.buttonBox)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Logging to DB:", None))
        self.loggingOn.setText(_translate("Dialog", "Enabled", None))
        self.label_2.setText(_translate("Dialog", "Log Frequency:", None))
        self.label_3.setText(_translate("Dialog", "P:", None))
        self.label_4.setText(_translate("Dialog", "I:", None))
        self.label_5.setText(_translate("Dialog", "D:", None))

