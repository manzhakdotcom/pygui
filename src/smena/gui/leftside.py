from tkinter import ttk
from tkinter import messagebox
from src.smena.gui.mainwindow import MainWindow


class LeftSide(MainWindow):
    def __init__(self, root):
        MainWindow.__init__(self, root)
        self.lbuttons()

    def lbuttons(self):
        ttk.Button(self.frameLeft, text=u'Показать записи СЦБ »', command=self.message).pack(ipady=10, padx=10, pady=10, fill='x')

        ttk.Button(self.frameLeft, text=u'Показать записи АЛСН »', command=self.message).pack(ipady=10, padx=10, anchor='nw', fill='x')

    def message(self):
        messagebox.showinfo(title=u'Заглушка', message=u'В разработке')