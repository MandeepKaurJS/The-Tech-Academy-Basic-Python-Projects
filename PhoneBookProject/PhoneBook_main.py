#for calling all widgets
from tkinter import *
import tkinter as tk

#calling our classes 
import phonebook_func
import phonebook_gui
#Frame is the tKinter frame class
class ParentWindow(Frame):
    #for initilize these lines are important
    #also u can use **args and **kawargs
    def __init__ (self,master,*args,**kwargs):
        Frame.__init__ (self,master,*args,**kwargs)
        #Define our master frame configuration
        self.master= master
        self.master.minsize(500,300)
        self.master.maxsize(500,300)
        #this CenterWindow method will center my app in tkinter
        phonebook_func.center_window(self,500,300)
        self.master.title("The Tkinter PhoneBook Demo")
        self.master.config(bg="#F0F0F0")
        #This protocol method is a tkinter built-in method to catch
        #if the user clicks the upper corner ,"X" on window
        self.master.protocol("WM_DELETE_WindOW",lambda:phonebook_func.ask_quit(self))
        arg=self.master
        #load in the GUI widgets from a seperate module,
        #Keeping your code comparmentalized and cluter free
        phonebook_gui.load_gui(self)

if __name__=="__main__":
    #Instance of class with Tk()
    root=Tk()
    #assigning or attach root to the ParentWindow by using app
    App=ParentWindow(root)
    #To stop or close the main loop use this method
    root.mainloop()