import pygame  # necessaire pour charger les images et les sons

pygame.init()
# création d'une fenêtre de 800 par 600
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invaders")
# Création d'un icon
programIcon = pygame.image.load('icon.png')
pygame.display.set_icon(programIcon)
# chargement de l'image de fond
fond = pygame.image.load('background.png')
fond = pygame.transform.scale(fond, (800, 600))


running = True  # variable pour laisser la fenêtre ouverte


while running:
    pygame.display.update()