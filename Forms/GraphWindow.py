# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from QT.graph_window import Ui_MainWindow

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.ticker as ticker

import threading
import datetime
import random
import time
from ruamel import yaml
import numpy as np
import pylab as pl

from ivPID.PID import PID

from Forms.AdvancedSettingsDialog import AdvancedSettingsDialog


class GraphWindow(QtGui.QMainWindow):
    closing = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(GraphWindow, self).__init__(parent, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)

        # Initiate UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Load Config
        self.loadconfig()

        self.ui.btnModifySettings.clicked.connect(self.opensettings)

        # Create new graph Widget
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.toolbar.setStyleSheet('background-color: #eeeeee')

        self.ui.canvasLayout.addWidget(self.toolbar)
        self.ui.canvasLayout.addWidget(self.canvas)

        # Temp values for testing
        pitTempInitial = 20.0
        meatTempInitial = 50.0
        outputInitial = 0.0

        # Setup graph
        self.pitTemp = self.figure.add_subplot(111)
        self.pitTemp.set_ylabel(u'Temperature (°C)')
        self.pitTemp.set_ylim(0, 180)
        now = datetime.datetime.now()

        # Populating - FOR TESTING ONLY
        arr = np.array([now + datetime.timedelta(minutes=i) for i in range(180)])
        vals = np.random.randint(50, 60, 180)
        # self.pitTempData, = self.pitTemp.plot_date(arr, vals, 'r-', label='Pit Temperature')
        # self.pitTemp.set_xlim(arr[0], arr[-1])

        # Pit Temp Graph
        self.pitTempData, = self.pitTemp.plot_date([now], [pitTempInitial], 'r-', label='Pit Temperature')

        # Meat Temp Graph
        self.meatTempData, = self.pitTemp.plot_date([now], [meatTempInitial], 'b-', label='Meat Temperature')

        # Output Graph
        self.output = self.pitTemp.twinx()
        self.output.set_ylabel('Fan Speed (%)')
        # self.output.set_xlim(now, now + datetime.timedelta(minutes=1))
        self.output.set_ylim(-100, 100)
        self.outputData, = self.output.plot_date([now], [outputInitial], '--', label='Fan Speed')

        # Setup Legends
        self.pitTemp.legend()
        self.output.legend(loc='lower right')

        # Ticker Formatting Function
        def format_date(x, pos=None):
            dt = pl.num2date(x)
            if dt.second == 0:
                return dt.strftime('%I:%M %p')
            else:
                return pl.num2date(x).strftime('%I:%M:%S')

        # Setup Ticker
        self.pitTemp.xaxis.set_major_formatter(ticker.FuncFormatter(format_date))
        self.figure.autofmt_xdate()

        # Draw the graph
        self.canvas.draw()

        # Setup PID
        self.pid = PID(self.Kp, self.Ki, self.Kd)
        self.pid.SetPoint = 120.0
        self.pid.setSampleTime(0.01)
        self.pid.setWindup(100.0)

        # Set an initial value for testing purposes
        self.feedback = pitTempInitial

        # Create background thread and start
        self.thread = BBQpiThread(self)
        self.thread.signal.connect(self.append_line)
        self.thread.start()

    def opensettings(self):
        # Open the settings dialog
        advanceddialog = AdvancedSettingsDialog(self)
        advanceddialog.settingchanged.connect(self.loadconfig)
        advanceddialog.show()

    def loadconfig(self):
        # Load data from config file
        config = yaml.safe_load(open('config.yaml'))
        self.logtodb = config['Logging']['LogToDB']
        self.logfrequency = config['Logging']['LogFrequency']
        self.Kp = config['PID Settings']['P']
        self.Ki = config['PID Settings']['I']
        self.Kd = config['PID Settings']['D']

        # Check if pid exists first (it doesn't when called from __init__)
        if hasattr(self, 'pid'):
            self.pid.setKp(self.Kp)
            self.pid.setKi(self.Ki)
            self.pid.setKd(self.Kd)

        # Set UI
        self.ui.pLabel.setText(str(self.Kp))
        self.ui.iLabel.setText(str(self.Ki))
        self.ui.dLabel.setText(str(self.Kd))

    def append_line(self, now, pitTemp, meatTemp, output):
        """Appends point to both graphs"""
        self.pitTempData.set_xdata(np.append(self.pitTempData.get_xdata(), now))
        self.pitTempData.set_ydata(np.append(self.pitTempData.get_ydata(), pitTemp))
        self.meatTempData.set_xdata(np.append(self.meatTempData.get_xdata(), now))
        self.meatTempData.set_ydata(np.append(self.meatTempData.get_ydata(), meatTemp))
        self.outputData.set_xdata(np.append(self.outputData.get_xdata(), now))
        self.outputData.set_ydata(np.append(self.outputData.get_ydata(), output))
        self.extents()
        self.ui.pitTempDisplay.setText(str(round(pitTemp, 1)) + u'°C')
        self.ui.pitMeatDisplay.setText(str(round(meatTemp, 1)) + u'°C')
        self.ui.outputLabel.setText(str(round(output, 1)) + '%')
        # print([now, pitTemp, meatTemp, output])
        self.figure.canvas.draw_idle()

    def extents(self):
        """Zooms extents"""
        xdata = self.pitTempData.get_xdata()
        self.pitTemp.set_xlim(xdata[0], xdata[-1])

        tempdata = self.pitTempData.get_ydata()
        if tempdata[-1] > self.pitTemp.get_ylim()[1]:
            self.pitTemp.set_ylim(0, tempdata[-1] + 0.1)

    def closeEvent(self, event):
        # TODO: Are you sure dialog
        quit_msg = 'Are you sure you want to quit? This will end the current cook.'
        reply = QtGui.QMessageBox.question(self, 'Message', quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            # Clean up then exit
            self.thread.cancel()
            self.closing.emit()
            event.accept()
        else:
            event.ignore()


class BBQpiThread(QtCore.QThread):
    signal = QtCore.pyqtSignal(datetime.datetime, float, float, float)

    def __init__(self, parent=None):
        super(BBQpiThread, self).__init__(parent)
        self.wasCancelled = False
        self.parent = parent
        self.signal.connect(self.logToDB)

    def cancel(self):
        self.wasCancelled = True

    def run(self):
        while True:
            time.sleep(self.parent.logfrequency)
            if not self.wasCancelled:
                self.parent.pid.update(self.parent.feedback)
                output = self.parent.pid.output
                # Replace this line with reading real temp
                self.parent.feedback += min(output + random.randint(-1, 1) / 5, 100.0)
                now = datetime.datetime.now()
                # Replace with reading real meat temp
                meattemp = self.readTemp()
                self.signal.emit(now, self.parent.feedback, meattemp, self.parent.pid.output)
            else:
                break
        self.exit(0)

    def logToDB(self, now, data1, data2, data3):
        if self.parent.logtodb:
            print('Logged to db')

    def readTemp(self):
        return random.randint(50, 60)
