# coding: utf-8

"""This module is the class Gui"""

import pygame
from pygame.locals import QUIT, KEYDOWN

from Player import Player
from Guardian import Guardian
from Object import Object


class Gui:
    """
        This is a class for launch a loop to playing the game in graphic mode.
        Attributes:
            laby (class): Allow to access of the class Labyrinth
            The class Labyrinth build the Labyrinth of the game.
    """

    def __init__(self, laby):
        self.laby = laby
        player_position = laby.get_symbol_position(Player.GAMER)
        self.macgyver = Player(player_position[0], player_position[1])
        self.guardian = Guardian()
        self.object = Object(laby)
        self.mac_bag = 0
        """
              The constructor for Gui class.
                Parameters:
                laby (class): Access of the class Labyrinth.
                player_position(tuple): return the vertical and horizontal position of the player.
                macgyver(class): Access of the class Player.
                guardian(class): Access of the class Guardian.
                object(class): Access of the class Object.
                self.mac_bag(int): The number of object catch by the player.
        """
        pygame.init()
        pygame.font.init()
        size = (900, 600)
        self.clock = pygame.time.Clock().tick(30)
        # Font
        self.font_text_winner = pygame.font.SysFont('Arial', 25)
        self.font_menu = pygame.font.SysFont('Arial', 15)

        self.window = pygame.display.set_mode(size)
        pygame.display.set_caption("Mac vs guardian")
        """
              Init pygame.
                Parameters:
                size (class): Access of the class Labyrinth.
                self.font_text_winner(pygame.font.Font): return the font of the message at the end of the game.
                self.font_menu(pygame.font.Font): return the font of the menu.
                self.window(pygame.Surface): Set the window of the game.
        """

        self.fond = pygame.image.load("gui/background.png").convert()
        self.wall = pygame.image.load("gui/wall.png").convert_alpha()
        self.ether = pygame.image.load("gui/ether.png").convert_alpha()
        self.needle = pygame.image.load("gui/needle.png").convert_alpha()
        self.pipe = pygame.image.load("gui/pipe.png").convert_alpha()
        self.guard = pygame.image.load("gui/guard.png").convert_alpha()
        # character setup
        self.character = pygame.image.load("gui/macgyver.png").convert()
        self.position_character = self.character.get_rect()
        """
              Load image.
                Parameters:
                self.fond: Load an image from background.png file.
                self.wall: Load an image from wall.png file.
                self.ether: Load an image from ether.png file.
                self.needle: Load an image from needle.png file.
                self.pipe: Load an image from pipe.png file.
                self.guard: Load an image from guard.png file.
                self.character: Load an image from macgyver.png file.
                self.position_character: Returns a new rectangle covering the entire surface.
                
        """

        self.store_wall_position = []
        for box in self.laby.all_box():
            x_wall = box[0] * 40
            y_wall = box[1] * 40
            self.store_wall_position.append((y_wall, x_wall))
        """Find the position for all walls in graphic mode."""

        self.list_gadget = [
            (self.object.needle_random_position, self.needle),
            (self.object.ether_random_position, self.ether),
            (self.object.pipe_random_position, self.pipe)
        ]
        """Find random position for the objects in graphic mode."""
        self.object.write_object_in_laby()
        """Write the objects in labyrinth with this position."""

    def draw_character(self):
        """
               The method get the player position in the labyrinth.
               Returns:
                   new position x and y in graphic mode.
        """
        player_position = self.laby.get_symbol_position(Player.GAMER)
        self.position_character.x = player_position[0] * 40
        self.position_character.y = player_position[1] * 40

    def draw_guard(self):
        """
               The method get the guardian position in the labyrinth.
               Returns:
                   new position x and y in graphic mode and add to the window.
        """
        position_guard = self.laby.get_symbol_position(Guardian.GUARDIAN)
        x_guard = position_guard[1] * 40
        y_guard = position_guard[0] * 40
        self.window.blit(self.guard, (y_guard, x_guard))

    def popup_message(self, text):
        """
               The method draw a rectangle with a text pass in argument.
               Returns:
                   add to the window.
        """
        pygame.draw.rect(self.window, (0, 0, 0), (180, 200, 400, 200))
        self.window.blit(self.font_text_winner.render(
            text, True, (255, 255, 255)), (280, 280))
        pygame.display.update()

    def draw_menu(self):
        """
               The method draw a menu of the game:
               First draw a rectangle to delete all value of the player's bag.
               Second draw a rectangle with five line of text.
               Third in last line update the bag of the player.
               Returns:
                   add to the window.
        """
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

        text_bag_three = self.font_menu.render(
            'You have: ' + str(self.mac_bag) + ' gadget.',
            True, (255, 255, 255))
        self.window.blit(text_bag_three, (620, 180))
        pygame.display.update()

    def launch_game(self):
        """
             The method continue the algorithm util carry_on is true.
             Algorithm:
                 Create clocks that can manage FPS, frame per second.
                 Loop all event the player will do in the keyboard
                 if  the player click on the red cross the window will close.
                 si other event on the keyboard:
                    store the old position of the player
                    store the new position of the player
                    find the symbol in the new position player
                    first condition if the symbol equal wall stop the player
                        and move the player in the old position in the labyrinth
                    second condition if the symbol equal one of the objects,
                        add object in the player's bag
                        and replace the object by the player in the labyrinth
                        find the position in graphic mode and delete the object.
                    third condition if the symbol equal the guardian finish
                        the game with the guardian method and display the message in the rectangle.
                    for all the other conditions move the player in this new place
                 Display images:
                    First the window of the game.
                    Second the menu.
                    Third the wall.
                    Fourth the object.
                    Fifth the player.
                    Sixth the guard.
         """
        carry_on = 1
        finish_game = 0

        while carry_on:
            for event in pygame.event.get():
                if event.type == QUIT:
                    carry_on = 0

                elif event.type == KEYDOWN:
                    old_position = self.macgyver.get_position()
                    new_position = self.macgyver.move_player_gui(event.key)
                    check_symbol = self.laby.get_symbol(
                        new_position[0], new_position[1])

                    if new_position == None:
                        continue
                    if check_symbol == self.laby.WALL:
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

                    elif check_symbol == Guardian.GUARDIAN:
                        finish_game = 1
                        result = self.guardian.macgyver_vs_guardian(
                            self.macgyver.bag)
                        msg = result

                    else:
                        self.laby.write_symbol(
                            new_position[0], new_position[1], Player.GAMER)
                        self.laby.write_symbol(
                            old_position[0], old_position[1], ' ')


            self.window.blit(self.fond, (0, 0))
            self.draw_menu()

            for wall in self.store_wall_position:
                self.window.blit(self.wall, (wall[0], wall[1]))

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
            self.clock



