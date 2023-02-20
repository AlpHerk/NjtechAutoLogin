#include <QApplication>
#include <QSystemSemaphore>
#include <QSharedMemory>
#include <QMessageBox>

#include "constants.h"
#include "window/main_wdo.h"
#include "qtsingleapplication.h"


int main(int argc, char *argv[])
{
    QtSingleApplication app(argc, argv);
    QStringList args = QCoreApplication::arguments();

    MainWdo  mainWdo ;

    if (app.isRunning()) {
        app.sendMessage("raise_window_noop");
        return EXIT_SUCCESS;
    }

    if (args.contains(ARG_HIDE)) {
        mainWdo.hide();
        mainWdo.authen->start();
        mainWdo.update->checkUpdate(1);
    } else {
        mainWdo.show();
        mainWdo.authen->start();
        mainWdo.update->checkUpdate(1);
    }


    return app.exec();
}


// 参考：https://blog.csdn.net/WMX843230304WMX/article/details/121955056
// Qt：程序启动一次 https://blog.csdn.net/weixin_41882459/article/details/108727851
