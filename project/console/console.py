"""
Вспомогательный модуль. Используется для вывода данных на экран.
"""
from tkinter import *
def _console(text):
    """ Вспомогательное окно. Выводит информацию без возможности редактирования """
    root = Tk()
    root.title('NFile info')
    root.minsize(width=600,height=400)    
    txt = Text(root, fg='#FFFFFF', bg='#303841', state=NORMAL)
    txt.pack(fill=BOTH,expand=True)
    txt.insert(END, text)
    txt.config(state=DISABLED)
    root.mainloop()

def console(): # полноценная консоль (доработать если останется время)
    pass



