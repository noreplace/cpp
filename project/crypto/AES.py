from tkinter import *
from tkinter.messagebox import *
from Crypto.Cipher import AES as aes
from console.console import _console
from tkinter.filedialog import *
from Crypto.Random import get_random_bytes
import log
class AES:
    def __init__(self,root, text):
        self.root = root
        self.text = text
    def _crp_file_AES(self, op):  # шифрование  файла(данные записываются в тот же файл.)
        def _encrp_AES(op):


            self.key = self.text3.get()
            if len(self.key) == 16 or 14 or 32:
                self.key = self.key.encode('utf-8')
                self.data = open(op, 'r').read().encode('utf-8')
                self.cipher = aes.new(self.key, aes.MODE_EAX)
                self.ciphertext, self.tag = self.cipher.encrypt_and_digest(self.data)
                print(f'tag {self.tag}')
                print(self.ciphertext)
                print(self.cipher.nonce)
                with open(op, "wb") as file:
                    file.write(self.cipher.nonce)
                    file.write(self.tag)
                    file.write(self.ciphertext)
                self.root0.destroy()
                showinfo('Шифрование',
                         'Данные были успешно зашифрованы в файл.\nИспользуйте ключ, который вы вводили при шифровании для дешифровки данных.')

                self.text.delete('1.0', END)

            else:
                showerror('Ошибка', 'Длина ключа должна быть 16, 24 или 32 символа!')

        self.root0 = Toplevel(self.root)
        self.root0.minsize(width=600, height=400)
        self.root0.maxsize(width=600, height=400)
        self.textt = Label(self.root0, text='Придумайте ключ (16, 24 или 32 символа)')
        self.textt.pack()
        self.text3 = Entry(self.root0)
        self.button = Button(self.root0, text='Отправить', command=lambda: _encrp_AES(op))
        self.text3.pack()
        self.button.pack()

    def _dcrp__AES(self, op):  # дешифрование данных(данные декодируются с открытого файла)
        def _decrtp(op):


            self.key = self.text3.get().encode('utf-8')
            self.file_in = open(op, "rb")
            self.nonce = self.file_in.read(16)
            self.tag = self.file_in.read(16)
            self.ciphertext = self.file_in.read()

            self.cipher = aes.new(self.key, aes.MODE_EAX, self.nonce)
            self.data = self.cipher.decrypt_and_verify(self.ciphertext, self.tag).decode('utf-8')
            message = f'Результат: {self.data}'
            _console(message)

        self.root0 = Toplevel(self.root)
        self.root0.minsize(width=600, height=400)
        self.root0.maxsize(width=600, height=400)
        self.textt = Label(self.root0, text='Введите ключ')
        self.textt.pack()
        self.text3 = Entry(self.root0)
        self.button = Button(self.root0, text='Отправить', command=lambda: _decrtp(op))
        self.text3.pack()
        self.button.pack()

    def _crp_AES(self, op):
        def _encrp_(op):  # зашифровать данные файла


            print(op)
            self.key = self.text3.get()
            if len(self.key) == 16 or 14 or 32:
                self.key = self.key.encode('utf-8')
                self.data = open(op, 'r').read().encode('utf-8')
                self.cipher = aes.new(self.key, aes.MODE_EAX)
                self.ciphertext, self.tag = self.cipher.encrypt_and_digest(self.data)
                self.root0.destroy()
                self.root0 = Toplevel(self.root)
                self.root0.minsize(width=600, height=400)
                self.root0.maxsize(width=600, height=400)
                self.text0 = Label(self.root0, text='Выберите файл для записи результатов')
                self.text0.pack()

                def open_file():
                    file = askopenfilename()
                    with open(file, "wb") as file:
                        [file.write(x) for x in (self.cipher.nonce, self.tag, self.ciphertext)]
                    self.root0.destroy()
                    showinfo('Шифрование файла', 'Данные были зашифрованы и записаны в файл.')

                def write_console():
                    with open('encrypt-data6534756.txt', 'wb') as file:
                        [file.write(x) for x in (self.cipher.nonce, self.tag, self.ciphertext)]
                    with open('encrypt-data6534756.txt', 'rb') as file:
                        data = file.read()#.decode('cp866')
                    self.root0.destroy()
                    message = f'Результат:\n{data}\n(encoding: cp866) '
                    _console(message)

                self.button = Button(self.root0, text='Выбрать файл', command=open_file)
                self.button.pack()
                self.button2 = Button(self.root0, text='Вывести на консоль', command=write_console)
                self.button2.pack()
            else:
                showerror('Ошибка', 'Длина ключа должна быть 16, 24 или 32 символа!')

        self.root0 = Toplevel(self.root)
        self.root0.minsize(width=600, height=400)
        self.root0.maxsize(width=600, height=400)
        self.textt = Label(self.root0, text='Придумайте ключ (16, 24 или 32 символа)')
        self.textt.pack()
        self.text3 = Entry(self.root0)
        self.button = Button(self.root0, text='Отправить', command=lambda: _encrp_(op))
        self.text3.pack()
        self.button.pack()

    def _decrtp_file(self, op):  #
        def _decrtp(op):
            global text

            self.key = self.text3.get().encode('utf-8')
            self.file_in = open(op, "rb")
            self.nonce, self.tag, self.ciphertext = [self.file_in.read(x) for x in (16, 16, -1)]

            self.cipher = aes.new(self.key, aes.MODE_EAX, self.nonce)
            self.data = self.cipher.decrypt_and_verify(self.ciphertext, self.tag).decode('utf-8')
            with open(op, 'w') as file:
                file.write(self.data)
            self.root0.destroy()
            showinfo('Дешифрование', 'Файл был дешифрован. Содержимое данных записано в файл.')
            self.text.delete('1.0', END)
            self.text.insert(END, self.data)

        self.root0 = Toplevel(self.root)
        self.root0.minsize(width=600, height=400)
        self.root0.maxsize(width=600, height=400)
        self.textt = Label(self.root0, text='Введите ключ')
        self.textt.pack()
        self.text3 = Entry(self.root0)
        self.button = Button(self.root0, text='Отправить', command=lambda: _decrtp(op))
        self.text3.pack()
        self.button.pack()
