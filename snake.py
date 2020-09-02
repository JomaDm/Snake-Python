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

    score = Score()
    snake = Snake(255, 255)
    food = Food(rd.randint(tam//10, tam-tam//10),
                rd.randint(tam//10, tam-tam//10))

    game_over = False
    clk = pygame.time.Clock()
    next_level_at = 5
    aux_level = 0
    separation = 12
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
                    if(dirx != separation):
                        dirx = -separation
                        diry = 0
                elif(evento.key == pygame.K_RIGHT or evento.key == pygame.K_d):
                    if(dirx != -separation):
                        dirx = separation
                        diry = 0
                elif(evento.key == pygame.K_DOWN or evento.key == pygame.K_s):
                    if(diry != -separation):
                        dirx = 0
                        diry = separation
                elif(evento.key == pygame.K_UP or evento.key == pygame.K_w):
                    if(diry != separation):
                        dirx = 0
                        diry = -separation
                elif(evento.key == pygame.K_ESCAPE):
                    game_over = True
                    score.guardarScore()

        snake.mover(dirx, diry)
        snake.dibujarSnake(display)

        if(score.verificarPunto(food, snake, separation)):
            score.cambioScore(1)
            snake.agregarBody(separation)
            food = Food(rd.randint(tam//10, tam-tam//10),
                        rd.randint(tam//10, tam-tam//10))
        if(score.getScore() % next_level_at == 0 and score.getScore() != 0):
            score.scoreLevelUp(display)

        autoEat, index = score.verificarAutoEat(snake, separation)
        if(autoEat):
            longitud_snake = snake.getSnakeLenght()
            snake.eliminarSnake(index)
            score.cambioScore(-longitud_snake+index)
            print("OUCH!!")

        food.dibujarFood(display)
        score.dibujarScore(display)

        if(score.verificarGame_Over(snake, tam)):
            game_over = True
            score.guardarScore()

        pygame.display.update()

    salir = 0
    while salir == 0:
        eventos = pygame.event.get()
        for evento in eventos:
            if(evento.type == pygame.QUIT):
                salir = 1
            if(evento.type == pygame.KEYDOWN):
                if evento.key == pygame.K_ESCAPE:
                    salir = 1
        score.scorePantallaGameOver(display, tam)
        pygame.display.update()
