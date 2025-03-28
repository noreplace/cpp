#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QWidget>
#include <QLabel>
#include <textwidget.h>
#include <panelframe.h>
#include "menu.h"
#include <QVBoxLayout>
#include <QMenuBar>
#include <QMenu>
#include <QAction>

class MainWindow : public QWidget
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();
    MyLineEdit* getTextField() const;
    QLabel* getlabel() const;
    QLabel* getlabelcoding() const;
    QFrame *textpanel;
    QFrame *welcomeFrame;

    QJsonDocument *doc;
    QJsonObject *rootObj;
    QFile *configFile;
     QLabel *coding;


    QString last;

    QString getLastFile() const;
private slots:
    void loadConfig();
    void closeEvent(QCloseEvent* event) override;
private:
    MyLineEdit *line1;
    panelframe *frame_panel;
    QLabel *label;
    Controller *h;
    menu *bar;
    panelframe *toolframe;
};
#endif // MAINWINDOW_H
