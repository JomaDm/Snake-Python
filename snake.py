import pygame
import random

class Manzana():

    def __init__(self,x,y,):
        self.x = x
        self.y = y

class Cabeza():

    def __init__(self,limitx=500,limity=500):        
        self.tam = 0
        self.x = 250
        self.y = 250
        self.vel = 1
        self.limitx = limitx*2
        self.limity = limity*2
        self.dir = None
    def moverDerecha(self):
        self.x += self.vel
        if(self.x >= self.limitx):
            self.x = 0
        self.dir = "r"

    def moverIzquierda(self):
        self.x -=self.vel
        if(self.x <= 0):
            self.x = self.limitx
        self.dir = "l"

    def moverArriba(self):
        self.y -= self.vel
        if(self.y <= 0):
            self.y = self.limity
        self.dir = "u"
    
    def moverAbajo(self):
        self.y += self.vel 
        if(self.y >= self.limity):
            self.y = 0
        self.dir = "d"

class Cuerpo():

    def __init__(self,x,y,direction,limitx=500,limity=500):
        self.x = x
        self.y = y
        self.limitx=limitx
        self.limity=limity
        self.dir = direction
        self.vel = 1
    def moverDerecha(self):
        self.x += self.vel
        if(self.x >= self.limitx):
            self.x = 0

    def moverIzquierda(self):
        self.x -=self.vel
        if(self.x <= 0):
            self.x = self.limitx

    def moverArriba(self):
        self.y -= self.vel
        if(self.y <= 0):
            self.y = self.limity

    
    def moverAbajo(self):
        self.y += self.vel 
        if(self.y >= self.limity):
            self.y = 0
            
    
    

class Snake():
    def __init__(self, x=250,y=250):        
        self.Body = [Cabeza(x,y)]        

    def agregarCuerpo(self):                
        x= self.Body[-1].x
        y= self.Body[-1].y
        direc = self.Body[-1].dir
        if(direc == "u"):
            self.Body.append(Cuerpo(x,y+20,direc))
        if(direc == "d"):
            self.Body.append(Cuerpo(x,y-20,direc))
        if(direc == "r"):
            self.Body.append(Cuerpo(x-20,y,direc))
        if(direc == "l"):
            self.Body.append(Cuerpo(x+20,y,direc))
        
    
    def mover(self,cuerpo,direction):
        if(direction == "u"):
            cuerpo.moverArriba()
        if(direction == "d"):
            cuerpo.moverAbajo()
        if(direction == "r"):
            cuerpo.moverDerecha()
        if(direction == "l"):
            cuerpo.moverIzquierda()

    def mostrarCoord(self):
        for i,e in enumerate(self.Body):
            print(str(i),"x:",e.x,"y:",e.y)

    def moverDerecha(self):
        coord = self.Body.copy()
        self.Body[0].moverDerecha() 
        if(len(self.Body) > 1):            
            for i in range(1,len(coord)):   
                self.Body[i].x=coord[i-1].x+10
                self.Body[i].y=coord[i-1].y+10
                self.mover(self.Body[i],self.Body[i].dir)
                
                
                """siguiente = self.Body[i+1]                               
                self.Body[i+1].dir = anterior.dir 
                if(anterior.dir == "u"):
                    self.Body[i+1].x = anterior.x                
                    self.Body[i+1].y = anterior.y+20
                if(anterior.dir == "d"):
                    self.Body[i+1].x = anterior.x                
                    self.Body[i+1].y = anterior.y-20 
                if(anterior.dir == "r"):
                    self.Body[i+1].x = anterior.x-20                
                    self.Body[i+1].y = anterior.y
                if(anterior.dir == "l"):
                    self.Body[i+1].x = anterior.x+20                
                    self.Body[i+1].y = anterior.y
                anterior = siguiente"""
                #self.mover(self.Body[i+1],self.Body[i+1].dir)
        
        
        

    def moverIzquierda(self):
        coord = self.Body.copy()
        self.Body[0].moverIzquierda()
        
        if(len(self.Body) > 1):            
            for i in range(1,len(coord)):   
                self.Body[i].x=coord[i-1].x+10
                self.Body[i].y=coord[i-1].y+10
                self.mover(self.Body[i],self.Body[i].dir)
                        
                
                """siguiente = self.Body[i+1]                               
                self.Body[i+1].dir = anterior.dir 
                if(anterior.dir == "u"):
                    self.Body[i+1].x = anterior.x                
                    self.Body[i+1].y = anterior.y+20
                if(anterior.dir == "d"):
                    self.Body[i+1].x = anterior.x                
                    self.Body[i+1].y = anterior.y-20 
                if(anterior.dir == "r"):
                    self.Body[i+1].x = anterior.x-20                
                    self.Body[i+1].y = anterior.y
                if(anterior.dir == "l"):
                    self.Body[i+1].x = anterior.x+20                
                    self.Body[i+1].y = anterior.y
                anterior = siguiente
                """
                #self.mover(self.Body[i+1],self.Body[i+1].dir)
        
        
    def moverArriba(self):
        coord = self.Body.copy()
        self.Body[0].moverArriba()
        #self.Body[0].moverAbajo()
                
        if(len(self.Body) > 1):            
            for i in range(1,len(coord)):   
                self.Body[i].x=coord[i-1].x+10
                self.Body[i].y=coord[i-1].y+10
                self.mover(self.Body[i],self.Body[i].dir)
                               
                
                """
                siguiente = self.Body[i+1]                               
                self.Body[i+1].dir = anterior.dir 
                if(anterior.dir == "u"):
                    self.Body[i+1].x = anterior.x                
                    self.Body[i+1].y = anterior.y+20
                if(anterior.dir == "d"):
                    self.Body[i+1].x = anterior.x                
                    self.Body[i+1].y = anterior.y-20 
                if(anterior.dir == "r"):
                    self.Body[i+1].x = anterior.x-20                
                    self.Body[i+1].y = anterior.y
                if(anterior.dir == "l"):
                    self.Body[i+1].x = anterior.x+20                
                    self.Body[i+1].y = anterior.y
                anterior = siguiente
                #self.mover(self.Body[i+1],self.Body[i+1].dir)
                """
                
    
    def moverAbajo(self):            
        #self.Body[0].moverAbajo()        
        coord = self.Body.copy()
        self.Body[0].moverAbajo()
        if(len(self.Body) > 1):            
            for i in range(1,len(coord)):                   
                self.Body[i].x=coord[i-1].x+10
                self.Body[i].y=coord[i-1].y+10
                self.mover(self.Body[i],self.Body[i].dir)
                
                
                
                """
                siguiente = self.Body[i+1]                               
                self.Body[i+1].dir = anterior.dir 
                if(anterior.dir == "u"):
                    self.Body[i+1].x = anterior.x                
                    self.Body[i+1].y = anterior.y+20
                if(anterior.dir == "d"):
                    self.Body[i+1].x = anterior.x                
                    self.Body[i+1].y = anterior.y-20 
                if(anterior.dir == "r"):
                    self.Body[i+1].x = anterior.x-20                
                    self.Body[i+1].y = anterior.y
                if(anterior.dir == "l"):
                    self.Body[i+1].x = anterior.x+20                
                    self.Body[i+1].y = anterior.y
                anterior = siguiente"""
                #self.mover(self.Body[i+1],self.Body[i+1].dir)
        

                
                
                


