#include "textwidget.h"
#include "mainwindow.h"

#include <QAction>
#include <iostream>
#include <QMenu>
#include <QMessageBox>
MyLineEdit::MyLineEdit(int id, QWidget *parent, MainWindow* w)
    : QTextEdit(parent), id_(id), mainwindow(w)
{

    setStyleSheet("background-color: #303841;");


    setTextColor("white");
    setAutoFormatting(QTextEdit::AutoNone);
    setWordWrapMode(QTextOption::NoWrap);
    setAcceptRichText(false);
    font = 13;

    a = new QFont("Courier New", font);
    setFont(*a);

    connect(this, SIGNAL(cursorPositionChanged()), this, SLOT(oncursorPositionChanged()));

}

void MyLineEdit::focusInEvent(QFocusEvent *e)
{
    std::cout << "Получен фокус полем " << id_ << std::endl;
    QTextEdit::focusInEvent(e);
}

void MyLineEdit::focusOutEvent(QFocusEvent *e)
{
    std::cout << "Потерян фокус полем " << id_ << std::endl;
    QTextEdit::focusOutEvent(e);
}
void MyLineEdit::keyPressEvent(QKeyEvent *event)
{



    if (event->modifiers().testFlag(Qt::ControlModifier) && event->key() == Qt::Key_Minus) {
        font-=2;
        a->setPointSize(font);
        setFont(*a);

    } else if (event->modifiers().testFlag(Qt::ControlModifier) && event->key() == Qt::Key_Plus){
        font+=2;
        a->setPointSize(font);
        setFont(*a); // Передаем остальные события родительскому классу
    }
    else
        QTextEdit::keyPressEvent(event);



}
void MyLineEdit::contextMenuEvent(QContextMenuEvent *event)
{
    QMenu *contextMenu = new QMenu(this);
    contextMenu->setStyleSheet( // CONST !!!!!!!!
        "QMenu::item { padding: 3px; background-color: #2d343b; }"
        "QMenu::item:selected { background-color: #353c45; color: white; }"
        "QMenu::item:hover { background-color: #353c45; color: white; }"
        "QMenuBar{background-color: #2d343b;}"
        "QMenu { border: 1px solid black; }"
        );
    cutAction = new QAction(tr("Вырезать"), this);
        cutAction->setShortcut(tr("Ctrl+X"));

    copyAction = new QAction(tr("Копировать"), this);
        copyAction->setShortcut(tr("Ctrl+C"));
    pasteAction = new QAction(tr("Вставить"), this);
        pasteAction->setShortcut(tr("Ctrl+V"));

    contextMenu->addAction(cutAction);
    contextMenu->addAction(copyAction);
    contextMenu->addAction(pasteAction);

    connect(cutAction, &QAction::triggered, this, &MyLineEdit::cut);
    connect(copyAction, &QAction::triggered, this, &MyLineEdit::copy);
    connect(pasteAction, &QAction::triggered, this, &MyLineEdit::paste);
    contextMenu->exec(event->globalPos());

}
void MyLineEdit::oncursorPositionChanged() {
    QTextCursor cursor = textCursor();

    int lineNumber = cursor.blockNumber(); // Номер строки, начиная с 0
    int columnNumber = cursor.columnNumber(); // Положение курсора в строке, начиная с 0

    QString message = QString("%1:%2").arg(lineNumber + 1).arg(columnNumber + 1);

    mainwindow->coding->setText(message);
    // Здесь можно выполнять любые другие действия при изменении позиции курсора
}
