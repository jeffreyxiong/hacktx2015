from flask import Flask
import sqlite3 as lite

app = Flask(__name__)
con = lite.connect('db.sqlite3', check_same_thread=False)


def make_dicts(cursor, row):
    return dict((cursor.description[idx][0], value)
                for idx, value in enumerate(row))
con.row_factory = make_dicts
cur = con.cursor()


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()

__author__ = 'phrayezzen'