import pygame
from settings import *
from ball import Ball
import random



pygame.init()



pygame.display.set_caption("Pong")

clock = pygame.time.Clock()




balls = [
    Ball(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT), random.randint(5, 25), random.randint(1, 10), random.randint(1,10)),


]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,0,0))

    for i in balls:
        i.draw()
        i.move()
        i.wall_collision()



    clock.tick(200)


    pygame.display.flip()


pygame.quit()