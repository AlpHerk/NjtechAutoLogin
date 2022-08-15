#include <QJsonDocument>
#include <QJsonObject>
#include <QEventLoop>
#include <QSettings>
#include <QTimer>

#include "authen.h"
#include "constants.h"

Authen::Authen(): dataReady(false)
{
    dataReady = Authen::readUsrData();
    Authen::authenCore();
    cntReady = 0;
}


Authen::~Authen() {
    delete this;
}

bool Authen::readUsrData()
{
    QSettings settings(AUTHOR, SOFTNAME);
    username  = settings.value(LOGIN_KEY1, "").toString();
    password  = settings.value(LOGIN_KEY2, "").toString();
    netCorpC  = settings.value(LOGIN_KEY3, "").toString();
    netCorpE  = settings.value(LOGIN_KEY4, "").toString();
    recntime  = settings.value(SETTING_KEY1, 5).toInt();

    if (username=="" || password=="") {
        QDateTime dateTime = QDateTime::currentDateTime();
        QString timeStr = dateTime.toString("[yy-MM-dd hh:mm:ss] ");
        if (cntReady < 3) {
            if (cntReady == 0) emit reqLoginWdo();
            QString failreason  = timeStr + "ℹ️ 请输入账号密码";
            emit emitAuthenInfo(failreason);
            cntReady++;
        }
        return false;
    }
    return true;
}

void Authen::run()
{
    while (recntime > 0) {   // 若设置了网络守护
        if (dataReady) {       // 若数据准备就绪
            if (!netConnect()) { // 若断网则重连
               Authen::authenCore();
            }
        } else {
            dataReady = Authen::readUsrData();
        }
        sleep(recntime);
    }
    emit quiteProgram();
}

bool Authen::netConnect()
{
    QDateTime dateTime = QDateTime::currentDateTime();
    QString timeStr = dateTime.toString("[yy-MM-dd hh:mm:ss] ");

    QNetworkRequest request;
    request.setUrl(QUrl("https://www.baidu.com/"));
    request.setRawHeader("Content-Type", "text/html;charset=UTF-8");
    request.setRawHeader("User-Agent", USERAGENT);
    getManager = new QNetworkAccessManager(this);
    QNetworkReply *reply = getManager->get(request);

    QEventLoop loop;
    connect(getManager, SIGNAL(finished(QNetworkReply*)), &loop, SLOT(quit()));
    QTimer::singleShot(5000, &loop, &QEventLoop::quit);
    loop.exec();

    getManager->deleteLater();
    reply->deleteLater();

    QVariant status = reply->attribute(QNetworkRequest::HttpStatusCodeAttribute);
    if (!status.isValid()) {
        QString failreason = timeStr + "🔃 网络断开，正在重连 ···";
        emit emitAuthenInfo(failreason);
        return false;
    }
    else {
        return true;
    }

}


void Authen::toAuthen()
{
    if (dataReady) {
        Authen::authenCore();
    }
    else {
        emit reqLoginWdo();
    }
}


void Authen::authenCore()
{
//    if (!dataReady) return ;

    getManager = new QNetworkAccessManager(this);

    QDateTime dateTime = QDateTime::currentDateTime();
    QString timeStr = dateTime.toString("[yy-MM-dd hh:mm:ss] ");

    // 第一步，获取登录页的认证数据
    QNetworkRequest request;
    request.setUrl(LOGIN_URL);
    request.setRawHeader("Content-Type", "text/html;charset=UTF-8");
    request.setRawHeader("User-Agent", USERAGENT);
    QNetworkReply *reply = getManager->get(request);

    QEventLoop loop;
    connect(getManager, SIGNAL(finished(QNetworkReply*)), &loop, SLOT(quit()), Qt::UniqueConnection);
    QTimer::singleShot(5000, &loop, &QEventLoop::quit);
    loop.exec();

    getManager->deleteLater();

    // 第二步，发送请求进行网络认证
    if (reply->error()==QNetworkReply::NoError) {
        QByteArray byte   = reply->readAll();

        QString    html   = QString(byte);
        QRegularExpression  static lt_re("lt\" value=\"(?<lt>.*?)\"");
        QRegularExpression  static ex_re("execution\" value=\"(?<exe>.*?)\"");

        QString matched1  = lt_re.match(html).captured("lt");
        QString matched2  = ex_re.match(html).captured("exe");

        QVariant cookies = reply->header(QNetworkRequest::SetCookieHeader);
        // String cookieStr = reply->rawHeader("Set-Cookie");
        // QStringList cookieLst = cookieStr.split(";");//QString字符串分割函数
        // QByteArray cookie = (cookieLst[0] + "; " + cookieLst[2].right(22)).toUtf8();

        // QString posturl = LOGIN_STR;
        // posturl.insert(33, insertcook);
        // String insertcook = ";" + cookie.left(51);

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
        postManager->post(postreq, postdata);
        connect(postManager, &QNetworkAccessManager::finished, this, &Authen::authBack, Qt::UniqueConnection);

        QString respsuccess = timeStr + "ℹ️ 响应完成，正在接入 ···";
        emit emitAuthenInfo(respsuccess);
    } else {
        QString failreason  = timeStr + "🟥 响应错误：" + reply->errorString().toUtf8();
        emit emitAuthenInfo(failreason);
    }
    delete reply;
}


void Authen::authBack(QNetworkReply *reply)
{
    QDateTime dateTime = QDateTime::currentDateTime();
    QString timeStr  = dateTime.toString("[yy-MM-dd hh:mm:ss] ");

    QByteArray bytes = reply->readAll();
    QString     html = QString(bytes);

    if (html.contains("账号或密码错误")) {
        QString failreason = timeStr + "🟥 账号或密码错误";
        emit emitAuthenInfo(failreason);
        emit reqLoginWdo();
        return;
    } else if (html.contains("停机")) {
        QString failreason = timeStr + "🟨 您的账号已停机";
        emit emitAuthenInfo(failreason);
        return;
    } else if (html.contains("运营商账号不存在")) {
        QString failreason = timeStr + "🟧 未绑定宽带账号";
        emit emitAuthenInfo(failreason);
        return;
    }

    QVariant statusCode = reply->attribute(QNetworkRequest::HttpStatusCodeAttribute);
    if (statusCode.isValid()) {
        QString authensuccess=timeStr+ "✅ 认证成功，网络畅通 ~";
        emit emitAuthenInfo(authensuccess);
    } else {
        QString failreason = timeStr + "🟥 认证失败：" + reply->errorString().toUtf8();
        emit emitAuthenInfo(failreason);
    }
    reply->deleteLater();
    postManager->deleteLater();
}




