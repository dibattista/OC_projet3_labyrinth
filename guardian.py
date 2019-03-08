class Guardian:
    GARDIAN = 'G'

    def __init__(self):
        self.list_all_objects = ['E', 'T', 'N']

    def macgyver_vs_guardian(self, store_object):
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
