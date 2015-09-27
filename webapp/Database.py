__author__ = 'phrayezzen'

from pymongo import MongoClient


class Database(object):
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.smash_vids

    def create(self):
        