import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from random import *
import graph_screen


class HomeScreen(QWidget):

    def __init__(self):
        super(HomeScreen, self).__init__()

        # Logo Image
        logo = QPixmap('flame-icon.png')
        logo = logo.scaled(100, 50, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        logowidget = QLabel()
        logowidget.setPixmap(logo)
        logowidget.setFixedSize(100, 50)

        # New Project Widget
        self.newprojectwidget = NewProjectWidget()

        # Temperature Display Widget
        self.tempdisplaywidget = TemperatureDisplayWidget()

        # Set Background Colour
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.gray)
        self.setAutoFillBackground(True)
        self.setPalette(p)

        # Set Layout
        grid = QGridLayout()
        grid.setColumnStretch(1, 1)
        grid.setColumnStretch(3, 1)
        grid.setRowStretch(1, 1)
        grid.setRowStretch(3, 1)
        grid.addWidget(logowidget, 0, 0)
        grid.addWidget(self.tempdisplaywidget, 0, 4)
        grid.addWidget(self.newprojectwidget, 2, 2)
        self.setLayout(grid)

        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle('BBQpi - Home Screen')
        self.show()
        # self.showFullScreen()


class NewProjectWidget(QWidget):
    def __init__(self):
        super(NewProjectWidget, self).__init__()

        # Fonts
        font = QFont()
        font.setFamily('Lato')
        font.setPointSize(16)
        btnfont = QFont()
        btnfont.setFamily('Lato')
        btnfont.setPointSize(12)
        lblfont = QFont()
        lblfont.setFamily('Lato')
        lblfont.setPointSize(14)

        # Labels
        title = QLabel('Create New Project')
        title.setFont(font)
        jobName = QLabel('Job Name:')
        pitSetpoint = QLabel('Pit Temp Set Point:')
        meatSetpoint = QLabel('Meat Temp Set Point:')
        degrees1 = QLabel('°C')
        degrees1.setFont(font)
        degrees2 = QLabel('°C')
        degrees2.setFont(font)

        # Labels
        jobNameEdit = QLineEdit()
        jobNameEdit.setFont(lblfont)
        pitSetpointEdit = QDoubleSpinBox()
        pitSetpointEdit.setMinimum(0)
        pitSetpointEdit.setMaximum(999)
        pitSetpointEdit.setFont(lblfont)
        meatSetpointEdit = QDoubleSpinBox()
        meatSetpointEdit.setMinimum(0)
        meatSetpointEdit.setMaximum(999)
        meatSetpointEdit.setFont(lblfont)

        # Buttons
        btnAdvanced = QPushButton('Advanced Settings')
        btnAdvanced.setFont(btnfont)
        btnAdvanced.clicked.connect(self.buttonclicked)
        btnCreate = QPushButton('Create Project')
        btnCreate.setFont(btnfont)
        btnCreate.clicked.connect(self.buttonclicked)
        btnQuit = QPushButton('Quit')
        btnQuit.setFont(btnfont)
        btnQuit.clicked.connect(self.buttonclicked)

        # Layout
        grid = QGridLayout()

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(title)
        hbox.addStretch(1)
        grid.addLayout(hbox, 0, 0, 1, 4)

        grid.addWidget(jobName, 1, 0)
        grid.addWidget(jobNameEdit, 1, 1, 1, 2)
        grid.addWidget(pitSetpoint, 2, 0)
        grid.addWidget(pitSetpointEdit, 2, 1)
        grid.addWidget(degrees1, 2, 2)
        grid.addWidget(meatSetpoint, 3, 0)
        grid.addWidget(meatSetpointEdit, 3, 1)
        grid.addWidget(degrees2, 3, 2)

        vbox = QVBoxLayout()
        vbox.addWidget(btnAdvanced)
        vbox.addWidget(btnCreate)
        vbox.addWidget(btnQuit)
        grid.addLayout(vbox, 4, 0, 1, 3)

        self.setLayout(grid)

        # Background colour
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.white)
        self.setAutoFillBackground(True)
        self.setPalette(p)

    def buttonclicked(self, event):
        sender = self.sender()
        if sender.text() == 'Advanced Settings':
            advancedwidget = AdvancedSettingsPopup()
            advancedwidget.exec_()
        elif sender.text() == 'Create Project':
            graph = graph_screen.GraphScreen()
            graph.exec_()
        elif sender.text() == 'Quit':
            QCoreApplication.instance().quit()


class TemperatureDisplayWidget(QWidget):
    def __init__(self):
        super(TemperatureDisplayWidget, self).__init__()

        font = QFont()
        font.setFamily('Lato')
        font.setPointSize(10)

        # Labels
        pitTemp = QLabel('Pit Temp:')
        pitTemp.setFont(font)
        meatTemp = QLabel('Meat Temp:')
        meatTemp.setFont(font)
        self.pitTempDisplay = QLabel(str(round(random()*100, 1)) + '°C')
        self.pitTempDisplay.setFont(font)
        self.meatTempDisplay = QLabel(str(round(random()*100, 1)) + '°C')
        self.meatTempDisplay.setFont(font)

        grid = QGridLayout()

        grid.addWidget(pitTemp, 0, 0)
        grid.addWidget(self.pitTempDisplay, 0, 1)

        grid.addWidget(meatTemp, 1, 0)
        grid.addWidget(self.meatTempDisplay, 1, 1)

        self.setLayout(grid)

        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.white)
        self.setAutoFillBackground(True)
        self.setPalette(p)

    def settemps(self, temp1, temp2):
        self.pitTempDisplay.setText(str(round(temp1, 1)) + '°C')
        self.meatTempDisplay.setText(str(round(temp2, 1)) + '°C')

class AdvancedSettingsPopup(QDialog):

    def __init__(self):
        super(AdvancedSettingsPopup, self).__init__()

        # Font
        font = QFont()
        font.setFamily('Lato')
        font.setPointSize(12)

        # Controls
        loggingOn = QCheckBox()
        logFrequency = QDoubleSpinBox()
        logFrequency.setMinimum(0)
        logFrequency.setMaximum(999)
        logFrequency.setFont(font)
        p = QDoubleSpinBox()
        p.setMinimum(0)
        p.setMaximum(999)
        p.setFont(font)
        i = QDoubleSpinBox()
        i.setMinimum(0)
        i.setMaximum(999)
        i.setFont(font)
        d = QDoubleSpinBox()
        d.setMinimum(0)
        d.setMaximum(999)
        d.setFont(font)
        btnCancel = QPushButton('Cancel')
        btnOK = QPushButton('OK')

        # Layout
        layout = QVBoxLayout()
        form = QFormLayout()
        form.addRow(QLabel('Logging Enabled:'), loggingOn)
        form.addRow(QLabel('Logging Frequency:'), logFrequency)
        form.addRow(QLabel('Proportional:'), p)
        form.addRow(QLabel('Integral:'), i)
        form.addRow(QLabel('Derivative:'), d)
        layout.addLayout(form)
        btnlayout = QHBoxLayout()
        btnlayout.addWidget(btnCancel)
        btnlayout.addWidget(btnOK)
        layout.addLayout(btnlayout)

        self.setLayout(layout)
        self.setWindowTitle('Advanced Settings')
        # self.setFixedSize(400, 200)


def main():

    app = QApplication(sys.argv)

    # Set Window Icon
    app.setWindowIcon(QIcon('flame-icon.ico'))

    # Set Default Font
    font = QFont()
    font.setFamily('Lato')
    font.setPointSize(12)
    app.setFont(font)

    h = HomeScreen()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()