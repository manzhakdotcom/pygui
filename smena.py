#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class Smena:
    def __init__(self, root):
        self.root = root
        
        # create elements
        self.menu()
        self.frames()
        self.buttonTop()
        self.buttonLeft()

    def frames(self):
        self.frameTop = Frame(self.root, bd=1, relief='sunken')
        self.frameLeft = Frame(self.root, bd=1, relief='sunken')
        self.frameRight = Frame(self.root, bd=1, relief='sunken')

        self.frameTop.grid(row=0, column=0, columnspan=2, sticky='nsew', padx=2, pady=2)
        self.frameLeft.grid(row=1, column=0, sticky='nsew', padx=2, pady=2)
        self.frameRight.grid(row=1, column=1, sticky='nsew', padx=2, pady=2)

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=12)

        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=6)

    def message(self):
        messagebox.showinfo(title=u'Заглушка', message=u'В разработке')

    def menu(self):
        self.root.option_add('*tearOff', False)
        menubar = Menu(self.root)
        self.root.config(menu=menubar)

        file = Menu(menubar)
        edit = Menu(menubar)
        tools = Menu(menubar)
        help_ = Menu(menubar)

        menubar.add_cascade(menu=file, label=u'Файл')
        menubar.add_cascade(menu=edit, label=u'Правка')
        menubar.add_cascade(menu=tools, label=u'Инструменты')
        menubar.add_cascade(menu=help_, label=u'Справка')

        file.add_command(label=u'Принять смену ОДЦ ЖАТС', command=self.message)
        file.add_separator()
        file.add_command(label=u'Новая запись СЦБ', command=self.message)
        file.add_command(label=u'Новая запись АЛСН', command=self.message)
        file.add_separator()
        file.add_command(label=u'Новый журнал замечаний СЦБ', command=self.message)
        file.add_separator()        
        file.add_command(label=u'Экспорт', command=self.message)        
        file.add_separator()
        file.add_command(label=u'Настройки', command=self.message)   
        file.add_separator()
        file.add_command(label=u'Выйти', command=self.message)
        
        tools.add_command(label=u'Архив записей', command=self.message)
        tools.add_separator()
        tools.add_command(label=u'Статистика', command=self.message)

        edit.add_command(label=u'Записи СЦБ', command=self.message)
        edit.add_command(label=u'Записи АЛСН', command=self.message)
        edit.add_separator()
        edit.add_command(label=u'Сотрудники ОДЦ ЖАТС', command=self.message)
        edit.add_command(label=u'Сотрудники ЦУП', command=self.message)
        edit.add_separator()
        edit.add_command(label=u'Диспетчерские круги ЦУП', command=self.message)
        edit.add_command(label=u'Дистанции БелЖД', command=self.message)

        help_.add_command(label=u'О программе', command=self.full)

    def full(self):
        self.root.state('zoomed')
    
    def buttonTop(self):
        ttk.Button(self.frameTop, text=u'+ Запись СЦБ', width='20', command=self.message).pack(side='left', fill='y', padx = 10, pady = 10)

        ttk.Button(self.frameTop, text=u'+ Запись АЛСН', width='20', command= lambda : ALSN(self.root)).pack(side='left', fill='y', pady = 10)
    
    def buttonLeft(self):
        ttk.Button(self.frameLeft, text=u'Записи СЦБ »', command=self.message).pack(ipady=10, padx = 10, pady = 10, fill='x')
    
        ttk.Button(self.frameLeft, text=u'Записи АЛСН »', command=self.message).pack(ipady=10, padx = 10,  anchor = 'nw', fill='x')        
                

class ALSN():
    def __init__(self, root):
        window = Toplevel(root)
        
        window.title(u'Добавить неисправность АЛСН')
        window.geometry('600x400+600+300')
        window.iconbitmap(os.getcwd() + os.path.sep + 'img' + os.path        .sep +'smena.ico')        
        
        frameTop = Frame(window, bd=1, relief='sunken')
        frameBottom = Frame(window, bd=1, relief='sunken')
        
        frameTop.grid(row=0, column=0, sticky='nsew', padx=2, pady=2)
        frameBottom.grid(row=1, column=0, sticky='nsew', padx=2, pady=2)
    
        window.grid_rowconfigure(0, weight=10)
        window.grid_rowconfigure(1, weight=1) 
        window.grid_columnconfigure(0, weight=1)
        
        
        ttk.Button(frameBottom, text=u'Закрыть', command=lambda: window.destroy()).pack(side='right', padx = 10)
        ttk.Button(frameBottom, text=u'Применить', command=lambda: window.destroy()).pack(side='right')
        
        
        window.focus_set()
        window.grab_set()
        window.wait_window()
        
        
        
    
    def frames(self):
        self.frameForm = Frame(Toplevel(), bg='#000000', bd=1, relief='sunken')
        self.frameButtons = Frame(Toplevel(), bd=1, relief='sunken')

        self.frameForm.grid(row=0, column=0, sticky='nsew', padx=2, pady=2)
        self.frameButtons.grid(row=1, column=0, sticky='nsew', padx=2, pady=2)

        self.root.grid_rowconfigure(0, weight=12)
        self.root.grid_rowconfigure(1, weight=1)
        
        self.root.grid_columnconfigure(0, weight=1)     
    
    def form(self):
        pass
    
    def buttons(self, window):
        ttk.Button(window, text=u'Закрыть').grid()
    
    
class Form:
    def __init__(self):
        pass

def main():
    root = Tk()
    root.geometry('900x800+500+200')
    root.title(u'Журнал замечаний СЦБ')
    root.iconbitmap(os.getcwd() + os.path.sep + 'img' + os.path.sep +'smena.ico')
    app = Smena(root)
    root.mainloop()


if __name__ == '__main__':
    main()
