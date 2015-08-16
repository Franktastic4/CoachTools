'''
Created on Aug 6, 2015

@author: Franktastin4
'''
import tkinter
import os
import csv
from tkinter import *
from ctypes.macholib import framework
from tkinter.filedialog import FileDialog
from macpath import dirname, join
from fileinput import filename
from _datetime import date, datetime

# Use frame for GUI
class Application(Frame):
    
    def __init__(self,master):
        # Initialize Frame
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
        
    def create_widgets(self):
        self.outputFilePath = 'Combined' + '.csv' #str(date.today()) + '.csv'
        
        self.selectFolderButton = Button(self, text='Select Folder')
        self.selectFolderButton["command"] = self.openFolderDialog
        self.selectFolderButton.grid()
        
        self.buttonCombine = Button(self, text='Combine Files')
        self.buttonCombine["command"] = self.combineFiles
        self.buttonCombine.grid()
        
        self.buttonClear = Button(self, text='Clear All')
        self.buttonClear['command'] = self.clearAll
        self.buttonClear.grid()
        
        self.buttonRemove = Button(self, text='Remove Selected')
        self.buttonRemove['command'] = self.removeSelectedFile
        self.buttonRemove.grid()
        
        self.label = Label(self)
        self.label = Label(text = "Explain Button Here" )
        self.label.grid()

        self.tableOfFiles = Listbox(root, height = 10)
        self.tableOfFiles.grid()
        
 
    def openFolderDialog(self):
        self.dirname = tkinter.filedialog.askdirectory(parent=root,initialdir="~/Desktop",title='Please select a directory')
        
        if (len(self.dirname) > 0 ):
            # If there is a directory
            
            self.seq=os.listdir(self.dirname)
            os.chdir(self.dirname)
            
            for self.f in self.seq:
                if os.path.isfile(self.f):
                    if(self.f != ".DS_Store" or self.f != self.outputFilePath ):
                        self.tableOfFiles.insert(END,self.f)
                        
    def clearAll(self):
        self.tableOfFiles.delete(0, END)
        del self.seq[:]

    def removeSelectedFile(self):
        index = self.tableOfFiles.index(self.tableOfFiles.curselection())
        self.seq.pop(index)
        self.tableOfFiles.delete(index)
        
    def combineFiles(self):
    
        with open(self.outputFilePath, 'a', newline='') as output: 
            writer = csv.writer(output, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)

            # iterate through directory
            for self.seqItor in self.seq:
                # ignore the .DS_Store
                if(self.seqItor != ".DS_Store" or self.seqItor != self.outputFilePath):
                    #Eligible file found    
                    #prepare to read
                    fileReader = csv.reader(open(self.seqItor, newline=''), delimiter=',', quotechar='|')                    
                    for fileItor in fileReader:
                        writer.writerow(fileItor)
                    
                        
        
        sys.exit('Success')
        
            
root = Tk()
root.title("MyLifts Coaching Tools")
root.geometry("145x307")
app = Application(root)
root.mainloop()
