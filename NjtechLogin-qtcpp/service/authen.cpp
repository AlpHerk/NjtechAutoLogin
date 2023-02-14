#include <QJsonDocument>
#include <QJsonObject>
#include <QEventLoop>
#include <QSettings>
#include <QTimer>

#include "authen.h"
#include "constants.h"

/// 类静态变量，需在类外初始化
bool Authen::isGuardOn = true;  // 默认开启网络守护

/// 网络认证类
Authen::Authen(): cntReady(0), cntGuardTip(0)
{
    Authen::toAuthen();
}

Authen::~Authen() {
    delete this;
}

/// 读取用户密码
bool Authen::readUsrData()
{
    QSettings settings(AUTHOR, SOFTNAME);
    username  = settings.value(LOGIN_KEY1, "").toString();
    password  = settings.value(LOGIN_KEY2, "").toString();
    netCorpC  = settings.value(LOGIN_KEY3, "").toString();
    netCorpE  = settings.value(LOGIN_KEY4, "").toString();
    recntime  = settings.value(SETTING_KEY1, 5).toInt();

    if ((username=="" || password=="") && cntReady < 3) {

        QString timeStr = QDateTime::currentDateTime().toString(timeForm);
        emit emitAuthenInfo(timeStr + "ℹ️ 请输入账号密码");
        emit reqLoginWdo();
        cntReady++;

        return false;
    }
    return true;
}


/// 网络认证
void Authen::toAuthen()
{
    if (Authen::readUsrData()) {

        Authen::authenCore();

        if (isGuardOn==false) {
            isGuardOn = true; // 手动点击认证按钮，开启守护服务
            QString timeStr = QDateTime::currentDateTime().toString(timeForm);
            emit emitAuthenInfo(timeStr + "🍀 守护服务已重新启动");
        }

    }
    else {
        emit reqLoginWdo();
    }
}

/// 网络认证：核心服务
void Authen::authenCore()
{
    QString timeStr = QDateTime::currentDateTime().toString(timeForm);

    // 第一步，获取登录页的认证数据
    QNetworkRequest request;
    request.setUrl(LOGIN_URL);
    request.setRawHeader("Content-Type", "text/html;charset=gbk");
    request.setRawHeader("User-Agent", USERAGENT);

    getManager  = new QNetworkAccessManager(this);
    QNetworkReply *reply = getManager->get(request);

    QEventLoop loop;
    connect(getManager, &QNetworkAccessManager::finished, &loop, &QEventLoop::quit);
    QTimer::singleShot(5000, &loop, &QEventLoop::quit);
    loop.exec();

    // 第二步，发送请求进行网络认证
    if (reply->error()==QNetworkReply::NoError) {
        QByteArray byte   = reply->readAll();

        QString    html   = QString(byte);
        QRegularExpression static ip_re("v46ip=\'(?<ip>.*?)\'");
        QString    v46ip  = ip_re.match(html).captured("ip");

        QByteArray postdata;
        QString param1 = "DDDDD=,0," + username + netCorpE;
        QString param2 = "&upass=" + password;
        QString param3 = "&R1=0";
        QString param4 = "&R2=0";
        QString param5 = "&R3=0";
        QString param6 = "&R6=0";
        QString param7 = "&para=00";
        QString param8 = "&0MKKey=123456";

        postdata.append(param1.toUtf8());
        postdata.append(param2.toUtf8());
        postdata.append(param3.toUtf8());
        postdata.append(param4.toUtf8());
        postdata.append(param5.toUtf8());
        postdata.append(param6.toUtf8());
        postdata.append(param7.toUtf8());
        postdata.append(param8.toUtf8());

        QNetworkRequest postreq;
        postreq.setUrl(LOGIN_URL1 + v46ip + LOGIN_URL3);
        postreq.setRawHeader("Content-Type", "application/x-www-form-urlencoded");
        postreq.setRawHeader("User-Agent", USERAGENT);

        postManager = new QNetworkAccessManager(this);
        connect(postManager, &QNetworkAccessManager::finished, this, &Authen::authBack);
        postManager->post(postreq, postdata);

    } else {
        emit emitAuthenInfo(timeStr + "🟥 响应错误：" + reply->errorString().toUtf8());
    }
    getManager->deleteLater();
}


