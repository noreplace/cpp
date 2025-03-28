from tkinter import *
import base64 as b64
from console.console import _console

class base64:

    def _encode_base64(self, op):

        self.tx = open(op, 'r', encoding='utf-8').read()
        if self.tx:

            self.sample_string_bytes = self.tx.encode("utf-8")
            self.base64_bytes = b64.b64encode(self.sample_string_bytes)
            self.base64_string = self.base64_bytes.decode("utf-8")
            self.base64_enc = f'Ваши захешированные данные в кодировке base64:\n {self.base64_string}'

            _console(self.base64_enc)

    def _decode_base64(self, op):

        self.base64_strink = open(op, 'r', encoding='utf-8').read()
        self.base64_bytes = self.base64_strink.encode("utf-8")

        self.sample_string_bytes = base64.b64decode(self.base64_bytes)
        self.sample_string = self.sample_string_bytes.decode("utf-8")

        self.base64_enc = f'Результат:\n {self.sample_string}'

        _console(self.base64_enc)