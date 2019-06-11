import sqlite3
conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tb1_persons(\ ID INTEGER PRIMARY KEY AUTOINCREMENT,\ col_fname TEXT, \ col_lname TEXT, \ col_email Text )")
    conn.commit()
conn.close()