#include "constants.h"
#include "rightbox.h"
#include "ui_rightbox.h"

#include <QDesktopServices>

RightBox::RightBox(QWidget *parent):
    QWidget(parent),
    ui(new Ui::RightBox)
{
    ui->setupUi(this);

    /// 右侧盒子按钮
    connect(ui->btn_officeweb_rightbox, &QPushButton::clicked, this, [=](){QDesktopServices::openUrl(WEB_URL);}     );
    connect(ui->btn_blog_rightbox,      &QPushButton::clicked, this, [=](){QDesktopServices::openUrl(CSDNPRJ_URL);} );
    connect(ui->btn_github_rightbox,    &QPushButton::clicked, this, [=](){QDesktopServices::openUrl(GITHUB_PRJ);}   );

}

RightBox::~RightBox()
{
    delete ui;
}
