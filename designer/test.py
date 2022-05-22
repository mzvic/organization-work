import sqlite3 as sq

con = sq.connect("designer/db/sql.db")

cur = con.cursor()

row = ('1111', '2222' , '3333', '4444', '5555', '6666')
cur.execute(f"INSERT INTO all_works (client, job, stat, dr, dl, ac) VALUES (?,?,?,?,?,?) ", row)
# cur.execute("DELETE FROM all_works ")

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
