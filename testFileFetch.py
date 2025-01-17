#for calling all widgets
import tkinter ,os,shutil,time
from tkinter import *
from tkinter import filedialog
import sqlite3
#parent class with tkinter
class ParentWindow(Frame):
    #for initilize these lines are important
    #also u can use **args and **kawargs
    def __init__ (self,master):
        Frame.__init__ (self)
        
        self.master= master
        self.master.resizable(width=False, height=False)
        #we can also give the size according to our requirement by using geometry
        self.master.geometry('{}x{}'.format(900,400))
        #use title for title for the window
        self.master.title("Browse Files!")
        #configure backgroud color with color name or hex color combinations
        self.master.config(bg='darkgrey')
        #add labels
        self.btnShow=Button(self.master,text="Browse..",font=('Helvetica',16),fg='Black',bg='lightgrey',command=self.showfiles)
        self.btnShow.grid(row=0,column=0,padx=(30,0),pady=(30,0))
               
        #createing string
        self.folder_path=StringVar()
        #Label for displaying name on submit button
        self.lblDisplay=Label(self.master,textvariable=self.folder_path,font=("Helvetica",16),fg='Black',bg='lightgrey')
        self.lblDisplay.grid(row=2,column=0,padx=(30,0),pady=(30,0))
    def showfiles(self):
        conn = sqlite3.connect('ShowFiles.db')
        #create a Database 
        with conn:
            cur = conn.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS tb1_AllFiles( ID INTEGER PRIMARY KEY AUTOINCREMENT,col_Files TEXT )")
            conn.commit()
        conn.close()
        global folder_path
        dirname=filedialog.askdirectory()
        destfolder=filedialog.askdirectory()
        files=os.listdir(dirname)
        now=time.time()
        #conn = sqlite3.connect('ShowFiles.db')
        for f in files:
            src=(dirname)+f
            #dest=(destfolder)+f
            show=os.path.join(dirname,f)
            #print(show)
            showtime=time.ctime(os.path.getmtime(show))
            
            '''with conn:
                cur=conn.cursor()
                cur.execute("Insert into tb1_AllFiles(col_Files) values (?)",[f])
                    #item +=1
                conn.commit()
            conn.close()'''
            #if item from list is end with .txt insert it to database
            if f.endswith(".txt"):
                print("{} {}".format(show,showtime))
                shutil.move(f,destfolder)
                #print(item)
                
    def moveFiles(self):
        destfolder=filedialog.askdirectory()
        
        
        
    
   
    
    







if __name__=="__main__":
    #Instance of class with Tk()
    root=Tk()
    #assigning or attach root to the ParentWindow by using app
    App=ParentWindow(root)
    #To stop or close the main loop use this method
    root.mainloop()