pygame.init()
display = pygame.display.set_mode((500,500))
pygame.display.set_caption("Snake Game")
snake = Snake()
manzana = Manzana(random.randint(0,500),random.randint(0,500))

display.fill((0,0,0))
pygame.display.update()

clk = pygame.time.Clock()

up = False
down = False
left = False
right = False

run = True
while run:
    
    clk.tick(60)
    event = pygame.event.get()
    for evnt in event:
        if(evnt.type == pygame.QUIT):
            run = False

        if evnt.type == pygame.KEYDOWN:

            if evnt.key == pygame.K_LEFT:
                snake.moverIzquierda()
                left = True
                right = False
                up = False
                down = False
            if evnt.key == pygame.K_RIGHT:
                snake.moverDerecha()
                left = False
                right = True
                up = False
                down = False
            if evnt.key == pygame.K_UP:
                snake.moverArriba()
                left = False
                right = False
                up = True
                down = False                
            if evnt.key == pygame.K_DOWN:
                snake.moverAbajo()
                left = False
                right = False
                up = False
                down = True

    if right:
        snake.moverDerecha()
    if left:
        snake.moverIzquierda()
    if up:
        snake.moverArriba()
    if down: 
        snake.moverAbajo()
    

    for i in snake.Body:
        pygame.draw.rect(display,(0,0,255),(i.x,i.y,20,20))
    pygame.draw.rect(display,(255,0,0),(manzana.x,manzana.y,15,15))

    for i in snake.Body:
        for j in range(20):
            if((manzana.x,manzana.y) == (i.x+j,i.y)):
                snake.agregarCuerpo()
                manzana = Manzana(random.randint(0,500),random.randint(0,500))
                print("Toco la manzana")
                #print(len(snake.Body))

            elif((manzana.x,manzana.y) == (i.x-j,i.y)):
                snake.agregarCuerpo()
                manzana = Manzana(random.randint(0,500),random.randint(0,500))
                print("Toco la manzana")
                #print(len(snake.Body))
        
            elif((manzana.x,manzana.y) == (i.x,i.y+j)):
                snake.agregarCuerpo()
                manzana = Manzana(random.randint(0,500),random.randint(0,500))
                print("Toco la manzana")
                #print(len(snake.Body))

            elif((manzana.x,manzana.y) == (i.x,i.y-j)):
                snake.agregarCuerpo()
                manzana = Manzana(random.randint(0,500),random.randint(0,500))
                print("Toco la manzana")
                #print(len(snake.Body))
        
            elif((manzana.x,manzana.y) == (i.x+j,i.y+j)):
                snake.agregarCuerpo()
                manzana = Manzana(random.randint(0,500),random.randint(0,500))
                print("Toco la manzana")
                print(len(snake.Body))

            elif((manzana.x,manzana.y) == (i.x-j,i.y-j)):
                snake.agregarCuerpo()
                manzana = Manzana(random.randint(0,500),random.randint(0,500))
                print("Toco la manzana")
                #print(len(snake.Body))
            
            elif((manzana.x,manzana.y) == (i.x+j,i.y-j)):
                snake.agregarCuerpo()
                manzana = Manzana(random.randint(0,500),random.randint(0,500))
                print("Toco la manzana")
                #print(len(snake.Body))
            
            elif((manzana.x,manzana.y) == (i.x-j,i.y+j)):
                snake.agregarCuerpo()
                manzana = Manzana(random.randint(0,500),random.randint(0,500))
                print("Toco la manzana")
            
                #print(len(snake.Body))
            
        #snake.mostrarCoord()

    pygame.display.update()
    display.fill((0,0,0))

    