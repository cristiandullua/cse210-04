import pygame, sys,random
import pygame.event
import pygame.locals
from game.artefacts import Artifact
from game.gema import Gema
from game.roca import Roca
from game.player import Player

pygame.init()       

ancho=700
alto=500        
white=(255,255,255)
color_gemas=(0,255,0)
color_rocas=(0,90,0)


pygame.display.set_caption("Greed --||")
clock = pygame.time.Clock()

 
gema=Gema()
gema.relleno_position()
roca=Roca()
roca.relleno_position()
player=Player()
cord_x=350
cord_y=0
velocidad_x=3

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    #ventana.fill(white)
    gema.dibujar_gemas()
    roca.dibujar_rocas()
    player.dibujar_player()
    player.move_player()
    #pygame.display.flip()
    pygame.display.update()
    clock.tick(30)
       


       

