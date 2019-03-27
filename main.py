#coding:utf-8

import pickle

class Player:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def whoami(self):
        print("{} ({})".format(self.name, self.level))


with open ("player.data", "rb") as fic:
    get_record = pickle.Unpickler(fic)
    player_one = get_record.load()

player_one.whoami()