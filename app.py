from flask import Flask, render_template, request
from db import get_all, get_by_id, insert, update, delete, get_by_price

app = Flask(__name__)


@app.route('/')
def index():
    groceries = get_all()

    return render_template('index.html', groceries=groceries)


@app.route('/<id>')
def id(id):
    grocery = get_by_id(id)

    return render_template('id.html',  grocery= grocery)

@app.route('/details/<int:id>')
def details(id: int):
    grocery = get_by_id(id)

    return render_template('details.html', grocery=grocery)

@app.route('/price')
def in_range():
    min = float(request.args.get('min'))
    max = float(request.args.get('max'))

    groceries = get_by_price(min, max)

    return render_template('index.html', groceries=groceries)

# delete route
@app.route('/delete/<int:id>')
def delete_grocery(id: int):
    pass

# insert route
@app.route('/insert', methods=['POST'])
def insert_grocery():
    pass



if __name__ == '__main__':
    app.run(debug=True)