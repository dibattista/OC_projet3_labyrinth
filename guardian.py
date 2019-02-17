class Guardian:
    GARDIAN = 'G'
    def __init__(self):
        self.list_all_objects = ['E', 'T', 'N']

    def sleeping_gardian(self, store_object):
        # savoir si le sac du jouer est plain 3 objects
        result = all(
            elem in store_object for elem in self.list_all_objects)
        if result:
            print('YOU WIN!')
        else:
            print('You are dead')


