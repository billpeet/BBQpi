#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sip
sip.setapi('QString', 2)
sip.setapi('QVariant', 2)

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class testShadow(QWidget):
    def __init__(self, parent=None):
        super(testShadow, self).__init__(parent)

        self.resize(94, 35)
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.button = QPushButton(self)
        self.button.setText("Text Label")

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setXOffset(1)
        self.shadow.setYOffset(1)
        self.shadow.setBlurRadius(10)
        self.button.setGraphicsEffect(self.shadow)

        self.verticalLayout.addWidget(self.button)

if __name__ == "__main__":
    import  sys

    app = QApplication(sys.argv)
    main = testShadow()
    main.show()
    sys.exit(app.exec_())
