#include "controller.h"
#include "mainwindow.h"
/* класс-обработчик главного окна. пока не нашел выигрыш в элегантности. */
Controller::Controller(MainWindow* mainWindow, QObject *parent)
    : QObject(parent), mainWindow_(mainWindow)
{
}

void Controller::setText(const QString& text) // устанавливает текст в поле
{
    mainWindow_->getTextField()->setText(text);
}
void Controller::gettext(const QString& text) // устанавливает текст в панели
{
    mainWindow_->getlabel()->setText(text);
    mainWindow_->setWindowTitle(text);
}
void Controller::openFile() // обработчик открытия файла
{

}
