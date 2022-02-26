import pygame 
from game.artefacts import Artifact


class Player(Artifact):
    def __init__(self):
        super().__init__()
        self._cord_x = 350
        self._cord_y = 0
        self._velocidad_x = 3
            
    def dibujar_player(self):
                
        pygame.draw.rect(self._ventana,(0,133,255),(x, 450, 35 , 5), 0)
        
    def move_player(self):
        self._cord_x += self._velocidad_x
        if self._cord_x > 660 or self._cord_x <0:
            self._velocidad_x *= -1




