from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3



class PaymentAI:
    def __init__(self,root):
        self.root = root
        # res
        self.root.geometry('774x530+100+100')

        # title
        self.root.title('VIMMO A.I')
        self.root.config(bg='#E5E7DB')
        self.root.focus_force()

if __name__ == '__main__':
    root = Tk()
    im = PaymentAI(root)
    root.mainloop()