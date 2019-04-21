import tkinter as tk
from tkinter.filedialog import askopenfilename

import methods as mt #class Method():

import os

"""
The Main application class of the
    encoder decoder program
Args:
    tk.Frame: the superclass this class inherits from
"""
class MainApplication(tk.Frame):

    """
    Creates the Methods list when running the program. If you
        wish to add your own encode/decode method, do it here.
        Simply add a new method using similar code below
    Args:
        self: the mainApplication calling this function

    """
    def createMethods(self):
        self.methods.append(mt.Method('Ceasar', mt.enCeasar, mt.deCeasar))
        self.methods.append(mt.Method('Rot10', mt.enRot, mt.deRot))

        #ADD NEW METHODS HERE#

        for i in self.methods:
            self.methodList.insert(tk.END,i.name)

    """
    Function that opens a file and writes the text
        contained within to the input field of the program
    Args:
        self: the mainApplication calling this function
    Raises:
        FileError: File to open doesn't exist
    """
    def openFile(self):
        name = askopenfilename(initialdir = os.getcwd(),
                           filetypes =(("Text File",".txt"),("All Files","*.*")),
                           title = "Choose a file."
                          )
        try:
            with open(name, 'r') as UseFile:
                self.input_text.delete(1.0, tk.END)
                self.input_text.insert(tk.END,UseFile.read())
        except:
            print("No file exists")


    """
    Function that writes to a file and using the text
        contained within the result field of the program
    Args:
        self: the mainApplication calling this function
    Raises:
        FileError: File to open doesn't exist
    """
    def writeFile(self):
        name = askopenfilename(initialdir = os.getcwd(),
                           filetypes =(("Text File",".txt"),("All Files","*.*")),
                           title = "Choose a file."
                          )
        try:
            with open(name, "w") as f:
                f.write(self.result_text.get("1.0",tk.END))
                f.close()
        except:
            print(" Failed to write to file: ", name)

    """
    Function that updates the results text field. It
        is called every 500 ms, and is called continiously
        throughout the duration of the application.
    Args: The application calling the function
    """
    def displayResult(self):
        p_itext = self.input_text.get("1.0",tk.END)
        translation = ""

        if self.currentMode.get() == 1:
            translation = "".join(self.methods[self.methodList.index(tk.ACTIVE)].encode(p_itext))
        elif self.currentMode.get() == 2:
            translation = "".join(self.methods[self.methodList.index(tk.ACTIVE)].decode(p_itext))

        self.result_text.delete("1.0",tk.END)
        self.result_text.insert(tk.END,translation)
        self.parent.after(500,self.displayResult)
        

    """
    MainApplication's constructor. It contains the gui 
        elements visible throughout the application
    Args:
        self: the application object to construct
        parent: the main tk window generated using tk.TK()
        *args:
        **kwargs:
    """
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, *kwargs)
        self.parent = parent

        #menu of the application
        self.menu = tk.Menu(parent)
        subMenu = tk.Menu(self.menu)
        subMenu.add_command(label = 'Open', command=self.openFile)
        subMenu.add_command(label = 'Save', command=self.writeFile)
        subMenu.add_command(label = 'Exit', command=lambda:exit())
        self.menu.add_cascade(label = 'File', menu = subMenu)
        self.parent.config(menu=self.menu)

        #left side of the applciation
        self.leftFrame = tk.Frame(self.parent)
        self.leftFrame.pack(side=tk.LEFT)

        #right side of the application
        self.rightFrame = tk.Frame(self.parent)
        self.rightFrame.pack(side=tk.RIGHT)

        #mode of either encode or decode
        self.currentMode = tk.IntVar(None, 1)

        tk.Radiobutton(self.leftFrame, text='Encode', variable=self.currentMode, value=1).pack(anchor=tk.W)
        tk.Radiobutton(self.leftFrame, text='Decode', variable=self.currentMode, value=2).pack(anchor=tk.W)


        #method of encoding and decoding
        self.methodList = tk.Listbox(self.leftFrame)
        self.methodList.pack()

        self.methods = []
        self.createMethods()
        self.methodList.selection_set(first = 0)

        #input text field for encoding or decoding
        self.input_text = tk.Text(self.rightFrame)
        self.input_text.pack()

        #result text field for encoding or decoding
        self.result_text = tk.Text(self.rightFrame)
        self.result_text.pack()
        
        #need to update result text box
        self.parent.after(500, self.displayResult)


if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
