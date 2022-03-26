from webbrowser import open_new_tab

from service.constants import DOWN_URL, SOFT_ZIP
from service.update import BackThread
from service import utils
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow

from windo.ui_init import ui_dialog, ui_reward
from windo.ui_init import ui_feedback


class WinFeedback(QMainWindow):
    """ 反馈说明界面 """

    def __init__(self):
        super(WinFeedback, self).__init__()
        self.ui = ui_feedback.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_csdn.clicked.connect(utils.jumpMyCSDN)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)


class WinGiveReward(QMainWindow):
    """ 打赏点赞界面 """

    def __init__(self):
        super(WinGiveReward, self).__init__()
        self.ui = ui_reward.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_csdn.clicked.connect(utils.jumpMyCSDN)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

class WinUpdateDialog(QDialog):
    """ 检查更新界面 """

    def __init__(self) -> None:
        super(WinUpdateDialog, self).__init__()
        self.ui = ui_dialog.Ui_Dialog()
        self.ui.setupUi(self) 
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.checkUpdate()

    def checkUpdate(self):
        """检查软件更新"""
        self.ui.textbrow_info.setText("检查更新中···")
        self.backend = BackThread() #后台检查更新
        self.backend.update_info.connect(self.updateDisplay)
        self.backend.start()
    
    def updateDisplay(self, version_name, yes_btn):
        """更新界面信息"""
        if   yes_btn == "确定":
            check_tip = f"已更新至最新版本：{version_name}"
            self.ui.btn_yes.clicked.connect(self.close)
        elif yes_btn == "下载":
            check_tip = f"最新版本为：{version_name}，是否自动跳转至浏览器下载？"
            self.ui.btn_yes.clicked.connect(self.downSoft)
            self.ui.btn_yes.setDefault(True) # FIXME
        self.version_name = version_name
        self.ui.btn_yes.setText(yes_btn)
        self.ui.textbrow_info.setText(check_tip)

    def downSoft(self):
        """跳转下载软件"""
        down_tips = F"正在下载最新版~\n请前往下载中心，找到 {self.version_name} 解压食用"
        self.ui.btn_yes.clicked.connect(self.close)
        self.ui.btn_yes.clicked.disconnect(self.downSoft)
        self.ui.btn_yes.setText("确定")
        self.ui.btn_yes.setDefault(True) # FIXME
        self.ui.textbrow_info.setText(down_tips)
        open_new_tab(F"{DOWN_URL}NjtechAutoLogin-v{self.version_name}.zip")


if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    dialog = WinUpdateDialog()
    dialog.show()
    sys.exit(app.exec_())