/// 退出认证
void Authen::toLogout()
{
    Authen::isGuardOn = false; // 手动点击退出认证按钮，暂时关闭守护服务

    QString timeStr = QDateTime::currentDateTime().toString(timeForm);

    // 第一步，获取登录页的认证数据
    QNetworkRequest request;
    request.setUrl(LOGIN_URL);
    request.setRawHeader("Content-Type", "text/html;charset=gbk");
    request.setRawHeader("User-Agent", USERAGENT);

    getManager  = new QNetworkAccessManager(this);
    QNetworkReply *reply = getManager->get(request);

    QEventLoop loop;
    connect(getManager, &QNetworkAccessManager::finished, &loop, &QEventLoop::quit);
    QTimer::singleShot(5000, &loop, &QEventLoop::quit);
    loop.exec();

    // 第二步，发送请求退出网络认证
    if (reply->error()==QNetworkReply::NoError) {
        QByteArray byte   = reply->readAll();

        QString    html   = QString(byte);
        QRegularExpression static ip_re("v46ip=\'(?<ip>.*?)\'");
        QString    v46ip  = ip_re.match(html).captured("ip");

        QNetworkRequest postreq;
        postreq.setUrl(LOGOUT_URL1 + v46ip + LOGOUT_URL3);
        postreq.setRawHeader("Content-Type", "application/x-www-form-urlencoded");
        postreq.setRawHeader("User-Agent", USERAGENT);

        QByteArray postdata;
        postdata.append("退出");

        postManager = new QNetworkAccessManager(this);
        connect(postManager, &QNetworkAccessManager::finished, this, &Authen::authBack);
        postManager->post(postreq, postdata);

    } else {
        emit emitAuthenInfo(timeStr + "🟥 响应错误：" + reply->errorString().toUtf8());
    }
    getManager->deleteLater();
}


/// 网络守护服务
void Authen::run()
{
    while (recntime > 0) {   /// 若设置了网络守护

        sleep(2);   // 延迟显示守护提示

        if (isGuardOn) {
            Authen::reConnect(); /// 在断网后智能重连
        }

        if (recntime > 2) {
            sleep(recntime-2);
        } else {
            sleep(recntime);
        }

    }

    /// 若未设置网络守护则延时退出程序
    QString timeStr = QDateTime::currentDateTime().toString(timeForm);
    emit emitAuthenInfo(timeStr + "✅ 网络连接，程序10秒后自动退出 ···");
    sleep(10);
    emit quiteProgram();
}

/// 网络守护：重连函数
bool Authen::reConnect()
{
    QString timeStr = QDateTime::currentDateTime().toString(timeForm);

    QNetworkRequest request;
    request.setUrl(QUrl("https://www.baidu.com/"));
    request.setRawHeader("Content-Type", "text/html;charset=UTF-8");
    request.setRawHeader("User-Agent", USERAGENT);

    getManager = new QNetworkAccessManager(this);
    QNetworkReply *reply = getManager->get(request);

    QEventLoop loop;
    connect(getManager, SIGNAL(finished(QNetworkReply*)), &loop, SLOT(quit()));
    QTimer::singleShot(1000, &loop, &QEventLoop::quit);
    loop.exec();

    QVariant status = reply->attribute(QNetworkRequest::HttpStatusCodeAttribute);
    delete getManager;

    if (!status.isValid()) {
        if  (Authen::readUsrData()) Authen::authenCore();
        emit emitAuthenInfo(timeStr + "🔃 网络中断，正在重连 ···");
        return false;
    }
    else if (cntGuardTip < 1) {
        emit emitAuthenInfo(timeStr + "🍀 网络畅通，正在守护 ···");
        cntGuardTip++;
    }
    return true;
}




