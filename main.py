#! /usr/bin/env pyhton3
# coding: utf-8
import pygame
from pygame.locals import *

from Labyrinth import Labyrinth
import Player as macgyver
from GameManager import GameManager

pygame.init()

#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((640, 480))

#Chargement et collage du fond
fond = pygame.image.load("background.jpg").convert()
fenetre.blit(fond, (0, 0))

#Rafraîchissement de l'écran
pygame.display.flip()

#BOUCLE INFINIE
continuer = 1
while continuer:
	continuer = int(input())


# if __name__ == "__main__":
#     pass
    # laby = Labyrinth('labyrinth.txt')
    # gamer = GameManager(laby)
    # gamer.lauch_game()
