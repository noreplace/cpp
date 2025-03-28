#ifndef FILEOPEN_H
#define FILEOPEN_H
#include <QFileDialog>
#include <QWidget>
#include "controller.h"
#include <QTextEdit>
std::string detect_encoding(const std::string& file_path);
class fileopen : public Controller
{
    Q_OBJECT
public:
    explicit fileopen(MainWindow* h, QWidget *parent, QString last);
    explicit fileopen(MainWindow *h, QWidget *parent);
    void getfile();
    MainWindow* m;
    QString file = "skdjfhksjf";
    void writefile(QTextEdit *text);
    QFile *filen;

    void getaskfile();
private:

};

#endif // FILEOPEN_H
