from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class DragWidget(QWidget):
    """ 左键拖拽窗口 """
    def __init__(self):
        super().__init__()
        
        self.initCustomUI()
        self.dragWidget()

    def initCustomUI(self):
        """ 初始化界面 """
        wdo_flag = Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint
        self.setWindowFlags(wdo_flag) #置顶窗口
        self.setAttribute(Qt.WA_DeleteOnClose, True)
        self.setAttribute(Qt.WA_TranslucentBackground)
        # self.setWindowOpacity(0.99)

    def dragWidget(self):
        self.setMouseTracking(True)
        self.move_flag = False #拖拽窗口

    def mousePressEvent(  self, a0):
        if a0.button() == Qt.LeftButton:
            self.move_flag = True
            self.mos_x = a0.globalX()
            self.mos_y = a0.globalY()
            self.wdo_x = self.x()
            self.wdo_y = self.y()
    
    def mouseMoveEvent(self, a0):
        if self.move_flag:
            move_x = a0.globalX() - self.mos_x
            move_y = a0.globalY() - self.mos_y
            new_x = self.wdo_x + move_x
            new_y = self.wdo_y + move_y
            self.move(new_x, new_y)
    
    def mouseReleaseEvent(self, a0):
        self.move_flag = False


if __name__ == '__main__':
    
    import sys
    
    app = QApplication(sys.argv)

    wdo = DragWidget()

    wdo.show()

    sys.exit(app.exec_())