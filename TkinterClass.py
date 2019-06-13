#for calling all widgets
import tkinter ,os
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
        self.lblFname=Label(self.master,text='First Name:',font=("Helvetic",16),fg='Black',bg='lightgrey')
        self.lblFname.grid(row=0,column=0,padx=(30,0),pady=(30,0))
        #second Label
        self.lblLname=Label(self.master,text='Last Name:',font=("Helvetic",16),fg='Black',bg='lightgrey')
        self.lblLname.grid(row=1,column=0,padx=(30,0),pady=(30,0))
        #Label for displaying name on submit button
        self.lblDisplay=Label(self.master,text='',font=("Helvetica",16),fg='Black',bg='lightgrey')
        self.lblDisplay.grid(row=3,column=1,padx=(30,0),pady=(30,0))
        #for paint the text box using Entry method of Tk
        #pss the fname value to text
        self.txtFname=Entry(self.master, text=self.varFname,font=("Helvetica",16),fg='black',bg='lightblue')
        #for showing it using
        self.txtFname.grid(row=0 , column=1,padx=(30,0),pady=(30,0))
         #for paint the text box using Entry method of Tk
        #pss the Lname value to text
        self.txtLname=Entry(self.master, text=self.varLname,font=("Helvetica",16),fg='black',bg='lightblue')
        #for showing it using pack()
        self.txtLname.grid(row=1 , column=1,padx=(30,0),pady=(30,0))
        #creating buttons and sticky set where you want to stick
        self.btnSubmit=Button(self.master,text="Submit",width=10,height=2,command=self.submit)
        self.btnSubmit.grid(row=2 , column=1,padx=(0,0),pady=(30,0),sticky=NE)
        #creating buttons and sticky set where you want to stick assignning command using command
        self.btnCancel=Button(self.master,text="Cancel",width=10,height=2,command=self.cancel)
        self.btnCancel.grid(row=2 , column=1,padx=(0,90),pady=(30,0),sticky=NE)
    def submit(self):
        #getting value from textBox
        fn=self.varFname.get()
        fl=self.varLname.get()
        self.lblDisplay.config(text='Hello {} {} !'.format(fn,fl))
    def cancel(self):
        #use destroy() for close the window
        self.master.destroy()
        os._exit(0)







if __name__=="__main__":
    #Instance of class with Tk()
    root=Tk()
    #assigning or attach root to the ParentWindow by using app
    App=ParentWindow(root)
    #To stop or close the main loop use this method
    root.mainloop()