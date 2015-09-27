__author__ = 'phrayezzen'

from pymongo import MongoClient


class Database(object):
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.smash_vids

    def create(self):
        self.db.videos.remove()
        self.db.players.remove()
        self.db.games.remove()
        self.db.characters.remove()
        self.db.stages.remove()

        self.db.players.insert_many([
            {'name': 'Armada', 'main': ['fox', 'peach']},
            {'name': 'Leffen', 'main': ['fox']},
            {'name': 'Mango', 'main': ['fox', 'falco']},
            {'name': 'PPMD', 'main': ['marth', 'falco']},
            {'name': 'Hungrybox', 'main': ['jigglypuff']},
            {'name': 'Mew2King', 'main': ['marth', 'sheik']},
            {'name': 'Plup', 'main': ['sheik']},
            {'name': 'Axe', 'main': ['pikachu']},
            {'name': 'Westballz', 'main': ['falco', 'fox', 'cf']},
            {'name': 'PewPewU', 'main': ['marth']},
            {'name': 'Shroomed', 'main': ['sheik']},
            {'name': 'Lucky', 'main': ['fox']},
            {'name': 'SFAT', 'main': ['fox']},
            {'name': 'Silent Wolf', 'main': ['fox']},
            {'name': 'Hax', 'main': ['fox']},
            {'name': 'MacD', 'main': ['peach']},
            {'name': 'Ice', 'main': ['fox', 'sheik']},
            {'name': 'S2J', 'main': ['cf']},
            {'name': 'HugS', 'main': ['samus']},
            {'name': 'KirbyKaze', 'main': ['sheik']},
            {'name': 'Fly Amanita', 'main': ['ic']},
            {'name': 'aMSa', 'main': ['yoshi']},
            {'name': 'Wizzrobe', 'main': ['cf']},
            {'name': 'DruggedFox', 'main': ['sheik']},
            {'name': 'The Moon', 'main': ['marth']}
        ])

        self.db.characters.insert_many([
            {'_id': 'mario', 'name': 'Mario'},
            {'_id': 'luigi', 'name': 'Luigi'},
            {'_id': 'yoshi', 'name': 'Yoshi'},
            {'_id': 'dk', 'name': 'Donkey Kong'},
            {'_id': 'link', 'name': 'Link'},
            {'_id': 'samus', 'name': 'Samus'},
            {'_id': 'kirby', 'name': 'Kirby'},
            {'_id': 'fox', 'name': 'Fox'},
            {'_id': 'pikachu', 'name': 'Pikachu'},
            {'_id': 'jigglypuff', 'name': 'Jigglypuff'},
            {'_id': 'cf', 'name': 'Captain Falcon'},
            {'_id': 'ness', 'name': 'Ness'},
            {'_id': 'peach', 'name': 'Peach'},
            {'_id': 'bowser', 'name': 'Bowser'},
            {'_id': 'dm', 'name': 'Dr. Mario'},
            {'_id': 'zelda', 'name': 'Zelda'},
            {'_id': 'sheik', 'name': 'Sheik'},
            {'_id': 'ganondorf', 'name': 'Ganondorf'},
            {'_id': 'yl', 'name': 'Young Link'},
            {'_id': 'falco', 'name': 'Falco'},
            {'_id': 'mewtwo', 'name': 'Mewtwo'},
            {'_id': 'pichu', 'name': 'Pichu'},
            {'_id': 'ic', 'name': 'Ice Climbers'},
            {'_id': 'marth', 'name': 'Marth'},
            {'_id': 'roy', 'name': 'Roy'},
            {'_id': 'mgaw', 'name': 'Mr. Game & Watch'}
        ])

        self.db.stages.insert_many([
            {'_id': 'ys', 'name': "Yoshi's Story"},
            {'_id': 'fod', 'name': 'Fountain of Dreams'},
            {'_id': 'bf', 'name': 'Battlefield'},
            {'_id': 'fd', 'name': 'Final Destination'},
            {'_id': 'dl', 'name': 'Dream Land (N64)'},
            {'_id': 'ps', 'name': 'Pokemon Stadium'}
        ])

        self.db.videos.insert_one({
            'winner': 'Armada',
            'loser': 'Hungrybox',
            'url': 'https://www.youtube.com/watch?v=Ea9_nwcN37I',
            'tournament': 'EVO',
            'year': '2015',
            'stages': ['bf', 'dl', 'ps', 'ps', 'fod'],
            
        })

    def get_videos(self, q):
        return self.db.videos.find(q)