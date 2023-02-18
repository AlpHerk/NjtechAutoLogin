#include <QSettings>
#include <QMessageBox>
#include <QDesktopServices>

#include "constants.h"
#include "service/utils.h"
#include "window/main_wdo.h"
#include "service/authen.h"
#include "custoui/mainwidget.cpp"


MainWdo::MainWdo(QWidget *parent): CustoWdo(parent)

{
    initMainWdo();

    authen   = new Authen(); // 认证进程
    update   = new Update(this); // 更新检查

    /// 登录页面相关
    connect(loginwdo, &LoginWidget::competeSave, this, &MainWdo::toggleLeftBox);

    /// 主页菜单侧栏
    connect(ui->btn_home,    &QPushButton::clicked, this, &MainWdo::PageSelect);
    connect(ui->btn_message, &QPushButton::clicked, this, &MainWdo::PageSelect);
    connect(ui->btn_setting, &QPushButton::clicked, this, &MainWdo::PageSelect);
    connect(ui->btn_about,   &QPushButton::clicked, this, &MainWdo::PageSelect);
    connect(ui->btn_exit,    &QPushButton::clicked, this, &QCoreApplication::quit);

    /// 主页功能按钮
    connect(ui->btn_authorize,  &QPushButton::clicked, authen,   &Authen::toAuthen);
    connect(ui->btn_logout_net, &QPushButton::clicked, authen,   &Authen::toLogout);
    connect(ui->toggleLeftBox,  &QPushButton::clicked, loginwdo, &LoginWidget::loadSettings);

    /// 设置中心页按钮
    connect(ui->checkBox_autorun,  &QCheckBox::clicked, loginwdo, &LoginWidget::powerBoot);

    /// 关于软件
    connect(ui->btn_upgrade,    &QPushButton::clicked, update, &Update::checkUpdate);
    connect(ui->btn_upgradelog, &QPushButton::clicked, update, &Update::updateLog);
    connect(ui->btn_logo_login, &QPushButton::clicked, this,   &MainWdo::toggleLeftBox);
    connect(ui->btn_officeweb,  &QPushButton::clicked, this, [=](){QDesktopServices::openUrl(WEB_URL);}  );

    connect(ui->btn_csdn,    &QPushButton::clicked, this, [=](){QDesktopServices::openUrl(CSDN_URL);}   );
    connect(ui->btn_feedback,&QPushButton::clicked, this, [=](){QDesktopServices::openUrl(FEEDBACK);}   );
    connect(ui->btn_getHelp, &QPushButton::clicked, this, [=](){QDesktopServices::openUrl(FEEDBACK);}   );
    connect(ui->btn_prjurl,  &QPushButton::clicked, this, [=](){QDesktopServices::openUrl(CSDNPRJ_URL);});

    connect(ui->btn_usrAgreement,  &QPushButton::clicked, this, [=](){QDesktopServices::openUrl(USR_AGREEM);});
    connect(ui->btn_privacyPolice, &QPushButton::clicked, this, [=](){QDesktopServices::openUrl(PRIV_POLIC);});


    /// 认证服务
    connect(authen,   &Authen::reqLoginWdo,  this, &MainWdo::toggleLeftBox);
    connect(authen,   &Authen::quiteProgram, this, &QCoreApplication::quit);

    /// 主页认证消息日志
    connect(authen,   &Authen::emitAuthenInfo, this, [=](QString info) {
        ui->textBrowserInteractInfo->append(info);
    });

    /// 设置网络抓取信息
    connect(update,  &Update::netPullResualt, this, [&](QStringList infoLst) {
        MainWdo::setTextBrow(infoLst);
    });

}


MainWdo::~MainWdo()
{
    delete this;
}


void MainWdo::initMainWdo()
{
    loginwdo = new LoginWidget(this);
    ui->loginLayout->addWidget(loginwdo);

    ui->stackedWidget->setCurrentWidget(ui->home_page);
    ui->version_code->setText(VER_NAME);
    Utils::powerBootCheck();
}


/// 菜单切换页面
void MainWdo::PageSelect()
{
    objSender = sender();
    switchBtn = dynamic_cast<QPushButton*>(objSender);
    QString btnName = switchBtn->objectName();

    if      (btnName ==    "btn_home") {
        ui->stackedWidget->setCurrentWidget(ui->home_page    );
    }
    else if (btnName == "btn_message") {
        ui->stackedWidget->setCurrentWidget(ui->message_page);
        update->pullNetText(NOICE_URL  , "message");
    }
    else if (btnName == "btn_setting") {
        ui->stackedWidget->setCurrentWidget(ui->setting_page);
    }
    else if (btnName ==   "btn_about") {
        ui->stackedWidget->setCurrentWidget(ui->about_page  );
        update->pullNetText(MANUL_URL  ,   "manul");
        update->pullNetText(LICENSE_URL, "license");
    }
    MainWdo::resetStyle(btnName);
    switchBtn->setStyleSheet(MainWdo::selectMenu(switchBtn->styleSheet()));
}



/// 设置各个文本框信息
void MainWdo::setTextBrow(QStringList &infoLst)
{
    if      (infoLst[1] == "message") {
        ui->textBrowser_push_msg->setMarkdown(infoLst[0]);
    }
    else if (infoLst[1] == "manul")   {
        ui->textBrowser_help->setMarkdown(  infoLst[0]  );
    }
    else if (infoLst[1] == "license") {
        ui->textBrowser_license->setMarkdown(infoLst[0] );
    }
}






