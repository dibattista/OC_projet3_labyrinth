import pygame


class Guardian:
    GARDIAN = 'G'

    def __init__(self):
        self.list_all_objects = ['E', 'T', 'N']

    def sleeping_guardian(self, store_object):
        result = all(
            elem in store_object for elem in self.list_all_objects)
        if result:
            print('YOU WIN!')
        else:
            print('You are dead')

    def message_display(text):
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects(text, largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)

    def macgyver_vs_guardian(self, store_object):
        result = all(
            elem in store_object for elem in self.list_all_objects)
        if result:
            print('YOU WIN!')
        else:
            print('You are dead')


