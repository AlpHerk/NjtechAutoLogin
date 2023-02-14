#ifndef UPDATE_H
#define UPDATE_H

#include <QWidget>
#include <QNetworkAccessManager>
#include <QNetworkRequest>
#include <QNetworkReply>

class Update : public QWidget
{
    Q_OBJECT
public:
    explicit Update(QWidget *parent = nullptr);
    QByteArray getNetBack(QUrl url);
    void checkUpdate(int hide=0);
    void updateLog();
    bool pullNetText(QUrl url, QString id);

private:
    QNetworkAccessManager *manager;

signals:
    void netPullResualt(QStringList);

};

#endif // UPDATE_H
