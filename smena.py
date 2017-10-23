#!/usr/bin/python3
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class Smena:
    def __init__(self, root):
        
        self.root = root
        
        self.frameTop = ttk.Frame(self.root)
        self.frameTop.pack(side=TOP)
        self.frameTop.config(relief = RIDGE)
        self.frameTop.config(height = 100, width = 900)
        
        
        self.frameLeft = ttk.Frame(self.root)
        self.frameLeft.pack(side=LEFT)
        self.frameLeft.config(relief = RIDGE)
        self.frameLeft.config(height = 700, width = 300)
        
        
        
        
        self.frameRight = ttk.Frame(self.root)
        self.frameRight.pack(side=RIGHT)
        self.frameRight.config(relief = RIDGE)
        self.frameRight.config(height = 700, width = 600)
        
        
        #self.frameRight = ttk.Frame(self.root)
        #self.frameRight.pack()        

        #self.frame.config(height = 100, width = 200)
        #self.frameTop.config(padding = (30, 10))
        
        
                
      
        
        #creat elements
        self.menu()
        #self.label()
        #self.button()
        
    
    def message(self):
        messagebox.showinfo(title=u'Заглушка', message=u'В разработке')
    
    def menu(self):
        self.root.option_add('*tearOff', False)
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        
        file = Menu(menubar)
        edit = Menu(menubar)
        help_ = Menu(menubar)
        
        menubar.add_cascade(menu = file, label = u'Файл')
        menubar.add_cascade(menu = edit, label = u'Редактировать')
        menubar.add_cascade(menu = help_, label = u'Спрвка')
        
        
        file.add_command(label = u'Новая смена ОДЦ ЖАТС', command = self.message)
        file.add_separator()        
        file.add_command(label = u'Новая запись СЦБ', command = self.message)
        file.add_command(label = u'Новая запись АЛСН', command = self.message)
        file.add_separator()
        file.add_command(label = u'Выйти', command = self.message)
        

        edit.add_command(label = u'Запись СЦБ', command = self.message)
        edit.add_command(label = u'Запись АЛСН', command = self.message)
        edit.add_separator()
        edit.add_command(label = u'Инженеры ОДЦ', command = self.message)
        edit.add_command(label = u'Диспетчера ЦУП', command = self.message)        
        
        help_.add_command(label = u'О программе', command = self.message)
        

    def button(self):
       
        ttk.Button(self.frameTop, text=u'СЦБ', command=self.message).grid()
        
        ttk.Button(self.frameTop, text=u'АЛСН', command=self.message).grid()
    
        ttk.Button(self.frameLeft, text=u'АЛСН', command=self.message).grid()
    
    def label(self):
        self.label = ttk.Label(self.frameRight, text=u'Неисправность')
        self.label.grid()        


def main():
    root = Tk()
    root.geometry('900x800')
    root.title(u'Журнал замечаний СЦБ')
    app = Smena(root)
    root.mainloop()

if __name__ == '__main__': main()