# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwidget.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTabWidget, QTextBrowser, QToolButton,
    QVBoxLayout, QWidget)

from custoui.titlebar import TitleBar
import resource_rc
import resources_rc

class Ui_CustoWdo(object):
    def setupUi(self, CustoWdo):
        if not CustoWdo.objectName():
            CustoWdo.setObjectName(u"CustoWdo")
        CustoWdo.resize(1002, 644)
        CustoWdo.setMinimumSize(QSize(940, 560))
        CustoWdo.setMouseTracking(True)
        CustoWdo.setTabletTracking(False)
        CustoWdo.setFocusPolicy(Qt.NoFocus)
        CustoWdo.setStyleSheet(u"")
        CustoWdo.setAnimated(True)
        self.actQuit = QAction(CustoWdo)
        self.actQuit.setObjectName(u"actQuit")
        icon = QIcon()
        icon.addFile(u":/icon/resource/icons/logout.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actQuit.setIcon(icon)
        self.styleSheet = QWidget(CustoWdo)
        self.styleSheet.setObjectName(u"styleSheet")
        self.styleSheet.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setMouseTracking(True)
        self.styleSheet.setStyleSheet(u"/*  ///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"QWidget {\n"
"  color: #333;\n"
"  font: 12pt '\u5fae\u8f6f\u96c5\u9ed1';\n"
"}\n"
"QToolTip {\n"
"  background-color: #fff;\n"
"  border: 1px solid #ccc;\n"
"  background-image: none;\n"
"  background-position: left center;\n"
"  background-repeat: no-repeat;\n"
"  border: none;\n"
"  border-left: 2px solid #ec7d74;\n"
"  text-align: left;\n"
"  padding-left: 8px;\n"
"  margin: 0px;\n"
"}\n"
"#bgApp {\n"
"  background-color: #fff;\n"
"  color: #333;\n"
"}\n"
"#leftMenuBg {\n"
"  background-color: #7abee6;\n"
"}\n"
"#leftMenuFrame {\n"
"  border-top: 3px solid #aed7ef;\n"
"}\n"
"#topLogo {\n"
"  background-color: #7abee6;\n"
"  background-position: centered;\n"
"  background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp {\n"
"  font: 65 12pt 'Segoe UI Semibold';\n"
"  color: #fff;\n"
"}\n"
"#titleLeftDescription {\n"
"  font: 8pt 'Segoe UI';\n"
"  color: #d4caca;\n"
"}\n"
"\n"
"#about_page .QPushButton {\n"
""
                        "    background-image: url(:/icons/images/icons/cil-chevron-right.png);\n"
"    background-origin: content;\n"
"    background-position: right;\n"
"    background-repeat: no-repeat;\n"
"\n"
"    text-align: left;\n"
"    padding-left:18px; \n"
"    padding-right:10px; \n"
"}\n"
"\n"
"#toggleButton {\n"
"  background-position: left center;\n"
"  background-repeat: no-repeat;\n"
"  border: none;\n"
"  border-left: 20px solid transparent;\n"
"  text-align: left;\n"
"  padding-left: 44px;\n"
"  color: #fff;\n"
"}\n"
"#toggleButton:hover {\n"
"  background-color: #aed7ef;\n"
"}\n"
"#toggleButton:pressed {\n"
"  background-color: #9dceec;\n"
"}\n"
"#topMenu .QPushButton {\n"
"  background-position: left center;\n"
"  background-repeat: no-repeat;\n"
"  border: none;\n"
"  border-left: 22px solid transparent;\n"
"  background-color: transparent;\n"
"  text-align: left;\n"
"  padding-left: 44px;\n"
"  color: #fff;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"  background-color: #aed7ef;\n"
"}\n"
"#topMenu .QPushButton:p"
                        "ressed {\n"
"  background-color: #9dceec;\n"
"  color: #fff;\n"
"}\n"
"#bottomMenu .QPushButton {\n"
"  background-position: left center;\n"
"  background-repeat: no-repeat;\n"
"  border: none;\n"
"  border-left: 20px solid transparent;\n"
"  background-color: transparent;\n"
"  text-align: left;\n"
"  padding-left: 44px;\n"
"  color: #fff;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"  background-color: #aed7ef;\n"
"}\n"
"#bottomMenu .QPushButton:pressed {\n"
"  background-color: #9dceec;\n"
"}\n"
"#extraLeftBox {\n"
"  background-color: #fff;\n"
"  color: #333;\n"
"}\n"
"#extraTopBg {\n"
"  background-color: #7abee6;\n"
"}\n"
"#extraIcon {\n"
"  background-position: center;\n"
"  background-repeat: no-repeat;\n"
"  background-image: url(\":/icons/images/icons/icon_settings.png\");\n"
"}\n"
"#extraLabel {\n"
"  color: #fff;\n"
"}\n"
"#extraCloseColumnBtn {\n"
"  border: none;\n"
"  border-radius: 5px;\n"
"}\n"
"#extraCloseColumnBtn:hover {\n"
"  background-color: #aed7ef;\n"
"  border-style: solid;\n"
"  bo"
                        "rder-radius: 4px;\n"
"}\n"
"#extraCloseColumnBtn:pressed {\n"
"  background-color: #ec7d74;\n"
"  border-style: solid;\n"
"  border-radius: 4px;\n"
"}\n"
"#extraContent {\n"
"  background-color: #dcedf2;\n"
"  border-top: 3px solid #ec7d74;\n"
"  border-right: 1px solid #aed7ef;\n"
"}\n"
"#extraTopMenu .QPushButton {\n"
"  background-position: left center;\n"
"  background-repeat: no-repeat;\n"
"  border: none;\n"
"  border-left: 22px solid transparent;\n"
"  background-color: transparent;\n"
"  text-align: left;\n"
"  padding-left: 44px;\n"
"  color: #333;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"  background-color: #aed7ef;\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {\n"
"  background-color: #9dceec;\n"
"  color: #fff;\n"
"}\n"
"#contentTopBg {\n"
"  background-color: #a4cde6;\n"
"  border-bottom: 3px solid #aed7ef;\n"
"}\n"
"#titleRightInfo {\n"
"  padding-left: 10px;\n"
"  color: #fff;\n"
"  font: 15px;\n"
"}\n"
"#rightButtons .QPushButton {\n"
"  background-color: transparent;\n"
"  border: none"
                        ";\n"
"  border-radius: 5px;\n"
"}\n"
"#rightButtons .QPushButton:hover {\n"
"  background-color: #aed7ef;\n"
"  border-style: solid;\n"
"  border-radius: 4px;\n"
"}\n"
"#rightButtons .QPushButton:pressed {\n"
"  background-color: #ec7d74;\n"
"  border-style: solid;\n"
"  border-radius: 4px;\n"
"}\n"
"#extraRightBox {\n"
"  background-color: #dcedf2;\n"
"  border-left: 1px solid #a4cde6;\n"
"}\n"
"#themeSettingsTopDetail {\n"
"  background-color: #ec7d74;\n"
"}\n"
"#contentSettings .QPushButton {\n"
"  background-position: left center;\n"
"  background-repeat: no-repeat;\n"
"  border: none;\n"
"  border-left: 22px solid transparent;\n"
"  background-color: transparent;\n"
"  text-align: left;\n"
"  padding-left: 44px;\n"
"  color: #333;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"  background-color: #aed7ef;\n"
"}\n"
"#contentSettings .QPushButton:pressed {\n"
"  background-color: #aed7ef;\n"
"  color: #fff;\n"
"}\n"
"/* \u5e95\u90e8\u72b6\u6001\u680f */\n"
"#bottomBar .QLabel {\n"
"  color: #333;\n"
" "
                        " font-size: 14px;\n"
"  padding-left: 10px;\n"
"  padding-right: 10px;\n"
"  padding-bottom: 2px;\n"
"}\n"
"#pagesContainer QPushButton {\n"
"  border: 2px solid #A0CBDA;\n"
"  border-radius: 5px;\n"
"  background-color: #A0CBDA;\n"
"  color: #fff;\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"  background-color: #73B2C9;\n"
"  border: 2px solid #73B2C9;\n"
"}\n"
"#pagesContainer QPushButton:pressed {\n"
"  background-color: #91a3d5;\n"
"  border: 2px solid #91a3d5;\n"
"}\n"
"#pagesContainer QCommandLinkButton {\n"
"  border-radius: 5px;\n"
"  padding: 5px;\n"
"  border: 2px solid #91a3d5;\n"
"  color: #ec7d74;\n"
"}\n"
"#pagesContainer QCommandLinkButton:hover {\n"
"  color: #ed837b;\n"
"  background-color: #7abee6;\n"
"}\n"
"#pagesContainer QCommandLinkButton:pressed {\n"
"  color: #aed7ef;\n"
"  background-color: #7abee6;\n"
"}\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"  border: 2px solid #7abee"
                        "6;\n"
"  width: 12px;\n"
"  height: 12px;\n"
"  border-radius: 3px;\n"
"  background: transparent;\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"  border: 2px solid #DAA0AE;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"  background: 2px solid #82C0D3;\n"
"  background-image: url(\":/icons/images/icons/cil-check-alt.png\");\n"
"}\n"
"\n"
"QSpinBox {\n"
"  border: 2px solid #7abee6;\n"
"  border-radius: 3px;\n"
"}\n"
"QSpinBox:hover {\n"
"  border: 2px solid #DAA0AE;\n"
"  border-radius: 3px;\n"
"}\n"
"QSpinBox::up-button {\n"
"  border: 2px solid #7abee6;\n"
"  background: 2px solid #7abee6;\n"
"  image: url(:/icons/images/icons/cil-chevron-top.png);\n"
"}\n"
"QSpinBox::down-button {\n"
"  border-left: 2px solid #7abee6;\n"
"  border-right: 2px solid #7abee6;\n"
"  border-bottom: 2px solid #7abee6;\n"
"  background: 2px solid #7abee6;\n"
"  image: url(:/icons/images/icons/cil-chevron-bottom.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
""
                        "RadioButton */\n"
"QRadioButton::indicator {\n"
"  border: 1px solid #7abee6;\n"
"  width: 12px;\n"
"  height: 12px;\n"
"  border-radius: 12px;\n"
"  background: transparent;\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"  border: 1px solid #DAA0AE;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"  background: 1px solid #DAA0AE;\n"
"}\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox {\n"
"  border-radius: 3px;\n"
"  border: 2px solid #7abee6;\n"
"  padding-left: 10px;\n"
"  color: #000;\n"
"  font-size:14px;\n"
"}\n"
"QComboBox:hover {\n"
"  border: 2px solid #DAA0AE;\n"
"}\n"
"QComboBox::drop-down {\n"
" font-size:14px;\n"
"  subcontrol-origin: padding;\n"
"  subcontrol-position: top right;\n"
"  width: 25px;\n"
"  border-left-width: 3px;\n"
"  border-left-color: #fff;\n"
"  border-left-style: solid;\n"
"  border-top-right-radius: 2px;\n"
"  border-bottom-right-radius: 2px;\n"
"  background-image: url(\":/icons/images/icons/"
                        "cil-arrow-bottom.png\");\n"
"  background-position: center;\n"
"  background-repeat: no-reperat;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"  color: #000;\n"
"  background-color: #fff;\n"
"  padding: 10px;\n"
"  selection-background-color: #DAA0AE;\n"
"}\n"
"QTextBrowser {\n"
"  border: none;\n"
"  background-color: #fff;\n"
"  padding: 10px;\n"
"  color: #333;\n"
"}\n"
"QTextBrowser QScrollBar:vertical {\n"
"  width: 8px;\n"
"}\n"
"QTextBrowser QScrollBar:horizontal {\n"
"  height: 8px;\n"
"}\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"  background-color: #F5F5F5;\n"
"  border-radius: 5px;\n"
"  border: 2px solid #7abee6;\n"
"  selection-color:  #CCE8FF;\n"
"  selection-background-color: #ec7d74;\n"
"  color: #333;\n"
"}\n"
"QLineEdit:hover {\n"
"  border: 2px solid #DAA0AE;\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 2px solid #DAA0AE;\n"
"}\n"
"/* //////////////////////////////////////////////////////////////////"
                        "///////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"  background-color: #7abee6;\n"
"  border-radius: 5px;\n"
"  padding: 10px;\n"
"  selection-color: #fff;\n"
"  selection-background-color: #ec7d74;\n"
"  color: #fff;\n"
"}\n"
"QPlainTextEdit QScrollBar:vertical {\n"
"  width: 8px;\n"
"}\n"
"QPlainTextEdit QScrollBar:horizontal {\n"
"  height: 8px;\n"
"}\n"
"QPlainTextEdit:hover {\n"
"  border: 2px solid #dcedf2;\n"
"}\n"
"QPlainTextEdit:focus {\n"
"  border: 2px solid #ec7d74;\n"
"}\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"\n"
"QTableWidget {\n"
"  background-color: transparent;\n"
"  padding: 0px;\n"
"  border-radius: 5px;\n"
"  gridline-color: #A0CBDA;\n"
"  outline: none;\n"
"}\n"
"QTabWidget::pane\n"
"{\n"
"	top:10px;\n"
"    border: none;  \n"
"\n"
"}\n"
"QTabBar::tab\n"
"{ \n"
"	background:transparent;\n"
"	border-bottom: 3px solid rgb(255,255,255);\n"
"	font-family:\"\u5fae\u8f6f\u96c5\u9ed1"
                        "\";\n"
"	font-size:18px;\n"
"	padding-left:0px;\n"
"	padding-right:0px;\n"
"	min-width: 85px;\n"
"	min-height:30px;		\n"
"}\n"
"QTabBar::tab:selected\n"
"{\n"
"	border-bottom: 3px solid rgb(236,65,65);\n"
"	color: rgb(55,55,55);\n"
"	font-size:18px;\n"
"	font-weight: bold;\n"
"} \n"
"\n"
"QTableWidget::item {\n"
"  border-color: #A0CBDA;\n"
"  padding-left: 0px;\n"
"  padding-right: 0px;\n"
"  gridline-color: #A0CBDA;\n"
"}\n"
"QTableWidget::item:selected {\n"
"  background-color: #aed7ef;\n"
"  color: #fff;\n"
"}\n"
"QTableWidget::horizontalHeader {\n"
"  background-color: #7abee6;\n"
"}\n"
"\n"
"\n"
"QHeaderView::section {\n"
"  background-color: #7abee6;\n"
"  max-width: 30px;\n"
"  border: none;\n"
"  border-style: none;\n"
"}\n"
"QHeaderView::section:horizontal {\n"
"  border: 1px solid #7abee6;\n"
"  background-color: #7abee6;\n"
"  padding: 3px;\n"
"  border-top-left-radius: 7px;\n"
"  border-top-right-radius: 7px;\n"
"  color: #fff;\n"
"}\n"
"QHeaderView::section:vertical {\n"
"  border: 1px solid #7ab"
                        "ee6;\n"
"}\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"  border: none;\n"
"  background: #7abee6;\n"
"  height: 8px;\n"
"  margin: 0px 21px 0 21px;\n"
"  border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"  background: #aed7ef;\n"
"  min-width: 25px;\n"
"  border-radius: 4px;\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"  border: none;\n"
"  background: #7abee6;\n"
"  width: 20px;\n"
"  border-top-right-radius: 4px;\n"
"  border-bottom-right-radius: 4px;\n"
"  subcontrol-position: right;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"  border: none;\n"
"  background: #7abee6;\n"
"  width: 20px;\n"
"  border-top-left-radius: 4px;\n"
"  border-bottom-left-radius: 4px;\n"
"  subcontrol-position: left;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal,\n"
"QScrollBar::down-arrow:horizontal {\n"
"  background: none;\n"
""
                        "}\n"
"QScrollBar::add-page:horizontal,\n"
"QScrollBar::sub-page:horizontal {\n"
"  background: none;\n"
"}\n"
"QScrollBar:vertical {\n"
"  border: none;\n"
"  background-color: #7abee6;\n"
"  width: 8px;\n"
"  margin: 21px 0 21px 0;\n"
"  border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"  background: #aed7ef;\n"
"  min-height: 25px;\n"
"  border-radius: 4px;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"  border: none;\n"
"  background: #7abee6;\n"
"  height: 20px;\n"
"  border-bottom-left-radius: 4px;\n"
"  border-bottom-right-radius: 4px;\n"
"  subcontrol-position: bottom;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"  border: none;\n"
"  background: #7abee6;\n"
"  height: 20px;\n"
"  border-top-left-radius: 4px;\n"
"  border-top-right-radius: 4px;\n"
"  subcontrol-position: top;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:vertical,\n"
"QScrollBar::down-arrow:vertical {\n"
"  background: none;\n"
"}\n"
"QScrollBar::add-page:vertical,\n"
"QS"
                        "crollBar::sub-page:vertical {\n"
"  background: none;\n"
"}\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"  border-radius: 5px;\n"
"  height: 10px;\n"
"  margin: 0px;\n"
"  background-color: #7abee6;\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"  background-color: #7abee6;\n"
"}\n"
"QSlider::handle:horizontal {\n"
"  background-color: #aed7ef;\n"
"  border: none;\n"
"  height: 10px;\n"
"  width: 10px;\n"
"  margin: 0px;\n"
"  border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"  background-color: #c39bff;\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"  background-color: #ec7d74;\n"
"}\n"
"QSlider::groove:vertical {\n"
"  border-radius: 5px;\n"
"  width: 10px;\n"
"  margin: 0px;\n"
"  background-color: #7abee6;\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"  background-color: #7abee6;\n"
"}\n"
"QSlider::handle:vertical {\n"
"  background-color: #aed7ef;\n"
"  border: none;\n"
""
                        "  height: 10px;\n"
"  width: 10px;\n"
"  margin: 0px;\n"
"  border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"  background-color: #c39bff;\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"  background-color: #ec7d74;\n"
"}\n"
"")
        self.verticalLayout_19 = QVBoxLayout(self.styleSheet)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(5, 5, 5, 5)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setMouseTracking(False)
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(240, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setMouseTracking(False)
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.topLogo = QWidget(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(12, 9, 36, 36))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.topLogo.sizePolicy().hasHeightForWidth())
        self.topLogo.setSizePolicy(sizePolicy)
        self.topLogo.setMinimumSize(QSize(36, 36))
        self.topLogo.setMaximumSize(QSize(36, 36))
        self.topLogo.setStyleSheet(u"")
        self.btn_logo_login = QToolButton(self.topLogo)
        self.btn_logo_login.setObjectName(u"btn_logo_login")
        self.btn_logo_login.setGeometry(QRect(0, 0, 36, 36))
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_logo_login.sizePolicy().hasHeightForWidth())
        self.btn_logo_login.setSizePolicy(sizePolicy1)
        self.btn_logo_login.setMinimumSize(QSize(36, 36))
        self.btn_logo_login.setStyleSheet(u"border-image: url(:/icon/resource/icons/NJtech02.ico);")
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy2)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy2.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy2)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_message = QPushButton(self.topMenu)
        self.btn_message.setObjectName(u"btn_message")
        sizePolicy2.setHeightForWidth(self.btn_message.sizePolicy().hasHeightForWidth())
        self.btn_message.setSizePolicy(sizePolicy2)
        self.btn_message.setMinimumSize(QSize(0, 45))
        self.btn_message.setFont(font)
        self.btn_message.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_message.setLayoutDirection(Qt.LeftToRight)
        self.btn_message.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-envelope-closed.png);")

        self.verticalLayout_8.addWidget(self.btn_message)

        self.btn_setting = QPushButton(self.topMenu)
        self.btn_setting.setObjectName(u"btn_setting")
        sizePolicy2.setHeightForWidth(self.btn_setting.sizePolicy().hasHeightForWidth())
        self.btn_setting.setSizePolicy(sizePolicy2)
        self.btn_setting.setMinimumSize(QSize(0, 45))
        self.btn_setting.setFont(font)
        self.btn_setting.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_setting.setLayoutDirection(Qt.LeftToRight)
        self.btn_setting.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-settings.png);")

        self.verticalLayout_8.addWidget(self.btn_setting)

        self.btn_about = QPushButton(self.topMenu)
        self.btn_about.setObjectName(u"btn_about")
        sizePolicy2.setHeightForWidth(self.btn_about.sizePolicy().hasHeightForWidth())
        self.btn_about.setSizePolicy(sizePolicy2)
        self.btn_about.setMinimumSize(QSize(0, 45))
        self.btn_about.setFont(font)
        self.btn_about.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_about.setLayoutDirection(Qt.LeftToRight)
        self.btn_about.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-layers.png);")

        self.verticalLayout_8.addWidget(self.btn_about)

        self.btn_exit = QPushButton(self.topMenu)
        self.btn_exit.setObjectName(u"btn_exit")
        sizePolicy2.setHeightForWidth(self.btn_exit.sizePolicy().hasHeightForWidth())
        self.btn_exit.setSizePolicy(sizePolicy2)
        self.btn_exit.setMinimumSize(QSize(0, 45))
        self.btn_exit.setFont(font)
        self.btn_exit.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_exit.setLayoutDirection(Qt.LeftToRight)
        self.btn_exit.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-x.png);")

        self.verticalLayout_8.addWidget(self.btn_exit)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.toggleLeftBox = QPushButton(self.bottomMenu)
        self.toggleLeftBox.setObjectName(u"toggleLeftBox")
        sizePolicy2.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
        self.toggleLeftBox.setSizePolicy(sizePolicy2)
        self.toggleLeftBox.setMinimumSize(QSize(0, 45))
        self.toggleLeftBox.setFont(font)
        self.toggleLeftBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleLeftBox.setLayoutDirection(Qt.LeftToRight)
        self.toggleLeftBox.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-people.png);")

        self.verticalLayout_9.addWidget(self.toggleLeftBox)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setMouseTracking(False)
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon1)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)

        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-mood-good.png);")
        self.extraIcon.setFrameShape(QFrame.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setMinimumSize(QSize(0, 0))
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.loginLayout = QVBoxLayout()
        self.loginLayout.setSpacing(0)
        self.loginLayout.setObjectName(u"loginLayout")

        self.verticalLayout_12.addLayout(self.loginLayout)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setMinimumSize(QSize(0, 0))
        self.contentBox.setMaximumSize(QSize(16777215, 16777215))
        self.contentBox.setMouseTracking(False)
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy3)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = TitleBar(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy4)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        font3 = QFont()
        font3.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font3.setBold(False)
        font3.setItalic(False)
        self.titleRightInfo.setFont(font3)
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/cil-menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsTopBtn.setIcon(icon2)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon3)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font4 = QFont()
        font4.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font4.setPointSize(12)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font4)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon4)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setIcon(icon1)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setFont(font)
        self.stackedWidget.setStyleSheet(u"")
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.home_page.setStyleSheet(u"")
        self.verticalLayout_16 = QVBoxLayout(self.home_page)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.home_row_1 = QFrame(self.home_page)
        self.home_row_1.setObjectName(u"home_row_1")
        self.home_row_1.setFrameShape(QFrame.StyledPanel)
        self.home_row_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.home_row_1)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label = QLabel(self.home_row_1)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setTextFormat(Qt.MarkdownText)
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.label)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_3)

        self.textBrowserInteractInfo = QTextBrowser(self.home_row_1)
        self.textBrowserInteractInfo.setObjectName(u"textBrowserInteractInfo")

        self.horizontalLayout_8.addWidget(self.textBrowserInteractInfo)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_4)

        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 4)
        self.horizontalLayout_8.setStretch(2, 1)

        self.verticalLayout_24.addLayout(self.horizontalLayout_8)


        self.verticalLayout_26.addLayout(self.verticalLayout_24)


        self.verticalLayout_16.addWidget(self.home_row_1)

        self.home_row_2 = QFrame(self.home_page)
        self.home_row_2.setObjectName(u"home_row_2")
        self.home_row_2.setFrameShape(QFrame.StyledPanel)
        self.home_row_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.home_row_2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.btn_authorize = QPushButton(self.home_row_2)
        self.btn_authorize.setObjectName(u"btn_authorize")
        sizePolicy5 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.btn_authorize.sizePolicy().hasHeightForWidth())
        self.btn_authorize.setSizePolicy(sizePolicy5)
        self.btn_authorize.setMinimumSize(QSize(120, 40))
        self.btn_authorize.setMaximumSize(QSize(200, 16777215))
        self.btn_authorize.setStyleSheet(u"background-color: rgb(0, 179, 134);")

        self.horizontalLayout_6.addWidget(self.btn_authorize)

        self.btn_logout_net = QPushButton(self.home_row_2)
        self.btn_logout_net.setObjectName(u"btn_logout_net")
        sizePolicy5.setHeightForWidth(self.btn_logout_net.sizePolicy().hasHeightForWidth())
        self.btn_logout_net.setSizePolicy(sizePolicy5)
        self.btn_logout_net.setMinimumSize(QSize(120, 40))
        self.btn_logout_net.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_6.addWidget(self.btn_logout_net)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)


        self.verticalLayout_10.addLayout(self.horizontalLayout_6)


        self.verticalLayout_16.addWidget(self.home_row_2)

        self.verticalLayout_16.setStretch(0, 3)
        self.verticalLayout_16.setStretch(1, 2)
        self.stackedWidget.addWidget(self.home_page)
        self.message_page = QWidget()
        self.message_page.setObjectName(u"message_page")
        self.message_page.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.message_page)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(15, 15, 15, 0)
        self.tabWidget = QTabWidget(self.message_page)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"background: transparent;")
        self.tab_notify = QWidget()
        self.tab_notify.setObjectName(u"tab_notify")
        self.verticalLayout_25 = QVBoxLayout(self.tab_notify)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.textBrowser_push_msg = QTextBrowser(self.tab_notify)
        self.textBrowser_push_msg.setObjectName(u"textBrowser_push_msg")

        self.verticalLayout_25.addWidget(self.textBrowser_push_msg)

        self.tabWidget.addTab(self.tab_notify, "")
        self.tab_feedback = QWidget()
        self.tab_feedback.setObjectName(u"tab_feedback")
        self.verticalLayout_11 = QVBoxLayout(self.tab_feedback)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.textBrowser_2 = QTextBrowser(self.tab_feedback)
        self.textBrowser_2.setObjectName(u"textBrowser_2")

        self.verticalLayout_11.addWidget(self.textBrowser_2)

        self.tabWidget.addTab(self.tab_feedback, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.stackedWidget.addWidget(self.message_page)
        self.setting_page = QWidget()
        self.setting_page.setObjectName(u"setting_page")
        self.layoutWidget_2 = QWidget(self.setting_page)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(30, 320, 141, 61))
        self.verticalLayout_34 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.layoutWidget_2)
        self.label_11.setObjectName(u"label_11")
        font5 = QFont()
        font5.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font5.setPointSize(12)
        font5.setBold(False)
        font5.setItalic(False)
        font5.setUnderline(False)
        font5.setStrikeOut(False)
        font5.setKerning(False)
        self.label_11.setFont(font5)

        self.verticalLayout_34.addWidget(self.label_11)

        self.comboBox_2 = QComboBox(self.layoutWidget_2)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setFont(font3)

        self.verticalLayout_34.addWidget(self.comboBox_2)

        self.layoutWidget = QWidget(self.setting_page)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 30, 661, 151))
        self.verticalLayout_17 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.setting_autorun = QLabel(self.layoutWidget)
        self.setting_autorun.setObjectName(u"setting_autorun")
        self.setting_autorun.setFont(font)

        self.verticalLayout_17.addWidget(self.setting_autorun)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_9 = QLabel(self.layoutWidget)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_9.addWidget(self.label_9)

        self.lineEdit = QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_9.addWidget(self.lineEdit)


        self.verticalLayout_17.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.checkBox_autorun_2 = QCheckBox(self.layoutWidget)
        self.checkBox_autorun_2.setObjectName(u"checkBox_autorun_2")
        self.checkBox_autorun_2.setEnabled(False)
        self.checkBox_autorun_2.setCheckable(False)

        self.horizontalLayout_10.addWidget(self.checkBox_autorun_2)

        self.horizontalSpacer_9 = QSpacerItem(10, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_9)

        self.label_10 = QLabel(self.layoutWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)

        self.horizontalLayout_10.addWidget(self.label_10)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_10)

        self.horizontalLayout_10.setStretch(0, 3)
        self.horizontalLayout_10.setStretch(1, 1)
        self.horizontalLayout_10.setStretch(2, 1)
        self.horizontalLayout_10.setStretch(3, 30)

        self.verticalLayout_17.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.checkBox_autorun = QCheckBox(self.layoutWidget)
        self.checkBox_autorun.setObjectName(u"checkBox_autorun")
        self.checkBox_autorun.setChecked(True)

        self.horizontalLayout_7.addWidget(self.checkBox_autorun)

        self.horizontalSpacer_8 = QSpacerItem(10, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_8)

        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_7.addWidget(self.label_7)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_7)

        self.horizontalLayout_7.setStretch(0, 3)
        self.horizontalLayout_7.setStretch(1, 1)
        self.horizontalLayout_7.setStretch(2, 1)
        self.horizontalLayout_7.setStretch(3, 30)

        self.verticalLayout_17.addLayout(self.horizontalLayout_7)

        self.layoutWidget1 = QWidget(self.setting_page)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(30, 210, 361, 81))
        self.verticalLayout_18 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.layoutWidget1)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.verticalLayout_18.addWidget(self.label_4)

        self.label_3 = QLabel(self.layoutWidget1)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_18.addWidget(self.label_3)

        self.checkBox_2 = QCheckBox(self.layoutWidget1)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setChecked(True)

        self.verticalLayout_18.addWidget(self.checkBox_2)

        self.layoutWidget2 = QWidget(self.setting_page)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(30, 410, 141, 61))
        self.verticalLayout_31 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.layoutWidget2)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_31.addWidget(self.label_8)

        self.comboBox = QComboBox(self.layoutWidget2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout_31.addWidget(self.comboBox)

        self.label_12 = QLabel(self.setting_page)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(30, 540, 281, 21))
        self.stackedWidget.addWidget(self.setting_page)
        self.about_page = QWidget()
        self.about_page.setObjectName(u"about_page")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.about_page.sizePolicy().hasHeightForWidth())
        self.about_page.setSizePolicy(sizePolicy6)
        self.verticalLayout_20 = QVBoxLayout(self.about_page)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(15, 15, 15, 0)
        self.tabWidget_2 = QTabWidget(self.about_page)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tab_version = QWidget()
        self.tab_version.setObjectName(u"tab_version")
        self.verticalLayout_22 = QVBoxLayout(self.tab_version)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 10, 0, 0)
        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setSpacing(12)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.btn_upgrade = QPushButton(self.tab_version)
        self.btn_upgrade.setObjectName(u"btn_upgrade")
        sizePolicy7 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.btn_upgrade.sizePolicy().hasHeightForWidth())
        self.btn_upgrade.setSizePolicy(sizePolicy7)
        self.btn_upgrade.setMinimumSize(QSize(0, 45))
        self.btn_upgrade.setMaximumSize(QSize(16777215, 45))
        self.btn_upgrade.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_21.addWidget(self.btn_upgrade)

        self.btn_upgradelog = QPushButton(self.tab_version)
        self.btn_upgradelog.setObjectName(u"btn_upgradelog")
        sizePolicy7.setHeightForWidth(self.btn_upgradelog.sizePolicy().hasHeightForWidth())
        self.btn_upgradelog.setSizePolicy(sizePolicy7)
        self.btn_upgradelog.setMinimumSize(QSize(0, 45))
        self.btn_upgradelog.setMaximumSize(QSize(16777215, 45))

        self.verticalLayout_21.addWidget(self.btn_upgradelog)

        self.btn_officeweb = QPushButton(self.tab_version)
        self.btn_officeweb.setObjectName(u"btn_officeweb")
        sizePolicy7.setHeightForWidth(self.btn_officeweb.sizePolicy().hasHeightForWidth())
        self.btn_officeweb.setSizePolicy(sizePolicy7)
        self.btn_officeweb.setMinimumSize(QSize(0, 45))
        self.btn_officeweb.setMaximumSize(QSize(16777215, 45))

        self.verticalLayout_21.addWidget(self.btn_officeweb)

        self.btn_usrAgreement = QPushButton(self.tab_version)
        self.btn_usrAgreement.setObjectName(u"btn_usrAgreement")
        self.btn_usrAgreement.setEnabled(True)
        sizePolicy7.setHeightForWidth(self.btn_usrAgreement.sizePolicy().hasHeightForWidth())
        self.btn_usrAgreement.setSizePolicy(sizePolicy7)
        self.btn_usrAgreement.setMinimumSize(QSize(0, 45))
        self.btn_usrAgreement.setMaximumSize(QSize(16777215, 45))
        self.btn_usrAgreement.setFlat(False)

        self.verticalLayout_21.addWidget(self.btn_usrAgreement)

        self.btn_privacyPolice = QPushButton(self.tab_version)
        self.btn_privacyPolice.setObjectName(u"btn_privacyPolice")
        self.btn_privacyPolice.setEnabled(True)
        sizePolicy7.setHeightForWidth(self.btn_privacyPolice.sizePolicy().hasHeightForWidth())
        self.btn_privacyPolice.setSizePolicy(sizePolicy7)
        self.btn_privacyPolice.setMinimumSize(QSize(0, 45))
        self.btn_privacyPolice.setMaximumSize(QSize(16777215, 45))
        self.btn_privacyPolice.setFlat(False)

        self.verticalLayout_21.addWidget(self.btn_privacyPolice)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer)

        self.verticalLayout_30 = QVBoxLayout()
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")

        self.verticalLayout_21.addLayout(self.verticalLayout_30)


        self.verticalLayout_22.addLayout(self.verticalLayout_21)

        self.tabWidget_2.addTab(self.tab_version, "")
        self.tab_help = QWidget()
        self.tab_help.setObjectName(u"tab_help")
        self.verticalLayout_29 = QVBoxLayout(self.tab_help)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 10, 0, 0)
        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setSpacing(12)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.btn_csdn = QPushButton(self.tab_help)
        self.btn_csdn.setObjectName(u"btn_csdn")
        self.btn_csdn.setMinimumSize(QSize(0, 45))

        self.verticalLayout_27.addWidget(self.btn_csdn)

        self.btn_prjurl = QPushButton(self.tab_help)
        self.btn_prjurl.setObjectName(u"btn_prjurl")
        self.btn_prjurl.setMinimumSize(QSize(0, 45))

        self.verticalLayout_27.addWidget(self.btn_prjurl)

        self.btn_getHelp = QPushButton(self.tab_help)
        self.btn_getHelp.setObjectName(u"btn_getHelp")
        self.btn_getHelp.setMinimumSize(QSize(0, 45))

        self.verticalLayout_27.addWidget(self.btn_getHelp)

        self.btn_feedback = QPushButton(self.tab_help)
        self.btn_feedback.setObjectName(u"btn_feedback")
        self.btn_feedback.setMinimumSize(QSize(0, 45))

        self.verticalLayout_27.addWidget(self.btn_feedback)

        self.textBrowser_help = QTextBrowser(self.tab_help)
        self.textBrowser_help.setObjectName(u"textBrowser_help")

        self.verticalLayout_27.addWidget(self.textBrowser_help)


        self.verticalLayout_29.addLayout(self.verticalLayout_27)

        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")

        self.verticalLayout_29.addLayout(self.verticalLayout_28)

        self.tabWidget_2.addTab(self.tab_help, "")
        self.tab_donate = QWidget()
        self.tab_donate.setObjectName(u"tab_donate")
        self.verticalLayout_33 = QVBoxLayout(self.tab_donate)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 10, 0, 0)
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 15, -1, -1)
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_5)

        self.label_2 = QLabel(self.tab_donate)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(200, 200))
        self.label_2.setMaximumSize(QSize(200, 200))
        self.label_2.setStyleSheet(u"border-image: url(:/payQR/images/donate/AliPay.jpg);")
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_2)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_6)


        self.verticalLayout_33.addLayout(self.horizontalLayout_13)

        self.verticalLayout_32 = QVBoxLayout()
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.textBrowser = QTextBrowser(self.tab_donate)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout_32.addWidget(self.textBrowser)


        self.verticalLayout_33.addLayout(self.verticalLayout_32)

        self.verticalLayout_33.setStretch(0, 2)
        self.verticalLayout_33.setStretch(1, 3)
        self.tabWidget_2.addTab(self.tab_donate, "")
        self.tab_license = QWidget()
        self.tab_license.setObjectName(u"tab_license")
        self.verticalLayout_23 = QVBoxLayout(self.tab_license)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 10, 0, 0)
        self.textBrowser_license = QTextBrowser(self.tab_license)
        self.textBrowser_license.setObjectName(u"textBrowser_license")

        self.verticalLayout_23.addWidget(self.textBrowser_license)

        self.tabWidget_2.addTab(self.tab_license, "")

        self.verticalLayout_20.addWidget(self.tabWidget_2)

        self.stackedWidget.addWidget(self.about_page)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setLayoutDirection(Qt.LeftToRight)
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setLayoutDirection(Qt.LeftToRight)
        self.topMenus.setFrameShape(QFrame.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy2.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy2)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font)
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LeftToRight)
        self.btn_logout.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-account-logout.png);")
        self.btn_logout.setIconSize(QSize(16, 16))
        self.btn_logout.setFlat(False)

        self.verticalLayout_14.addWidget(self.btn_logout)

        self.btn_print = QPushButton(self.topMenus)
        self.btn_print.setObjectName(u"btn_print")
        sizePolicy2.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
        self.btn_print.setSizePolicy(sizePolicy2)
        self.btn_print.setMinimumSize(QSize(0, 45))
        self.btn_print.setFont(font)
        self.btn_print.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_print.setLayoutDirection(Qt.LeftToRight)
        self.btn_print.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-print.png);")

        self.verticalLayout_14.addWidget(self.btn_print)

        self.btn_message_ = QPushButton(self.topMenus)
        self.btn_message_.setObjectName(u"btn_message_")
        self.btn_message_.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.btn_message_.sizePolicy().hasHeightForWidth())
        self.btn_message_.setSizePolicy(sizePolicy2)
        self.btn_message_.setMinimumSize(QSize(0, 45))
        self.btn_message_.setFont(font)
        self.btn_message_.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_message_.setLayoutDirection(Qt.LeftToRight)
        self.btn_message_.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-envelope-open.png);")

        self.verticalLayout_14.addWidget(self.btn_message_)


        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        self.creditsLabel.setFont(font3)
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version_code = QLabel(self.bottomBar)
        self.version_code.setObjectName(u"version_code")
        self.version_code.setLayoutDirection(Qt.LeftToRight)
        self.version_code.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version_code)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.verticalLayout_19.addWidget(self.bgApp)

        CustoWdo.setCentralWidget(self.styleSheet)

        self.retranslateUi(CustoWdo)
        self.minimizeAppBtn.clicked.connect(CustoWdo.showMinimized)
        self.closeAppBtn.clicked.connect(CustoWdo.hide)

        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(CustoWdo)
    # setupUi

    def retranslateUi(self, CustoWdo):
        CustoWdo.setWindowTitle(QCoreApplication.translate("CustoWdo", u"MainWindow", None))
        self.actQuit.setText(QCoreApplication.translate("CustoWdo", u"\u5b8c\u5168\u9000\u51fa", None))
