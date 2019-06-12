import sqlite3,re,os
conn = sqlite3.connect('ShowFiles.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tb1_AllFiles( ID INTEGER PRIMARY KEY AUTOINCREMENT,col_Files TEXT )")
    conn.commit()
conn.close()
def checkext(filename):
    if re.search('\.txt$',filename,flags=re.IGNORECASE):
        return('txt')
fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')
conn = sqlite3.connect('ShowFiles.db')
for list in fileList:
   # fname,fileextension=os.path.splitext(list)
    #print("{}==>{}".format(list,checkext(list)))
    for e in list.split():
        if e.endswith(".txt"):
            print(list)
            with conn:
                cur=conn.cursor()
                cur.executemany("Insert into tb1_AllFiles(col_Files) values (?)",list)
                conn.commit()
            
    """if list.split(".")[1]=="txt":
        with conn:
            cur=conn.cursor()
            cur.execute("Insert into tb1_AllFiles(col_Files) values (?)",list)
            conn.commit()
conn.close()"""
        
    
#conn = sqlite3.connect('ShowFiles.db')

"""with conn:
    cur=conn.cursor()
    cur.execute("delete from tb1_AllFiles")
    conn.commit()
conn.close()"""

    
    
