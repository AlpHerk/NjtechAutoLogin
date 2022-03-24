import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtCore import Qt
from windo.win_login import WinLogin, WinLoginControl

if __name__ == '__main__':

    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling) # 缩放适应高分屏

    app = QApplication(sys.argv)

    WinLoginControl.loginWin = WinLogin()

    WinLoginControl.loginWin.show()
    
    sys.exit(app.exec_())
