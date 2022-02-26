import pygame, sys,random
import pygame.event
import pygame.locals

pygame.init()       

ancho=700
alto=500        
white=(255,255,255)
color_gemas=(0,255,0)
color_rocas=(0,90,0)
##linea 13
pygame.mouse.set_visible(0)
pygame.display.set_caption("Greed --||")
clock = pygame.time.Clock()
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
                
        pygame.draw.rect(self._ventana,(0,133,255),(x, 450, 35 , 5), 0)
        

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
    
    #Keyboard movement
    #if event==
    
    mouse_pos = pygame.mouse.get_pos()
    x=mouse_pos[0]
    y=mouse_pos[1]
    #
    #aumento la velocidad en 3 pixeles del player
    cord_x += velocidad_x
    if cord_x > 660 or cord_x < 0:
        #Invierte la velocidad
        velocidad_x *= -1
    
    #ventana.fill(white)
    gema.dibujar_gemas()
    roca.dibujar_rocas()
    player.dibujar_player()
    #pygame.display.flip()
    pygame.display.update()
    clock.tick(30)
       




       

