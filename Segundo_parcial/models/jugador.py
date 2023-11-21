import pygame
from auxiliar.constantes import *
from models.bomba import *

class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)#Pongo al jugador en el centro del suelo
        self.velocidad_x = 0
        self.velocidad_y = 0
        self.gravedad = 1
        self.jump_height = -15
        self.en_suelo = False
        self.bombas = pygame.sprite.Group()
        
    def update(self):
        # Gravedad
        self.velocidad_y += self.gravedad

        # Posición
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y

        if self.rect.y > HEIGHT - 50:
            self.rect.y = HEIGHT - 50
            self.velocidad_y = 0
            self.en_suelo = True
        else:
            self.en_suelo = False

    def mover_izquierda_derecha(self, keys):
        if keys[pygame.K_a]:
            self.velocidad_x = -3
        elif keys[pygame.K_d]:
            self.velocidad_x = 3
        else:
            self.velocidad_x = 0

    def jump(self):
        if self.en_suelo:
            self.velocidad_y = self.jump_height
            
    def lanzar_bomba(self):
        nueva_bomba = Bomba(self.rect.centerx, self.rect.top)
        self.bombas.add(nueva_bomba)

    def dibujar(self, screen):
        self.bombas.draw(screen)
