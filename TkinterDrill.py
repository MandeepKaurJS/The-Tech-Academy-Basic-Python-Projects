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
        self.master.geometry('{}x{}'.format(700,300))
        #use title for title for the window
        self.master.title("Check files")
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
        #add buttons
        self.btnBrowse=Button(self.master,text='Browse...',width=15,height=1,font=("Helvetic",16),fg='Black',bg='lightgrey')
        self.btnBrowse.grid(row=0,column=0,padx=(30,0),pady=(40,0))
        #second button
        self.btnBrowse2=Button(self.master,text='Browse...',width=15,height=1,font=("Helvetic",16),fg='Black',bg='lightgrey')
        self.btnBrowse2.grid(row=1,column=0,padx=(30,0),pady=(10,0))
        #Label for displaying name on submit button
        self.btncheckforFiles=Button(self.master,text='Check for files...',width=15,height=2,font=("Helvetic",16),fg='Black',bg='lightgrey')
        self.btncheckforFiles.grid(row=2,column=0,padx=(30,0),pady=(10,0))
               #for paint the text box using Entry method of Tk
        #pss the fname value to text
        self.txtFname=Entry(self.master,width=35,font=("Helvetica",16),fg='black',bg='white')
        #for showing it using
        self.txtFname.grid(row=0 ,column=1,padx=(20,0),pady=(30,0))
         #for paint the text box using Entry method of Tk
        #pss the Lname value to text
        self.txtLname=Entry(self.master,width=35,font=("Helvetica",16),fg='black',bg='white')
        #for showing it using pack()
        self.txtLname.grid(row=1 ,column=1,padx=(20,0),pady=(10,0))
        #creating buttons and sticky set where you want to stick
        self.btnSubmit=Button(self.master,width=15,height=2,text="Close Program",font=("Helvetica",16),fg='Black',bg='lightgrey')
        self.btnSubmit.grid(row=2 , column=1,padx=(10,0),pady=(10,0),sticky=NE)
       
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
