# coding=utf-8

from Guardian import Guardian


class Labyrinth:
    WALL = 'X'

    def __init__(self, data_file):
        self.file = data_file
        self.store_lines = []
        self.gardian = Guardian()

        with open(self.file) as files:
            lines = files.readlines()
            for y in lines:
                x = [i for i in y.strip()]
                self.store_lines.append(x)

    # x vertical
    # y horizontal
    def getSymbolPosition(self, symbol):
        for line in self.store_lines:
            for positionx in line:
                if positionx == symbol:
                    horizontal = self.store_lines.index(line)
                    vertical = line.index(positionx)
        return (vertical, horizontal)

    def write_symbole(self, x, y, symbol):
        self.store_lines[y][x] = symbol

    def getSymbol(self, x, y):
        return self.store_lines[y][x]

    def emptyBox(self):
        store_empty_box = []
        for y, line in enumerate(self.store_lines):
            for x, symbole in enumerate(line):
                if symbole == ' ':
                    store_empty_box.append((y, x))
        return store_empty_box
    
    def all_box(self):
        store_box = []
        for y, line in enumerate(self.store_lines):
            for x, symbole in enumerate(line):
                if symbole == 'X':
                    store_box.append((y, x))
        return store_box

    def __str__(self):
        list_labyrinth = self.store_lines
        str1 = '\n'.join(str(''.join(e)) for e in list_labyrinth)

        return str1

