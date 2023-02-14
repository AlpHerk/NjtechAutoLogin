#ifndef LOGINWIDGET_H
#define LOGINWIDGET_H

#include <QWidget>
#include <QPointF>

namespace Ui {
class LoginWidget;
}

class LoginWidget : public QWidget
{
    Q_OBJECT

public:
    explicit LoginWidget(QWidget *parent = nullptr);
    ~LoginWidget();

public:
    void loadSettings();     //从注册表读取设置
    void saveSettings();    //从注册表写入设置
    void powerBoot(bool checked);


signals:
    void competeSave();

private:
    Ui::LoginWidget *ui;
    QPoint localOffPos;
    bool   mouseMoving;
};

#endif // LOGINWIDGET_H
