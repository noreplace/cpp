#ifndef CONTROLLER_H
#define CONTROLLER_H

#include <QObject>

class MainWindow;

class Controller : public QObject
{
    Q_OBJECT

public:
    explicit Controller(MainWindow* mainWindow, QObject *parent = nullptr);


public slots:
    void setText(const QString& text);
    void gettext(const QString&);
    void openFile();

private:
    MainWindow* mainWindow_;
};

#endif // CONTROLLER_H
