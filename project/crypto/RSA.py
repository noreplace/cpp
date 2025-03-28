'''
Модуль RSA, работает с криптографичееским методом асимметричного  шифрования RSA.
'''
from log.loggingNF import *
from Crypto.Random import get_random_bytes
from Crypto.PublicKey import RSA as RSA_gen
from Crypto.Cipher import AES, PKCS1_OAEP
from tkinter import *
from tkinter.messagebox import showinfo, showerror, askyesno
from tkinter.filedialog import askopenfilename
import re
class RSA:
    def __init__(self, root, text):
        self.root = root
        self.text = text
    def RSA_encrypt_file(self, op):
        print(op)                                   # функция если нажали кнопку зашифровать
        def encrypt(public):  # шифруем данные
            with open(op, 'r', encoding='utf-8') as file:
                data = file.read()
            print(data)
            with open(op, 'wb') as out_file:
                recipient_key = RSA_gen.import_key(
                    open(public).read()
                )
                session_key = get_random_bytes(16)

                cipher_rsa = PKCS1_OAEP.new(recipient_key)
                out_file.write(cipher_rsa.encrypt(session_key))

                cipher_aes = AES.new(session_key, AES.MODE_EAX)

                ciphertext, tag = cipher_aes.encrypt_and_digest(data.encode('utf-8'))

                out_file.write(cipher_aes.nonce)
                out_file.write(tag)
                out_file.write(ciphertext)
            showinfo('Шифрование файла', 'Успешно')
            a = Logging()
            a._encrypt_file_log_RSA()

        def save_passphrase():  # генерируем ключи

            self.code = self.text2.get()
            if self.code:
                if askyesno('Шифрование','Ваши данные с выбранных файлов будут удалены и переформатированы.\nВаш файл будет зашифрован\nВы уверены?'):

                    try:
                        key = RSA_gen.generate(2048)
                        encrypted_key = key.exportKey(
                            passphrase = self.code,
                            pkcs=8,
                            protection="scryptAndAES128-CBC"
                        )
                        private_key_file = self.text4.get()
                        result = re.sub(r'\.([^.]+)$', '', private_key_file)
                        file_private = f'{result}.bin'
                        with open(file_private, 'wb') as f:
                            f.write(encrypted_key)

                        public_key_file = self.text3.get()
                        result = re.sub(r'\.([^.]+)$', '', public_key_file)
                        file_public = f'{result}.pem'
                        with open(file_public, 'wb') as f:
                            f.write(key.publickey().exportKey())
                    except:
                        showerror("Ошибка", "Ошибка")
                        pass
                    else:
                        encrypt(file_public)
                        self.root2.destroy()

        def paste_file(configure):
            file = askopenfilename()
            if configure.get():
                configure.delete("1.0", "end")  #
            configure.insert(END, file)  #



        self.root2 = Toplevel(self.root)
        # root2.minsize(width=600,height=300)
        # root2.maxsize(width=600,height=300)
        self.frame1 = Frame(self.root2)
        self.frame1.pack()

        self.label = Label(self.frame1, text='Придумайте ключ(он нужен для составления ключей)')
        self.label.grid(row=0, column=0)

        self.text2 = Entry(self.frame1)  ##########
        self.text2.grid(row=1, column=0)
        self.label2 = Label(self.frame1, text='Введите имя или путь к файлу для записи открытого ключа')
        self.label2.grid(row=2, column=0)
        self.text3 = Entry(self.frame1)  ##########
        self.text3.grid(row=3, column=0)
        self.button2 = Button(self.frame1, text='Выбрать файл', command=lambda: paste_file(self.text3))
        self.button2.grid(row=3, column=1, sticky='w')

        self.label3 = Label(self.frame1, text='Введите имя файла для записи закрытого ключа')
        self.label3.grid(row=4, column=0)
        self.text4 = Entry(self.frame1)  #####
        self.text4.grid(row=5, column=0)

        self.button3 = Button(self.frame1, text='Выбрать файл', command=lambda: paste_file(self.text4))
        self.button3.grid(row=5, column=1)

        self.button = Button(self.frame1, text='Отправить', command= save_passphrase)
        self.button.grid(row=6, column=0)


    def RSA_decrypt_file(self, op):  # дешифровальщик
        def decrypt_rsa():  # дешифруем данные и выводим на экран

            self.code = self.text2.get()
            self.file = self.text3.get()
            self.root2.destroy()
            if self.code:
                with open(op, 'rb') as fobj:
                    try:
                        private_key = RSA_gen.import_key(
                            open(self.file).read(),
                            passphrase=self.code
                        )

                        enc_session_key, nonce, tag, ciphertext = [
                            fobj.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1)
                        ]
                        cipher_rsa = PKCS1_OAEP.new(private_key)
                    except ValueError:
                        showerror('Ошибка', 'Неверный ключ!')

                    if len(enc_session_key) != private_key.size_in_bytes():
                        raise ValueError("Длина зашифрованного ключа не соответствует размеру ключа RSA.")
                    session_key = cipher_rsa.decrypt(enc_session_key)

                    cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
                    data = cipher_aes.decrypt_and_verify(ciphertext, tag)
                    print(data)
                    with open(op, 'w') as file:
                        file.write(data.decode('utf-8'))
                        self.text.delete('1.0', END)
                        self.text.insert(END, data.decode('utf-8'))

                a = Logging()
                a._decrypt_file_log_RSA()
        def paste_file(configure):
            file = askopenfilename()
            if configure.get():
                configure.delete("1.0", "end")  #
            configure.insert(END, file)  #

        self.root2 = Toplevel(self.root)
        # root2.minsize(width=600,height=300)
        # root2.maxsize(width=600,height=300)

        self.frame1 = Frame(self.root2)
        self.frame1.pack()

        self.label = Label(self.frame1, text='Введите ключ')
        self.label.grid(row=0, column=0)

        self.text2 = Entry(self.frame1)  ##########
        self.text2.grid(row=1, column=0)
        self.label2 = Label(self.frame1, text='Введите имя или путь к файлу, содержащему приватный ключ для дешифрования')
        self.label2.grid(row=2, column=0)
        self.text3 = Entry(self.frame1)  ##########
        self.text3.grid(row=3, column=0)
        self.button2 = Button(self.frame1, text='Выбрать файл', command=lambda: paste_file(self.text3))
        self.button2.grid(row=3, column=1, sticky='w')
        self.button = Button(self.frame1, text='Отправить', command=decrypt_rsa)
        self.button.grid(row=6, column=0)

















































