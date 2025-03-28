#include "mainwindow.h"
#include "panelframe.h"
#include "menu.h"
#include "fileopen.h"



#include <QPushButton>
#include <QVBoxLayout>
#include <QHBoxLayout>
#include <QLabel>
#include <QFrame>

#include <QJsonDocument>
#include <QJsonObject>

#include <QMessageBox>

#include <iostream>
/* Это код главного окна проекта. Он собирает все (виджеты) в кучу и компонует их. */
MainWindow::MainWindow(QWidget *parent) :
    QWidget(parent)

{



    // фрейм всего окна
    QFrame *frame = new QFrame(this);

    frame->setLineWidth(2);

    QVBoxLayout *layout = new QVBoxLayout(this);
    layout->setContentsMargins(0, 0, 0, 0);


    setWindowTitle("NFile editor");

    resize(900, 700);



    loadConfig();


    // производный класс меню
    bar = new menu(this, this);


    layout->setMenuBar(bar);
    layout->addWidget(frame);

    QHBoxLayout *vbox = new QHBoxLayout(frame); // компоновка всего, что за меню
    vbox->setContentsMargins(0, 0, 0, 0); // компоновка панели инструментов и текстового поля
    vbox->setSpacing(0);



        toolframe = new panelframe(frame); // фрейм-панель для отображения инструментов
        vbox->addWidget(toolframe); // компоновка слева

            QVBoxLayout *vbox_tools = new QVBoxLayout(toolframe); // размещение
            vbox_tools->setContentsMargins(0, 0, 0, 0);

                QPushButton *test = new QPushButton(toolframe); //

                    QIcon icon(":/images/img.png");
                    test->setIcon(icon);
                    test->setFlat(true);

                vbox_tools->addWidget(test);
                vbox_tools->addStretch();



        QFrame *textframe = new QFrame(frame); // фрейм для отображения текстового поля и нижней панели
        vbox->addWidget(textframe);

            QVBoxLayout *panelbox = new QVBoxLayout(textframe); // компоновка текстового поля и панели
            panelbox->setContentsMargins(0, 0, 0, 0);
            panelbox->setSpacing(0);

            textpanel = new QFrame(textframe);
            textpanel->setHidden(true); // пока скроем
            panelbox->addWidget(textpanel);

            QVBoxLayout *textbox = new QVBoxLayout(textpanel); // компоновка текстового поля
            textbox->setContentsMargins(0, 0, 0, 0);
            textbox->setSpacing(0);
                line1 = new MyLineEdit(1, textpanel, this);  // само поле
                textbox->addWidget(line1);

            welcomeFrame = new QFrame(textframe);
            panelbox->addWidget(welcomeFrame);

                QVBoxLayout *panel = new QVBoxLayout(welcomeFrame); // компоновка текстового поля и панели
                panel->setContentsMargins(0, 0, 0, 0);
                panel->setSpacing(0);

                QLabel *llabel = new QLabel("Добро пожаловать в NFile editor.\nВоспользуйтесь меню или клавишами Ctrl+O\nчтобы открыть документ.", welcomeFrame);
                llabel->setAlignment(Qt::AlignCenter);
                panel->addWidget(llabel);



            frame_panel = new panelframe(textframe); // нижняя панель
            panelbox->addWidget(frame_panel);

                        QGridLayout *panellayout = new QGridLayout(frame_panel);
                        panellayout->setContentsMargins(10, 0, 10, 0);
                        label = new QLabel("fwe", frame_panel);
                        panellayout->addWidget(label, 0, 0);
                        coding = new QLabel("fe");
                        coding->setAlignment(Qt::AlignRight);
                        panellayout->addWidget(coding, 0, 1);

        vbox->setStretchFactor(toolframe, 0);
        vbox->setStretchFactor(textframe, 1); // задание веса фреймов

        panelbox->setStretchFactor(textpanel, 1);
        panelbox->setStretchFactor(welcomeFrame, 1);
        panelbox->setStretchFactor(frame_panel, 0);

        bar->checkLastFile();
}
/* Структура интерфейса.
 Сверху расположено меню. После меню расположен фрейм, занимающий все пространство. На фрейме
 расположены еще 2 фрейма. главный компоновщик - компоновщак по горизонтали. Он компонует 2 этих
фрейма. На первом фрейме расположена левая панель инструментов, значение веса выставлено 0. На втором
фрейме расположены еще 2 фрейма, скомпонованных по вертикали. На первом фрейме расположено текстовое
поле. На втором фрейме расположена нижняя панель, значение веса выставлено 0.



*/

// деструктор
MainWindow::~MainWindow()
{

}


MyLineEdit* MainWindow::getTextField() const
{
    return line1;
}
QLabel* MainWindow::getlabel() const
{
    return label;
}
QLabel* MainWindow::getlabelcoding() const
{
    return coding;
}
QString MainWindow::getLastFile() const
{
    if (rootObj->contains("LastFile"))
        return (rootObj->value("LastFile").toString());
    return "";
}
void MainWindow::loadConfig()
{

    configFile = new QFile("config.json");
    if (!configFile->open(QIODevice::ReadOnly | QIODevice::Text)) {
        return;
    }

    QByteArray data = configFile->readAll();
    configFile->close();

    QJsonParseError error;
    doc = new QJsonDocument(QJsonDocument::fromJson(data, &error));

    if (doc->isNull()) {
        std::cout  << error.errorString().toStdString();
        qDebug() << "JSON Data:" << data;
        QMessageBox::critical(this, tr("Error"), (error.errorString()));
        return;
    }

    rootObj = new QJsonObject(doc->object());


    if (rootObj->contains("title")) {
        setWindowTitle(rootObj->value("title").toString());
    }
    if (rootObj->contains("size")) {
        int width = rootObj->value("width").toInt();
        std::cout << width;
        int height = rootObj->value("height").toInt();
        resize(width, height);
    }
}

void MainWindow::closeEvent(QCloseEvent* event)
{
    QFile *configFile = new QFile("config.json");
    if (!configFile->open(QIODevice::WriteOnly | QIODevice::Text)) {

        QMessageBox::information(this, tr("Success"), (configFile->errorString()));
    }
    if (!configFile->isWritable()) {
        qDebug() << "Файл не доступен для записи.";
        QMessageBox::information(this, tr("Success"), tr("файл не доступен для записи"));
    }

    if (configFile->isOpen()) {
        QJsonObject roottObj = doc->object();
        roottObj["title"] = windowTitle();
        roottObj["width"] = size().width();
        roottObj["height"] = size().height();
        roottObj["LastFile"] = last;

        doc->setObject(roottObj);
        configFile->write(doc->toJson());
        configFile->close();


    }


}
