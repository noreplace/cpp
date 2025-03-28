from tkinter import *
from PIL import Image, ImageTk
from tkinter.filedialog import *
from tkinter.messagebox import *
def image_open(root, file): #открытие граф.файла и окно рисовалки

    def draw(event):        
        canv.create_oval(event.x - brush_size,
                         event.y - brush_size,
                         event.x + brush_size,
                         event.y + brush_size,
                         fill=color, outline=color)

    def set_color(new_color):        
        global color
        color = new_color

    def set_brush_size(new_size):        
        global brush_size
        brush_size = new_size

    def setUI():
        global gfile
        global canv, gfile, rootp
        rootp.title("NFile graphics")
        frame.pack(fill=BOTH, expand=1)
        
        frame.columnconfigure(7, weight=1)
        frame.rowconfigure(2, weight=1)

        canv = Canvas(frame, bg="white")
        
        if gfile:
            
            image = Image.open(gfile)
            image_width, image_height = image.size
            
            imagee = image.resize((800, 500), Image.LANCZOS)
            python_image = ImageTk.PhotoImage(imagee)
            canv.image = python_image
            rootp_width = rootp.winfo_width()
            rootp_height = rootp.winfo_height()
            
            canv.x = (rootp_width // 2) - (image_width // 2)
            canv.y = (rootp_height // 2) - (image_height // 2)
            #ПРОВЕРИТЬ
            canv.create_image(700, 400, image=canv.image)
            
        canv.grid(row=2, column=0, columnspan=8, padx=5, pady=5, sticky=E + W + S + N)
    
        canv.bind("<B1-Motion>", draw)
        canv.bind("<Button-1>", draw)
       
        color_lab = Label(frame, text="Цвет: ")
        color_lab.grid(row=0, column=0, padx=6)

        red_btn = Button(frame, text="Красный", width=10, command=lambda: set_color("red"))
        red_btn.grid(row=0, column=1)

        green_btn = Button(frame, text="Зеленый", width=10, command=lambda: set_color("green"))
        green_btn.grid(row=0, column=2)

        blue_btn = Button(frame, text="Синий", width=10, command=lambda: set_color("blue"))
        blue_btn.grid(row=0, column=3)

        black_btn = Button(frame, text="черный", width=10, command=lambda: set_color("black"))
        black_btn.grid(row=0, column=4)

        white_btn = Button(frame, text="Белый", width=10, command=lambda: set_color("white"))
        white_btn.grid(row=0, column=5)

        size_lab = Label(frame, text="Размер кисти: ")
        size_lab.grid(row=1, column=0, padx=5)

        one_btn = Button(frame, text="2x", width=10, command=lambda: set_brush_size(2))
        one_btn.grid(row=1, column=1)

        two_btn = Button(frame, text="5x", width=10, command=lambda: set_brush_size(5))
        two_btn.grid(row=1, column=2)

        five_btn = Button(frame, text="7x", width=10, command=lambda: set_brush_size(7))
        five_btn.grid(row=1, column=3)

        seven_btn = Button(frame, text="10x", width=10, command=lambda: set_brush_size(10))
        seven_btn.grid(row=1, column=4)

        ten_btn = Button(frame, text="20x", width=10, command=lambda: set_brush_size(20))
        ten_btn.grid(row=1, column=5)

        twenty_btn = Button(frame, text="50x", width=10, command=lambda: set_brush_size(50))
        twenty_btn.grid(row=1, column=6, sticky=W)

        hund_btn = Button(frame, text="100x", width=10, command=lambda: set_brush_size(100))
        hund_btn.grid(row=1, column=7, sticky=W)

        clear_btn = Button(frame, text="Очистить", width=10, command=lambda: canv.delete("all"))
        clear_btn.grid(row=0, column=6, sticky=W)

    def close_win():       
        if askyesno("Выход", "Вы уверены?"):
            rootp.destroy()
    def open_file():
        pass
    def main():     
        global rootp, frame, brush_size, color, gfile
        brush_size = 10
        gfile = file
        color = "red"
        rootp = Toplevel(root)
        rootp.option_add("*tearOff", FALSE)
        rootp.geometry("800x600+300+300")
        rootp.attributes('-fullscreen', True)
        frame = Frame(rootp)
        setUI()
        m = Menu(rootp)
        rootp.config(menu=m)
        
        fm = Menu(m)
        m.add_cascade(label="Файл", menu=fm)
        fm.add_command(label="Открыть", command = open_file)
        fm.add_command(label="Сохранить")
        fm.add_command(label="")
        fm.add_command(label="Выход", command=close_win)

        rootp.mainloop()
    main()






