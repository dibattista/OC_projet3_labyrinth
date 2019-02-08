# coding: utf-8

from Player import Player

class GameManager:
    def __init__(self, laby):
        self.laby = laby
        player_position = laby.getSymbolPosition(Player.GAMER)
        self.macgyver = Player(player_position[0], player_position[1])
    
    def lauch_game(self):
        # while true
        # demander au jouer de bouger
        # recupere nouvelle coordonee
        # est-ce qu'il peut bouger?
        # si oui on suprime m 
        # write symbole pour donner les coordonéen pour le déplacer

        while True:
            print(self.laby)
            # demander au jouer de bouger
            new_position = self.macgyver.movePlayer()
            # recupere nouvelle coordonee
            print('new_position', new_position)
            self.laby.write_symbole(
                new_position[0], new_position[1], Player.GAMER)


