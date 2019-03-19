# coding=utf-8

"""This module is the class Player"""

from pygame.locals import K_UP, K_RIGHT, K_LEFT, K_DOWN


class Player:
    """
        This is a class about the player.
        instance attributes:
            x (int): the position x of the player in the labyrinth
            y (int): the position y of the player in the labyrinth
        class attribute:
            GAMER: (str) define the player in the labyrinth
    """
    GAMER = 'M'

    def __init__(self, x, y):
        self.position_x = x
        self.position_y = y
        self.bag = []
        # x vertical
        # y horizontal
        self.old_x = self.position_x
        self.old_y = self.position_y

        """
              The constructor for Player class.
                Parameters:
                self.position_x (int): the position x of
                    the player in the labyrinth
                self.position_y (int): the position y of
                    the player in the labyrinth
                self.bag (list): list will contain
                    the objects catch by the player
                self.old_x (int): the old position x
                    of the player in the labyrinth
                self.old_y (int): the old position y
                    of the player in the labyrinth
        """

    def move_up(self):
        """
               The method to move up the player.
               Returns:
                   new position x and y,
                      after go up one the box in the labyrinth.
        """
        self.position_y -= 1
        return self.position_x, self.position_y

    def move_down(self):
        """
                 The method to move down the player.
                 Returns:
                     new position x and y,
                        after go down one the box in the labyrinth.
        """
        self.position_y += 1
        return self.position_x, self.position_y

    def move_right(self):
        """
                 The method to move right the player.
                 Returns:
                     new position x and y,
                        after go right one the box in the labyrinth.
        """
        self.position_x += 1
        return self.position_x, self.position_y

    def move_left(self):
        """
                 The method to move left the player.
                 Returns:
                     new position x and y,
                        after go left one the box in the labyrinth.
        """
        self.position_x -= 1
        return self.position_x, self.position_y

    def get_position(self):
        """
                 The method to get the player's position.
                 Returns:
                     position x and y.
        """
        return self.position_x, self.position_y

    def add_object(self, tool):
        """
                The method add a object to the list bag.
                Returns:
                     The list bag.
        """
        self.bag.append(tool)
        return self.bag

    def move_back(self):
        """
                 The method to go back to the player in old position.
                 Returns:
                     olf position x and old position y.
        """
        self.position_x = self.old_x
        self.position_y = self.old_y

    def move_player(self):
        """
            The method continue the algorithm util while is true.
            before the algorithm, store the old position of the player
            Algorithm:
                Ask the player where he wants to move
                first condition if the player tape 'r'
                    return the new position to move right
                second condition if the player tape 'l'
                    return the new position to move left
                third condition if the player tape 'u'
                    return the new position to move up
                fourth condition if the player tape 'd'
                    return the new position to move down
                for all the other conditions move
                    tell the player to try one of the required key
        """
        self.old_x = self.position_x
        self.old_y = self.position_y

        while True:
            player_move = input("Press touch to play r for right,"
                                "   l for left, u for up, d for down")
            if player_move == 'r':
                return self.move_right()
            elif player_move == 'l':
                return self.move_left()
            elif player_move == 'u':
                return self.move_up()
            elif player_move == 'd':
                return self.move_down()
            else:
                print('Wrong key try r for right,'
                      'l for left,u for up, d for down')

    def move_player_gui(self, key):
        """
            The method continue the algorithm util while is true.
            before the algorithm, store the old position of the player
            Algorithm:
                first condition if the key press
                    is up return the new position to move up
                second condition if the key press
                    is right return the new position to move right
                third condition if the key press
                    is left return the new position to move left
                fourth condition if the key press
                    is down return the new position to move down
        """
        self.old_x = self.position_x
        self.old_y = self.position_y

        if key == K_UP:
            return self.move_up()
        elif key == K_RIGHT:
            return self.move_right()
        elif key == K_LEFT:
            return self.move_left()
        elif key == K_DOWN:
            return self.move_down()
