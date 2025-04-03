import pygame
from settings import *
from ball import Ball

pygame.init()



pygame.display.set_caption("Pong")

clock = pygame.time.Clock()




balls = [
    Ball(200, 300, 25, 5, 5),
    Ball(400, 300, 25, 5, 5),
    Ball(400, 300, 25, 5, 5),
    Ball(400, 300, 25, 5, 5),

]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,0,0))

    for i in range(0, len(balls)):
        balls[i].draw()
        balls[i].move()
        balls[i].wall_collision()



    clock.tick(200)


    pygame.display.flip()


pygame.quit()