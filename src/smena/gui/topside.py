from tkinter import ttk
from tkinter import messagebox
from src.smena.gui.mainwindow import MainWindow


class TopSide(MainWindow):
    def __init__(self, root):
        MainWindow.__init__(self, root)
        self.buttons()

    def buttons(self):
        ttk.Button(self.frameTop, text=u'Добавить\nзапись СЦБ', width='20', command=self.message).pack(side='left', fill='y', padx=10, pady=10)

        ttk.Button(self.frameTop, text=u'Добавить\nзапись АЛСН', width='20', command=self.message).pack(side='left', fill='y', pady=10)

    def message(self):
        messagebox.showinfo(title=u'Заглушка', message=u'В разработке')