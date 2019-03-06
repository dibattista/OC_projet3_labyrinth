# coding=utf-8

from pygame.locals import *

class Player:
    GAMER = 'M'
    def __init__(self, x, y, bag):
        self.position_x = x
        self.position_y = y
        self.bag = []
        self.old_x = self.position_x
        self.old_y = self.position_y

        # x vertical
        # y horizontal

    def moveUp(self):
        self.position_y -= 1
        return self.position_x, self.position_y
    
    def moveDown(self):
        self.position_y += 1
        return self.position_x, self.position_y

    def moveRight(self):
        self.position_x += 1
        return self.position_x, self.position_y

    def moveLeft(self):
        self.position_x -= 1
        return self.position_x, self.position_y
    
    def getPosition(self):
        return self.position_x, self.position_y
    
    def addObject(self, tool):
        self.bag.append(tool)
        print('self.bag', self.bag)
        return self.bag
    
    def moveBack(self):
        self.position_x = self.old_x
        self.position_y = self.old_y
    
    def movePlayer(self):
        self.old_x = self.position_x
        self.old_y = self.position_y

        while True:
            player_move = input("Press touch to play ")
            # ici les positions
            if player_move == 'r':
                return self.moveRight()
            elif player_move == 'l':
                return self.moveLeft()
            elif player_move == 'u': 
                return self.moveUp()
            elif player_move == 'd':
                return self.moveDown()
            else:
                print('Wrong key try r,l,u,d')

    def movePlayerGui(self, key):
        self.old_x = self.position_x
        self.old_y = self.position_y

        if key == K_UP:
            return self.moveUp()
        elif key == K_RIGHT:
            return self.moveRight()
        elif key == K_LEFT:
            return self.moveLeft()
        elif key == K_DOWN:
            return self.moveDown()

        
