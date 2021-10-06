# Python Version: 3.7.8
#
# Author: Ryan Spears
#

from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import shutil
import os
import time
from datetime import timedelta, datetime


win = Tk()
win.minsize(400, 200)
win.title("File Transfer")

class FolderSelect(Frame):
    def __init__(self,parent=None,folderDescription="",**kw):
        Frame.__init__(self,master=parent,**kw)
        self.folderPath = StringVar()
        self.lblName = Label(self, text=folderDescription)
        self.lblName.grid(row=0,column=0)
        self.entPath = Entry(self, textvariable=self.folderPath)
        self.entPath.grid(row=0,column=1)
        self.btnFind = ttk.Button(self, text="Browse Folders",command=self.setFolderPath)
        self.btnFind.grid(row=0,column=2)
        
    def setFolderPath(self):
        folder_selected = filedialog.askdirectory()
        self.folderPath.set(folder_selected)
        
    @property
    def folder_path(self):
        return self.folderPath.get()

def fileCheck():
    folder1 = directory1Select.folder_path
    folder2 = directory2Select.folder_path

    for i in folder1:
        path = os.path.join(folder1, i)
        timestamp = time.strftime('%m/%d/%Y :: %H:%M/%S', time.gmtime(os.path.getmtime(path)))
        datetimeObj = datetime.strptime(timestamp, '%m/%d/%Y :: %H:%M/%S')

        if datetimeObj >= datetime.today() - timedelta(days = 1):
            shutil.copy(folder1 + i, folder2)

folderPath = StringVar()

directory1Select = FolderSelect(win,"Choose the folder you want \nto check the files of:")
directory1Select.grid(row = 1, column = 1, padx = 10, pady = 10)

directory2Select = FolderSelect(win,"Choose the folder you want \nto send copied files to:")
directory2Select.grid(row = 3, column = 1, padx = 10, pady = 10)

c = ttk.Button(win, text="Initialize File Check", command=fileCheck)
c.grid(row = 5, column = 4, padx = 10, pady = 10)

win.mainloop()
