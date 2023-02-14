#ifndef MAIN_WDO_H
#define MAIN_WDO_H
#include <QPushButton>
#include "service/authen.h"
#include "service/update.h"
#include "custoui/mainwidget.h"
#include "custoui/loginwidget.h"


namespace Ui { class MainWdo; }

class MainWdo : public CustoWdo
{
    Q_OBJECT

public:
    explicit MainWdo(QWidget *parent = nullptr);
    ~MainWdo();
    void initMainWdo();
    Update  *update;
    Authen  *authen;
    Authen  *netGuard;
    QObject *objSender;
    QPushButton *switchBtn;
    LoginWidget *loginwdo;

private slots:
    void PageSelect();
    void setTextBrow(QStringList &);


signals:
    void authlogin();
    void updateLoginInfo();
};

#endif // MAIN_WDO_H
