# coding=utf-8
# je pars toujours de mon point de départ 
# comment partir de ma dernière commande?


class Player:
    GAMER = 'M'
    def __init__(self, x, y):
        self.position_x = x
        print('in class Player possition_x', self.position_x)
        self.position_y = y
        print('in class Player position_y', self.position_y)

        # x vertical
        # y horizontal

    def moveUp(self):
        self.position_y -= 1
        return self.position_x, self.position_y
    
    def moveDown(self):
        self.position_y += 1
        return self.position_x, self.position_y

    def moveRight(self):
        self.position_x += 1
        return self.position_x, self.position_y

    def moveLeft(self):
        self.position_x -= 1
        return self.position_x, self.position_y
    
    def movePlayer(self):
        player_move = input("Press touch to play ")
        # ici les positions
        if player_move == 'r':
            return self.moveRight()
        elif player_move == 'l':
            return self.moveLeft()
        elif player_move == 'u': 
            return self.moveUp()
        elif player_move == 'd':
            return self.moveDown()
        


playe = Player(0, 0)
