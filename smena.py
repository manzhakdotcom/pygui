#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
from tkinter import *
from src.smena.gui.menu import MenuBar
from src.smena.gui.mainwindow import MainWindow
from src.smena.gui.topside import TopSide
from src.smena.gui.leftside import LeftSide


class Smena:
    def __init__(self, root):
        self.root = root

        # create elements
        MenuBar(self.root)
        MainWindow(self.root)
        TopSide(self.root)
        LeftSide(self.root)


def main():
    root = Tk()
    root.geometry('900x800+500+200')
    root.title(u'Журнал замечаний СЦБ')
    root.iconbitmap(os.getcwd() + os.path.sep + 'img' + os.path.sep + 'smena.ico')
    app = Smena(root)
    root.mainloop()


if __name__ == '__main__':
    main()
