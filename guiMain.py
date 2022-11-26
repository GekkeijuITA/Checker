from tkinter import *

class App(Frame):

    def __init__(self, master , width , height):
        super().__init__(master)
        self.listBox = Listbox(master, width = width, height = height)
        self.scrollbarY = Scrollbar(master)
        self.scrollbarX = Scrollbar(master, orient = HORIZONTAL)
        
        self.scrollbarX.pack(side = BOTTOM, fill = X)
        self.scrollbarY.pack(side = RIGHT, fill = Y)
        
        self.listBox.config(yscrollcommand = self.scrollbarY.set , xscrollcommand = self.scrollbarX.set)
        self.scrollbarY.config(command = self.listBox.yview)
        self.scrollbarX.config(command = self.listBox.xview)

    def get_listBox(self):
        return self.listBox
    