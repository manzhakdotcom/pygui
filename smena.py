#!/usr/bin/python3
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class Smena:
    def __init__(self, root):
        self.root = root
        # create elements
        self.menu()
        self.frames()
        self.label()
        self.button()

    def frames(self):
        self.frameTop = Frame(self.root, bd=1, relief='sunken')
        self.frameLeft = Frame(self.root, background='#cce4ca', bd=1, relief='sunken')
        self.frameRight = Frame(self.root, background='#f5c2c1', bd=1, relief='sunken')

        self.frameTop.grid(row=0, column=0, columnspan=2, sticky='nsew', padx=2, pady=2)
        self.frameLeft.grid(row=1, column=0, sticky='nsew', padx=2, pady=2)
        self.frameRight.grid(row=1, column=1, sticky='nsew', padx=2, pady=2)

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=10)

        self.root.grid_columnconfigure(0, weight=2)
        self.root.grid_columnconfigure(1, weight=5)

    def message(self):
        messagebox.showinfo(title=u'Заглушка', message=u'В разработке')

    def menu(self):
        self.root.option_add('*tearOff', False)
        menubar = Menu(self.root)
        self.root.config(menu=menubar)

        file = Menu(menubar)
        edit = Menu(menubar)
        help_ = Menu(menubar)

        menubar.add_cascade(menu=file, label=u'Файл')
        menubar.add_cascade(menu=edit, label=u'Правка')
        menubar.add_cascade(menu=help_, label=u'Справка')

        file.add_command(label=u'Новая смена ОДЦ ЖАТС', command=self.message)
        file.add_separator()
        file.add_command(label=u'Новая запись СЦБ', command=self.message)
        file.add_command(label=u'Новая запись АЛСН', command=self.message)
        file.add_separator()
        file.add_command(label=u'Выйти', command=self.message)

        edit.add_command(label=u'Запись СЦБ', command=self.message)
        edit.add_command(label=u'Запись АЛСН', command=self.message)
        edit.add_separator()
        edit.add_command(label=u'Инженеры ОДЦ', command=self.message)
        edit.add_command(label=u'Диспетчера ЦУП', command=self.message)

        help_.add_command(label=u'О программе', command=self.message)

    def button(self):
        ttk.Button(self.frameTop, text=u'Запись СЦБ', width='20', command=self.message).pack(side='left', fill='y')

        ttk.Button(self.frameTop, text=u'Запись АЛСН', width='20', command=self.message).pack(side='left', fill='y')


    def label(self):
        # self.labelTop = Label(self.frameTop, text=u'Поле вверху')
        self.labelLeft = Label(self.frameLeft, text=u'Поле слева')
        self.labelRight = Label(self.frameRight, text=u'Поле справа')
        # self.labelTop.pack(side='right', fill='y')
        self.labelLeft.pack(side='left', fill='both', expand='True')
        self.labelRight.pack(side='bottom', fill='x')


def main():
    root = Tk()
    root.geometry('900x800')
    root.title(u'Журнал замечаний СЦБ')
    app = Smena(root)
    root.mainloop()


if __name__ == '__main__':
    main()