/// 此认证函数已弃用 2023.2.13
void Authen::authenCoreDeprecated()
{
    QString timeStr = QDateTime::currentDateTime().toString(timeForm);

    // 第一步，获取登录页的认证数据
    QNetworkRequest request;
    request.setUrl(LOGIN_URL);
    request.setRawHeader("Content-Type", "text/html;charset=UTF-8");
    request.setRawHeader("User-Agent", USERAGENT);

    getManager  = new QNetworkAccessManager(this);
    QNetworkReply *reply = getManager->get(request);

    QEventLoop loop;
    connect(getManager, &QNetworkAccessManager::finished, &loop, &QEventLoop::quit);
    QTimer::singleShot(5000, &loop, &QEventLoop::quit);
    loop.exec();

    // 第二步，发送请求进行网络认证
    if (reply->error()==QNetworkReply::NoError) {
        QByteArray byte   = reply->readAll();
        QVariant cookies  = reply->header(QNetworkRequest::SetCookieHeader);

        QString    html   = QString(byte);
        QRegularExpression static lt_re("lt\" value=\"(?<lt>.*?)\"");
        QRegularExpression static ex_re("execution\" value=\"(?<exe>.*?)\"");

        QString matched1  = lt_re.match(html).captured("lt");
        QString matched2  = ex_re.match(html).captured("exe");

        QByteArray postdata;
        QString param1 = "username="     + username;
        QString param2 = "&password="    + password;
        QString param3 = "&channelshow=" + netCorpC;
        QString param4 = "&channel="     + netCorpE;
        QString param5 = "&lt="          + matched1;
        QString param6 = "&execution="   + matched2;
        QString param7 = "&_eventId=submit";
        QString param8 = "&login=登录";

        postdata.append(param1.toUtf8());
        postdata.append(param2.toUtf8());
        postdata.append(param3.toUtf8());
        postdata.append(param4.toUtf8());
        postdata.append(param5.toUtf8());
        postdata.append(param6.toUtf8());
        postdata.append(param7.toUtf8());
        postdata.append(param8.toUtf8());

        QNetworkRequest postreq;
        postreq.setUrl(LOGIN_URL);
        postreq.setHeader(QNetworkRequest::CookieHeader, QVariant::fromValue(cookies));
        postreq.setRawHeader("Content-Type", "application/x-www-form-urlencoded");
        postreq.setRawHeader("Origin",     "https://u.njtech.edu.cn");
        postreq.setRawHeader("Host",       "u.njtech.edu.cn");
        postreq.setRawHeader("User-Agent", USERAGENT);
        postreq.setRawHeader("Referer",    LOGIN_STR);

        postManager = new QNetworkAccessManager(this);
        connect(postManager, &QNetworkAccessManager::finished, this, &Authen::authBack);
        postManager->post(postreq, postdata);

    } else {
        emit emitAuthenInfo(timeStr + "🟥 响应错误：" + reply->errorString().toUtf8());
    }
    getManager->deleteLater();
}

/// 网络认证：回调函数
void Authen::authBack(QNetworkReply *reply)
{
    QVariant status  = reply->attribute(QNetworkRequest::HttpStatusCodeAttribute);
    QString timeStr = QDateTime::currentDateTime().toString(timeForm);

    QByteArray bytes = reply->readAll();
    QString     html = QString(bytes);

    if (html.contains("请检查您绑定的运营商账号是否正确")) {
        emit emitAuthenInfo(timeStr + "🟥账号或密码错误");
        emit reqLoginWdo();
    }
    else if (html.contains("停机")) {
        emit emitAuthenInfo(timeStr + "🟥 您的账号已停机");
    }
    else if (html.contains("运营商账号不正确，请检查绑定！")) {
        emit emitAuthenInfo(timeStr + "🟥 运营商账号不正确，请检查绑定！");
    }
    else if (!isGuardOn) {
        emit emitAuthenInfo(timeStr + "🟧 网络断开，守护关闭");
    }
    else if (status.isValid()) {
        emit emitAuthenInfo(timeStr + "✅ 认证成功，开始冲浪 ~");
    }
    else {
        emit emitAuthenInfo(timeStr + "🟥 认证失败：" + reply->errorString().toUtf8());
    }
    postManager->deleteLater();
}




