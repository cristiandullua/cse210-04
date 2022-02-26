import pygame
from game.artefacts import Artifact

white=(255,255,255)
color_gemas=(0,255,0)


class Gema(Artifact):

    def __init__(self):
        super().__init__()
        self._gema="*"
        self._positionX=0
        self._positionY=0        
        
    def dibujar_gemas(self):
        self._ventana.fill(white)        
        for coordenada in self._position:
            pygame.draw.circle(self._ventana,color_gemas,(coordenada),7)
            #el cuatro es la velocidad o la cantidad de pixeles que avanzan los puntos de las coordenadas de las pelotitas que avanzaran hasta llegar al final de pantalla.
            coordenada[1]+=4
            #verifico que las gemas vuelvan a aparecen al llegar al final e la pantalla eje de las 'Y'
            if  coordenada[1] == 600 :
                coordenada[1] = 0

