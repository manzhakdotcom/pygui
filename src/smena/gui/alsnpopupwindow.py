import os
from tkinter import *
from tkinter import ttk

class ALSN:
    def __init__(self, root):
        window = Toplevel(root)

        window.title(u'Добавить неисправность АЛСН')
        window.geometry('600x400+600+300')
        window.iconbitmap(os.getcwd() + os.path.sep + 'img' + os.path.sep + 'smena.ico')

        frameTop = Frame(window, bd=1, relief='sunken')
        frameBottom = Frame(window, bd=1, relief='sunken')

        frameTop.grid(row=0, column=0, sticky='nsew', padx=2, pady=2)
        frameBottom.grid(row=1, column=0, sticky='nsew', padx=2, pady=2)

        window.grid_rowconfigure(0, weight=10)
        window.grid_rowconfigure(1, weight=1)
        window.grid_columnconfigure(0, weight=1)

        ttk.Button(frameBottom, text=u'Закрыть', command=lambda: window.destroy()).pack(side='right', padx=10)
        ttk.Button(frameBottom, text=u'Применить', command=lambda: print(
            u'Применил'
        )).pack(side='right')

        window.focus_set()
        window.grab_set()
        window.wait_window()

    def frames(self):
        pass

    def form(self):
        pass

    def buttons(self, window):
        pass
