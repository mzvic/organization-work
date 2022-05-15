import sqlite3 as sq

con = sq.connect("designer/db/sql.db")

cur = con.cursor()
value = ["generic value 5"]
g = 'generic'
cur.execute(f"INSERT INTO all_works VALUES ('{g} client', '{g} job', '{g} status', '{g} dr', '{g} dl', '{g} ac')")

con.commit()
con.close()