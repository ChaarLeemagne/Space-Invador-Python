import pygame  # importation de la librairie pygame
import space
import sys  # pour fermer correctement l'application
import threading # pour générer les nouveaux ennemis toutes les 5 secondes
import os
# import de la bibliothèque random pour les nombres aleatoires
import random
# lancement des modules inclus dans pygame
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
fond2 = pygame.image.load('background2.png')
fond2 = pygame.transform.scale(fond2, (800, 600))

# Affichage d'un texte en hat à gauche de l'écran avec le score du joueur
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()

# jouez de la musique
bruitage = pygame.mixer.Sound("musique.mp3")
ascenseur = pygame.mixer.Sound("ascenseur.mp3")
over = pygame.mixer.Sound("Over.mp3")
over.set_volume(0.2)

# creation des ennemis
listeEnnemis = []
listeBalles= []
for indice in range(space.Ennemi.NbEnnemis):
    vaisseau = space.Ennemi()
    listeEnnemis.append(vaisseau)
# creation du joueur
player = space.Joueur(vaisseau)
for i in range(2) :
    if i == 0 : 
        tir2 = space.Balle(player)
        tir2.etat = "chargee"
        listeBalles.append(tir2)
        print(tir2)
        
    if i == 1:
        tir3 = space.Balle(player)
        tir3.etat = "chargee"
        listeBalles.append(tir3)

GENERER_ENNEMIS = pygame.USEREVENT + 1
# ajout de deux def pour les textes
def game_over_text():
    """Permet d'initialisée la font pour l'evenement Game Over"""
    over_text = over_font.render("GAME OVER", 1, (240, 0, 32))
    text_rect = over_text.get_rect(center=(800/2, 400/2))
    screen.blit(over_text, text_rect)
    over_text2 = font.render("Press Space For Restart", 1, (255, 255, 255))
    text_rect2 = over_text.get_rect(center=(250, 300))
    screen.blit(over_text2, text_rect2)
def resource_path(relative_path):
    """Permet de rechercher une ressource en renvoyant (base_path, relative_path) on l'utilisera pour crée des font
depuis des fichiers externes"""
    try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
# Importation d'un font

asset_font = resource_path('.\RAVIE.ttf')
font = pygame.font.Font(asset_font,40)
asset_over_font = resource_path('.\comicbd.ttf')
over_font = pygame.font.Font(asset_over_font,60)
#image coeur
coeur = pygame.image.load('coeur.png')
coeur = pygame.transform.scale(coeur, (40, 45))
### BOUCLE DE JEU  ###
# appel de l'evenement GENERER_ENNEMIS toutes les 5 secondes
running = False  # variable pour laisser la fenêtre ouverte
verif = True
a = True
clock.tick(90)
while a :
    screen.blit(fond2, (0, 0))
    ascenseur.play()
    ascenseur.set_volume(0.2)
    for event in pygame.event.get():# parcours de tous les event pygame dans cette fenêtre
        if event.type == pygame.QUIT:  # si l'événement est le clic sur la fermeture de la fenêtre
            running = False  # running est sur False
            sys.exit()  # pour fermer correctement
        if event.type == pygame.KEYDOWN:  # si une touche a été tapée KEYUP quand on relache la touche
            if event.key == pygame.K_SPACE:
                a= False# si la touche est la barre espace
                running= True
                ascenseur.stop()
                bruitage.play()
    pygame.display.update()
while running:  # boucle infinie pour laisser la fenêtre ouverte
    # dessin du fond
    screen.blit(fond, (0, 0))
    # affichage du score
    text = font.render(f"Score = {player.score} points", 1, (255, 255, 255))
    textpos = text.get_rect()
    textpos.left = 10
    textpos.top = 10
    screen.blit(text, textpos)
    text2 = font.render(f"{player.Vlives}", 1, (255, 255, 255))
    screen.blit(text2, [640, 10])
    screen.blit(coeur, (700, 10))
    """if player.score == 2 :
        for tir in listeBalles : 
            space.EasterEgg.sprite1(player, tir)"""

    if player.deplacer() == True or player.score < -100:
            game_over_text()
            bruitage.stop()
            over.play()
            listeEnnemis = [] #on réecrit la list pour faire depop les ennemis
            
    ### Gestion des événements  ###
    for event in pygame.event.get(): # parcours de tous les event pygame dans cette fenêtre
        if event.type == pygame.QUIT:  # si l'événement est le clic sur la fermeture de la fenêtre
            running = False  # running est sur False
            sys.exit()  # pour fermer correctement
        if player.deplacer() == True or player.score < -10:
            if event.type == pygame.KEYDOWN:  # si une touche a été tapée KEYUP quand on relache la touche
                if event.key == pygame.K_SPACE:  # si la touche est la barre espace
                    player.Vlives = 5 # on redonne 5 lives 
                    verif= False
                    player.score = 0
                    over.stop()
                    bruitage.play()
                    for indice in range(space.Ennemi.NbEnnemis): # on recrée les ennemis
                        vaisseau = space.Ennemi()
                        listeEnnemis.append(vaisseau)
        # gestion du clavier
        if event.type == pygame.KEYDOWN:  # si une touche a été tapée KEYUP quand on relache la touche
            if event.key == pygame.K_LEFT:  # si la touche est la fleche gauche
                player.sens = "gauche"  # on déplace le vaisseau de 1 pixel sur la gauche
            if event.key == pygame.K_RIGHT:  # si la touche est la fleche droite
                player.sens = "droite"  # on déplace le vaisseau de 1 pixel sur la gauche
            if event.key == pygame.K_SPACE :
                player.tirer()
                tir2.etat = "tiree"
            if event.key == pygame.K_UP :
                player.tirer()
                tir3.etat = "tiree"
    ### Actualisation de la scene ###

    # Gestions des collisions
    for ennemi in listeEnnemis:
        for tir in listeBalles:
            if tir == tir2 :
                a = "2"
                if tir.toucher(ennemi,player,a):
                    ennemi.disparaitre()
                    player.marquer()
            if tir == tir3 :
                a= "3"
                if tir.toucher(ennemi,player,a):
                    ennemi.disparaitre()
                    player.marquer()
            # si l'ennemi touche le joueur on perd 10 sur la variable player.score
        if ennemi.touchPlayer(player):
            ennemi.disparaitre()
    
    # placement des objets
    # le joueur
    player.deplacer()
    screen.blit(player.image, [player.position, 500])  # appel de la fonction qui dessine le vaisseau du joueur
    for tir in listeBalles :
        if tir == tir2 :
            tir.bouger()
            screen.blit(tir.image,[tir.depart, tir.hauteur])
        if tir == tir3 :
            tir.bouger()
            screen.blit(tir.image,[tir.depart-45, tir.hauteur])

    # les ennemis
    for ennemi in listeEnnemis:
        ennemi.avancer()
        screen.blit(ennemi.image,
                    [ennemi.depart, ennemi.hauteur])  # appel de la fonction qui dessine le vaisseau du joueur
        if ennemi.hauteur > 600:
            ennemi.disparaitre()
            ennemi.avancer()
    

    pygame.display.update()  # pour ajouter tout changement à l'écran


