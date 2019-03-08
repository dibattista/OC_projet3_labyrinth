# coding: utf-8
import random

from Player import Player
from Object import Object
from Guardian import Guardian


class GameManager:

    def __init__(self, laby):
        self.laby = laby
        player_position = laby.get_symbol_position(Player.GAMER)
        self.macgyver = Player(player_position[0], player_position[1])
        self.guardian = Guardian()

    def launch_game(self):
        store_object = ['N', 'T', 'E']
        for ob in store_object:
            needle_ramdom_position = random.choice(self.laby.empty_box())
            self.laby.write_symbol(
                needle_ramdom_position[1], needle_ramdom_position[0], ob)

        while True:
            print(self.laby)
            # Old position of gamer
            old_position = self.macgyver.get_position()
            # New position of gamer
            new_position = self.macgyver.move_player()
            check_symbol = self.laby.get_symbol(new_position[0],
                                               new_position[1])

            # If a player find a wall try again
            if check_symbol == self.laby.WALL:
                self.macgyver.move_back()
                print('Sorry wrong place try again')
                continue

            # If a player find a object store it and delete from laby
            elif check_symbol == Object.TUBE or \
                    check_symbol == Object.ETHER or \
                    check_symbol == Object.NEEDLE:
                self.macgyver.add_object(check_symbol)

                self.laby.write_symbol(
                    new_position[0], new_position[1], Player.GAMER)
                self.laby.write_symbol(old_position[0], old_position[1], ' ')

            # If the player find the guardian
            elif check_symbol == Guardian.GARDIAN:
                self.guardian.macgyver_vs_guardian(self.macgyver.bag)

            else:
                # replace symbol by space
                self.laby.write_symbol(
                    new_position[0], new_position[1], Player.GAMER)

                self.laby.write_symbol(old_position[0], old_position[1], ' ')
