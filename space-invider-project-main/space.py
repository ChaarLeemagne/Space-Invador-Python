import pygame  # necessaire pour charger les images et les sons
# import de la bibliothèque random pour les nombres aleatoires
import random
# import de la bibliothèque math pour les fonctions mathematiques
import math

        
class Joueur:  # classe pour créer le vaisseau du joueur
    def __init__(self):
        """
        Constructeur de la classe Joueur
        :return:
        """
        self.position = 400
        self.hauteur = 0
        self.depart = self.position
        self.image = pygame.image.load('vaisseau.png')
        self.image = pygame.transform.scale(self.image, (80, 90))
        self.sens = "O"
        self.vitesse = 5
        self.score = 0


    def deplacer(self):
        """
        Fonction qui permet de déplacer le vaisseau du joueur
        :return:
        """
        if (self.sens == "droite") and (self.position < 740):
            self.position = self.position + self.vitesse
            self.depart = self.position
        elif (self.sens == "gauche") and (self.position > 0):
            self.position = self.position - self.vitesse
            self.depart = self.position

    def tirer(self):
        """
        Fonction qui permet de tirer
        :return:
        """
        self.sens = "O"

    def marquer(self):
        """
        Fonction qui permet de marquer un point
        :return:
        """
        self.score = self.score + 2

    def demarquer(self):
        """
        Fonction qui permet de démarquer un point
        :return:
        """
        self.score = self.score - 5


class Balle:  # classe pour créer la balle
    def __init__(self, player):
        """
        Constructeur de la classe Balle
        :param player:
        """
        self.tireur = player
        self.depart = player.position + 16
        self.hauteur = 492
        self.image = pygame.image.load('balle.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.etat = "chargee"
        self.vitesse = 7

    def bouger(self):
        """
        Fonction pour faire bouger la balle
        :return:
        """
        if self.etat == "chargee":
            self.depart = self.tireur.position + 16
            self.hauteur = 492
        elif self.etat == "tiree":
            self.hauteur = self.hauteur - self.vitesse
        if self.hauteur < 0:
            self.etat = "chargee"
        

    def toucher(self, vaisseau):
        """
        Fonction qui permet de savoir si la balle touche un ennemi
        :param vaisseau : vaisseau ennemi
        :return: True si la balle touche l'ennemi sinon False
        """
        """
        Ne pas faire ça car pas le bonne ordre
        if (math.fabs(self.depart - vaisseau.hauteur) < 40) and (math.fabs(self.depart - vaisseau.depart) < 40):
            return True
        """
        if (math.fabs(self.depart - vaisseau.depart) < 40) and (math.fabs(self.hauteur - vaisseau.hauteur) < 40):
            bruitage2 = pygame.mixer.Sound("explosion.wav")
            bruitage2.play()
            bruitage2.set_volume(0.1)
            return True

class Ennemi:
    NbEnnemis = random.randint(1, 4)

    def __init__(self):
        """
        Constructeur de la classe Ennemi
        """
        self.depart = random.randint(1, 700)
        self.hauteur = 10
        self.type = random.randint(1, 2)
        if self.type == 1:
            self.image = pygame.image.load('invader1.png')
            self.image = pygame.transform.scale(self.image, (80, 90))
            self.vitesse = 1
        elif self.type == 2:
            self.image = pygame.image.load('invader2.png')
            self.image = pygame.transform.scale(self.image, (80, 90))
            self.vitesse = 2

    def avancer(self):
        """
        Avance l'ennemi d'une distance égale à sa vitesse
        :return:
        """
        self.hauteur = self.hauteur + self.vitesse

    def disparaitre(self):
        """
        Fait disparaitre l'ennemi
        :return:
        """
        self.depart = random.randint(1, 700)
        self.hauteur = 10
        self.type = random.randint(1, 2)
        if self.type == 1:
            self.image = pygame.image.load('invader1.png')
            self.image = pygame.transform.scale(self.image, (80, 90))
            self.vitesse = 1
        elif self.type == 2:
            self.image = pygame.image.load('invader2.png')
            self.image = pygame.transform.scale(self.image, (80, 90))
            self.vitesse = 2

    def touchPlayer(self, player):
        """
        Fonction qui permet d'appeler demarquer si l'ennemie touche le joueur ou alors passe en dessous de la fenêtre
        :param player:
        :return:
        """
        if self.hauteur >= 600 :
            player.demarquer()

    