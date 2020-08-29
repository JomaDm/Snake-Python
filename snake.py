import sys
import pygame
import random as rd
from modules_snake import *

if __name__ == "__main__":
    pygame.init()
    tam = 500
    display = pygame.display.set_mode((tam,tam))
    pygame.display.set_caption("Snake")
    
    Score = score()
    Snake = snake()
    Food = food(rd.randint(tam%10,tam-tam%10),rd.randint(tam%10,tam-tam%10))
    
    game_over = False
    clk = pygame.time.Clock()
    dirx = 0
    diry = 0
    
    while not game_over:
        pygame.time.delay(60)
        dibujarFondo(display)
        eventos = pygame.event.get()
        
        for evento in eventos:
            if(evento.type == pygame.QUIT):
                game_over = True
            if(evento.type == pygame.KEYDOWN):
                if(evento.key == pygame.K_LEFT):
                    dirx = -10
                    diry = 0
                elif(evento.key == pygame.K_RIGHT):
                    dirx = 10
                    diry = 0
                elif(evento.key == pygame.K_DOWN):
                    dirx = 0
                    diry = 10
                elif(evento.key == pygame.K_UP):
                    dirx = 0
                    diry = -10
                elif(evento.key == pygame.K_ESCAPE):
                    pygame.time.delay(1200)
                    
        Snake.mover(dirx,diry)
        Snake.dibujarSnake(display)
        
        if(Score.verificarPunto(Food,Snake)):
            Score.cambioScore(1)
            Snake.agregarBody()
            print(Snake.getCoordBody())
            Food = food(rd.randint(tam%10,tam-tam%10),rd.randint(tam%10,tam-tam%10))
           
        AutoEat,index = Score.verificarAutoEat(Snake)         
        Food.dibujarFood(display)
        
        pygame.display.update()
        
        