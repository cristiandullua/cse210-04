import pygame, random

ancho = 700
alto = 500

class Artifact:

    def __init__(self):
        self._position=[]
        self._center = ancho/2
        self._velocidad = 3
        self._ventana = pygame.display.set_mode((ancho, alto))        


    def relleno_position(self):
        for i in range(60):
            x=random.randint(1,700)
            y=random.randint(1,600)           
            self._position.append([x,y])       


    