import pygame  # importation de la librairie pygame
import space
import sys  # pour fermer correctement l'application
import threading # pour générer les nouveaux ennemis toutes les 5 secondes
import os
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
# creation du joueur
player = space.Joueur()
# Affichage d'un texte en hat à gauche de l'écran avec le score du joueur
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()
# creation de la balle
tir = space.Balle(player)
tir.etat = "chargee"
GENERER_ENNEMIS = pygame.USEREVENT + 1
# jouez de la musique
bruitage = pygame.mixer.Sound("musique.mp3")
bruitage.play()
over = pygame.mixer.Sound("Over.mp3")
over.set_volume(0.2)

# creation des ennemis
listeEnnemis = []
for indice in range(space.Ennemi.NbEnnemis):
    vaisseau = space.Ennemi()
    listeEnnemis.append(vaisseau)
# ajout de deux def pour les textes
def game_over_text():
    """Permet d'initialisée la font pour l'evenement Game Over"""
    over_text = over_font.render("GAME OVER", True, (240, 0, 32))
    text_rect = over_text.get_rect(center=(800/2, 400/2))
    screen.blit(over_text, text_rect)
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
### BOUCLE DE JEU  ###
# appel de l'evenement GENERER_ENNEMIS toutes les 5 secondes
running = True  # variable pour laisser la fenêtre ouverte
clock.tick(80)

while running:  # boucle infinie pour laisser la fenêtre ouverte
    # dessin du fond
    screen.blit(fond, (0, 0))
    # affichage du score
    text = font.render(f"Score = {player.score} points", 1, (255, 255, 255))
    textpos = text.get_rect()
    textpos.left = 10
    textpos.top = 10
    screen.blit(text, textpos)
    if player.deplacer() == True:
        game_over_text()
        bruitage.stop()
        over.play()
    ### Gestion des événements  ###
    for event in pygame.event.get():  # parcours de tous les event pygame dans cette fenêtre
        if event.type == pygame.QUIT:  # si l'événement est le clic sur la fermeture de la fenêtre
            running = False  # running est sur False
            sys.exit()  # pour fermer correctement

        # gestion du clavier
        if event.type == pygame.KEYDOWN:  # si une touche a été tapée KEYUP quand on relache la touche
            if event.key == pygame.K_LEFT:  # si la touche est la fleche gauche
                player.sens = "gauche"  # on déplace le vaisseau de 1 pixel sur la gauche
            if event.key == pygame.K_RIGHT:  # si la touche est la fleche droite
                player.sens = "droite"  # on déplace le vaisseau de 1 pixel sur la gauche
            if event.key == pygame.K_SPACE:  # espace pour tirer
                player.tirer()
                tir.etat = "tiree"
    ### Actualisation de la scene ###

    # Gestions des collisions
    for ennemi in listeEnnemis:
        if tir.toucher(ennemi):
            ennemi.disparaitre()
            player.marquer()
        # si l'ennemi touche le joueur on perd 10 sur la variable player.score
        if ennemi.touchPlayer(player):
            ennemi.disparaitre()

    # placement des objets
    # le joueur
    player.deplacer()
    screen.blit(tir.image, [tir.depart, tir.hauteur])  # appel de la fonction qui dessine le vaisseau du joueur
    # la balle
    tir.bouger()
    screen.blit(player.image, [player.position, 500])  # appel de la fonction qui dessine le vaisseau du joueur
    # les ennemis
    for ennemi in listeEnnemis:
        ennemi.avancer()
        screen.blit(ennemi.image,
                    [ennemi.depart, ennemi.hauteur])  # appel de la fonction qui dessine le vaisseau du joueur
        if ennemi.hauteur > 600:
            ennemi.disparaitre()
            ennemi.avancer()
    


    pygame.display.update()  # pour ajouter tout changement à l'écran