#if QT_CONFIG(tooltip)
        self.actQuit.setToolTip(QCoreApplication.translate("CustoWdo", u"\u9000\u51fa\u540e\u5c06\u65e0\u6cd5\u5b88\u62a4\u7f51\u7edc", None))
#endif // QT_CONFIG(tooltip)
        self.btn_logo_login.setText("")
        self.titleLeftApp.setText(QCoreApplication.translate("CustoWdo", u"NJTECH SOFT", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("CustoWdo", u"campus net auto authorize", None))
        self.toggleButton.setText(QCoreApplication.translate("CustoWdo", u"\u9690\u85cf\u83dc\u5355", None))
        self.btn_home.setText(QCoreApplication.translate("CustoWdo", u"\u4e3b\u9875\u529f\u80fd", None))
        self.btn_message.setText(QCoreApplication.translate("CustoWdo", u"\u6d88\u606f\u516c\u544a", None))
        self.btn_setting.setText(QCoreApplication.translate("CustoWdo", u"\u8bbe\u7f6e\u4e2d\u5fc3", None))
        self.btn_about.setText(QCoreApplication.translate("CustoWdo", u"\u5173\u4e8e\u8f6f\u4ef6", None))
        self.btn_exit.setText(QCoreApplication.translate("CustoWdo", u"\u9000\u51fa\u8f6f\u4ef6", None))
        self.toggleLeftBox.setText(QCoreApplication.translate("CustoWdo", u"\u7528\u6237\u767b\u5f55", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("CustoWdo", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.extraLabel.setText(QCoreApplication.translate("CustoWdo", u"\u6b22\u8fce\u4f7f\u7528", None))
        self.titleRightInfo.setText(QCoreApplication.translate("CustoWdo", u"\u5357\u4eac\u5de5\u4e1a\u5927\u5b66\u7f51\u7edc\u670d\u52a1 - \u7545\u4eab\u6781\u81f4\u7f51\u7edc", None))
#if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("CustoWdo", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("CustoWdo", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("CustoWdo", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("CustoWdo", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.label.setText(QCoreApplication.translate("CustoWdo", u"## \u6b22\u8fce\u4f7f\u7528\u5357\u5de5\u8ba4\u8bc1", None))
        self.textBrowserInteractInfo.setHtml(QCoreApplication.translate("CustoWdo", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:'\u5fae\u8f6f\u96c5\u9ed1'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:10pt;\"><br /></p></body></html>", None))
        self.btn_authorize.setText(QCoreApplication.translate("CustoWdo", u"\u4e00\u952e\u8ba4\u8bc1", None))
        self.btn_logout_net.setText(QCoreApplication.translate("CustoWdo", u"\u9000\u51fa\u8ba4\u8bc1", None))
        self.textBrowser_push_msg.setHtml(QCoreApplication.translate("CustoWdo", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:'\u5fae\u8f6f\u96c5\u9ed1'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u6682\u65e0\u6d88\u606f</p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_notify), QCoreApplication.translate("CustoWdo", u"\u901a\u77e5\u4e2d\u5fc3", None))
        self.textBrowser_2.setHtml(QCoreApplication.translate("CustoWdo", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:'\u5fae\u8f6f\u96c5\u9ed1'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u6682\u65e0\u6d88\u606f</p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_feedback), QCoreApplication.translate("CustoWdo", u"\u8054\u7cfb\u53cd\u9988", None))
        self.label_11.setText(QCoreApplication.translate("CustoWdo", u"<html><head/><body><p><span style=\" font-weight:700;\">\u4e3b\u9898\u989c\u8272</span></p></body></html>", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("CustoWdo", u"\u8f6f\u4ef6\u9ed8\u8ba4", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("CustoWdo", u"\u8fd8\u6ca1\u6709\u5199", None))

        self.setting_autorun.setText(QCoreApplication.translate("CustoWdo", u"<html><head/><body><p><span style=\" font-weight:700;\">\u5f00\u673a\u542f\u52a8</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("CustoWdo", u"\u6ce8\u518c\u8def\u5f84", None))
        self.lineEdit.setText(QCoreApplication.translate("CustoWdo", u"\\HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Run", None))
#if QT_CONFIG(tooltip)
        self.checkBox_autorun_2.setToolTip(QCoreApplication.translate("CustoWdo", u"<html><head/><body><p>\u5b9e\u73b0\u66f4\u5feb\u7684\u5f00\u673a\u81ea\u542f\uff0c\u9700\u7ba1\u7406\u5458\u6743\u9650\u6253\u5f00\u7a0b\u5e8f</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_autorun_2.setText(QCoreApplication.translate("CustoWdo", u"\u5f3a\u529b\u81ea\u542f", None))
        self.label_10.setText(QCoreApplication.translate("CustoWdo", u"<html><head/><body><p><span style=\" color:#626262;\">\u5b9e\u73b0\u66f4\u5feb\u81ea\u542f (\u8be5\u529f\u80fd\u5f00\u53d1\u4e2d)</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.checkBox_autorun.setToolTip(QCoreApplication.translate("CustoWdo", u"<html><head/><body><p>\u5f00\u673a\u81ea\u52a8\u8fdb\u884c\u7f51\u7edc\u767b\u5f55\u8ba4\u8bc1</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_autorun.setText(QCoreApplication.translate("CustoWdo", u"\u5f00\u673a\u81ea\u542f", None))
        self.label_7.setText(QCoreApplication.translate("CustoWdo", u"<html><head/><body><p><span style=\" color:#626262;\">\u5728\u6821\u671f\u95f4\u52a1\u5fc5\u52fe\u9009</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("CustoWdo", u"<html><head/><body><p><span style=\" font-weight:700;\">\u7248\u672c\u66f4\u65b0</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("CustoWdo", u"\u5efa\u8bae\u4fdd\u6301\u6700\u65b0\uff0c\u4eab\u53d7\u66f4\u4f18\u7684\u7f51\u7edc\u4f53\u9a8c", None))
#if QT_CONFIG(tooltip)
        self.checkBox_2.setToolTip(QCoreApplication.translate("CustoWdo", u"<html><head/><body><p>\u5f00\u673a\u8ba4\u8bc1\u65f6\u81ea\u52a8\u68c0\u67e5\u66f4\u65b0</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_2.setText(QCoreApplication.translate("CustoWdo", u"\u81ea\u52a8\u68c0\u67e5", None))
        self.label_8.setText(QCoreApplication.translate("CustoWdo", u"<html><head/><body><p><span style=\" font-weight:700;\">\u663e\u793a\u8bed\u8a00</span></p></body></html>", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("CustoWdo", u"\u7b80\u4f53\u4e2d\u6587", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("CustoWdo", u"\u53ea\u6709\u4e2d\u6587", None))

        self.label_12.setText(QCoreApplication.translate("CustoWdo", u"<html><head/><body><p><span style=\" color:#626262;\">\u6ce8\u610f\uff1a\u8be5\u9875\u8bbe\u7f6e\u76ee\u524d\u65e0\u7528</span></p></body></html>", None))
        self.btn_upgrade.setText(QCoreApplication.translate("CustoWdo", u"\u68c0\u67e5\u66f4\u65b0", None))
        self.btn_upgradelog.setText(QCoreApplication.translate("CustoWdo", u"\u66f4\u65b0\u65e5\u5fd7", None))
        self.btn_officeweb.setText(QCoreApplication.translate("CustoWdo", u"\u524d\u5f80\u5b98\u7f51", None))
        self.btn_usrAgreement.setText(QCoreApplication.translate("CustoWdo", u"\u7528\u6237\u534f\u8bae", None))
        self.btn_privacyPolice.setText(QCoreApplication.translate("CustoWdo", u"\u9690\u79c1\u653f\u7b56", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_version), QCoreApplication.translate("CustoWdo", u"\u8f6f\u4ef6\u4fe1\u606f", None))
        self.btn_csdn.setText(QCoreApplication.translate("CustoWdo", u"CSDN\u535a\u5ba2 @Alpherkin", None))
        self.btn_prjurl.setText(QCoreApplication.translate("CustoWdo", u"\u9879\u76ee\u5730\u5740   @NjtechAutoLogin", None))
        self.btn_getHelp.setText(QCoreApplication.translate("CustoWdo", u"\u83b7\u53d6\u5e2e\u52a9", None))
        self.btn_feedback.setText(QCoreApplication.translate("CustoWdo", u"\u95ee\u9898\u53cd\u9988", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_help), QCoreApplication.translate("CustoWdo", u"\u5e2e\u52a9\u8bf4\u660e", None))
        self.label_2.setText("")
        self.textBrowser.setHtml(QCoreApplication.translate("CustoWdo", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:'\u5fae\u8f6f\u96c5\u9ed1'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">\u6070\u4e2a\u996d</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">\u5982\u679c\u89c9\u5f97\u8fd8\u7b97"
                        "\u597d\u7528\uff0c\u8bf7\u5173\u6ce8\u6211\u7684CSDN\u535a\u5ba2\u5427</span><span style=\" font-size:18pt;\"> </span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_donate), QCoreApplication.translate("CustoWdo", u"\u6350\u8d60\u652f\u6301", None))
        self.textBrowser_license.setHtml(QCoreApplication.translate("CustoWdo", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:'\u5fae\u8f6f\u96c5\u9ed1'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u6b63\u5728\u52a0\u8f7d\u4e2d...</p></body></html>", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_license), QCoreApplication.translate("CustoWdo", u"\u5f00\u6e90\u8bb8\u53ef", None))
        self.btn_logout.setText(QCoreApplication.translate("CustoWdo", u"\u524d\u5f80\u5b98\u7f51", None))
        self.btn_print.setText(QCoreApplication.translate("CustoWdo", u"\u524d\u5f80\u535a\u5ba2", None))
        self.btn_message_.setText(QCoreApplication.translate("CustoWdo", u"\u540e\u7eed\u5f00\u53d1", None))
        self.creditsLabel.setText("")
        self.version_code.setText(QCoreApplication.translate("CustoWdo", u"v1.0.0", None))
    # retranslateUi

