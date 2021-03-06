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

# This builds the labels and browse buttons along with the entry fields for the path.
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

    # This stores the selected path to copy the files from.    
    def setFolderPath(self):
        folder_selected = filedialog.askdirectory()
        self.folderPath.set(folder_selected)

    # This returns the selected folder path to use later.    
    @property
    def folder_path(self):
        return self.folderPath.get()

# This gets the path from the above function and lists its directory.
def fileCheck():
    folder1 = directory1Select.folder_path
    folder2 = directory2Select.folder_path
    folder1files = os.listdir(folder1)

    # This checks each file in the folder and gets the date each one was last modified.
    for i in folder1files:
        newPath = folder1 + '/' + i
        timestamp = time.strftime('%m/%d/%Y :: %H:%M/%S', time.gmtime(os.path.getmtime(newPath)))
        datetimeObj = datetime.strptime(timestamp, '%m/%d/%Y :: %H:%M/%S')

        # This checks to see if the files have been modified in the past 24 hours, and
        # copies those files to a new selected folder.
        if datetimeObj >= datetime.today() - timedelta(days = 1):
            shutil.copy(newPath, folder2)

# This is storing the path as a string variable.
folderPath = StringVar()


# This builds the rest of the GUI.
directory1Select = FolderSelect(win,"Choose the folder you want \nto check the files of:")
directory1Select.grid(row = 1, column = 1, padx = 10, pady = 10)

directory2Select = FolderSelect(win,"Choose the folder you want \nto send copied files to:")
directory2Select.grid(row = 3, column = 1, padx = 10, pady = 10)

c = ttk.Button(win, text="Initialize File Check", command=fileCheck)
c.grid(row = 5, column = 4, padx = 10, pady = 10)

win.mainloop()
