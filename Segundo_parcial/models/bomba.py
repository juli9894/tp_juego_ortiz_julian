import pygame
from auxiliar.constantes import *

class Bomba(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(RED)#Por ahora en color
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.tiempo_explosion = 3000 #Tiempo de explosion
        self.tiempo_transcurrido = 0

    def iniciar_temporizador(self):
        pygame.time.set_timer(pygame.USEREVENT, self.tiempo_explosion)

    def explosion(self):
        print("BOOM")
        self.kill()
        pygame.time.set_timer(pygame.USEREVENT, 0)