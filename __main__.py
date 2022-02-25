import pygame, sys,random
import pygame.event
import pygame.locals

pygame.init()       

white=(255,255,255)
color_gemas=(0,255,0)
color_rocas=(0,90,0)

pygame.display.set_caption("Greed --||")
clock = pygame.time.Clock()

class Artifact:

    def __init__(self):
        self._position=[]
        self._ancho=700
        self._alto=500
        self._ventana= pygame.display.set_mode((self._ancho, self._alto))        


    def relleno_position(self):
        for i in range(60):
            x=random.randint(1,700)
            y=random.randint(1,600)           
            self._position.append([x,y])                    
    
class Gema(Artifact):

    def __init__(self):
        super().__init__()
        self._gema="*"        
        
    def dibujar_gemas(self):
        self._ventana.fill(white)        
        for coordenada in self._position:
            pygame.draw.circle(self._ventana,color_gemas,(coordenada),7)
            #el cuatro es la velocidad o la cantidad de pixeles que avanzan los puntos de las coordenadas de las pelotitas que avanzaran hasta llegar al final de pantalla.
            coordenada[1]+=4
            #verifico que las gemas vuelvan a aparecen al llegar al final e la pantalla eje de las 'Y'
            if  coordenada[1] == 600 :
                coordenada[1] = 0
        
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

class Player(Artifact):
    def __init__(self):
        super().__init__()
        
            
    def dibujar_player(self):
       
            pygame.draw.rect(self._ventana,(0,133,255),(300,450,35,5),0)
            
gema=Gema()
gema.relleno_position()
roca=Roca()
roca.relleno_position()
player=Player()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    
    gema.dibujar_gemas()
    roca.dibujar_rocas()
    player.dibujar_player()
    pygame.display.update()
    clock.tick(30)
       

