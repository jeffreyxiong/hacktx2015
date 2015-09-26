__author__ = 'phrayezzen'

from flask import Flask, request, jsonify
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

@app.route('/video', methods=['GET', 'POST'])
def video():
    if request.method == "GET":
        f = request.form
        with con:
            cur.execute("""SELECT * FROM contact""")
            rows = {"result": cur.fetchall()}
            return jsonify(rows)
        return jsonify({})
    elif request.method == "POST":
        f = request.form
        with con:
            cur.execute("""INSERT INTO contact (firstName, lastName, phone, address, city, state, zip)
                           VALUES (?, ?, ?, ?, ?, ?, ?)""",
                           (f['first'], f['last'], f['phone'], f['address'], f['city'], f['state'], f['zip']))
            con.commit()
            cur.execute("""SELECT * FROM contact WHERE contactId = ?""", (str(cur.lastrowid),))
            contact = {"result": [cur.fetchone()]}
            return jsonify(contact)
        return jsonify({})


if __name__ == '__main__':
    app.run()
