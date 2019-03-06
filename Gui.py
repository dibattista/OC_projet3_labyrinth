# coding: utf-8
import pygame
from pygame.locals import *
import random

from Player import Player
from Guardian import Guardian
from Object import Object


class Gui:

    def __init__(self, laby):
        self.laby = laby
        player_position = laby.getSymbolPosition(Player.GAMER)
        self.macgyver = Player(player_position[0], player_position[1], [])
        self.guardian = Guardian()

        #############################
        # Init pygame
        pygame.init()
        size = (800, 600)
        self.window = pygame.display.set_mode(size)
        pygame.display.set_caption("My First Game")

        # Guidelines
        pygame.font.init()
        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        textsurface = myfont.render(('Hello ' + 'Player'), False, (255, 255, 255))
        self.window.blit(textsurface, (610, 50))
        # mettre les valeurs du sac

        # Load all images
        self.fond = pygame.image.load("gui/background.png").convert()
        self.wall = pygame.image.load("gui/wall.png").convert_alpha()
        self.ether = pygame.image.load("gui/ether.png").convert_alpha()
        self.needle = pygame.image.load("gui/needle.png").convert_alpha()
        self.pipe = pygame.image.load("gui/pipe.png").convert_alpha()
        self.guard = pygame.image.load("gui/guard.png").convert_alpha()

        self.perso = pygame.image.load("gui/macgyver.png").convert()
        self.position_perso = self.perso.get_rect()

        #####################################
        # Find all the position of the wall
        self.store_wall_position = []
        for box in self.laby.all_box():
            x_wall = box[0] * 40
            y_wall = box[1] * 40
            self.store_wall_position.append((y_wall, x_wall))

        ######################################
        # Write Object
        # find the empty box to find the random positions of graphics objects
        self.store_emptyBox = []
        for box in self.laby.emptyBox():
            x = box[0] * 40
            y = box[1] * 40
            self.store_emptyBox.append((y, x))

        # Store graphic random position
        self.needle_ramdom_position = random.choice(self.store_emptyBox)
        self.store_emptyBox.remove(self.needle_ramdom_position)
        self.ether_ramdom_position = random.choice(self.store_emptyBox)
        self.store_emptyBox.remove(self.ether_ramdom_position)
        self.pipe_ramdom_position = random.choice(self.store_emptyBox)

        self.list_gadget = [(self.needle_ramdom_position, self.needle), (self.ether_ramdom_position, self.ether), (self.pipe_ramdom_position, self.pipe)]

        # Write the position in laby
        self.needle_ramdom_position_laby = (int(self.needle_ramdom_position[0] / 40), int(self.needle_ramdom_position[1] / 40))
        self.laby.write_symbole(self.needle_ramdom_position_laby[0], self.needle_ramdom_position_laby[1], 'N')

        self.ether_ramdom_position_laby = (int(self.ether_ramdom_position[0] / 40), int(self.ether_ramdom_position[1] / 40))
        self.laby.write_symbole(self.ether_ramdom_position_laby[0], self.ether_ramdom_position_laby[1], 'E')

        self.pipe_ramdom_position_laby = (int(self.pipe_ramdom_position[0] / 40), int(self.pipe_ramdom_position[1] / 40))
        self.laby.write_symbole(self.pipe_ramdom_position_laby[0], self.pipe_ramdom_position_laby[1], 'T')

        pygame.display.flip()

    # Player
    def draw_character(self):
        player_position = self.laby.getSymbolPosition(Player.GAMER)
        self.position_perso.x = player_position[0] * 40
        self.position_perso.y = player_position[1] * 40

    # Guard
    def draw_guard(self):
        position_guard = self.laby.getSymbolPosition(Guardian.GARDIAN)
        x_guard = position_guard[1] * 40
        y_guard = position_guard[0] * 40
        self.window.blit(self.guard, (y_guard, x_guard))

    def launch_game(self):
        ###################
        # A Faire:
        # Ecrire les objects dans le laby (comme version terminal) - Fait
        # Recuper la position des object - fait
        # faire le if pour stocket les obejct et les effacer
        # Finir le jeu avec le gardian
        # mettre un autre texte pour dire au jouer le nombre d'objet qu'il a
        # Flake8 corriger les erreurs
        # push sur github
        ###################
        carry_on = 1

        while carry_on:
            pygame.time.Clock().tick(30)

            for event in pygame.event.get():
                if event.type == QUIT:
                    carry_on = 0

                elif event.type == KEYDOWN:
                    old_position = self.macgyver.getPosition()
                    new_position = self.macgyver.movePlayerGui(event.key)
                    check_symbol = self.laby.getSymbol(new_position[0], new_position[1])

                    # If wall
                    if check_symbol == 'X':
                        self.macgyver.moveBack()
                        print('sorry try again')
                        continue

                    # If a player find a object store it and delete
                    elif check_symbol == Object.TUBE or check_symbol == Object.ETHER or check_symbol == Object.NEEDLE:
                        print('new_position', new_position)
                        self.macgyver.addObject(check_symbol)
                        self.laby.write_symbole(
                            new_position[0], new_position[1], Player.GAMER)
                        self.laby.write_symbole(old_position[0], old_position[1], ' ')
                        # Delete object in graphic
                        x = new_position[0] * 40
                        y = new_position[1] * 40
                        position_gadget = (x, y)
                        for gadget in self.list_gadget:
                            if position_gadget == gadget[0]:
                                self.list_gadget.remove(gadget)

                    # If the player find the guardian
                    elif check_symbol == Guardian.GARDIAN:
                        self.guardian.macgyver_vs_guardian(self.macgyver.bag)
                    #image tu as gagner ou perdu

                    else:
                        self.laby.write_symbole(
                            new_position[0], new_position[1], Player.GAMER)
                        self.laby.write_symbole(old_position[0], old_position[1], ' ')

            # Display images
            self.window.blit(self.fond, (0, 0))

            # Wall
            for wall in self.store_wall_position:
                self.window.blit(self.wall, (wall[0], wall[1]))

            # Object
            for gadget in self.list_gadget:
                self.window.blit(gadget[1], (gadget[0][0], gadget[0][1]))

            # Player
            self.draw_character()
            self.window.blit(self.perso, self.position_perso)

            # Guard
            self.draw_guard()

            pygame.display.flip()


