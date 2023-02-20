#include "utils.h"
#include "constants.h"

Utils::Utils(QObject *parent)
    : QObject{parent}
{

}

bool Utils::powerBootCheck()
{
    QSettings settings(AUTHOR, SOFTNAME);
    bool      checked = settings.value(SETTING_KEY2, true).toBool();
    QSettings runpath = QSettings(RUNPATH, QSettings::NativeFormat);

    if (checked) {
        QString softPath = QApplication::applicationFilePath();     // 应用的路径
        QString runCommand = softPath + " " + ARG_HIDE;            // 开机自启命令
        runpath.setValue(SOFTNAME, runCommand.replace("/", "\\"));  // 写入注册表
        //qDebug() << "Herkin" << "写入开机注册表";
        return true;

    } else {
        runpath.remove(SOFTNAME);                                   // 删除注册表
        qDebug() << "Herkin" << "删除开机注册表";
        return false;
    }
}

QString Utils::getIpv4Adds()
{
    QString localHostName = QHostInfo::localHostName();

    QHostInfo info = QHostInfo::fromName(localHostName);
    foreach (QHostAddress address, info.addresses()) {
        if (address.protocol() == QAbstractSocket::IPv4Protocol) {
//            qDebug() << "HERKIN" << "主机名：" << localHostName << "  IPv4：" << address.toString();
            return address.toString();
        }
    }
    return "";
}

QString Utils::getSysProxy() {
    QNetworkProxyQuery proxyQuery(QUrl("https://www.baidu.com"));
    QList<QNetworkProxy> proxyList = QNetworkProxyFactory::systemProxyForQuery(proxyQuery);
    if(proxyList.count() > 0)
    {
//        qDebug() << "HERKIN" << "系统代理名：" << proxyList.at(0).hostName();
        return proxyList.at(0).hostName();
    }

//    QNetworkProxy proxy;
//    proxy.setApplicationProxy(QNetworkProxy(proxy.NoProxy));

    return "";
}

bool Utils::isNetPing()
{
    QNetworkRequest request;
    request.setUrl(QUrl("https://www.baidu.com/"));
    request.setRawHeader("Content-Type", "text/html;charset=UTF-8");
    request.setRawHeader("User-Agent", USERAGENT);

    netManager = new QNetworkAccessManager( );
    QNetworkReply *reply = netManager->get(request);

    QEventLoop loop;
    connect(netManager, SIGNAL(finished(QNetworkReply*)), &loop, SLOT(quit()));
    QTimer::singleShot(1000, &loop, &QEventLoop::quit);
    loop.exec();

    QVariant status = reply->attribute(QNetworkRequest::HttpStatusCodeAttribute);
    delete netManager;

    if (!status.isValid()) {
        qDebug() << "HERKIN" << "已经接入互联网";
        return true;
    } else {
        qDebug() << "HERKIN" << "无法接入互联网";
        return false;
    }

}











