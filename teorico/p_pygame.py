import pygame
from pygame.locals import *
from sys import exit

pygame.init()

screen = pygame.display.set_mode((720, 640))
pygame.display.set_caption('funcionando!')

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
                