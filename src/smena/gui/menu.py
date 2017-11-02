from tkinter import *
from tkinter import messagebox


class MenuBar:
    def __init__(self, root):
        self.root = root

        self.root.option_add('*tearOff', False)
        self.menubar = Menu(self.root)
        self.root.config(menu=self.menubar)

        self.setup()

    def setup(self):
        file = Menu(self.menubar)
        edit = Menu(self.menubar)
        tools = Menu(self.menubar)
        help_ = Menu(self.menubar)

        self.menubar.add_cascade(menu=file, label=u'Файл')
        self.menubar.add_cascade(menu=edit, label=u'Правка')
        self.menubar.add_cascade(menu=tools, label=u'Инструменты')
        self.menubar.add_cascade(menu=help_, label=u'Справка')

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

        help_.add_command(label=u'О программе', command=self.message)

    def message(self):
        messagebox.showinfo(title=u'Заглушка', message=u'В разработке')

