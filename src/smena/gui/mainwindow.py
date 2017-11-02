from tkinter import *


class MainWindow:
    def __init__(self, root):
        self.root = root
        self.setup()

    def setup(self):
        self.frameTop = Frame(self.root, bd=1, relief='sunken')
        self.frameLeft = Frame(self.root, bd=1, relief='sunken')
        self.frameRight = Frame(self.root, bd=1, relief='sunken')

        self.frameTop.grid(row=0, column=0, columnspan=2, sticky='nsew', padx=2, pady=2)
        self.frameLeft.grid(row=1, column=0, sticky='nsew', padx=2, pady=2)
        self.frameRight.grid(row=1, column=1, sticky='nsew', padx=2, pady=2)

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=12)

        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=10)