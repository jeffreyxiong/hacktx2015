__author__ = 'phrayezzen'

from flask import Flask, request, jsonify
import sqlite3 as lite
from Database import Database
import copy

app = Flask(__name__)
db = Database()
# con = lite.connect('db.sqlite3', check_same_thread=False)


# def make_dicts(cursor, row):
#     return dict((cursor.description[idx][0], value)
#                 for idx, value in enumerate(row))
# con.row_factory = make_dicts
# cur = con.cursor()


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/video', methods=['GET', 'POST'])
def video():
    if True:#request.method == "GET":
        f = la#request.form
        vid = {}
        game = {}

        # conditions that apply to both vid and game
        if 'winner' in f:
            if 'player1' in f:
                if 'player2' in f:
                    if f['winner']:
                        vid['winner'] = f['player1']
                        vid['loser'] = f['player2']
                    else:
                        vid['winner'] = f['player1']
                        vid['loser'] = f['player2']
                else:
                    if f['winner']:
                        vid['winner'] = f['player1']
                    else:
                        vid['loser'] = f['player1']
            else:
                if 'player2' in f:
                    if f['winner']:
                        vid['loser'] = f['player2']
                    else:
                        vid['winner'] = f['player2']
        if 'winner' not in f:
            if 'player1' in f:
                if 'player2' in f:
                    vid['or'] = [{'winner' : f['player1'], 'loser': f['player2']}, {'winner': f['player2'], 'loser': f['player1']}]
                else:
                    vid['or'] = [{'winner' : f['player1']}, {'loser': f['player1']}]
            else:
                if 'player2' in f:
                    vid['or'] = [{'winner' : f['player2']}, {'loser': f['player2']}]


        if 'stage' in f:
            vid['stage'] = f['stage']

        game = vid.copy()

        # everything only in vid

        if 'tournament' in f:
            vid['tournament'] = f['tournament']

        if 'year' in f:
            vid['year'] = f['year']

        if 'matches' in f:
            vid['matches'] = f['matches']

        # everything only in game

        if 'winner' in f:
            if 'char1' in f:
                if 'char2' in f:
                    if f['winner']:
                        game['winnerChar'] = f['char1']
                        game['loserChar'] = f['char2']
                    else:
                        game['winnerChar'] = f['char1']
                        game['loserChar'] = f['char2']
                else:
                    if f['winner']:
                        game['winnerChar'] = f['char1']
                    else:
                        game['loserChar'] = f['char2']
            else:
                if 'char2' in f:
                    if f['winner']:
                        game['loserChar'] = f['char2']
                    else:
                        game['winnerChar'] = f['char2']
        if 'winner' not in f:
            if 'char1' in f:
                if 'char2' in f:
                    game['or'] = [{'winnerChar' : f['char1'], 'loserChar': f['char2']}, {'winnerChar' : f['char2'], 'loserChar': f['char1']}]
                else:
                    game['or'] = [{'winnerChar' : f['char1']}, {'loserChar': f['char1']}]
            else:
                if 'char2' in f:
                    game['or'] = [{'winnerChar' : f['char2']}, {'loser': f['char2']}]
    return db.get_videos(game)

la = {
    'player1': 'Armada',
    'player2': 'Hungrybox',
    'char1': 'Fox',
    'char2': 'Jigglypuff',
    'winner': True
}
print video()




    #     query = 'SELECT url FROM video '
    #     if 'player1' in f:
    #         if 'winner' in f:
    #             if f['winner']:
    #                 query += 'winner = ' + f['player1'] + ' and '
    #             else:
    #                 query += 'loser = ' + f['player1'] + ' and '
    #         else:
    #             query += '(winner = ' + f['player1'] + ' or loser = ' + f['player1'] + ') and '

    #     if 'player2' in f:
    #         if 'winner' in f:
    #             if f['winner']:
    #                 query += 'loser = ' + f['player2'] + ' and '
    #             else:
    #                 query += 'winner = ' + f['player2'] + ' and '
    #         else:
    #             query += '(winner = ' + f['player2'] + ' or loser = ' + f['player2'] + ') and '

    #     if 'char1' in f:
    #         query += 'SELECT v.vID FROM PlayerGameCharacter as p join video as v on ' \
    #                  'v.winner = p.player or v.loser = p.player where p.character = '+ f['char1'] + ' and '
    #     if 'char2' in f:
    #         query += 'SELECT v.vID FROM PlayerGameCharacter as p join video as v on ' \
    #                  'v.winner = p.player or v.loser = p.player where p.character = ' + f['char2'] + ' and '
    #     if 'stage' in f:
    #         query += 'SELECT v.vID FROM Game as g join video as v on v.winner = p.player or v.loser = p.player where g.game= ' + f['stage'] + ' and '
    #     #match num?
    #     if 'tournament' in f:
    #         query += 'tournament = ' + f['tournament'] + ' and '
    #     if 'year' in f:
    #         query += 'year = ' + f['year'] + ' and '
    #     query = query[:-5]
        
    #     with con:
    #         cur.execute("""SELECT * FROM contact""")
    #         rows = {"result": cur.fetchall()}
    #         return jsonify(rows)
    #     return jsonify({})
    # elif request.method == "POST":
    #     f = request.form
    #     with con:
    #         cur.execute("""INSERT INTO contact (firstName, lastName, phone, address, city, state, zip)
    #                        VALUES (?, ?, ?, ?, ?, ?, ?)""",
    #                        (f['first'], f['last'], f['phone'], f['address'], f['city'], f['state'], f['zip']))
    #         con.commit()
    #         cur.execute("""SELECT * FROM contact WHERE contactId = ?""", (str(cur.lastrowid),))
    #         contact = {"result": [cur.fetchone()]}
    #         return jsonify(contact)
    #     return jsonify({})


if __name__ == '__main__':
    app.run()