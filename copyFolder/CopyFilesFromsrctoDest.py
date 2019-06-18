#for calling all widgets
import tkinter ,os,time,glob
from tkinter import *
from tkinter import filedialog
import datetime,sqlite3,shutil
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
        #add buttons
        self.btnShow=Button(self.master,text="Origin..",width=10,height=1,font=('Helvetica',16),fg='Black',bg='lightgrey',command=self.showfiles)
        self.btnShow.grid(row=0,column=0,padx=(30,0),pady=(30,0))
        #use this directory for copy files from origin
        self.btndest=Button(self.master,text="Destination..",width=10,height=1,font=('Helvetica',16),fg='Black',bg='lightgrey',command=self.destinationDir)
        self.btndest.grid(row=2,column=0,padx=(30,0),pady=(30,0))
        #show files which are move from origin to destination directory
        self.btnCopy=Button(self.master,text="show Files..",width=10,height=1,font=('Helvetica',16),fg='Black',bg='lightgrey',command=self.showfiles)
        self.btnCopy.grid(row=4,column=0,padx=(30,0),pady=(30,0))
        #createing string
        self.folder_path=StringVar()
        self.dest_path=StringVar()
        #Label for displaying files path on  button click
        self.lblDisplay=Label(self.master,textvariable=self.folder_path,font=("Helvetica",16),fg='Black',bg='lightgrey')
        self.lblDisplay.grid(row=1,column=0,padx=(30,0),pady=(30,0))
        #Label for displaying files path on button click for destButton
        self.lblDestShow=Label(self.master,textvariable=self.dest_path,font=("Helvetica",16),fg='Black',bg='lightgrey')
        self.lblDestShow.grid(row=3,column=0,padx=(30,0),pady=(30,0))
        conn = sqlite3.connect('CopyOfFiles.db')
        #create a Database 
        with conn:
            cur = conn.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS tb1_CopyFiles( ID INTEGER PRIMARY KEY AUTOINCREMENT,col_Files TEXT,created_at DATE )")
            conn.commit()
        conn.close()
        now=time.time()    
    def showfiles(self):
        global folder_path
        dirname=filedialog.askdirectory()
        files=os.listdir(dirname)
        now=time.time()
        old_files = [] # list of files older than 7 days
        new_files = [] # list of files newer than 1 day
        for f in files:
            fn = os.path.join(dirname, f)
            mtime = os.stat(fn).st_mtime
            if mtime > now - 1 * 86400:
                
                # this is a new file
                new_files.append(fn)
                filestime=time.ctime(os.path.getmtime(fn))
                print(filestime)
               
            elif mtime < now - 7 * 86400:
                # this is an old file
                old_files.append(fn)
                filestimes=time.ctime(os.path.getmtime(fn))
                print(filestime)
            # else file between 1 and 7 days old, ignore
            if f.endswith(".txt"):
                showtime=time.ctime(os.path.getmtime(fn))
                print("{} {}".format(fn,showtime))
                shutil.move(fn,destfolder)
                conn = sqlite3.connect('CopyOfFiles.db')
                with conn:
                    cur=conn.cursor()
                    cur.execute("Insert into tb1_AllFiles(col_Files,created_at) values (?,?)",[f,showtime])
                    conn.commit()
                conn.close()
        
        self.folder_path.set(dirname)
        print(dirname)
        return dirname
    def destinationDir(self):
        global dest_path
        destfolder=filedialog.askdirectory()
        self.dest_path.set(destfolder)
        print(destfolder)
        return destfolder
        
        #self.lblDisplay.config("{}".format(self.lblDisplay))
'''conn = sqlite3.connect('CreationOfFiles.db')        
with conn:
    cur=conn.cursor()
    cur.execute("delete from tb1_AllFiles")
    conn.commit()
conn.close()'''       
    
   
    
    







if __name__=="__main__":
    #Instance of class with Tk()
    root=Tk()
    #assigning or attach root to the ParentWindow by using app
    App=ParentWindow(root)
    #To stop or close the main loop use this method
    root.mainloop()


