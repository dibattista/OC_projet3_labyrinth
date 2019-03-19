"""This module is the class Guardian"""


class Guardian:
    """
        This is a class about the guardian.
        class attribute:
            GUARDIAN: (str) define the guardian in the labyrinth
    """
    GUARDIAN = 'G'

    def __init__(self):
        self.list_all_objects = ['E', 'T', 'N']

        """
                The constructor for Guardian class.
                  Parameters:
                  self.list_all_objects (list): The list of object.
        """

    def macgyver_vs_guardian(self, store_object):
        """
            The method check if the bag of the player contain all objects.
            With the method 'all' of python.
            Returns:
                A string if the case is True
                    or a other string for others cases.

        """
        winner_msg = '    YOU WIN!'
        lose_msg = 'YOU ARE DEAD!'
        result = all(
            elem in store_object for elem in self.list_all_objects)
        if result:
            print(winner_msg)
            return winner_msg
        else:
            print(lose_msg)
            return lose_msg
