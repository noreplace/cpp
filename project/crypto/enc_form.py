from tkinter import *
from tkinter.filedialog import *
from tkinter import ttk
class form():
    def __init__(self, root):
        self.root = root
        self.root2 = Toplevel(self.root)
        self.root2.geometry('1700x1200')
        self.interface()
        self.root2.mainloop()
    def interface(self):



        self.frame = Frame(self.root2)
        self.frame.pack(fill=BOTH, expand=True)

        self.frame.columnconfigure(1, weight=0)
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(2, weight=0)
        self.frame.columnconfigure(1, weight=0)
        self.frame.columnconfigure(0, weight=0)


        self.label = Label(self.frame, text='Укажите файл или директорию')
        self.label.grid(row=0, column=0, sticky='nw', padx=20, pady=20)
        self.label_list = Label(self.frame, text='Алгоритм шифрования')
        self.label_list.grid(row=0, column=2, padx = 60)



        self.entry_file = Entry(self.frame, width=40)
        self.entry_file.grid(row=1, column = 0, padx=20,sticky='nw')


        def paste_file(widget):
            file = askopenfilename()
            if widget.get():
                widget.delete(1.0, END)
            widget.insert(END, file)

        self.button_1 = Button(self.frame, text='Выбрать', command=lambda: paste_file(self.entry_file))
        self.button_1.grid(row=1, column=1, sticky='nw')



        self.encryption_mode = ['AES', 'AES-GCM', 'AES-CBC', 'ChaCha1305Poly', 'AES', 'ECC', 'RSA', '', '']

        self.mode = StringVar()

        self.mode_enc = ttk.Combobox(self.frame, textvariable=self.mode, values=self.encryption_mode, width=20)
        self.mode_enc.grid(row=1, column=2, sticky='nw', padx = 60)

        self.mode_enc.bind("<<ComboboxSelected>>", self.get_mode_interface)

    def get_mode_interface(self, event):
        enc_mode = self.mode.get()
        if enc_mode in ['AES', 'AES-CBC', 'AES-GCM']:
            try:
                self.frame_key.destroy()
            except:
                pass
            self.frame_key = Frame(self.frame)
            self.frame_key.grid(row = 2, columnspan=3, sticky='nswe')

            self.label_key = Label(self.frame_key, text = 'Ключ')
            self.label_key.grid(row=0, column = 0, sticky='nw', padx=20, pady=30)

            self.entry_key = Entry(self.frame_key, width = 30)
            self.entry_key.grid(row=1, column=0, sticky='nw', padx=20, pady=10)

            self.button_key = Button(self.frame_key, text='Импортировать')
            self.button_key.grid(row=1, column=1)

            self.button_generate = Button(self.frame_key, text='Сгенерировать')
            self.button_generate.grid(row=1, column=2)

        if enc_mode in ['RSA']:
            try:
                self.frame_key.destroy()
            except:
                pass
            self.frame_key = Frame(self.frame)
            self.frame_key.grid(rowspan = 2, columnspan=3, sticky='nswe')

            self.label_key = Label(self.frame_key, text='Открытый ключ')
            self.label_key.grid(row=0, column=0, sticky='nw', padx=20, pady=30)

            self.entry_key = Entry(self.frame_key, width=30)
            self.entry_key.grid(row=1, column=0, sticky='nw', padx=20, pady=10)

            self.button_key = Button(self.frame_key, text='Импортировать')
            self.button_key.grid(row=1, column=1)

            self.button_generate = Button(self.frame_key, text='Сгенерировать')
            self.button_generate.grid(row=1, column=2)

            self.label_private_key = Label(self.frame_key, text = 'Закрытый ключ')
            self.label_private_key.grid(row = 2)
class form_base64():
    def __init__(self, root):
        self.root = root
class sha():
    def __init__(self, root):
        self.root = root
    def verify_file(self):
        pass

