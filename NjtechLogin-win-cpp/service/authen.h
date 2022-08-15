#ifndef AUTHEN_H
#define AUTHEN_H

#include <QNetworkRequest>
#include <QNetworkReply>
#include <QHostInfo>
#include <QProcess>
#include <QThread>

class Authen : public QThread
{
    Q_OBJECT

public:
    Authen();
    ~Authen();
    void toAuthen();

protected:
    void run() override;

private:

    void authBack(QNetworkReply *reply);
    bool readUsrData();
    bool netConnect();
    void authenCore();

    QNetworkAccessManager *getManager;
    QNetworkAccessManager *postManager;

    QString username;
    QString password;
    QString netCorpC;
    QString netCorpE;
    int     recntime;
    bool    dataReady;
    int     cntReady;
signals:
    void reqLoginWdo();
    void quiteProgram();
    void emitAuthenInfo(QString);

};

#endif // AUTHEN_H
