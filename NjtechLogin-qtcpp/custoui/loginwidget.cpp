#include <QSettings>
#include <QMouseEvent>
#include <QCryptographicHash>
#include <QGraphicsDropShadowEffect>

#include "constants.h"
#include "loginwidget.h"
#include "ui_loginwidget.h"


LoginWidget::LoginWidget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::LoginWidget)
{
    ui->setupUi(this);
    LoginWidget::loadSettings();

    connect(ui->btnLogin,       &QPushButton::clicked, this, &LoginWidget::saveSettings);
    connect(ui->ckboxPowerBoot, &QCheckBox::clicked,   this, &LoginWidget::powerBoot);
}

LoginWidget::~LoginWidget()
{
    delete ui;
}

void LoginWidget::loadSettings()
{
    //HKEY_CURRENT_USER/Software/AUTHOR/SOFTNAME
    QSettings settings(AUTHOR, SOFTNAME);
    QString username     = settings.value(LOGIN_KEY1,     "").toString();
    QString password     = settings.value(LOGIN_KEY2,     "").toString();
    int  netCorpCode     = settings.value(LOGIN_KEY5,      0).toInt();
    int    reconnect     = settings.value(SETTING_KEY1,   10).toInt();
    bool     autoRun     = settings.value(SETTING_KEY2, true).toBool();
    bool    showinfo     = settings.value(SETTING_KEY3,false).toBool();

    ui->editUserName     ->setText(username);
    ui->editPassWord     ->setText(password);
    ui->ckboxPowerBoot   ->setChecked(autoRun);
    ui->cmboxChannel     ->setCurrentIndex(netCorpCode);
    ui->spboxConnectTime ->setValue(reconnect);
    ui->ckboxShowLogin   ->setChecked(showinfo);
    ui->btnLogin         ->setText("登录");
}

void LoginWidget::saveSettings()
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
    ui->btnLogin->setText("保存成功");
    emit competeSave();
}



void LoginWidget::powerBoot(bool checked)
{
    QSettings settings = QSettings(RUNPATH, QSettings::NativeFormat);
    if (checked) {
        QString softPath = QApplication::applicationFilePath();     // 应用的路径
        QString runCommand = softPath + " " + ARG_HIDE;            // 开机自启命令
        settings.setValue(SOFTNAME, runCommand.replace("/", "\\")); // 写入注册表

    }
    else settings.remove(SOFTNAME);                                 // 删除注册表

    QSettings settis(AUTHOR, SOFTNAME);
    settings.setValue(SETTING_KEY2, checked);
}






