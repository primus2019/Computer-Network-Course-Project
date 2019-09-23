from tkinter import Tk, messagebox
from tkouter import *


class HelloWorld(TkOutWidget):

    layout = open('Computer-Network-Course-Project\sample.html').read()

    def hello(self):
        messagebox.showinfo('welcome to tkouter', 'hello world')


if __name__ == '__main__':
    root = Tk()
    hl = HelloWorld(root)
    hl.pack()
    root.mainloop()