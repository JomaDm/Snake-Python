import pygame
import math
import os

global BLACK, BLUE, RED, GREEN, WHITE
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (0, 0, 0)


class score():
    score = 0
    best_score = 0
    def __init__(self):
        try:
            os.system("touch scores.txt")                              
        except :
            print("Ocurrio un error al intentar leer los scores del archivo scores.txt")

        archivo_scores = open("scores.txt","r")
        mejor = archivo_scores.read()      
        
        if(mejor):
            self.best_score = int(mejor)
        
        archivo_scores.close()
    
    def guardarScore(self):
        if(self.score > self.best_score):
            archivo_scores = open("scores.txt","w")
            archivo_scores.write(str(self.score))
            archivo_scores.close()
            
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
        

    def verificarPunto(self, Food, Snake):
        coord_Food = Food.getCoord()
        coord_snake = Snake.getCoordBody()

        if(math.fabs(coord_snake[0][0]-coord_Food[0]) < 10 and math.fabs(coord_snake[0][1]-coord_Food[1]) < 10):
            return True
        return False

    def verificarAutoEat(self, Snake):
        coord_snake = Snake.getCoordBody()
        cabeza = coord_snake[0]

        for i in range(1, len(coord_snake)):
            if(math.fabs(cabeza[0] - coord_snake[i][0]) < 10 and math.fabs(cabeza[1] - coord_snake[i][1]) < 10):
                return True, i
        return False, 0
    
    


class snake():
    Body = []
    height = 10
    width = 10

    def __init__(self, coordx=0, coordy=0, diry=0, dirx=0):
        self.Body.append(body(coordx, coordy, dirx, diry))

    def getBody(self):
        return self.Body

    def getSnakeLenght(self):
        return len(self.Body)

    def getCoordBody(self):
        return [i.getCoord() for i in self.Body]

    def getCoordElement(self, index):
        try:
            return self.Body[index].getCoord()
        except:
            return self.Body[-1].getCoord()

    def getDirectionElement(self, index):
        try:
            return self.Body[index].getDir()
        except:
            return self.Body[-1].getDir()

    def setDirectionElement(self, index, dirx, diry):
        try:
            self.Body[index].setDir(dirx, diry)
        except:
            print("Error")

    def mover(self, dirx, diry):
        self.Body[0].dirx = dirx
        self.Body[0].diry = diry

        for i in self.Body:
            i.coordx += i.dirx
            i.coordy += i.diry

        direcciones = self.Body.copy()

        for i in range(len(self.Body)-1, 0, -1):
            self.Body[i].dirx = direcciones[i-1].dirx
            self.Body[i].diry = direcciones[i-1].diry
        # print(self.Body)

    def eliminarSnake(self, from_=0):
        aux = 0
        for i in range(from_, len(self.Body)):
            del self.Body[i-aux]
            aux += 1

    def getTam(self):
        return len(self.Body)

    def dibujarSnake(self, display):
        for i in self.Body:
            pygame.draw.rect(
                display, GREEN, (i.coordx, i.coordy, self.height, self.width))

    def agregarBody(self):
        coord = self.getCoordElement(-1)
        direction = self.getDirectionElement(-1)
        self.Body.append(
            body(coord[0]-direction[0], coord[1]-direction[1], direction[0], direction[1]))
        print("YUMMY")


class body():
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


class food():
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
