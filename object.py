# coding=utf-8

"""This module is the class Object"""

import random


class Object:
    NEEDLE = 'N'
    TUBE = 'T'
    ETHER = 'E'

    def __init__(self, laby):
        self.laby = laby
        ######################################
        # Write Object
        # find the empty box to find the random positions of graphics objects
        self.store_emptyBox = []
        for box in self.laby.empty_box():
            x = box[0] * 40
            y = box[1] * 40
            self.store_emptyBox.append((y, x))

        # Store graphic random position
        self.needle_ramdom_position = random.choice(self.store_emptyBox)
        self.store_emptyBox.remove(self.needle_ramdom_position)
        self.ether_ramdom_position = random.choice(self.store_emptyBox)
        self.store_emptyBox.remove(self.ether_ramdom_position)
        self.pipe_ramdom_position = random.choice(self.store_emptyBox)

    def write_object_in_laby(self):
        # Write the position in laby
        needle_ramdom_position_laby = (
            int(self.needle_ramdom_position[0] / 40),
            int(self.needle_ramdom_position[1] / 40))
        self.laby.write_symbol(needle_ramdom_position_laby[0],
                               needle_ramdom_position_laby[1], 'N')

        ether_ramdom_position_laby = (
            int(self.ether_ramdom_position[0] / 40),
            int(self.ether_ramdom_position[1] / 40))
        self.laby.write_symbol(ether_ramdom_position_laby[0],
                               ether_ramdom_position_laby[1], 'E')

        pipe_ramdom_position_laby = (
            int(self.pipe_ramdom_position[0] / 40),
            int(self.pipe_ramdom_position[1] / 40))
        self.laby.write_symbol(pipe_ramdom_position_laby[0],
                               pipe_ramdom_position_laby[1], 'T')
