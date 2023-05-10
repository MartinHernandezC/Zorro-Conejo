import pygame
from assets import Assets
import math

pygame.init()

#Ventana
SCREEN_WIDHT= 1000
SCREEN_HEIGHT= 600

#Música
pygame.mixer.music.load("DeadPool.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1, 0.0, 5000)

screen= pygame.display.set_mode((SCREEN_WIDHT, SCREEN_HEIGHT))
pygame.display.set_caption("Zorro&Conejo")

#Fondo
bg_image = pygame.image.load("fondo.gif").convert_alpha()

#Cargar imágenes de conejo y zorro
conejo_image = pygame.image.load("conejo.png").convert_alpha()
conejo_imag= pygame.transform.scale(conejo_image, (60, 65))
zorro_image = pygame.image.load("zorro.png").convert_alpha()
zorro_imag = pygame.transform.scale(zorro_image, (80, 100))

#Crear instancias
assets_1 = Assets(0, 510, zorro_imag)
assets_2 = Assets(125, 510, conejo_imag)

#Asignar FPS
clock = pygame.time.Clock()
FPS = 60

#Dibujar Fondo
def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDHT,SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0,0))

#game loop
run = True
while run:
    clock.tick(FPS)

    #Dibujar
    draw_bg()
    assets_1.move(SCREEN_WIDHT, SCREEN_HEIGHT)
    assets_2.move(SCREEN_WIDHT, SCREEN_HEIGHT)
    #Dibujar personajes
    assets_1.draw(screen)
    assets_2.draw(screen)

    #Manejador de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #Actualizar pantalla
    pygame.display.update()

#Fin
pygame.quit()
