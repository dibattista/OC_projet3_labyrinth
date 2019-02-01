# coding=utf-8
import Labyrinth as lab

class Player:
    def __init__(self, x, y, mapGame):
        self.position_x = x
        self.position_y = y
        self.map = mapGame
        self.GAMER = 'M'

        # x vertical
        # y horizontal

    def playerPosition(self):
        for line in self.map:
            for positionx in line:
                if positionx == self.GAMER:
                    horizontal = self.map.index(line)
                    vertical = line.index(positionx)
        # print('The player is in line: ', horizontal, vertical)
        return Player(vertical, horizontal, self.map)

    def moveUp(self):
        # pourquoi le position_x et y non pas la même valeur 
        # que self.playerPosition().position_y et x?

        # First remove the player in old place
        line_player = self.map[self.playerPosition().position_y]
        line_player.remove(self.GAMER)
        line_player.insert(self.playerPosition().position_x, ' ')

        # Put the player in the new place
        new_position_line = self.map[self.playerPosition().position_y - 1]
        # delete the element in this place and return it
        new_position_line.pop(self.playerPosition().position_x)
        # check if mur ou gardien ou object
        # if not put the player in this place
        new_position_line.insert(self.playerPosition().position_x, self.GAMER)
        return Player(self.position_x, self.playerPosition().position_y-1, self.map)
    
    # def moveDown(self):
    #     return Player(self.position_x+1, self.position_y)
    
    # def moveRight(self):
    #     return Player(self.position_x, self.position_y+1)

    # def moveLeft(self):
    #     return Player(self.position_x, self.position_y-1)
    
    def movePlayer(self):
        return input("Press touch to play")


playe = Player(0, 0, lab.laby.store_lines)
