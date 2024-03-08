from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal
from .ui.ui_settings import Ui_Settings

from pyqtconfig import QSettings
from dataclasses import dataclass

@dataclass
class AppSettings():
    hostname: str
    username: str
    password: str
    downloadDir: str
    jackettHost: str
    jackettApiKey: str

class SettingsWindow(QWidget):
    '''The window letting the user set transmission daemon RPC settings'''
    # Signal sent when new settings are applied
    newSettingsApplied = Signal()

    def __init__(self, qsettings:QSettings, parent=None):
        super().__init__(parent)
        self.ui = Ui_Settings()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.confirmSettingsclicked)
        self.qsettings = qsettings
        self.appSettings = SettingsHelper.retrieveSettings(self.qsettings)
        self.ui.hostTextEdit.setText(self.appSettings.hostname)
        self.ui.usernameTextEdit.setText(self.appSettings.username)
        self.ui.passwordTextEdit.setText(self.appSettings.password)
        self.ui.downloadDirTextEdit.setText(self.appSettings.downloadDir)
        self.ui.jackettHostTextEdit.setText(self.appSettings.jackettHost)
        self.ui.jackettApiKeyTextEdit.setText(self.appSettings.jackettApiKey)
        SettingsHelper.showSettings(self.appSettings)

    def confirmSettingsclicked(self):
        self.qsettings.beginGroup("rpc")
        self.qsettings.setValue("hostname", self.ui.hostTextEdit.text())
        self.qsettings.setValue("username", self.ui.usernameTextEdit.text())
        self.qsettings.setValue("password", self.ui.passwordTextEdit.text())
        self.qsettings.setValue("downloadDir", self.ui.downloadDirTextEdit.text())
        self.qsettings.setValue("jackettHost", self.ui.jackettHostTextEdit.text())
        self.qsettings.setValue("jackettApiKey", self.ui.jackettApiKeyTextEdit.text())
        self.qsettings.endGroup()
        self.appSettings = SettingsHelper.retrieveSettings(self.qsettings)
        SettingsHelper.showSettings(self.appSettings)
        self.newSettingsApplied.emit()
        self.hide()

class SettingsHelper():

    @staticmethod
    def retrieveSettings(settings:QSettings) -> AppSettings:
        settings.beginGroup("rpc")
        if settings.value("hostname") is None:
            settings.setValue("hostname", "")
        if settings.value("username") is None:
            settings.setValue("username", "")
        if settings.value("password") is None:
            settings.setValue("password", "")
        if settings.value("downloadDir") is None:
            settings.setValue("downloadDir", "")
        if settings.value("jackettHost") is None:
            settings.setValue("jackettHost", "")
        if settings.value("jackettApiKey") is None:
            settings.setValue("jackettApiKey", "")
        result = AppSettings(settings.value("hostname"), settings.value("username"),
                                     settings.value("password"), settings.value("downloadDir"),
                                     settings.value("jackettHost"), settings.value("jackettApiKey"))
        settings.endGroup()
        return result

    @staticmethod
    def rpcSettingsValid(settings:QSettings) -> bool:
        settings.beginGroup("rpc")
        valid = settings.value("hostname") != "" and settings.value("username") != "" and settings.value("password")!= ""
        settings.endGroup()
        return valid

    @staticmethod
    def showSettings(appSettings:AppSettings):
        dir = appSettings.downloadDir
        s = "=== RPC Server Settings ===\r\n"
        s += "Hostname : " + appSettings.hostname + "\r\n"
        s += "Username : " + appSettings.username + "\r\n"
        s += "Password : " + appSettings.password + "\r\n"
        s += "Download Directory : " + (dir if dir != "" else "default") + "\r\n"
        s += "Jackett Host : " + appSettings.jackettHost + "\r\n"
        s += "Jackett API key : " + appSettings.jackettApiKey + "\r\n"
        print(s)

    @staticmethod
    def clearSettings(settings:QSettings):
        settings.beginGroup("rpc")
        settings.remove("hostname")
        settings.remove("username")
        settings.remove("password")
        settings.remove("downloadDir")
        settings.remove("jackettHost")
        settings.remove("jackettApiKey")
        settings.clear()
        settings.endGroup()