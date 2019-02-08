import os
from Player import Player
from Guardian import Guardian
from Object import Object

# Creer une classe Labyrinth qui dans son constructeur 
# ouvre le fichier texte et stocke chaque ligne dans une liste


class Labyrinth:
    WALL = 'X'
    def __init__(self, data_file):
        self.file = data_file
        self.store_lines = []
        self.store_object = []
        # self.object = Object(self.store_object)



        with open(self.file) as files:
            lines = files.readlines()
            for y in lines:
                x = [i for i in y.strip()]
                self.store_lines.append(x)
    # chercher la position object et player et gardien

    # x vertical
    # y horizontal
    def getSymbolPosition(self, symbol):
        for line in self.store_lines:
            for positionx in line:
                if positionx == symbol:
                    horizontal = self.store_lines.index(line)
                    vertical = line.index(positionx)
        return (vertical, horizontal)
    
    # Mettre le jouer ou autre symbole à ça nouvelle place
    def write_symbole(self, x, y, symbol):
        check_symbol_new_place = self.store_lines[y][x]
        old_possition_line_player = self.getSymbolPosition(symbol)[1]


        # If a player find a wall try again
        if check_symbol_new_place == self.WALL:
            print('Sorry wrong place try again')
            Player(x, y).movePlayer()

        # If a player find a object store it
        elif check_symbol_new_place == Object.TUBE or check_symbol_new_place == Object.ETHER or check_symbol_new_place == Object.NEEDLE:
            print('check_symbol_new_place in if: ', check_symbol_new_place)
            self.store_object.append(
                check_symbol_new_place)
            # supprimer l'object
            # si jouer quite la partie object bouge
            self.store_object
            print('self.store_object', self.store_object)


        # If the player find the gardian
        elif check_symbol_new_place == Guardian.GARDIAN:
            print('check store_object', self.store_object)
            list_all_objects = ['E', 'T', 'N']
            result = all(
                elem in self.store_object for elem in list_all_objects)
            if result:
                print('YOU WIN!')
            else: 
                print('You are dead')

        else:
            # replace symbole by space
            self.store_lines[old_possition_line_player] = [line.replace(symbol, ' ')
                        for line in self.store_lines[old_possition_line_player]]

            # Add symbol in nex place
            self.store_lines[y][x] = symbol
            print('symbol', symbol)

    
    def __str__(self):
        list_labyrinth = self.store_lines
        str1 = '\n'.join(str(''.join(e)) for e in list_labyrinth)

        return str1

