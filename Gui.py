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
        player_position = laby.get_symbol_position(Player.GAMER)
        self.macgyver = Player(player_position[0], player_position[1])
        self.guardian = Guardian()
        self.object = Object(laby)

        #############################
        # Init pygame
        pygame.init()
        pygame.font.init()
        size = (900, 600)
        # Font
        self.font_text_winner = pygame.font.SysFont('Arial', 25)
        self.font_menu = pygame.font.SysFont('Arial', 15)

        self.window = pygame.display.set_mode(size)
        pygame.display.set_caption("My First Game")

        #############################
        # Load all images
        self.fond = pygame.image.load("gui/background.png").convert()
        self.wall = pygame.image.load("gui/wall.png").convert_alpha()
        self.ether = pygame.image.load("gui/ether.png").convert_alpha()
        self.needle = pygame.image.load("gui/needle.png").convert_alpha()
        self.pipe = pygame.image.load("gui/pipe.png").convert_alpha()
        self.guard = pygame.image.load("gui/guard.png").convert_alpha()
        # character setup
        self.character = pygame.image.load("gui/macgyver.png").convert()
        self.position_character = self.character.get_rect()
        self.mac_bag = 0

        #####################################
        # Find all the position of the wall
        self.store_wall_position = []
        for box in self.laby.all_box():
            x_wall = box[0] * 40
            y_wall = box[1] * 40
            self.store_wall_position.append((y_wall, x_wall))

        ######################################
        # Find random position object in graphic and write in laby
        self.list_gadget = [
            (self.object.needle_ramdom_position, self.needle),
            (self.object.ether_ramdom_position, self.ether),
            (self.object.pipe_ramdom_position, self.pipe)
        ]
        self.object.write_object_in_laby()

        pygame.display.flip()

    # Player
    def draw_character(self):
        player_position = self.laby.get_symbol_position(Player.GAMER)
        self.position_character.x = player_position[0] * 40
        self.position_character.y = player_position[1] * 40

    # Guard
    def draw_guard(self):
        position_guard = self.laby.get_symbol_position(Guardian.GARDIAN)
        x_guard = position_guard[1] * 40
        y_guard = position_guard[0] * 40
        self.window.blit(self.guard, (y_guard, x_guard))

    def popup_message(self, text):
        pygame.draw.rect(self.window, (0, 0, 0), (180, 200, 400, 200))
        self.window.blit(self.font_text_winner.render(
            text, True, (255, 255, 255)), (280, 280))
        pygame.display.update()

    def draw_menu(self):
        # Menu
        # draw rectangle to delete old value of self.mac_bag)
        pygame.draw.rect(self.window, (0, 0, 0), (620, 40, 260, 300))

        text_menu = self.font_menu.render(
            'Ready to help Mac?', True, (255, 255, 255))
        tex_movement = self.font_menu.render(
            'To move, use the keyboard arrow keys.', True, (255, 255, 255))
        text_bag_one = self.font_menu.render(
            'You need to find 3 gadgets in the', True, (255, 255, 255))
        text_bag_two = self.font_menu.render(
            'labyrinth to asleep the guardian and win.', True, (255, 255, 255))

        self.window.blit(text_menu, (620, 50))
        self.window.blit(tex_movement, (620, 100))
        self.window.blit(text_bag_one, (620, 140))
        self.window.blit(text_bag_two, (620, 160))

        # Update the number of gadget
        text_bag_three = self.font_menu.render(
            'You have: ' + str(self.mac_bag) + ' gadget.',
            True, (255, 255, 255))
        self.window.blit(text_bag_three, (620, 180))
        pygame.display.update()

    def launch_game(self):
        carry_on = 1
        finish_game = 0

        while carry_on:
            pygame.time.Clock().tick(30)

            for event in pygame.event.get():
                if event.type == QUIT:
                    carry_on = 0

                elif event.type == KEYDOWN:
                    old_position = self.macgyver.get_position()
                    new_position = self.macgyver.move_player_gui(event.key)
                    check_symbol = self.laby.get_symbol(
                        new_position[0], new_position[1])

                    # If wall
                    if check_symbol == 'X':
                        self.macgyver.move_back()
                        print('sorry try again')
                        continue

                    # If a player find a object store it and delete
                    elif check_symbol == Object.TUBE \
                            or check_symbol == Object.ETHER \
                            or check_symbol == Object.NEEDLE:
                        self.macgyver.add_object(check_symbol)
                        self.mac_bag = len(self.macgyver.bag)

                        self.laby.write_symbol(
                            new_position[0], new_position[1], Player.GAMER)
                        self.laby.write_symbol(
                            old_position[0], old_position[1], ' ')
                        # Delete object in graphic
                        x = new_position[0] * 40
                        y = new_position[1] * 40
                        position_gadget = (x, y)
                        for gadget in self.list_gadget:
                            if position_gadget == gadget[0]:
                                self.list_gadget.remove(gadget)

                    # If the player find the guardian
                    elif check_symbol == Guardian.GARDIAN:
                        finish_game = 1
                        result = self.guardian.macgyver_vs_guardian(
                            self.macgyver.bag)
                        msg = result

                    else:
                        self.laby.write_symbol(
                            new_position[0], new_position[1], Player.GAMER)
                        self.laby.write_symbol(
                            old_position[0], old_position[1], ' ')

            # Display images

            self.window.blit(self.fond, (0, 0))
            self.draw_menu()

            # Wall
            for wall in self.store_wall_position:
                self.window.blit(self.wall, (wall[0], wall[1]))

            # Object
            for gadget in self.list_gadget:
                self.window.blit(gadget[1], (gadget[0][0], gadget[0][1]))

            # Player
            self.draw_character()
            self.window.blit(self.character, self.position_character)

            # Guard
            self.draw_guard()
            if finish_game == 1:
                self.popup_message(msg)

            pygame.display.flip()
