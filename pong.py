import pygame
from settings import *
from ball import Ball
from paddle import Paddle
import random

pygame.init()

pygame.display.set_caption("Pong")

clock = pygame.time.Clock()

ball_group = pygame.sprite.Group()
paddle_group = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
num_balls = 100

for i in range(num_balls):
    Ball(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT),\
          random.randint(10, 30), paddle_group, [ball_group, all_sprites])

for players in range(2):
    paddle1 = Paddle(20, pygame.K_w, pygame.K_s, [paddle_group, all_sprites]),
    paddle2 = Paddle(SCREEN_WIDTH - 20, pygame.K_UP, pygame.K_DOWN, [paddle_group, all_sprites])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,0,0))

    all_sprites.update()
    all_sprites.draw(screen)

    if len(ball_group) < num_balls:
        Ball(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT),\
          random.randint(10, 30), paddle_group, [ball_group, all_sprites])

    pygame.display.flip()
    clock.tick(200)

pygame.quit()