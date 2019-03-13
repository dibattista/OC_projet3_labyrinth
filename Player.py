# coding=utf-8

"""This module is the class Player"""

from pygame.locals import *


class Player:
    GAMER = 'M'

    def __init__(self, x, y):
        self.position_x = x
        self.position_y = y
        self.bag = []
        # x vertical
        # y horizontal
        self.old_x = self.position_x
        self.old_y = self.position_y

    def move_up(self):
        self.position_y -= 1
        return self.position_x, self.position_y

    def move_down(self):
        self.position_y += 1
        return self.position_x, self.position_y

    def move_right(self):
        self.position_x += 1
        return self.position_x, self.position_y

    def move_left(self):
        self.position_x -= 1
        return self.position_x, self.position_y

    def get_position(self):
        return self.position_x, self.position_y

    def add_object(self, tool):
        self.bag.append(tool)
        return self.bag

    def move_back(self):
        self.position_x = self.old_x
        self.position_y = self.old_y

    def move_player(self):
        self.old_x = self.position_x
        self.old_y = self.position_y

        while True:
            player_move = input("Press touch to play ")
            if player_move == 'r':
                return self.move_right()
            elif player_move == 'l':
                return self.move_left()
            elif player_move == 'u':
                return self.move_up()
            elif player_move == 'd':
                return self.move_down()
            else:
                print('Wrong key try r,l,u,d')

    def move_player_gui(self, key):
        self.old_x = self.position_x
        self.old_y = self.position_y

        if key == K_UP:
            return self.move_up()
        elif key == K_RIGHT:
            return self.move_right()
        elif key == K_LEFT:
            return self.move_left()
        elif key == K_DOWN:
            return self.move_down()
