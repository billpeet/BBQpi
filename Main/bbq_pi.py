import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import QT.main_window as main_window
from Forms.AdvancedSettingsDialog import AdvancedSettingsDialog
from Forms.GraphWindow import GraphWindow

import yaml


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.mainwindow = main_window.Ui_MainWindow()
        self.mainwindow.setupUi(self)
        self.mainwindow.btnCreate.clicked.connect(self.btnpressed)
        self.mainwindow.btnAdvanced.clicked.connect(self.advancedsettings)
        self.mainwindow.btnQuit.clicked.connect(self.quit)

        # Setup graphics effects
        self.mainwindow.shadow = QGraphicsDropShadowEffect(self)
        self.mainwindow.shadow.setOffset(2, 2)
        self.mainwindow.shadow.setBlurRadius(5)
        self.mainwindow.NewProjectWidget.setGraphicsEffect(self.mainwindow.shadow)

        self.mainwindow.tempshadow = QGraphicsDropShadowEffect(self)
        self.mainwindow.tempshadow.setOffset(2, 2)
        self.mainwindow.tempshadow.setBlurRadius(5)
        self.mainwindow.TemperatureDisplayWidget_2.setGraphicsEffect(self.mainwindow.tempshadow)

        self.show()

    def btnpressed(self):
        print("Pressed")
        graphwindow = GraphWindow(self)
        graphwindow.closing.connect(self.show)
        self.hide()
        graphwindow.show()

    def advancedsettings(self):
        advanceddialog = AdvancedSettingsDialog(self)
        advanceddialog.show()

    def quit(self, newvalue):
        sys.exit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('flame-icon.ico'))
    myapp = MainWindow()
    sys.exit(app.exec_())
