#ifndef AUTHEN_H
#define AUTHEN_H

#include <QNetworkRequest>
#include <QNetworkReply>
#include <QProcess>
#include <QThread>

class Authen : public QThread
{
    Q_OBJECT

public:
    Authen();
    ~Authen();
    void toAuthen();
    void toLogout();



protected:
    void run() override;


private:
    bool reConnect();
    bool readUsrData();

    void authBack(QNetworkReply *reply);
    void authBackDeprecated(QNetworkReply *reply);

    /// 已弃用的函数
    void authenCore();
    void authenCoreDeprecated();
    QString getIPv4fromNetDeprecated();

    QNetworkAccessManager *postManager;
    QNetworkAccessManager *getManager;
    QString username;
    QString password;
    QString netCorpC;
    QString netCorpE;

    int recntime;
    int cntReady;
    int cntGuardTip;

    static bool isGuardOn;

signals:
    void reqLoginWdo();
    void quiteProgram();
    void emitAuthenInfo(QString);

};

#endif // AUTHEN_H
