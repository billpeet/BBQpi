import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.figure import Figure

import random
import numpy as np
import datetime
import main_screen
import threading


class GraphCanvas(FigureCanvas):
    def __init__(self, parent):
        self.hogwash = 23
        self.ax1 = self.ax2 = None
        self.fig = Figure(tight_layout={"pad": .2},frameon=True)  # ,"h_pad":0.0,"w_pad":0.0
        self.ax = self.fig.add_subplot(111)
        FigureCanvas.__init__(self, self.fig)

        self.setParent(parent)
        FigureCanvas.updateGeometry(self)


class GraphScreen(QDialog):

    def __init__(self, parent=None):
        super(GraphScreen, self).__init__()

        self.t = [datetime.datetime.now()]
        self.data = [1]
        self.data2 = [1]

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.tempdisplay = main_screen.TemperatureDisplayWidget()

        self.button = QPushButton('Plot')
        self.button.clicked.connect(lambda: self.adddatapoint())

        # Set Layout
        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)

        templayout = QHBoxLayout()
        templayout.addStretch(0)
        templayout.addWidget(self.tempdisplay)
        layout.addLayout(templayout)

        layout.addWidget(self.canvas)
        layout.addWidget(self.button)

        self.setLayout(layout)

        self.ax = self.figure.add_subplot(111)
        self.ax.set_ylabel('dog')
        self.ax.plot_date(self.t, self.data, '--')

        self.ax2 = self.ax.twinx()
        self.ax2.set_ylabel('cat')
        self.ax2.plot_date(self.t, self.data2, 'r-')
        self.canvas.draw()

        self.plot()
        self.adddatapoint()
        # threading.Timer(100, self.adddatapoint()).start()

    def plot(self):
        self.figure.clear()
        self.ax = self.figure.add_subplot(111)
        self.ax.hold(False)
        self.ax.plot_date(self.t, self.data, 'r-')
        self.ax.format_xdata = mdates.DateFormatter('%Y-%m-%d')

        self.ax2 = self.ax.twinx()
        self.ax2.hold(False)
        self.ax2.plot_date(self.t, self.data2, 'b-')

        self.canvas.draw()

        self.tempdisplay.settemps(self.data[-1],self.data2[-1])

    def adddatapoint(self):
        threading.Timer(1, self.adddatapoint).start()
        self.t.append(datetime.datetime.now())
        self.data.append(self.data[-1] + (random.randint(-1, 1)/10))
        self.data2.append(self.data2[-1] + (random.randint(-2, 2)/10))
        self.plot()

def main():
    app = QApplication(sys.argv)

    h = GraphScreen()
    h.exec_()

if __name__ == '__main__':
    main()