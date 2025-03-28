#ifndef TEXTWIDGET_H
#define TEXTWIDGET_H

#include <QWidget>
#include <QTextEdit>
#include <QFocusEvent>
#include <QMenu>
class MainWindow;
class MyLineEdit : public QTextEdit
{
    Q_OBJECT
public:
    MyLineEdit(int id, QWidget *parent=nullptr, MainWindow *w = nullptr);
    int font ;
protected:
    void focusInEvent(QFocusEvent *e) override;
    void focusOutEvent(QFocusEvent *e) override;
    void keyPressEvent(QKeyEvent *event) override;
    void contextMenuEvent(QContextMenuEvent *event) override;

private slots:
    void oncursorPositionChanged();

private:
    QMenu *contextMenu;
    QAction *cutAction;
    QAction *copyAction;
    QAction *pasteAction;

signals:


private:
    int id_;
    QFont *a;
    MainWindow *mainwindow;
};
#endif // MYLINEEDIT_H
