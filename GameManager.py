# coding: utf-8

"""This module is the class GameManager"""

import random

from Player import Player
from Object import Object
from Guardian import Guardian


class GameManager:
    """
        This is a class for launch a loop to playing the game.
        Attributes:
            laby (class): Allow to access of the class Labyrinth
            The class Labyrinth build the Labyrinth of the game.
    """

    def __init__(self, laby):
        self.laby = laby
        player_position = laby.get_symbol_position(Player.GAMER)
        self.macgyver = Player(player_position[0], player_position[1])
        self.guardian = Guardian()

        """
              The constructor for GameManager class.
                Parameters:
                laby (class): Access of the class Labyrinth.
                player_position(tuple): return the vertical and horizontal position of the player.
                macgyver(class): Access of the class Player
                guardian(class): Access of the class Guardian
        """

    def launch_game(self):
        """
            The method continue the algorithm util while is true.
            before the algorithm, add in the labyrinth, the objects in the random position
            Algorithm:
                print the labyrinth to see player move
                store the old position of the player
                store the new position of the player
                find the symbol in the new position player
                first condition if the symbol equal wall stop the player
                second condition if the symbol equal one of the objects,
                    add object in the player's bag and replace the object by the player
                third condition if the symbol equal the guardian finish the game with two options to print:
                    win or lose.
                for all the other conditions move the player in this new place
        """
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
            elif check_symbol == Guardian.GUARDIAN:
                self.guardian.macgyver_vs_guardian(self.macgyver.bag)
                return


            else:
                # replace symbol by space
                self.laby.write_symbol(
                    new_position[0], new_position[1], Player.GAMER)

                self.laby.write_symbol(old_position[0], old_position[1], ' ')
