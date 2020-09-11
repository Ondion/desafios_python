import pygame
from pygame.locals import *
from sys import exit

pygame.init()

screen = pygame.display.set_mode((720, 640))
pygame.display.set_caption('funcionando!')
pygame.draw.rect(screen, (255,0,0), [360,320,100,100])

while True:
    pygame.draw.rect(screen, (255, 0, 0), [360, 320, 100, 100])
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()