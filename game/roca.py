import pygame
from game.artefacts import Artifact


white=(255,255,255)
color_rocas=(0,90,0)


class Roca(Artifact):
    def __init__(self):
        super().__init__()
        self._rocas="O"

    def dibujar_rocas(self):        
        for coordenada in self._position:
            pygame.draw.circle(self._ventana,color_rocas,(coordenada),9)
            #el cuatro es la velocidad o la cantidad de pixeles que avanzan los puntos de las coordenadas de las pelotitas que avanzaran hasta llegar al final de pantalla.
            coordenada[1]+=4
            if  coordenada[1] == 596 :
                coordenada[1] = 0
