from tinydb import TinyDB, Query

db = TinyDB('db.json', indent=4)
grocery = db.table('grocery')

def get_all():
    return grocery.all()

def get_by_id(id):
    return grocery.get(doc_id=id)

def get_by_price(min, max):
    return grocery.search(Query().price >= min and Query().price <= max)

def insert(data):
    return grocery.insert(data)

def update(id, data):
    return grocery.update(data, doc_ids=[id])

def delete(id):
    return grocery.remove(doc_ids=[id])
