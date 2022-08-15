#ifndef RIGHTBOX_H
#define RIGHTBOX_H

#include <QWidget>

namespace Ui {
class RightBox;
}

class RightBox : public QWidget
{
    Q_OBJECT

public:
    explicit RightBox(QWidget *parent = nullptr);
    ~RightBox();

private:
    Ui::RightBox *ui;
};

#endif // RIGHTBOX_H
