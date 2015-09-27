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
        query = 'SELECT url FROM video '
        if 'player1' in f:
            if 'winner' in f:
                if f['winner']:
                    query += 'winner = ' + f['player1'] + ' and '
                else:
                    query += 'loser = ' + f['player1'] + ' and '
            else:
                query += '(winner = ' + f['player1'] + ' or loser = ' + f['player1'] + ') and '

        if 'player2' in f:
            if 'winner' in f:
                if f['winner']:
                    query += 'loser = ' + f['player2'] + ' and '
                else:
                    query += 'winner = ' + f['player2'] + ' and '
            else:
                query += '(winner = ' + f['player2'] + ' or loser = ' + f['player2'] + ') and '

        if 'char1' in f:
            query += 'SELECT v.vID FROM PlayerGameCharacter as p join video as v on ' \
                     'v.winner = p.player or v.loser = p.player where p.character = '+ f['char1'] + ' and '
        if 'char2' in f:
            query += 'SELECT v.vID FROM PlayerGameCharacter as p join video as v on ' \
                     'v.winner = p.player or v.loser = p.player where p.character = ' + f['char2'] + ' and '
        if 'stage' in f:
            query += 'SELECT v.vID FROM Game as g join video as v on v.winner = p.player or v.loser = p.player where g.game= ' + f['stage'] + ' and '
        #match num?
        if 'tournament' in f:
            query += 'tournament = ' + f['tournament'] + ' and '
        if 'year' in f:
            query += 'year = ' + f['year'] + ' and '
        query = query[:-5]
        
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