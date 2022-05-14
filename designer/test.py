import sqlite3 as sq

con = sq.connect("designer/db/sql.db")

cur = con.cursor()


cur.execute("SELECT * FROM clientsdb")
datos = cur.fetchall()
for a in list(datos):
    print(a)

con.commit()
con.close()