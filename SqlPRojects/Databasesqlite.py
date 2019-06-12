import sqlite3
conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tb1_persons( ID INTEGER PRIMARY KEY AUTOINCREMENT,col_fname TEXT,  col_lname TEXT,  col_email Text )")
    conn.commit()
conn.close()

conn = sqlite3.connect('test.db')
with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tb1_persons (col_fname,col_lname,col_email) VALUES (?,?,?)", \
                ('Mandeep','Kaur','deep.mandeep83@gmail.com'))
    cur.execute("INSERT INTO tb1_persons (col_fname,col_lname,col_email) VALUES (?,?,?)", \
                ('Varinder','Singh','varinder@gmail.com'))
    cur.execute("INSERT INTO tb1_persons (col_fname,col_lname,col_email) VALUES (?,?,?)", \
                ('Navpreet','Kaur','navpreet@gmail.com'))
    conn.commit()
conn.close()

conn = sqlite3.connect('test.db')
with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_fname,col_lname,col_email from tb1_persons WHERE col_fname='Varinder'")
    varPerson= cur.fetchall()
    for item in varPerson:
        msg = "First Name: {} \n Last Name: {} \nEmail: {}".format(item[0],item[1],item[2])
    print(msg)