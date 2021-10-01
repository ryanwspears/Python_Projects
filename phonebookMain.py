from tkinter import *
import tkinter as tk
from tkinter import messagebox


import phonebookGUI
import phonebookFunc

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(500,300) 
        self.master.maxsize(500,300)
        phonebookFunc.center_window(self,500,300)
        self.master.title("The Tkinter Phonebook Demo")
        self.master.configure(bg="#F0F0F0")
        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebookFunc.ask_quit(self))
        arg = self.master

        phonebookGUI.load_gui(self)
        
        menubar = Menu(self.master)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", underline=1,accelerator="Ctrl+Q",command=lambda: phonebookFunc.ask_quit(self))
        menubar.add_cascade(label="File", underline=0, menu=filemenu)
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_separator()
        helpmenu.add_command(label="How to use this program")
        helpmenu.add_separator()
        helpmenu.add_command(label="About This Phonebook Demo")
        menubar.add_cascade(label="Help", menu=helpmenu) 
        
        self.master.config(menu=menubar, borderwidth='1')

        
if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
