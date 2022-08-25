#include <QPointF>
#include <QMouseEvent>

#include "custoui/titlebar.h"


TitleBar::TitleBar(QWidget *parent): QLabel{parent}
{
    mouseMoving = false;
    wdo = this->window();
}


// 鼠标拖拽标题栏移动 *************************************************
void TitleBar::mousePressEvent(QMouseEvent *event)
{
    if (event->button() == Qt::LeftButton) {
         mouseMoving = true;
         localOffPos = event->globalPosition().toPoint() - wdo->pos();
    }
    return QLabel::mousePressEvent(event);
}

void TitleBar::mouseMoveEvent(QMouseEvent *event)
{
    if (mouseMoving) {
         wdo->move(event->globalPosition().toPoint() - localOffPos);
    }
    return QLabel::mouseMoveEvent(event);
}

void TitleBar::mouseReleaseEvent(QMouseEvent *event)
{
    mouseMoving = false;
    return QLabel::mouseReleaseEvent(event);
}
// 鼠标拖拽标题栏移动 **********************************************

// 双击最大最小化窗口
void TitleBar::mouseDoubleClickEvent(QMouseEvent *)
{
    emit doubleClick();
}
