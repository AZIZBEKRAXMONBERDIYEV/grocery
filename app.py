from flask import Flask, render_template, request
from db import get_all, get_by_id, insert, update, delete

app = Flask(__name__)


@app.route('/')
def index():
    groceries = get_all()

    return render_template('index.html', groceries=groceries)


if __name__ == '__main__':
    app.run(debug=True)