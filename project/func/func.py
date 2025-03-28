from tkinter import *
import images
from tkinter.filedialog import *
from tkinter.messagebox import *
import re
import log
from configparser import ConfigParser
import os



def encoding_():
    """ """
    encoding = [
        'utf-8',
        'cp866',
        'utf-16',
        'GBK',
        'windows-1251',
        'ASCII',
        'Big5',
        'US-ASCII'
    ]
    encodingy = encoding
    return encodingy
class func():
    def __init__(self, op, vidget, root):
        self.op = op
        self.vidget = vidget
        self.root = root



    def _copy_file(self):
        print('q')
        """  """
        sa = asksaveasfilename(title="", filetypes=[("Text File", ('*.text')), ("All files", "*.*"), ("Python files", ('*.py'))])
        if sa:
            content = self.vidget.get(1.0, END)
            with open(sa, "w", encoding='utf-8') as f:
                f.write(content)

    def close_win(self, config, result, file):
        print(self.root.winfo_geometry())
        save_file_destroy = config['files'].get('flag_saving_files')
        if save_file_destroy:
                self._save()
        config.set('Window_configs', 'size', self.root.winfo_geometry())

        print(self.op)
        #if result is not ['.jpg','.png','.ico']:
        config.set('files', 'last_file', self.op)
        with open('config.ini', 'w') as configfile:
            config.write(configfile)
        self.root.destroy()




    def _delete(self):
        """  """
        global op
        try:
            if askyesno('',''):
                os.remove(self.op)
                self.vidget.delete(1.0, END)
                showinfo('','')

        except:
            showerror('','')
        else:
            a = log.loggingNF.Logging()
            a._delete_file_log(self.op)

    def _save(self, event = None):
        """  """

        text8 = self.vidget.get("1.0", END)
        if self.op:

            with open(self.op, "wb") as f:
                f.write(text8.encode('utf-8'))
        else:
            self.file = asksaveasfilename()
            if self.file:
                with open(self.file, "wb") as f:
                    f.write(text8.encode('utf-8'))


        a = log.loggingNF.Logging()
        a._save_file_log(self.op)
        self.flag_edit = 0

    #////////////////////////////////////////////////////////////////////////

    def font_changed(font):
        label["font"] = font

    def select_font(self):
        self.text.pack_propagate(False)
        self.text.config(font=("Times"))
    def _select_VERDANA(self):
        self.text.pack_propagate(False)
        font2 = font.Font(family= "Verdana", size=10, weight="normal", slant="roman")
        self.text["font"]=font2
        self.numbers["font"] = font2

    def _select_ARIAL(self):
        pass
    def _select_TIMES(self):
        pass


    #////////////////////////////////////////////////////////////////////////
    def create_file(self):

        self.root.title("Безымянный - NFile editor")
        self.op = None
    def _chardet(self):

        global correct_encoding

    def _about_info(self):

        pass






