from configparser import ConfigParser
from os import getcwd

import win32api
import win32con
from PyQt5.QtWidgets import QApplication

from service import utils
from service.constants import *
from windo.win_loginadh import WinFeedback, WinGiveReward, WinUpdateDialog
from windo.ui_init import ui_login
from windo.ui_init.drag_widget import DragWidget

class WinLogin(DragWidget):
    """ 登录界面·入口界面 """

    def __init__(self):

        super(WinLogin, self).__init__()
        self.ui = ui_login.Ui_Form()
        self.ui.setupUi(self)
        # from PyQt5.uic import loadUi
        # self.ui = loadUi('pyqtui\\ui_login.ui')
        try: self.loadLoginData()
        except: pass

        # 登录信息配置事件
        self.ui.ckbx_pwrboot.stateChanged.connect(self.powerBoot)
        self.ui.ckbx_showlogin.stateChanged.connect(self.showLoginInfo)
        self.ui.spbox_cnct_time.valueChanged.connect(self.btnLink)

        # 登录按钮点击事件
        self.ui.btn_login.clicked.connect(self.saveLoginData)
        self.ui.ed_pwd.returnPressed.connect(self.saveLoginData)

        # 底部信息处理事件
        self.ui.btn_feedback.clicked.connect(self.jumpFeedBack)
        self.ui.btn_upgrade.clicked.connect(self.jumpGetUpgrade)
        self.ui.btn_givereward.clicked.connect(self.jumpGiveReward)

    def saveLoginData(self):
        self.username  = self.ui.ed_usr.text()
        self.password  = self.ui.ed_pwd.text()
        self.channel   = self.ui.cbbx_channel.currentText()
        self.powerboot = self.ui.ckbx_pwrboot.isChecked()
        self.showlogin = self.ui.ckbx_showlogin.isChecked()
        self.reconnect = self.ui.spbox_cnct_time.value()

        utils.mkConfigDir()   # 创建若不存在
        config = ConfigParser()
        config[LOGIN_DATA_WARN1] = {
        }
        config[LOGIN_DATA_WARN2] = {
        }
        config[LOGIN_PART_1] = {
            LOGIN_DATA_1: self.username,
            LOGIN_DATA_2: self.password,
            LOGIN_DATA_3: self.channel }
        config[LOGIN_PART_2] = {
            LOGIN_DATA_4: self.powerboot,
            LOGIN_DATA_5: self.reconnect,
            LOGIN_DATA_6: self.showlogin}
        with open(LOGINFILE_PATH, 'w', encoding='utf-8') as configfile:
            config.write(configfile)

    def loadLoginData(self):
        self.config = ConfigParser()
        self.config.read(LOGINFILE_PATH, encoding='utf-8')
        self.username  = self.config[LOGIN_PART_1][LOGIN_DATA_1]
        self.password  = self.config[LOGIN_PART_1][LOGIN_DATA_2]
        self.channel   = self.config[LOGIN_PART_1][LOGIN_DATA_3]
        self.powerboot = self.config[LOGIN_PART_2][LOGIN_DATA_4]
        self.reconnect = self.config[LOGIN_PART_2][LOGIN_DATA_5]
        self.showlogin = self.config[LOGIN_PART_2][LOGIN_DATA_6]
        self.reconnect = int(self.reconnect)

        self.ui.ed_usr.setText(self.username)
        self.ui.ed_pwd.setText(self.password)
        self.channel_index = 0 if self.channel=='中国移动' else 1
        self.ui.cbbx_channel.setCurrentIndex(self.channel_index)
        self.ui.spbox_cnct_time.setValue(self.reconnect)

        if self.powerboot == 'True':
            self.ui.ckbx_pwrboot.setChecked(True)
        if self.showlogin == 'True':
            self.ui.ckbx_showlogin.setChecked(True)

        self.powerBoot()

    def showLoginInfo(self):
        if self.ui.ckbx_showlogin.isChecked():
            # 屏蔽复选框点击事件 21.10.04
            pass

    def powerBoot(self):
        path = getcwd() + f"\\{AUTOLOGIN_EXE}"
        runpath = "Software\\Microsoft\\Windows\\CurrentVersion\\Run"
        hKey = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, runpath, 0, win32con.KEY_ALL_ACCESS)

        if self.ui.ckbx_pwrboot.isChecked():
            win32api.RegSetValueEx(hKey, AUTOLOGIN_EXE, 0, win32con.REG_SZ, path)
        else:
            try: win32api.RegDeleteValue(hKey, AUTOLOGIN_EXE)
            except: pass
        win32api.RegCloseKey(hKey)

    def btnLink(self):
        if int(self.ui.spbox_cnct_time.value()) > -1:
            self.ui.ckbx_pwrboot.setChecked(True)
            self.ui.ckbx_showlogin.setChecked(False)

    def jumpFeedBack(self):
        WinLoginControl.showWin = WinFeedback()
        WinLoginControl.showWin.show()

    def jumpGiveReward(self):
        WinLoginControl.showWin = WinGiveReward()
        WinLoginControl.showWin.show()
        
    def jumpGetUpgrade(self):
        WinLoginControl.showWin = WinUpdateDialog()
        WinLoginControl.showWin.show()


class WinLoginControl:

    loginWin = None

    showWin  = None


if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    WinLoginControl.loginWin = WinLogin()
    WinLoginControl.loginWin.show()
    sys.exit(app.exec_())


