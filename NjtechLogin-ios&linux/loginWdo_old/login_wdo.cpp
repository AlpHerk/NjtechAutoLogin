#include <QSettings>
#include <QMouseEvent>
#include <QCryptographicHash>
#include <QGraphicsDropShadowEffect>

#include "constants.h"
#include "ui_login_wdo.h"
#include "window/login_wdo.h"
#include "window/main_wdo.h"


LoginWdo::LoginWdo(QWidget *parent):
    QDialog(parent),
    ui(new Ui::LoginWdo)
{
    ui->setupUi(this);
    this->setWindowFlag(Qt::FramelessWindowHint);
    this->setAttribute(Qt::WA_TranslucentBackground);

    QGraphicsDropShadowEffect *shadow = new QGraphicsDropShadowEffect();
    shadow->setColor(Qt::black);
    shadow->setBlurRadius(5);
    shadow->setOffset(0);
    setGraphicsEffect(shadow);
    mouseMoving = false;
    readSettings();
}

LoginWdo::~LoginWdo() {
    delete ui;
}


// 登录界面相关数据 *************************************************
void LoginWdo::readSettings()
{
    //HKEY_CURRENT_USER/Software/"AUTHOR"/"SOFTNAME"
    QSettings settings(AUTHOR, SOFTNAME);
    QString username     = settings.value(LOGIN_KEY1,     "").toString();
    QString password     = settings.value(LOGIN_KEY2,     "").toString();
    int  netCorpCode     = settings.value(LOGIN_KEY5,      0).toInt();
    int    reconnect     = settings.value(SETTING_KEY1,    5).toInt();
    bool     autoRun     = settings.value(SETTING_KEY2, true).toBool();
    bool    showinfo     = settings.value(SETTING_KEY3,false).toBool();

    ui->editUserName     ->setText(username);
    ui->editPassWord     ->setText(password);
    ui->ckboxPowerBoot   ->setChecked(autoRun);
    ui->cmboxChannel     ->setCurrentIndex(netCorpCode);
    ui->spboxConnectTime ->setValue(reconnect);
    ui->ckboxShowLogin   ->setChecked(showinfo);
}

void LoginWdo::writeSettings()
{
    //保存登录界面信息设置
    int netCorpCode   = ui->cmboxChannel->currentIndex();
    QString netCorpCn = "中国移动";
    QString netCorpEn = "@cmcc";

    if (netCorpCode != 0) {
        netCorpCn   = "中国电信";
        netCorpEn   = "@telecom";
    }
    QSettings settings(AUTHOR, SOFTNAME);                               // 注册表键组
    settings.setValue(LOGIN_KEY1,   ui->editUserName->text().trimmed());// 学号
    settings.setValue(LOGIN_KEY2,   ui->editPassWord->text().trimmed());// 密码
    settings.setValue(LOGIN_KEY3,   netCorpCn);                         // 宽带中文名
    settings.setValue(LOGIN_KEY4,   netCorpEn);                         // 宽带英文名
    settings.setValue(LOGIN_KEY5,   netCorpCode);                       // 宽带运营商

    settings.setValue(SETTING_KEY1, ui->spboxConnectTime->value()  );   // 设置重连时间(s)
    settings.setValue(SETTING_KEY2, ui->ckboxPowerBoot->isChecked());   // 开机自启项
    settings.setValue(SETTING_KEY3, ui->ckboxShowLogin->isChecked());   // 显示登录信息弹窗
}


// 鼠标拖拽窗口事件 *************************************************
void LoginWdo::mousePressEvent(QMouseEvent *event)
{
     if (event->button() == Qt::LeftButton) {
         mouseMoving = true;
         localOffPos = event->globalPosition().toPoint() - pos();
     }
    return QDialog::mousePressEvent(event);
}
void LoginWdo::mouseMoveEvent(QMouseEvent *event)
{
    if (mouseMoving) {
        move(event->globalPosition().toPoint() - localOffPos);
    }
    return QDialog::mouseMoveEvent(event);
}
void LoginWdo::mouseReleaseEvent(QMouseEvent *event)
{
    mouseMoving = false;
    return QDialog::mouseReleaseEvent(event);
} // 鼠标拖拽窗口事件 **********************************************



// 信号槽函数 ***************************************************
void LoginWdo::on_btnLogin_clicked()
{
    writeSettings();
}

void LoginWdo::on_ckboxPowerBoot_clicked(bool checked)
{
    QSettings settings = QSettings(AUTORUN, QSettings::NativeFormat);
    if (checked) {
        QString path = QApplication::applicationFilePath();     // 找到应用的目录
        settings.setValue(SOFTNAME, path.replace("/", "\\"));   // 写入注册表
    }
    else settings.remove(SOFTNAME);                             //删除注册表
} // 信号槽函数 ***************************************************
