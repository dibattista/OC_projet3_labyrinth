# coding: utf-8
import random

from Player import Player
from Object import Object
from Guardian import Guardian

class GameManager:
    def __init__(self, laby):
        self.laby = laby
        player_position = laby.getSymbolPosition(Player.GAMER)
        self.macgyver = Player(player_position[0], player_position[1], [])
        self.guardian = Guardian()

    def lauch_game(self):
        # add object to laaby
        store_object = ['N', 'T', 'E']
        for ob in store_object:
            needle_ramdom_position = random.choice(self.laby.emptyBox())
            self.laby.write_symbole(
                needle_ramdom_position[1], needle_ramdom_position[0], ob)

        while True:
            print(self.laby)
            # Old position of gamer
            old_position = self.macgyver.getPosition()
            # New position og gamer
            new_position = self.macgyver.movePlayer()

            check_symbol = self.laby.getSymbol(new_position[0], new_position[1])
            old_possition_line_player = self.laby.getSymbolPosition(Player.GAMER)[1]

            # If a player find a wall try again
            if check_symbol == self.laby.WALL:
                print('Sorry wrong place try again')
                # Bug si rencontre un mur et rejoue refait une erreur???
                continue

            # If a player find a object store it and delete from laby
            elif check_symbol == Object.TUBE or check_symbol == Object.ETHER or check_symbol == Object.NEEDLE:
                self.macgyver.addObject(check_symbol)
    
                self.laby.write_symbole(
                    new_position[0], new_position[1], Player.GAMER)
                self.laby.write_symbole(old_position[0], old_position[1], ' ')

            # If the player find the gardian
            elif check_symbol == Guardian.GARDIAN:
                self.guardian.sleeping_gardian(self.macgyver.bag)

            else:
                # replace symbole by space
                self.laby.write_symbole(
                    new_position[0], new_position[1], Player.GAMER)
                
                self.laby.write_symbole(old_position[0], old_position[1], ' ')

