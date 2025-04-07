import pygame
from settings import *
from ball import Ball
import random

pygame.init()

pygame.display.set_caption("Pong")

clock = pygame.time.Clock()

ball_group = pygame.sprite.Group()

for i in range(5):
    Ball(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT), random.randint(10, 30), ball_group)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,0,0))

    ball_group.update()
    ball_group.draw(screen)

    pygame.display.flip()
    clock.tick(200)

pygame.quit()