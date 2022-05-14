import sqlite3 as sq

con = sq.connect("designer/db/sql.db")

cur = con.cursor()
value = ["generic value 5"]
cur.execute("CREATE TABLE all_works ()")


con.commit()
con.close()