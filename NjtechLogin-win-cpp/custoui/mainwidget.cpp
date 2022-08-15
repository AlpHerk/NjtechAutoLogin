#include <QDir>
#include <QFile>
#include <QMouseEvent>
#include <QPropertyAnimation>
#include <QCryptographicHash>
#include <QParallelAnimationGroup>
#include <QGraphicsDropShadowEffect>

#include "ui_mainwidget.h"
#include "custoui/titlebar.h"
#include "custoui/appsetting.h"
#include "custoui/mainwidget.h"



CustoWdo::CustoWdo(QWidget *parent):
    QMainWindow(parent),
    ui(new Ui::CustoWdo)
{
    ui->setupUi(this);
    QApplication::setQuitOnLastWindowClosed(false);
    setWindowFlag(Qt::FramelessWindowHint);
    setAttribute(Qt::WA_TranslucentBackground);

    /// 设置窗口阴影
    QGraphicsDropShadowEffect *shadow = new QGraphicsDropShadowEffect(this);
    shadow->setColor(Qt::black);
    shadow->setBlurRadius(5);
    shadow->setOffset(0);
    setGraphicsEffect(shadow);


    /// 设置任务栏托盘
    QMenu *trayMenu = new QMenu(this);
    trayMenu->addAction(ui->actQuit);

    QSystemTrayIcon *systemTray = new QSystemTrayIcon(this);
    systemTray->setIcon(QIcon(":/icon/resource/icons/NJtech02.ico"));
    systemTray->setToolTip("校园网守护中~");
    systemTray->setContextMenu(trayMenu);
    systemTray->show();

    connect(ui->actQuit, &QAction::triggered, this,  &QCoreApplication::quit);
    connect(systemTray,  SIGNAL(activated(QSystemTrayIcon::ActivationReason)),
                this, SLOT(sysTrayCilick(QSystemTrayIcon::ActivationReason)));


    /// 伸缩盒子
    connect(ui->toggleButton,   &QPushButton::clicked, this, &CustoWdo::toggleMenu);
    connect(ui->toggleLeftBox,  &QPushButton::clicked, this, &CustoWdo::toggleLeftBox);
    connect(ui->settingsTopBtn, &QPushButton::clicked, this, &CustoWdo::toggleRightBox);
    connect(ui->extraCloseColumnBtn,&QPushButton::clicked, this, &CustoWdo::toggleLeftBox);

    /// 双击标题栏窗口变化
    connect(ui->titleRightInfo, &TitleBar::doubleClick, this, &CustoWdo::maximizeRestore);
    connect(ui->maximizeRestoreAppBtn, &QPushButton::clicked, this, &CustoWdo::maximizeRestore);

}

CustoWdo::~CustoWdo()
{
    delete ui;
}

void CustoWdo::sysTrayCilick(QSystemTrayIcon::ActivationReason action)
{
    switch (action) {
        case QSystemTrayIcon::Trigger:
            showNormalize(); //单击托盘图标
            break;
        case QSystemTrayIcon::DoubleClick:
            showNormalize(); //双击后显示主程序窗口
            break;
        default: break;
    }
}

void CustoWdo::showMaximize()
{
    showMaximized();
    ui->maximizeRestoreAppBtn->setToolTip("Restore");
    ui->maximizeRestoreAppBtn->setIcon(QIcon(":/icons/images/icons/icon_restore.png"));
}

void CustoWdo::showNormalize()
{
    showNormal();
    ui->maximizeRestoreAppBtn->setToolTip("Maximize");
    ui->maximizeRestoreAppBtn->setIcon(QIcon(":/icons/images/icons/icon_maximize.png"));
}

void CustoWdo::maximizeRestore()
{
    Qt::WindowStates state = windowState();
    if (state & Qt::WindowMaximized) {
        showNormalize();
    } else {
        showMaximize();
    }
}





QString CustoWdo::selectMenu(QString getStyle)
{
    return getStyle + MENU_SELECTED_STYLESHEET;
}
QString CustoWdo::deselectMenu(QString getStyle)
{
    return getStyle.replace(MENU_SELECTED_STYLESHEET, "");
}

void CustoWdo::selectStandardMenu(QString widget)
{
    foreach (QPushButton *w, ui->topMenu->findChildren<QPushButton *>()){
        if (w->objectName() == widget) {
            w->setStyleSheet(selectMenu(w->styleSheet()));
            delete w;
        }
    }
}