'''

def _global_decryptor_RSA():
    def _decryptor_file_global_RSA():  # глобальный дешифровальщик
        global op  # дешифрует данные и записывает их в тот же файл
        global correct_encoding
        text4 = text3.get()
        code = f'{text4}'
        root3.destroy()
        path = op
        file_name = re.search(r'([^\\/]+)(?=\.\w+$)', path)
        if file_name:
            file_name = file_name.group(1)
        else:
            file_name = re.search(r'([^/\\]+)(?=\.[^./\\]+$|$)', path).group(1)
            if file_name:
                file_name = file_name.group(1)
            else:
                print('-')
        with open(op, 'rb') as fobj:
            try:
                private_key = RSA.import_key(
                    open(f'my_private_rsa_key_{file_name}.bin').read(),
                    passphrase=code
                )

                enc_session_key, nonce, tag, ciphertext = [
                    fobj.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1)
                ]
                cipher_rsa = PKCS1_OAEP.new(private_key)
            except ValueError:
                showerror('Ошибка', 'Неверный ключ!')
            if len(enc_session_key) != private_key.size_in_bytes():
                raise ValueError("Длина зашифрованного ключа не соответствует размеру ключа RSA.")
            session_key = cipher_rsa.decrypt(enc_session_key)

            cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
            data = cipher_aes.decrypt_and_verify(ciphertext, tag)
            text.delete(1.0, END)
            text.insert(END, data.decode('utf-8'))
            decrypt = text.get("1.0", "end")
            correct_encoding = 'utf-8'
            with open(op, 'w') as file:
                file.write(decrypt)

    root3 = Toplevel()
    root3.minsize(width=200, height=100)
    root3.maxsize(width=200, height=100)
    textt = Label(root3, text='Введите ключ')
    textt.pack()
    text3 = Entry(root3)
    button = Button(root3, text='Отправить', command=_decryptor_file_global)
    text3.pack()
    button.pack()


'''

