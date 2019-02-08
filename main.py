#! /usr/bin/env pyhton3
# coding: utf-8
from Labyrinth import Labyrinth
import Player as macgyver
from GameManager import GameManager
# Afficher le labyrinth
# Create class to move Macgyver
# create method to find the place of object
# create method to store the object Macgyver find
# create a if Macgyver has all Object
#   and if he is on place where the Guardian are
#   message winning
# if else Macgyver doesn't has all 3 objects and he is on the
#   place where the Guardian are
#   message lose
# if the game was close change the position of object

if __name__ == "__main__":
    laby = Labyrinth('labyrinth.txt')
    gamer = GameManager(laby)
    gamer.lauch_game()
    # macgyver.playe.moveUp()
    # # macgyver.playe.moveDown()
    # macgyver.playe.moveRight()
    # # macgyver.playe.moveLeft()
    # # macgyver.playe.movePlayer()
    # macgyver.playe.playerPosition()

    # nouvelle instance de labyrinth
    # class GameManager avec les régles de jeu
    # lui mettre instance de labyrinth
    # class Mac_gyver: attribut pour savoir ou tu es, les coordonés y et x
    #   et les méthod pour bouger
    # GameManager game faire une boucle des actions lui demander de faire une action et répondre à l'action
