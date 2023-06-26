#ifndef LOGIN_WDO_H
#define LOGIN_WDO_H
#include <QDialog>
#include <QPointF>

namespace Ui { class LoginWdo; }

class LoginWdo : public QDialog
{
    Q_OBJECT

public:
    explicit LoginWdo(QWidget *parent = nullptr);
    ~LoginWdo();

protected:
     //用于鼠标拖动窗口的鼠标事件操作
    void mousePressEvent(QMouseEvent *event);
    void mouseMoveEvent (QMouseEvent *event);
    void mouseReleaseEvent(QMouseEvent *event);

private:
    QPoint localOffPos;
    bool   mouseMoving;

    void readSettings();     //从注册表读取设置
    void writeSettings();    //从注册表写入设置

private slots:
    void on_btnLogin_clicked();
    void on_ckboxPowerBoot_clicked(bool checked);


private:
    Ui::LoginWdo *ui;

};
#endif // LOGIN_WDO_H
