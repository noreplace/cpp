#include "menu.h"
#include "mainwindow.h"
#include "aes.h"
#include <iostream>
#include <QStyle>
/* Конструктор класса menu. Код в menu.h в целях поддержки других методов, которые будут добавляться сюда. */
menu::menu(QWidget *parent, MainWindow* mainWindow)
    : QMenuBar(parent), mainWindow_(mainWindow)
{




    fileMenu = QMenuBar::addMenu("&Файл");

    // Добавление пунктов в меню "Файл"

        openAction = fileMenu->addAction("&Открыть");
            openAction->setShortcut(tr("Ctrl+O"));

        newAction = fileMenu->addAction("Со&здать");
            newAction->setShortcut(tr("Ctrl+Shift+N"));

        saveaction = fileMenu->addAction("&Сохранить");
           saveaction->setShortcut(tr("Ctrl+S"));
        saveas = fileMenu->addAction("Со&хранить как...");

        copyfile = fileMenu->addAction("&Копировать файл");
        fileMenu->addSeparator();
        exitAction = fileMenu->addAction("&Выход");



    // Создание вложенного меню "Редактирование"
    editMenu = QMenuBar::addMenu("&Правка");

        // Добавление пунктов во вложенное меню "Редактирование"
        undo = editMenu->addAction("Отменить");
            undo->setShortcut(tr("Ctrl+Z"));
        redo = editMenu->addAction("Повторить");
             redo->setShortcut(tr("Ctrl+Shift+Z"));

        cutAction = editMenu->addAction("Вырезать");

        copyAction = editMenu->addAction("Копировать");

        pasteAction = editMenu->addAction("Вставить");


    toolMenu = QMenuBar::addMenu("&Инструменты");

        crpAction = toolMenu->addMenu("&Шифрование");

            formenc = crpAction->addAction("Открыть форму на шифрование");

            formdec = crpAction->addAction("Открыть форму на дешифрование");

        hashAction = toolMenu->addMenu("&Хеширование");

        QAction *tested = toolMenu->addAction("&Зашифровать (AES)");
        QAction *dcrptest = toolMenu->addAction("&Дешифровать (AES)");
    about = QMenuBar::addMenu("Cправка");

        QAction *management = about->addAction("Руководство по использованию");

        about_program = about->addAction("О программе");

        QAction *sayError = about->addAction("Сообщить об ошибке");
    setStyleSheet( // CONST !!!!!!!!
        "QMenu::item { padding: 3px; background-color: #2d343b; \
        text-align: left; padding-left: 10px; min-width: 180px; padding-right: 30px;}"


        "QMenu::item:selected { background-color: #353c45; color: white; }"
        "QMenu::item:hover { background-color: #353c45; color: white; }"
        "QMenuBar{background-color: #2d343b;}"
        "QMenu { border: 1px solid black; }"
        );

    connect(openAction, &QAction::triggered, [this]() {

        h = new fileopen(mainWindow_, this);


        h->getfile();



    });
    connect(undo, &QAction::triggered, [this]() {
        mainWindow_->getTextField()->undo();
    });
    connect(redo, &QAction::triggered, [this]() {
        mainWindow_->getTextField()->redo();
    });
    connect(saveaction, &QAction::triggered, [this]() {

        h->writefile(mainWindow_->getTextField());

    });

    connect(exitAction, &QAction::triggered, this, exit);

    connect(tested, &QAction::triggered, [this]() {
        std::string inputFilePath(mainWindow_->last.toStdString());
        std::string outputFilePath(mainWindow_->last.toStdString() + ".enc");

        // Ключ и IV
        unsigned char key[32], iv[16];

        if (!generateKeyAndIv(key, iv)) {
            std::cerr << "Ошибка генерации ключа и IV." << std::endl;
            return 1;
        }

        // Шифруем файл
        if (encryptFile(inputFilePath, outputFilePath, key, iv) != 0) {
            std::cerr << "Ошибка шифрования файла." << std::endl;
            return 1;
        }
        saveKeyAndIvToFile("keys.txt", key, iv);
        std::cout << "Файл успешно зашифрован!" << std::endl;
        return 1;
    });

    connect(dcrptest, &QAction::triggered, [this]() {
        std::string inputFilePath(mainWindow_->last.toStdString());
        std::string outputFilePath(mainWindow_->last.toStdString());

        unsigned char key[32], iv[16];

        loadKeyAndIvFromFile("keys.txt", key, iv);

        if (decryptFile(inputFilePath, outputFilePath, key, iv) != 0) {
            std::cerr << "Ошибка дешифрования файла." << std::endl;
            return 1;
        }
        return 1;
    });

}
void menu::checkLastFile()
{
    if (!(mainWindow_->getLastFile() == ""))
    {
        h = new fileopen(mainWindow_, this, mainWindow_->getLastFile());
        h->getfile();
    }
}
