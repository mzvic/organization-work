import sqlite3 as sq

con = sq.connect("designer/db/sql.db")

cur = con.cursor()
cur.execute("SELECT * FROM clientsdb")
lista = ["one", "two", "three"]
datos = cur.fetchall()
x = list(datos)
for a in list(datos):
    print(a.strip("(),'"))

# Save (commit) the changes
con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()