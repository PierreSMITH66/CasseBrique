import core
import pygame
from pygame.math import Vector2

class Ball :
    def __init__(self, largeur=200, hauteur=10):
        self.score = 0
        self.couleur = (255, 0, 0)
        self.vitesse = Vector2(0, 0)
        self.origine = Vector2(largeur, hauteur)
        self.force = Vector2(0, 0)
        self.vitesseMAX = 100
        self.rect = (int(self.position.x), int(self.position.y), 50, 20)

    def show(self,screen):
        pygame.draw.rect(screen, self.couleur, self.rect, 0, 2)
