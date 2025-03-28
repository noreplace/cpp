'''
файл, отвечающий за логирование проекта.
Создан для отслеживания действий на непредвиденный случай.
'''
import time
import getpass
import json
class Logging:
    def __init__(self):
        self.times = time.strftime("%d.%m.%Y %H:%M:%S")
        self.file = None
        self.name = getpass.getuser()
    def _new_file_log(self, file):
        self.file = file
    
    def _start_session_log(self):
        with open('../logNF.txt', "a", encoding='utf-8') as log_file:
            log_file.write(f'\n\n++++++++++NEW SESSION: {self.times} USERNAME: {self.name} ++++++++++<<<<<<<<<<<<<<')
            print('+')
    def _open_file_log(self, file):
        with open('../logNF.txt', "a", encoding='utf-8') as log_file:
            log_file.write(f'\n{self.times}: открыт файл {self.file} | Пользователь: {self.name}')
           
    def _save_file_log(self, file):
        with open('../logNF.txt', "a", encoding='utf-8') as log_file:
            log_file.write(f'\n{self.times}: сохранен файл {self.file} | Пользователь: {self.name} ')
           
    def _delete_file_log(self):
        with open('../logNF.txt', "a", encoding='utf-8') as log_file:
            log_file.write(f'\n{self.times}: удален файл {self.file} | Пользователь: {self.name} ')
           
    def _encrypt_file_log_RSA(self):
        with open('../logNF.txt', "a", encoding='utf-8') as log_file:
            log_file.write(f'\n{self.times}: (RSA) Зашифрован файл {self.file} | Пользователь: {self.name} ')
            
    def _decrypt_file_log_RSA(self):
        with open('../logNF.txt', "a", encoding='utf-8') as log_file:
            log_file.write(f'\n{self.times}: (RSA) Дешифрован файл {self.file} | Пользователь: {self.name} ')
    def _encrypt_AES(self):
        with open('../logNF.txt', "a", encoding='utf-8') as log_file:
            log_file.write(f'\n{self.times}: (AES) Зашифрованы данные файла {self.file} и выведены на консоль | Пользователь: {self.name} ')
    def _decrypt_AES(self):
        with open('../logNF.txt', "a", encoding='utf-8') as log_file:
            log_file.write(f'\n{self.times}: (AES) Дешифрованы данные с файла  {self.file} и выведены на консоль | Пользователь: {self.name} ')
    def _encrypt_file_AES(self):
        with open('../logNF.txt', "a", encoding='utf-8') as log_file:
            log_file.write(f'\n{self.times}: (AES) Зашифрован файл {self.file} | Пользователь: {self.name} ')
    def _decrypt_file_AES(self):
        with open('../logNF.txt', "a", encoding='utf-8') as log_file:
            log_file.write(f'\n{self.times}: (AES) Дешифрован файл {self.file} | Пользователь: {self.name} ')
    # сессионные файлы
    def session_file_write(self):
        with open('session_nfile423956.json', 'w') as file:
            json.dump(self.file, file)
    def session_file_read(self):
        with open('session_nfile423956.json', 'r') as file:
            data = json.load(file)
        return data



































