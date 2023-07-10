from flask import Flask, render_template, request ,jsonify
from tinydb import TinyDB, Query


db = TinyDB('db.json', indent=4)
grocery = db.table('grocery')



app = Flask(__name__)

    
product = db.table('grocery')


@app.route('/')
def index():
    groceries = grocery.all()

    return render_template('index.html', groceries=groceries)


@app.route('/id/<id>')
def id(id):
    grocery =product.get(doc_id=id)

    return render_template('id.html',  grocery= grocery)




if __name__ == '__main__':
    app.run(debug=True)