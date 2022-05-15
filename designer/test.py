import sqlite3 as sq

con = sq.connect("designer/db/sql.db")

cur = con.cursor()

cur.execute(f"SELECT name FROM sqlite_master WHERE type='table'")
tables = cur.fetchall()
print(len(tables))
table = str(tables[0])
print(table.strip("()',"))

con.commit()
con.close()