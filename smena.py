#!/usr/bin/python3

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class Smena:
    def __init__(self, root):
        self.label = ttk.Label(root, text=u'Неисправность')
        self.label.grid(row=0, column=0, columnspan=2)
        
        ttk.Button(root, text=u'СЦБ', command=self.message).grid(row=1, column=0)
        
        ttk.Button(root, text=u'АЛСН', command=self.message).grid(row=1, column=1)
    
    def message(self):
        messagebox.showinfo(title=u'Напоминание', message=u'Устранено')


def main():
    root = Tk()
    app = Smena(root)
    root.mainloop()

if __name__ == '__main__': main()