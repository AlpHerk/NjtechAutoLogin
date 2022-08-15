#ifndef MAINWDO_H
#define MAINWDO_H

#include "qpushbutton.h"
#include <QMenu>
#include <QMainWindow>
#include <QSystemTrayIcon>



namespace Ui { class CustoWdo; }

class CustoWdo : public QMainWindow
{
    Q_OBJECT


public:
    CustoWdo(QWidget *parent = nullptr);
    ~CustoWdo();

    Ui::CustoWdo *ui;


protected:
    QString selectMenu(QString getStyle);
    QString deselectMenu(QString getStyle);

    void selectStandardMenu(QString widget);
    void resetStyle(QString widget);

    void theme(QString filename, bool useCustomTheme);
    void start_box_animation(int , int , QString);

    void showMaximize();
    void showNormalize();


protected slots:
    void sysTrayCilick(QSystemTrayIcon::ActivationReason action);
    void maximizeRestore();
    void toggleMenu();
    void toggleLeftBox();
    void toggleRightBox();

private:
    QPushButton *btnChild;

};
#endif // MAINWDO_H
