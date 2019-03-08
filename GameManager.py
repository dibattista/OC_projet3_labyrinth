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

    def launch_game(self):
        store_object = ['N', 'T', 'E']
        for ob in store_object:
            needle_ramdom_position = random.choice(self.laby.emptyBox())
            self.laby.write_symbole(
                needle_ramdom_position[1], needle_ramdom_position[0], ob)

        while True:
            print(self.laby)
            # Old position of gamer
            old_position = self.macgyver.getPosition()
            print('old_position', old_position)
            # New position of gamer
            new_position = self.macgyver.movePlayer()
            print('new_position', new_position)

            check_symbol = self.laby.getSymbol(new_position[0], new_position[1])

            # If a player find a wall try again
            if check_symbol == self.laby.WALL:
                self.macgyver.moveBack()
                print('Sorry wrong place try again')
                continue

            # If a player find a object store it and delete from laby
            elif check_symbol == Object.TUBE or check_symbol == Object.ETHER or check_symbol == Object.NEEDLE:
                self.macgyver.addObject(check_symbol)
    
                self.laby.write_symbole(
                    new_position[0], new_position[1], Player.GAMER)
                self.laby.write_symbole(old_position[0], old_position[1], ' ')

            # If the player find the gardian
            elif check_symbol == Guardian.GARDIAN:
                self.guardian.macgyver_vs_guardian(self.macgyver.bag)

            else:
                # replace symbole by space
                self.laby.write_symbole(
                    new_position[0], new_position[1], Player.GAMER)
                
                self.laby.write_symbole(old_position[0], old_position[1], ' ')

