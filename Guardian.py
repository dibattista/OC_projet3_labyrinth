"""This module is the class Guardian"""


class Guardian:
    """
        This is a class about the guardian.
        class attribute:
            GUARDIAN: (str) define the guardian in the labyrinth
    """
    GUARDIAN = 'G'

    def __init__(self):
        self.list_all_tools = ['E', 'T', 'N']

        """
                The constructor for Guardian class.
                  Parameters:
                  self.list_all_tools (list): The list of Tool.
        """

    def macgyver_vs_guardian(self, store_tool):
        """
            The method check if the bag of the player contain all tools.
            With the method 'all' of python.
            Returns:
                A string if the case is True
                    or a other string for others cases.

        """
        winner_msg = '    YOU WIN!'
        lose_msg = 'YOU ARE DEAD!'
        result = all(
            elem in store_tool for elem in self.list_all_tools)
        if result:
            print(winner_msg)
            return winner_msg
        else:
            print(lose_msg)
            return lose_msg
