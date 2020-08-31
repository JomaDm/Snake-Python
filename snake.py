import sys
import pygame
import random as rd
from modules_snake import *

if __name__ == "__main__":
    pygame.init()
    tam = 500
    #flags = pygame.FULLSCREEN | pygame.DOUBLEBUF
    #display = pygame.display.set_mode((tam,tam),flags)
    display = pygame.display.set_mode((tam, tam))
    pygame.display.set_caption("Snake")

    Score = score()
    Snake = snake(255, 255)
    Food = food(rd.randint(tam//10, tam-tam//10),
                rd.randint(tam//10, tam-tam//10))

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
                if(evento.key == pygame.K_LEFT or evento.key == pygame.K_a):
                    if(dirx != 10):
                        dirx = -10
                        diry = 0
                elif(evento.key == pygame.K_RIGHT or evento.key == pygame.K_d):
                    if(dirx != -10):
                        dirx = 10
                        diry = 0
                elif(evento.key == pygame.K_DOWN or evento.key == pygame.K_s):
                    if(diry != -10):
                        dirx = 0
                        diry = 10
                elif(evento.key == pygame.K_UP or evento.key == pygame.K_w):
                    if(diry != 10):
                        dirx = 0
                        diry = -10
                elif(evento.key == pygame.K_ESCAPE):
                    game_over = True

        Snake.mover(dirx, diry)
        Snake.dibujarSnake(display)

        if(Score.verificarPunto(Food, Snake)):
            Score.cambioScore(1)
            Snake.agregarBody()
            Food = food(rd.randint(tam//10, tam-tam//10),
                        rd.randint(tam//10, tam-tam//10))

        AutoEat, index = Score.verificarAutoEat(Snake)
        if(AutoEat):
            longitud_snake = Snake.getSnakeLenght()
            Snake.eliminarSnake(index)
            Score.cambioScore(-longitud_snake+index)
            print("OUCH!!")
        Food.dibujarFood(display)
        Score.dibujarScore(display)

        pygame.display.update()
