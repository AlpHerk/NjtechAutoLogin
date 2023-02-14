#include <QDesktopServices>
#include <QJsonParseError>
#include <QJsonObject>
#include <QJsonArray>
#include <QMessageBox>
#include <QEventLoop>
#include <QTimer>

#include "update.h"
#include "constants.h"


Update::Update(QWidget *parent): QWidget{parent}
{
    manager = new QNetworkAccessManager(this);
}

/// 返回网页比特信息
QByteArray Update::getNetBack(QUrl url)
{
    QNetworkRequest request;
    request.setUrl(url);
    request.setHeader(QNetworkRequest::ContentTypeHeader, "application/json; charset=utf-8");
    request.setRawHeader("User-Agent", USERAGENT);
    QNetworkReply *resonse = manager->get(request);

    QEventLoop loop;
    connect(manager, SIGNAL(finished(QNetworkReply*)), &loop, SLOT(quit()));
    QTimer::singleShot(5000, &loop, &QEventLoop::quit);
    loop.exec();

    QByteArray bytes = resonse->readAll();
    delete resonse;
    return bytes;
}

/// 软件检查更新
void Update::checkUpdate(int hide)
{
    QJsonParseError jsonError;
    QByteArray bytes = Update::getNetBack(CHECK_URL);
    QJsonDocument jsonDoc = QJsonDocument::fromJson(bytes, &jsonError);

    if (jsonError.error == QJsonParseError::NoError) {
        QJsonObject jsonObj = jsonDoc.object();
        QString  appName  = jsonObj.value("name").toString();
        QJsonArray assets = jsonObj.value("assets").toArray();

        if (!assets.isEmpty()) {
            for (int i = 0; i < assets.size(); i++) {
                QJsonObject obj = assets.at(i).toObject();
                QString downUrl = obj.value("browser_download_url").toString();

                if (downUrl.contains("win")) {
                    int newVerCode = downUrl.right(9).left(6).replace(".", "").toInt();

                    if (VER_CODE < newVerCode) {
                        QString name = "最新版本：" + appName;
                        QString down = "\n\n下载链接：" + QByteArray::fromPercentEncoding(downUrl.toUtf8());
                        QString ques = "\n\n是否自动跳转至浏览器下载？";
                        QMessageBox::StandardButton box = QMessageBox::question(this, "检查更新", name+down+ques + "\n");
                        if (box==QMessageBox::Yes)  QDesktopServices::openUrl(QUrl(downUrl));
                    }
                    else {
                        if (!hide) QMessageBox::information(this, "检查更新", "当前已是最新版：" + appName + "\n");
                    }
                }
            }
        }
        else {
            if (!hide) QMessageBox::information(this, "检查更新", "当前已是最新版：" + appName + "\n");
        }
    }
    else {
        if (!hide) QMessageBox::information(this, "检查更新", "检查配置解析失败, 请联系开发者\n");
    }
}

/// 获取更新日志
void Update::updateLog()
{
    QJsonParseError jsonError;
    QByteArray bytes = Update::getNetBack(CHECK_URL);
    QJsonDocument jsonDoc = QJsonDocument::fromJson(bytes, &jsonError);

    if (jsonError.error == QJsonParseError::NoError) {
        QJsonObject jsonObj = jsonDoc.object();
        QString  updatelog  = jsonObj.value("body").toString();
        QMessageBox::information(this, "更新日志", updatelog + "\n");
    }
    else {
        QMessageBox::information(this, "更新日志", "解析失败, 请联系开发者\n");
    }
}

/// 获取网页文本信息
bool Update::pullNetText(QUrl url, QString id)
{
    QStringList lst;
    QByteArray bytes = Update::getNetBack(url);
    if (bytes != "") {
        emit netPullResualt(lst << QString(bytes) << id);
        return true;
    }
    else {
        emit netPullResualt(lst << FAILSTR << id);
        return false;
    }
}

