#include "rightbox.h"
#include "ui_rightbox.h"

RightBox::RightBox(QWidget *parent):
    QWidget(parent),
    ui(new Ui::RightBox)
{
    ui->setupUi(this);
}

RightBox::~RightBox()
{
    delete ui;
}
