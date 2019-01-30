import Labyrinth as lab

class Macgyver:
    line = 0
    column = 0

    def __init__(self, labyrinth):
        self.labyrinth = labyrinth

    def find_player(self):
        search = 'M'
        coordinates = []

        for player in self.labyrinth:
            for y in player:
                if y == search:
                    self.line = self.labyrinth.index(player)
                    column = player.index(y)
        coordinates = [self.line, column]
        print('The player is in: ', coordinates)
        return coordinates
    
    def moveUp(self):
        pass
    
    def moveRight(self, num_right):
        self.num_right = num_right
        player_number_column = self.find_player()[1]
        player_number_line = self.find_player()[0]

        line_player = self.labyrinth[player_number_line]
        print('before move line_player', line_player)
        line_player.remove('M')
        line_player.insert(player_number_column + self.num_right, 'M')
        print('after move line_player', line_player)
        # comment le sauvegarder ?


            
    def moveDown(self):
        pass
    
    def moveLeft(self):
        pass
    
    def move(self):
        pass





player = Macgyver(lab.laby.launch_labyrinth())
# mac_gyver = pygame.image.load('ressource/MacGyver.png')
# Creer une classe Player/MacGyver stockant les coordonées du joueur.

    # class Mac_gyver: attribut pour savoir ou tu es, les coordonés y et x
    #   et les méthod pour bouger
