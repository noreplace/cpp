"""
Главный модуль проекта, содержит в себе построение структуры приложения.

Автор проекта: Максим Воропаев (noreplace)
Редакторы проекта отсутствуют.
Тестировщики проекта отсутствуют.

"""


from tkinter import ttk
from tkinter import *

from tkinter.filedialog import *
from tkinter.messagebox import *
import chardet
import re
from configparser import ConfigParser
from pathlib import Path

#импорт файлов проекта
import images
import log
import crypto
import func
#UPD: 18.11.24
title_window = "Nfile editor"
class editor:
    def __init__(self):
        pass
class Editor:
    def __init__(self, title, size, last_file):
        self.root = Tk()
        self.root.geometry(size)
        self.FRAME = Frame(self.root)
        self.root.title(title)
        self.op = last_file
        self.root.option_add("*tearOff", FALSE)

        self.root.config(bg='#303841')
        self.FRAME.pack(fill=BOTH, expand=True)
        self.FRAME.configure(bg='#303841')
        #self.root.iconphoto(True, PhotoImage(file='img.png'))
        self.interface()
        self.menu_interface()
        self.root.mainloop()
        self.flag_edit = 0


    def states(self, state):
        self.m.entryconfig("Правка", state=state)

    def interface(self):
        self.FRAME.columnconfigure(0, weight=0)
        self.FRAME.columnconfigure(1, weight=1)
        self.FRAME.rowconfigure(0, weight=0)
        self.FRAME.rowconfigure(1, weight=1)
        self.FRAME.columnconfigure(2, weight=0)

        self.hello_label = ttk.Label(self.FRAME, text='hello world')
        self.hello_label.grid(row=1, columnspan=3)


        self.numbers = Text(self.FRAME, width=5, bg='#303841', state=DISABLED, relief=FLAT, fg='#FFFFFF', highlightthickness=0)
        #font2 = font.Font(family="Arial", size=10, weight="normal")
        #self.numbers["font"] = font2
        self.numbers.grid(row=1, column=0, sticky='NS', padx = 30)
        scrl = ttk.Style()


        self.scroll = ttk.Scrollbar(self.FRAME, orient = "vertical")
        self.scroll.grid(row=1, column=2, sticky='NS')

        def on_yscrollcommand(*args):
            self.scroll.set(*args)
            self.numbers.yview_moveto(args[0])


        self.text = Text(self.FRAME, yscrollcommand=on_yscrollcommand, wrap=NONE, bg='#303841', fg='#FFFFFF', bd = 0, highlightthickness=0)
        self.text.grid(row=1, column = 1, sticky='NSWE')

        #self.text["font"] = font2

        color = '#2b2d30'

        self.frame_panel = Frame(self.FRAME, bg=color, height=1)
        self.frame_panel.grid(row=2, columnspan=3, sticky='NSWE')

        self.frame_panel.columnconfigure(2, weight=0)
        self.frame_panel.columnconfigure(1, weight=1)
        self.frame_panel.columnconfigure(0, weight=0)

        self.label_coding = ttk.Label(self.frame_panel, text='-',  background = color, foreground = 'white')
        self.label_coding.grid(row=0,column=2, padx=20)

        self.label_row_col = ttk.Label(self.frame_panel, text='-',  background = color, foreground = 'white')
        self.label_row_col.grid(row=0,column=1, sticky='SE', padx=40)


        def scroll_command(*args):
            self.text.yview(*args)
            self.numbers.yview(*args)

        self.scroll.config(command=scroll_command)

        def insert_numbers():
            count_of_lines = self.text.get(1.0, END).count('\n') + 1

            self.numbers.config(state=NORMAL)
            self.numbers.delete(1.0, END)
            self.numbers.insert(1.0, '\n'.join(map(str, range(1, count_of_lines))))
            self.numbers.config(state=DISABLED)

        def on_edit(event):
            insert_numbers()
            self.text.edit_modified(0)
        self.text.bind('<<Modified>>', on_edit)


        def show_cursor_position(flag=False):
            def wrapper(event):
                if flag:
                    x, y = event.x, event.y
                    index = self.text.index(f'@{x},{y}')
                    self.text.mark_set("insert", index)
                    self.text.see("insert")

                self.cursor_index = self.text.index(INSERT)
                line, column = self.cursor_index.split('.')
                self.label_row_col.config(text=f'{line}:{column}')

            return wrapper

        self.text.bind('<KeyRelease>', show_cursor_position())
        self.text.bind('<Button-1>', show_cursor_position(True))


        style = ttk.Style()
        style.map(
            'TLabel',

            background=[('active', '#43464b'), ('!active', color)],
            foreground=[('active', 'white'), ('!active', 'white')]
        )


        self.label_fileshow = ttk.Label(self.frame_panel, text='Hello', relief=FLAT, cursor='hand2', style='TLabel')
        self.label_fileshow.grid(row=0, column=0, sticky='SE', padx=40)

        def on_enter(event):
            event.widget.state(['active'])

        def on_leave(event):
            event.widget.state(['!active'])

        self.label_fileshow.bind('<Enter>', on_enter)
        self.label_fileshow.bind('<Leave>', on_leave)

    def menu_interface(self):
        self.frame_menu_panel = Frame(self.FRAME, bg='white')
        self.frame_menu_panel.grid(row=0, columnspan=3)
        self.frame_menu_panel.columnconfigure(0, weight=0)
        self.frame_menu_panel.columnconfigure(1, weight=1)
        self.frame_menu = Frame(self.frame_menu_panel)
        self.frame_menu.grid(row=0, column = 0)


        self.m = Menu(self.frame_menu, bg='#303841', fg='White', relief = FLAT, activebackground='#bcbcbc', font=('Times', 10) )
        self.root.config(menu=self.m)


        self.label_text_panel=Label(self.frame_menu_panel)
        self.label_text_panel.grid(row=0, sticky='E')

        """ Обработка меню и функционала."""
        self.fm = Menu(self.m)

        self.m.add_cascade(label="Файл", menu=self.fm)
        self.fm.add_command(label='Открыть                 Ctrl+O', command=self._open)
        self.fm.add_command(label="Создать                  Ctrl+Q", command = lambda a = func.func.func(self.op, self.text, self.root): a.create_file())
        self.fm.add_command(label="Сохранить", command=lambda a = func.func.func(self.op, self.text, self.root): a._save())
        self.fm.add_command(label="Сохранить как...")
        self.fm.add_command(label="Копировать", command= lambda a = func.func.func(self.op, self.text, self.root): a._copy_file())
        self.fm.add_command(label="Удалить", command=lambda a = func.func.func(self.op, self.text, self.root): a._delete())
        self.fm.add_command(label="Выход", command=lambda a = func.func.func(self.op, self.text, self.root): a.close_win(config, self.result))

        self.hm = Menu(self.m)
        self.FONT = Menu(self.m)
        self.size = Menu(self.m)
        self.m.add_cascade(label="Правка", menu=self.hm)  # !
        self.hm.add_cascade(label='Шрифт', menu=self.FONT)  # !
        self.FONT.add_command(label='Arial')
        self.FONT.add_command(label='Times New roman')
        self.FONT.add_command(label='Verdana')
        self.hm.add_command(label='Цвет')
        self.hm.add_cascade(label='Размер', menu=self.size)
        self.size.add_command(label='Увеличить')
        self.size.add_command(label='Уменьшить')



        self.cm = Menu(self.m)
        self.CRP = Menu(self.m)

        self.m.add_cascade(label="Шифрование", menu=self.cm)
        self.cm.add_cascade(label="Инструменты шифрования", menu=self.CRP)
        self.CRP.add_command(label='Открыть форму на шифрование', command=lambda: crypto.enc_form.form(self.root))
        self.CRP.add_command(label='Открыть форму на дешифрование', command=lambda: crypto.dcrp_form.form(self.root))

        self.HASH = Menu(self.m)
        self.BASE64 = Menu(self.m)
        self.sha = Menu(self.m)

        self.cm.add_cascade(label='Инструменты хеширования', menu=self.HASH)
        self.HASH.add_cascade(label='Base64', menu=self.BASE64)
        self.HASH.add_cascade(label='SHA-3', menu=self.sha)

        self.BASE64.add_command(label='Открыть форму на хеширование', command=lambda: crypto.enc_form.form_base64(self.root))
        self.BASE64.add_command(label='Открыть форму на дехеширование', command=lambda: crypto.dcrp_form.form_base64(self.root))

        self.sha.add_command(label='Хешировать', command = lambda: crypto.enc_form.sha(self.root))
        self.sha.add_command(label='Проверить целостность файла', command=lambda: crypto.enc_form.verify_file(self.root))
        self.BASE64.add_command(label='О Base64')

        self.qr = Menu(self.m)
        self.cm.add_cascade(label='QR', menu=self.qr)

        #self.encode_change = Menu(self.m)
        self.code = Menu(self.m)
        self.m.add_cascade(label='Кодировка', menu=self.code)
        self.code.add_command(label='Текущая кодировка', command=lambda a = func.func.func(self.op, self.text, self.root): a._chardet())
        #self.code.add_cascade(label='Перекодировать файл', menu=self.encode_change)
        #for n in encoding_():
            #self.encode_change.add_command(label=n, command=lambda enc=n: self.change_encode(enc))

        self.mm = Menu(self.m)
        self.m.add_cascade(label='Справка', menu=self.mm)  # !
        self.mm.add_command(label='О программе', command=lambda a = func.func.func(self.op, self.text, self.root): a._about_info())  # !
        self.mm.add_command(label='Руководство по использованию')  # !
        self.mm.add_command(label='Получить исходный код программы')  # !

        self.m.add_separator()

        self.states("disabled")

        if self.op != "0":
            self._open(flag=0)
            self.states("normal")
        self.root.bind('<Control-o>', self._open)
    def _open(self, event=None, flag=1):
        """ Ключевая функция. Открытие файла """
        global op
        global text_window
        if self.op == '0' or flag != 0:
            file = askopenfilename(title="Выберите файл",
                             filetypes=[("All files", "*.*"), ("Text File", ('*.text')), ("Python files", ('*.py')),
                                        ("PNG file", ('*.png')), ("JPG files", ('*.jpg'))])
            if file is not None:
                self.op = file

        if self.op:
            self.file = Path(self.op)

            if self.file.suffix in ['.jpg','.png','.ico']:
                images.file_open_image.image_open(self.root, self.op)

            try:
                with open(self.op, 'rb') as data:
                    bytes_data = data.read()
                result = chardet.detect(bytes_data)
                print(result)
                self.encoding = result['encoding']
                if self.encoding is None:
                    self.encoding = 'utf-8'
                with open(self.op, 'r', encoding=self.encoding) as file:
                    content = file.read()

                if content.endswith('\n'):
                    content = content[:-1]
                self.text.delete(1.0, END)
                self.text.insert(END, content)
                self.label_fileshow.config(text=self.op, font =('Times', 10) )
            except:
                pass
            self.root.bind('<Control-s>', lambda event: func.func.func(self.op, self.text, self.root)._save())


            self.root.protocol("WM_DELETE_WINDOW", lambda a = func.func.func(self.op, self.text, self.root): a.close_win(config, self.file.suffix, self.op))

            self.label_coding.config(text=self.encoding.upper())

            a = log.loggingNF.Logging()
            a._new_file_log(self.op)
            a._open_file_log(self.op)

if __name__ == '__main__':
    a = log.loggingNF.Logging()
    a._start_session_log()
    config = ConfigParser()
    config.read('config.ini')
    window = config['Window_configs']
    title = window.get('title')
    size = window.get('size')
    last_file = config['files'].get('last_file')

    if last_file is not None:
        start = Editor(title, size, last_file)
    else:
        start = Editor(title, size, None)

