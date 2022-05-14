import sqlite3 as sq

con = sq.connect("designer/db/sql.db")

cur = con.cursor()
value = ["generic value 5"]
cur.execute("INSERT INTO jobsdb VALUES (?)", value)


con.commit()
con.close()