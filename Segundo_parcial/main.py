import pygame
import sys
from auxiliar.constantes import *
from models.plataformas import *
from models.jugador import *
from models.bomba import *

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bombita")

# Fondo
background = pygame.image.load(r"C:\Users\eze98\OneDrive\Escritorio\Nueva carpeta\Progra\Segundo_parcial\assets\img\fondo juego.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Plataformas
plataformas = pygame.sprite.Group()
plataformas.add(Plataforma(0, 550, 800, 20))  # Plataforma principal
plataformas.add(Plataforma(0, 450, 150, 20))
plataformas.add(Plataforma(100, 350, 200, 20))
plataformas.add(Plataforma(150, 300, 100, 20))
plataformas.add(Plataforma(200, 400, 100, 20))

# Jugador
jugador = Jugador()
lista_sprites = pygame.sprite.Group()
lista_sprites.add(jugador)

bombas = pygame.sprite.Group()

# Bucle principal
clock = pygame.time.Clock()

while True:
    
    lista_eventos = pygame.event.get()
    lista_teclas_presionadas = pygame.key.get_pressed()
    
    for event in lista_eventos:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if lista_teclas_presionadas[pygame.K_SPACE] and jugador.en_suelo:
                jugador.jump()

            elif event.key == pygame.K_b:
                nueva_bomba = Bomba(jugador.rect.centerx, jugador.rect.top)
                bombas.add(nueva_bomba)
                jugador.lanzar_bomba()
        
        elif event.type == pygame.USEREVENT:  # Evento de temporizador
            for bomba in jugador.bombas:
                bomba.explosion()
                
    # Movimiento horizontal
    jugador.mover_izquierda_derecha(lista_teclas_presionadas)

    # Verificar colisiones entre el jugador y las plataformas
    jugador.en_suelo = False
    for plataforma in plataformas:
        if pygame.sprite.collide_rect(jugador, plataforma):
            if jugador.velocidad_y > 0:  # Cayendo
                jugador.rect.y = plataforma.rect.y - jugador.rect.height
                jugador.velocidad_y = 0
                jugador.en_suelo = True
            elif jugador.velocidad_y < 0:  # Saltando
                jugador.rect.y = plataforma.rect.bottom 
                jugador.velocidad_y = 0  # Detener el salto

    # Limitar el movimiento del jugador para que no se salga de la pantalla
    if jugador.rect.left < 0:
        jugador.rect.left = 0
    if jugador.rect.right > WIDTH:
        jugador.rect.right = WIDTH

    jugador.update()
    jugador.bombas.update()
    lista_sprites.update()

    # Dibujar el fondo
    screen.blit(background, (0, 0))
    plataformas.draw(screen)
    bombas.draw(screen)

    # Dibujar todos los sprites
    lista_sprites.draw(screen)

    pygame.display.update()

    clock.tick(60)
