from PyQt4 import QtGui, QtCore
from QT.advancedsettings_dialog import Ui_Dialog
from ruamel import yaml


class AdvancedSettingsDialog(QtGui.QDialog):
    settingchanged = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(AdvancedSettingsDialog, self).__init__(parent, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.buttonBox.clicked.connect(self.submitclose)

        # self.createconfig()
        self.getsettings()

    def getsettings(self):
        try:
            config = yaml.load(open('config.yaml', 'r'), Loader=yaml.RoundTripLoader)
            self.ui.loggingOn.setChecked(config['Logging']['LogToDB'])
            self.ui.logFrequency.setValue(config['Logging']['LogFrequency'])
            self.ui.p.setValue(config['PID Settings']['P'])
            self.ui.i.setValue(config['PID Settings']['I'])
            self.ui.d.setValue(config['PID Settings']['D'])
        except FileNotFoundError:
            print('Config file not found!')
        except KeyError:
            print('Malformed config file!')

    def save(self):
        config = yaml.load(open('config.yaml', 'r'), Loader=yaml.RoundTripLoader)
        config['Logging']['LogToDB'] = self.ui.loggingOn.isChecked()
        config['Logging']['LogFrequency'] = self.ui.logFrequency.value()
        config['PID Settings']['P'] = self.ui.p.value()
        config['PID Settings']['I'] = self.ui.i.value()
        config['PID Settings']['D'] = self.ui.d.value()
        with open('config.yaml', 'w') as yaml_file:
            yaml_file.write(yaml.dump(config, Dumper=yaml.RoundTripDumper))

    def submitclose(self):
        self.save()
        self.settingchanged.emit()
