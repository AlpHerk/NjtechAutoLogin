#include <QApplication>
#include <QSystemSemaphore>
#include <QSharedMemory>
#include <QMessageBox>

#include "constants.h"
#include "window/main_wdo.h"

int main(int argc, char *argv[])
{
    QApplication app(argc, argv);


    /// 利用信号量设计单例模式
    QSystemSemaphore semaphore("ProgramKey", 1, QSystemSemaphore::Open);
    semaphore.acquire();
    QSharedMemory memory("Program");    //全局对象名
    if (!memory.create(1)) //如果全局对象存在则提示退出
    {
        QMessageBox::information(0, "提示", "程序已经在运行了");
        semaphore.release();
        return app.exec();
    }
    semaphore.release();


    /// 启动程序
    MainWdo *mainWdo = new MainWdo();
    QStringList args = QCoreApplication::arguments();

    if (args.contains(ARG_HIDE)) {
        mainWdo->hide();
        mainWdo->authen->start();
        mainWdo->update->checkUpdate(1);
    } else {
        mainWdo->show();
        mainWdo->authen->start();
    }

    return app.exec();
}


// 参考：https://blog.csdn.net/WMX843230304WMX/article/details/121955056
// Qt：程序启动一次 https://blog.csdn.net/weixin_41882459/article/details/108727851
