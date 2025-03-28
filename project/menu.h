#ifndef MENU_H
#define MENU_H
#include "controller.h"
#include "fileopen.h"
#include <QWidget>
#include <QMenuBar>
#include <QMenu>
#include <QAction>
class MainWindow;
class menu : public QMenuBar // меню
{
    Q_OBJECT
public:
    explicit menu( QWidget *parent = nullptr, MainWindow* mainWindow = nullptr);
    fileopen *h;
    QString a;

    void checkLastFile();

private:
    /* Тут код меню проекта, Обработчики в конструкторе. */
    MainWindow* mainWindow_;


    QMenu *fileMenu;

    // Добавление пунктов в меню "Файл"

    QAction *openAction ;

    QAction *newAction ;

    QAction *saveaction ;

    QAction *saveas ;
    QAction *copyfile ;

    QAction *exitAction ;

    // Создание вложенного меню "Редактирование"
    QMenu *editMenu ;

    // Добавление пунктов во вложенное меню "Редактирование"
    QAction *undo ;
    QAction *redo ;
    QAction *cutAction ;
    QAction *copyAction ;
    QAction *pasteAction ;


    QMenu *toolMenu ;

    QMenu *crpAction;
    QAction *formenc ;
    QAction *formdec ;
    QMenu *hashAction ;

    QMenu *about ;

    QAction *about_program ;

};

#endif // MENU_H
