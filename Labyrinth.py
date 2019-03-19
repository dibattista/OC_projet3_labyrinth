# coding=utf-8

"""This module is the class Labyrinth"""


class Labyrinth:
    """
        This class store the labyrinth in list
            and the modified with these methods.
        class attribute:
            WALL: (str) define the wall in the labyrinth
    """
    WALL = 'X'

    def __init__(self, data_file):
        self.file = data_file
        self.store_lines = []

        """
              The constructor for Labyrinth class.
                Parameters:
                data_file (str): The labyrinth draw in txt.
                self.store_lines (list) All line of
                    the labyrinth store in this list.
        """

        with open(self.file) as files:
            lines = files.readlines()
            for y in lines:
                x = [i for i in y.strip()]
                self.store_lines.append(x)

    # x vertical
    # y horizontal
    def get_symbol_position(self, symbol):
        """
            The method iterate in the list of all line of the labyrinth.
            Returns:
                The tuple of the position of the symbol wanted.
        """
        for line in self.store_lines:
            for position_x in line:
                if position_x == symbol:
                    horizontal = self.store_lines.index(line)
                    vertical = line.index(position_x)
        return (vertical, horizontal)

    def write_symbol(self, x, y, symbol):
        """
            Assign the position to the symbol.
        """
        self.store_lines[y][x] = symbol

    def get_symbol(self, x, y):
        """
            Return the symbol with the position.
        """
        return self.store_lines[y][x]

    def empty_box(self):
        """
            The method iterate in the list of all line
                of the labyrinth and find the number of line or column  in it.
            Because line don't give the number of the line
                but only that you have in it.
            Returns:
                The list of the empty box in the labyrinth.
        """
        store_empty_box = []
        for y, line in enumerate(self.store_lines):
            for x, symbol in enumerate(line):
                if symbol == ' ':
                    store_empty_box.append((y, x))
        return store_empty_box

    def all_box(self):
        """
             The method iterate in the list of all line
                of the labyrinth and find the number of line or column in it.
             Because line don't give the number of the line
                but only that you have in it.
             Returns:
                 The list of the all box in the labyrinth.
         """
        store_box = []
        for y, line in enumerate(self.store_lines):
            for x, symbol in enumerate(line):
                if symbol == self.WALL:
                    store_box.append((y, x))
        return store_box

    def __str__(self):
        """
            The method iterate the list of list of all lines in the labyrinth.
            And convert to the string each lines
            And join the string with new line for each lines
            Returns:
                The string of the labyrinth.
        """
        list_labyrinth = self.store_lines
        str1 = '\n'.join(str(''.join(e)) for e in list_labyrinth)
        return str1
