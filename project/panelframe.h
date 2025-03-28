#ifndef PANELFRAME_H
#define PANELFRAME_H

#include <QFrame>
#include <QWidget>
class panelframe : public QFrame
{
    Q_OBJECT
public:
    explicit panelframe(QWidget *parent = nullptr);

signals:
};

#endif // PANELFRAME_H
