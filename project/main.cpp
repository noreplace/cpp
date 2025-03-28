#include "mainwindow.h"
#include <QApplication>

/* Главный файл. Тут можно тестировать все, но весь код должен помещаться в этот файл.
 Если ты это читаешь, я буду рад тебя видеть в моей команде в качестве разработчика/тестировщика.
Проект пишется с декабря 2024г. */

int main(int argc, char *argv[])
{
    QApplication app(argc, argv);

    MainWindow w;


    w.show();

    return app.exec();
}
