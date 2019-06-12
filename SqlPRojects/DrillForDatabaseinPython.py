import sqlite3
conn = sqlite3.connect('ShowFiles.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tb1_AllFiles( ID INTEGER PRIMARY KEY AUTOINCREMENT,col_Files TEXT )")
    conn.commit()
conn.close()
fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')
for list in fileList:
    print(list)
   
    
