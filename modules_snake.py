import pygame
import math
import os

global BLACK, BLUE, RED, GREEN, WHITE
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (0, 0, 0)


class Score():
    score = 0
    best_score = 0
    def __init__(self):
        mejor = None
        try:
            archivo_scores = open("scores.txt","r+")
            mejor = archivo_scores.read()                                                    
            archivo_scores.close()
        except :
            print("Ocurrio un error al intentar leer los scores del archivo scores.txt")
                
        if(mejor):
            self.best_score = int(mejor)                
    
    def guardarScore(self):
        if(self.score > self.best_score):
            archivo_scores = open("scores.txt","w+")
            archivo_scores.write(str(self.score))
            archivo_scores.close()
    
    def getScore(self):
        return self.score
            
    def showScore(self):
        return score

    def cambioScore(self, cambio):
        self.score += cambio

    def dibujarScore(self, display):
        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        texto = 'Score :'+str(self.score)
        textsurface = myfont.render(texto, True, GREEN)
        display.blit(textsurface, (10, 10))
        
        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        texto = 'Best Score :'+str(self.best_score)
        textsurface = myfont.render(texto, True, GREEN)
        display.blit(textsurface, (10, 30))
        

    def verificarPunto(self, food, snake,velocity):
        coord_Food = food.getCoord()
        coord_snake = snake.getCoordBody()

        if(math.fabs(coord_snake[0][0]-coord_Food[0]) <= velocity and math.fabs(coord_snake[0][1]-coord_Food[1]) <= velocity):
            return True
        return False

    def verificarAutoEat(self, snake,velocity):
        coord_snake = snake.getCoordBody()
        #print(coord_snake)
        cabeza = coord_snake[0]

        for i in range(1, len(coord_snake)):
            if(math.fabs(cabeza[0] - coord_snake[i][0]) < velocity-1 and math.fabs(cabeza[1] - coord_snake[i][1]) < velocity-1):
                #print("Se comio:",cabeza[0],"a",coord_snake[i][0],"y\nSe comio:",cabeza[1],"a",coord_snake[i][1],"vel:",velocity)                
                return True, i
        return False, 0
    
    def scoreLevelUp(self,display):
        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        texto = 'LEVEL UP!!!'
        textsurface = myfont.render(texto, True, GREEN)
        display.blit(textsurface, (250, 10))
        
    def verificarGame_Over(self,snake,tam):
        serpiente = snake.getBody()
        if(serpiente[0].coordx <= 0 or
           serpiente[0].coordx >= tam or
           serpiente[0].coordy <= 0 or
           serpiente[0].coordy >= tam ):
            return True
    
    def scorePantallaGameOver(self,display,tam):
        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        texto = 'GAME OVER'
        texto2 = 'Puntuación:'+str(self.score)
        textsurface = myfont.render(texto, True, GREEN)
        textsurface2 = myfont.render(texto2, True, GREEN)
        display.blit(textsurface, (tam//2, tam//2))
        display.blit(textsurface2, (tam//2, tam//2+30))
        

class Snake():
    body = []
    height = 10
    width = 10

    def __init__(self, coordx=0, coordy=0, diry=0, dirx=0):
        self.body.append(Body(coordx, coordy, dirx, diry))

    def getBody(self):
        return self.body

    def getSnakeLenght(self):
        return len(self.body)

    def getCoordBody(self):
        return [i.getCoord() for i in self.body]

    def getCoordElement(self, index):
        try:
            return self.body[index].getCoord()
        except:
            return self.body[-1].getCoord()

    def getDirectionElement(self, index):
        try:
            return self.body[index].getDir()
        except:
            return self.body[-1].getDir()

    def setDirectionElement(self, index, dirx, diry):
        try:
            self.body[index].setDir(dirx, diry)
        except:
            print("Error en la escritura de dirección en",index)

    def mover(self, dirx, diry):                                
        self.body[0].dirx = dirx
        self.body[0].diry = diry

        for i in self.body:
            i.coordx += i.dirx
            i.coordy += i.diry

        direcciones = self.body.copy()

        for i in range(len(self.body)-1, 0, -1):
            self.body[i].dirx = direcciones[i-1].dirx
            self.body[i].diry = direcciones[i-1].diry
        # print(self.Body)

    def eliminarSnake(self, from_=0):
        aux = 0
        for i in range(from_, len(self.body)):
            del self.body[i-aux]
            aux += 1

    def dibujarSnake(self, display):
        for i in self.body:
            pygame.draw.rect(
                display, GREEN, (i.coordx, i.coordy, self.height, self.width))

    def agregarBody(self,velocity):
        coord = self.getCoordElement(-1)
        direction = self.getDirectionElement(-1)
                
        self.body.append(
            Body(coord[0]-direction[0], coord[1]-direction[1], direction[0], direction[1]))
        print("YUMMY")
            


class Body():
    dirx = 0
    diry = 0
    coordx = 0
    coordy = 0

    def __init__(self, coordx, coordy, dirx, diry):
        self.diry = diry
        self.dirx = dirx
        self.coordx = coordx
        self.coordy = coordy

    def getCoord(self):
        return [self.coordx, self.coordy]

    def getDir(self):
        return [self.dirx, self.diry]

    def setCoord(self, Coordx, Coordy):
        self.coordy = Coordy
        self.coordx = Coordx

    def setDir(self, dirx, diry):
        self.dirx = dirx
        self.diry = diry

    def __str__(self):
        return "("+str(self.coordx)+","+str(self.coordy)+")"


class Food():
    coordx = 0
    coordy = 0
    height = 10
    width = 10

    def __init__(self, coordx, coordy):
        self.coordx = coordx
        self.coordy = coordy

    def dibujarFood(self, display):
        pygame.draw.rect(display, RED, (self.coordx,
                                        self.coordy, self.height, self.width))

    def getCoord(self):
        return [self.coordx, self.coordy]


def dibujarFondo(display):
    display.fill(BLACK)
