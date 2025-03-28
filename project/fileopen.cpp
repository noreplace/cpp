#include "fileopen.h"
#include <iostream>
#include <QFile>
#include <QFileInfo>
#include <string>

#include "mainwindow.h"

/* файл, работающий с файлами. Содержит производный от контроллера класс. */
fileopen::fileopen(MainWindow *h, QWidget *parent, QString last)
    : Controller(h, parent), m(h), file(last)
{

    filen = new QFile(file);
    std::cout << file.toStdString() << std::endl;
    filen = new QFile(file);
    m->last = file;


}
fileopen::fileopen(MainWindow *h, QWidget *parent)
    : Controller(h, parent), m(h)
{
    file = QFileDialog::getOpenFileName();
    filen = new QFile(file);
    std::cout << file.toStdString() << std::endl;
    m->last = file;

}
void fileopen::getfile() // получить файл
{

    if (!filen->isOpen()) {
        filen->open(QIODevice::ReadOnly);
    }

    if (filen->isOpen()) {
        QByteArray fileData = filen->readAll();
        m->textpanel->setHidden(false);
        m->welcomeFrame->setHidden(true);

        m->getTextField()->setPlainText(QString::fromUtf8(fileData));
        filen->close(); // Закрытие файла после чтения
        QFileInfo inf = QFileInfo(file);
        m->getlabel()->setText(inf.fileName());
    }

}
void fileopen::writefile(QTextEdit *text)
{


    if (!filen->isOpen()) {
        filen->open(QIODevice::WriteOnly);
    }

    if (filen->isOpen()) {
        QByteArray fileData = text->toPlainText().toUtf8();
        filen->write(fileData);
        filen->flush();
        filen->close();
    }

}
