import sqlite3 as sq

con = sq.connect("designer/db/sql.db")

cur = con.cursor()

row = ('1 1adssdasas', '2 2 2' , '3 3 3', '4 4 4', '5 5 5', '6 6 6')

cur.execute(f"INSERT INTO all_works VALUES (?,?,?,?,?,?) ", row)

# cur.execute("DELETE FROM all_works WHERE 1")

con.commit()
con.close()
