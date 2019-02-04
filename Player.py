# coding=utf-8
import Labyrinth as lab
# import pygame

# iniatilise the game
# pygame.init()

# display_width = 800
# display_height = 600
# gameDisplay = pygame.display.set_mode((display_width, display_height))
# pygame.display.set_caption('Let save MacGyver')
# clock = pygame.time.Clock()


# je pars toujours de mon point de départ 
# comment partir de ma dernière commande?


class Player:
    def __init__(self, x, y, mapGame):
        self.position_x = x
        print('in class possition_x', self.position_x)
        self.position_y = y
        print('in class position_y', self.position_y)
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
        print('The player is : ', horizontal, vertical)
        return Player(vertical, horizontal, self.map)

    def moveUp(self):
        place_x = self.playerPosition().position_x
        place_y = self.playerPosition().position_y
        # First remove the player in old place
        line_player = self.map[place_y]
        line_player.remove(self.GAMER)
        line_player.insert(place_x, ' ')

        # Put the player in the new place
        new_position_line = self.map[place_y - 1]
        # delete the element in this place and return it
        new_position_line.pop(place_x)
        # check if mur ou gardien ou object
        # if not put the player in this place
        new_position_line.insert(place_x, self.GAMER)
        return Player(place_x, place_y-1, self.map)
    
    def moveDown(self):
        place_x = self.playerPosition().position_x
        place_y = self.playerPosition().position_y

        # First remove the player in old place
        line_player = self.map[place_y]
        line_player.remove(self.GAMER)
        line_player.insert(place_x, ' ')

        # Put the player in the new place
        new_position_line = self.map[place_y + 1]
        # delete the element in this place and return it
        new_position_line.pop(place_x)
        # check if mur ou gardien ou object
        # if not put the player in this place
        new_position_line.insert(place_x, self.GAMER)
        return Player(place_x, place_y+1, self.map)
    
    def moveRight(self):
        place_x = self.playerPosition().position_x
        place_y = self.playerPosition().position_y

        # Find the player's line
        line_player = self.map[place_y]

        # check if mur ou gardien ou object
        # new_place_element = line_player[place_x + 1]
        # if new_place_element is gadien or object or mur do someting else

        # Remove Player
        line_player.remove(self.GAMER)
        # if not put the player in this place
        line_player.insert(place_x + 1, self.GAMER)
        return Player(place_x + 1, place_y, self.map)

    def moveLeft(self):
        place_x = self.playerPosition().position_x
        place_y = self.playerPosition().position_y

        # Find the player's line
        line_player = self.map[place_y]

        # check if mur ou gardien ou object
        # new_place_element = line_player[place_x - 1]
        # if new_place_element is gadien or object or mur do someting else

        # Remove Player
        line_player.remove(self.GAMER)
        # if not put the player in this place
        line_player.insert(place_x - 1, self.GAMER)
        return Player(place_x - 1, place_y, self.map)
    
    def movePlayer(self):
        input("Press touch to play ")
        # for event in pygame.event.get():
        #     if event.type == pygame.KEYDOWN:
        #         pygame.quit()
        #         quit()


playe = Player(0, 0, lab.laby.store_lines)
