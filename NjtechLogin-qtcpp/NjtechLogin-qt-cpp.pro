QT       += core gui network
greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

CONFIG += c++11

TARGET = NjtechAuthen

# You can make your code fail to compile if it uses deprecated APIs.
# In order to do so, uncomment the following line.
#DEFINES += QT_DISABLE_DEPRECATED_BEFORE=0x060000    # disables all the APIs deprecated before Qt 6.0.0

SOURCES += \
    custoui/loginwidget.cpp \
    custoui/rightbox.cpp    \
    custoui/titlebar.cpp    \
    custoui/mainwidget.cpp  \
    service/authen.cpp \
    service/update.cpp      \
    service/utils.cpp \
    window/main_wdo.cpp     \
    main.cpp \


HEADERS += \
    constants.h             \
    custoui/appsetting.h    \
    custoui/loginwidget.h   \
    custoui/mainwidget.h    \
    custoui/rightbox.h      \
    custoui/titlebar.h      \
    service/authen.h \
    service/update.h        \
    service/utils.h \
    window/main_wdo.h       \


FORMS += \
    custoui/loginwidget.ui \
    custoui/mainwidget.ui  \
    custoui/rightbox.ui


# Default rules for deployment.
qnx: target.path = /tmp/$${TARGET}/bin
else: unix:!android: target.path = /opt/$${TARGET}/bin
!isEmpty(target.path): INSTALLS += target

RESOURCES += \
    resource.qrc \
    resources.qrc

DISTFILES += \
    appinfo.rc

RC_FILE += appinfo.rc
