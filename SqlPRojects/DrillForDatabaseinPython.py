import sqlite3,re,os
conn = sqlite3.connect('ShowFiles.db')
#create a Database 
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tb1_AllFiles( ID INTEGER PRIMARY KEY AUTOINCREMENT,col_Files TEXT )")
    conn.commit()
conn.close()
#list of files 
fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')
conn = sqlite3.connect('ShowFiles.db')
#Iterate the list by using for loop
for item in fileList:
    #if item from list is end with .txt insert it to database
    if item.endswith("txt"):
        print(item)
        with conn:
            cur=conn.cursor()
            cur.execute("Insert into tb1_AllFiles(col_Files) values (?)",[item])
            #item +=1
        conn.commit()
#Iterate data from database        
conn = sqlite3.connect('ShowFiles.db')
with conn:
    cur=conn.cursor()
    cur.execute("Select * from tb1_AllFiles")
    varFiles= cur.fetchall()
    for item in varFiles:
        print(varFiles)
conn.commit()
'''with conn:
    cur=conn.cursor()
    cur.execute("delete from tb1_AllFiles")
    conn.commit()
conn.close()'''

    
    
