from tkinter import *
from tkinter import ttk

class Smena:
    def __init__(self, root):
        self.label = ttk.Label(root, text='Hello')
        self.label.grid(row=0, column=0, columnspan=2)
        
        ttk.Button(root, text='Click me!', command=self.change_label).grid(row=1, column=1)
    
    def change_label(self):
        self.label.config(text='World')


def main():
    root = Tk()
    app = Smena(root)
    root.mainloop()

if __name__ == '__main__': main()