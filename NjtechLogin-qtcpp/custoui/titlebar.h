#ifndef TITLEBAR_H
#define TITLEBAR_H

#include <QLabel>

class TitleBar : public QLabel
{
    Q_OBJECT

public:
    explicit TitleBar(QWidget *parent = nullptr);

protected:
     //用于鼠标拖动窗口的鼠标事件操作
    void mousePressEvent(QMouseEvent *event) override;
    void mouseMoveEvent (QMouseEvent *event) override;
    void mouseReleaseEvent(QMouseEvent *event) override;
    void mouseDoubleClickEvent(QMouseEvent *event) override;


private:
    bool   mouseMoving;
    QPoint localOffPos;
    QWidget *wdo;

signals:
    void doubleClick();

};

#endif // TITLEBAR_H
