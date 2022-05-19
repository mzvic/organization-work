import sqlite3 as sq

con = sq.connect("designer/db/sql.db")

cur = con.cursor()

# row = ('1', '2' , '3', '4', '5', '6')
# cur.execute(f"INSERT INTO all_works (client, job, stat, dr, dl, ac) VALUES (?,?,?,?,?,?) ", row)
# cur.execute("DELETE FROM all_works ")
cur.execute("SELECT MAX(id) FROM all_works")
a = cur.fetchall()
print(a)
# cur.execute("""CREATE TABLE all_works (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             client TEXT,
#             job TEXT,
#             stat TEXT,
#             dr TEXT,
#             dl TEXT, 
#             ac TEXT

# )""")
con.commit()
con.close()
