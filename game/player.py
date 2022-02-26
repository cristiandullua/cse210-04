import pygame 
from game.artefacts import Artifact

cord_x = 350


class Player(Artifact):
    def __init__(self):
        super().__init__()
        
            
    def dibujar_player(self):
                
        pygame.draw.rect(self._ventana,(0,133,255),(cord_x, 450, 35 , 5), 0)
        
        

