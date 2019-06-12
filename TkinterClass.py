#for calling all widgets
import tkinter
from tkinter import *
#parent class with tkinter
class ParentWindow(Frame):
    #for initilize these lines are important
    #also u can use **args and **kawargs
    def __init__ (self,master):
        Frame.__init__ (self)
        
        self.master= master
        self.master.resizable(width=False, height=False)
        #we can also give the size according to our requirement by using geometry
        self.master.geometry('{}x{}'.format(700,400))
        #use title for title for the window
        self.master.title("Learning Tkinter!")
        #configure backgroud color with color name or hex color combinations
        self.master.config(bg='darkgrey')
        #Create vatiable and use them and 
        self.varFname=StringVar()
        self.varLname=StringVar()
        #use set for set the value 
        '''self.varFname.set('Mandeep')
        self.varLname.set('Kaur')
        #print for get the value use get()
        print(self.varFname.get())
        print(self.varLname.get())'''
        #add labels
        self.lblFname=Label(self.master,text='First Name:',font=("Helvetic",16),fg='Black',bg='lightblue')
        self.lblFname.grid(row=0,column=0)
        #second Label
        self.lblLname=Label(self.master,text='Last Name:',font=("Helvetic",16),fg='Black',bg='lightblue')
        self.lblLname.grid(row=1,column=0)
        #for paint the text box using Entry method of Tk
        #pss the fname value to text
        self.txtFname=Entry(self.master, text=self.varFname,font=("Helvetica",16),fg='black',bg='lightblue')
        #for showing it using
        self.txtFname.grid(row=0 , column=1)
         #for paint the text box using Entry method of Tk
        #pss the Lname value to text
        self.txtLname=Entry(self.master, text=self.varLname,font=("Helvetica",16),fg='black',bg='lightblue')
        #for showing it using pack()
        self.txtLname.grid(row=1 , column=1)
        







if __name__=="__main__":
    #Instance of class with Tk()
    root=Tk()
    #assigning or attach root to the ParentWindow by using app
    App=ParentWindow(root)
    #To stop or close the main loop use this method
    root.mainloop()