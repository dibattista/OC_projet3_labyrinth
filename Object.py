# coding=utf-8

"""This module is the class Object"""

import random


class Object:
    """
        This is a class about the objects.
        instance attributes:
            laby (class): Allow to access of the class Labyrinth
        class attribute:
            NEEDLE (str): define the needle object in the labyrinth.
            TUBE: (str): define the tube object in the labyrinth.
            ETHER: (str): define ether object in the labyrinth.
    """

    NEEDLE = 'N'
    TUBE = 'T'
    ETHER = 'E'

    def __init__(self, laby):
        self.laby = laby
        self.store_emptyBox = []

        self.needle_random_position = random.choice(
            self.store_empty_graphic_box())

        self.store_emptyBox.remove(self.needle_random_position)
        self.ether_random_position = random.choice(
            self.store_empty_graphic_box())

        self.store_emptyBox.remove(self.ether_random_position)
        self.pipe_random_position = random.choice(
            self.store_empty_graphic_box())

        """
              The constructor for Object class.
                Parameters:
                self.laby (class): Allow to access of the class Labyrinth
                self.store_emptyBox (list): list empty in the start
                self.needle_random_position (tuple): Tuple with two
                    random int from empty box of the labyrinth
                remove self.needle_random_position to avoid duplicate
                self.ether_random_position (tuple): Tuple with
                    two random int from empty box of the labyrinth
                remove self.ether_random_position to avoid duplicate
                self.pipe_random_position (tuple): Tuple with two random int

        """

    def store_empty_graphic_box(self):
        """
            The method iterate in the list of empty box of the labyrinth,
            to have the value of x and y of this empty box in the graphic.
            Returns:
                The list of tuples of x and y for the graphic.
        """
        for box in self.laby.empty_box():
            x = box[0] * 40
            y = box[1] * 40
            self.store_emptyBox.append((y, x))
        return self.store_emptyBox

    def write_object_in_laby(self):
        """
            The method write in the labyrinth the objects
                with the value of their attributes.
            Returns:
                The string of the object in the new position in the labyrinth.
        """
        needle_random_position_laby = (
            int(self.needle_random_position[0] / 40),
            int(self.needle_random_position[1] / 40))
        self.laby.write_symbol(needle_random_position_laby[0],
                               needle_random_position_laby[1], 'N')

        ether_random_position_laby = (
            int(self.ether_random_position[0] / 40),
            int(self.ether_random_position[1] / 40))
        self.laby.write_symbol(ether_random_position_laby[0],
                               ether_random_position_laby[1], 'E')

        pipe_random_position_laby = (
            int(self.pipe_random_position[0] / 40),
            int(self.pipe_random_position[1] / 40))
        self.laby.write_symbol(pipe_random_position_laby[0],
                               pipe_random_position_laby[1], 'T')