void CustoWdo::resetStyle(QString widget)
{
    foreach (QPushButton *btnChild, ui->topMenu->findChildren<QPushButton *>()){
        if (btnChild->objectName() != widget) {
            btnChild->setStyleSheet(deselectMenu(btnChild->styleSheet()));
        }
    }
}

void CustoWdo::theme(QString filename, bool useCustomTheme)
{
    if (useCustomTheme) {
        QFile file(filename.arg(QDir::currentPath()));
        file.open(QFile::ReadOnly);
        ui->styleSheet->setStyleSheet(file.readAll());
        file.close();
    }
}




void CustoWdo::toggleMenu()
{
    int width = ui->leftMenuBg->width();
    int maxExtend = MENU_WIDTH;
    int widthExtended;

    // 菜单的最大宽度
    if (width < maxExtend) widthExtended = maxExtend;
    else widthExtended = MENU_STANDARD;

    // 菜单切换动画
    QPropertyAnimation *animation = new QPropertyAnimation(ui->leftMenuBg, "minimumWidth");
    animation->setDuration(TIME_ANIMATION);
    animation->setStartValue(width);
    animation->setEndValue(widthExtended);
    animation->setEasingCurve(QEasingCurve::InOutQuart);
    animation->start();

}


void CustoWdo::start_box_animation(int left_box_width, int right_box_width, QString direction)
{
    int right_width = 0;
    int left_width  = 0 ;

    if (left_box_width == 0 and direction == "left") left_width = LEFT_BOX_WIDTH;

    if (right_box_width == 0 and direction == "right") right_width = RIGHT_BOX_WIDTH;

    // 左侧伸缩盒子动画
    QPropertyAnimation *animation1 = new QPropertyAnimation(ui->extraLeftBox, "minimumWidth");
    animation1->setDuration(TIME_ANIMATION);
    animation1->setStartValue(left_box_width);
    animation1->setEndValue(left_width);
    animation1->setEasingCurve(QEasingCurve::InOutQuart);

    // 右侧伸缩盒子动画
    QPropertyAnimation *animation2 = new QPropertyAnimation(ui->extraRightBox, "minimumWidth");
    animation2->setDuration(TIME_ANIMATION);
    animation2->setStartValue(right_box_width);
    animation2->setEndValue(right_width);
    animation2->setEasingCurve(QEasingCurve::InOutQuart);

    // 左右盒子组合动画
    QParallelAnimationGroup *animgroup = new QParallelAnimationGroup;
    animgroup->addAnimation(animation1);
    animgroup->addAnimation(animation2);
    animgroup->start();
}

void CustoWdo::toggleLeftBox()
{
    int leftBoxWidth = ui->extraLeftBox->width();
    int righBoxWidth = ui->extraRightBox->width();
    QString style = ui->toggleLeftBox->styleSheet();
    QString color = BTN_LEFT_BOX_COLOR;

    if (leftBoxWidth < LEFT_BOX_WIDTH) {
        ui->toggleLeftBox->setStyleSheet(style + color);
        if (righBoxWidth > RIGHT_BOX_MIN) {
            QString style = ui->settingsTopBtn->styleSheet();
            ui->settingsTopBtn->setStyleSheet(style.replace(BTN_RIGHT_BOX_COLOR, ""));
        }
    } else {
        ui->toggleLeftBox->setStyleSheet(style.replace(color, ""));
    }
    start_box_animation(leftBoxWidth, righBoxWidth, "left");

}

void CustoWdo::toggleRightBox()
{
    int righBoxWidth = ui->extraRightBox->width();
    int leftBoxWidth = ui->extraLeftBox->width();

    QString color = BTN_RIGHT_BOX_COLOR;
    QString style = ui->settingsTopBtn->styleSheet();

    if (righBoxWidth < RIGHT_BOX_WIDTH) {
        ui->settingsTopBtn->setStyleSheet(style + color);
        if (leftBoxWidth > LEFT_BOX_MIN) {
            QString style = ui->toggleLeftBox->styleSheet();
            ui->toggleLeftBox->setStyleSheet(style.replace(BTN_LEFT_BOX_COLOR, ""));
        }
    } else {
        ui->settingsTopBtn->setStyleSheet(style.replace(color, ""));
    }
    start_box_animation(leftBoxWidth, righBoxWidth, "right");
}





