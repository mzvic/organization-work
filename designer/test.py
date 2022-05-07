from tinydb import TinyDB, Query
dbjs = TinyDB('db/db.json')

print(dbjs.search(Query().client == 'client 2'))