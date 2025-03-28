#include "panelframe.h"
#include <QLabel>
/* Нижняя панель. Будет отображаться файл, позиция курсора и кодировка. */
panelframe::panelframe(QWidget *parent)
    : QFrame{parent}
{


    setFrameShape(QFrame::Box);  // Просто для наглядности, чтобы видеть границы фрейма

    setFrameStyle(QFrame::StyledPanel | QFrame::Raised);
    setLineWidth(2);

    setStyleSheet( "background-color: #2d343b;");
}
