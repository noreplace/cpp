CONFIG += static
QT       += core gui
QT += core gui widgets
greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

CONFIG += c++17

# You can make your code fail to compile if it uses deprecated APIs.
# In order to do so, uncomment the following line.
#DEFINES += QT_DISABLE_DEPRECATED_BEFORE=0x060000    # disables all the APIs deprecated before Qt 6.0.0

SOURCES += \
    aes.cpp \
    coding.cpp \
    controller.cpp \
    fileopen.cpp \
    main.cpp \
    mainwindow.cpp \
    menu.cpp \
    panelframe.cpp \
    textwidget.cpp

HEADERS += \
    aes.h \
    coding.h \
    controller.h \
    fileopen.h \
    mainwindow.h \
    menu.h \
    panelframe.h \
    textwidget.h


LIBS += -L/usr/lib -lcrypto -lssl
# Default rules for deployment.
qnx: target.path = /tmp/$${TARGET}/bin
else: unix:!android: target.path = /opt/$${TARGET}/bin
!isEmpty(target.path): INSTALLS += target

DISTFILES += \
    config.json \
    img.png

RESOURCES += \
    resources.qrc
