import sqlite3 as sq

con = sq.connect("designer/db/sql.db")

cur = con.cursor()
value = input()
cur.execute(f"DELETE FROM clientsdb WHERE client = '{value}' ")


con.commit()
con.close()