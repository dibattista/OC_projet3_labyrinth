#! /usr/bin/env pyhton3
# coding: utf-8

import pygame

pygame.init()

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

# iniatilise the game
display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Let same MacGyver')
clock = pygame.time.Clock()

# display image
mac_gyver = pygame.image.load('ressource/MacGyver.png')
def mac(x,y):
    gameDisplay.blit(mac_gyver, (x,y))
x = (display_width * 0)
y = (display_height * 0)

# start the game
crashed = False

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    mac(x,y)
    pygame.display.update()
    clock.tick(60)

# stop the game
pygame.quit()
quit()

# if __name__ == "__main__":

