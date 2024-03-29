#ifndef UTILS_H
#define UTILS_H

#include <QObject>
#include <QHostInfo>
#include <QAbstractSocket>
#include <QNetworkProxyQuery>
#include <QNetworkRequest>
#include <QNetworkReply>
#include <QTimer>
#include <QEventLoop>
#include <QSettings>
#include <QApplication>

class Utils : public QObject
{
    Q_OBJECT
public:
    explicit Utils(QObject *parent = nullptr);

    static bool powerBootCheck();
    static QString getIpv4Adds();
    static QString getSysProxy();
    bool isNetPing();

private:
    QNetworkAccessManager *netManager;

signals:

};


#endif // UTILS_H
