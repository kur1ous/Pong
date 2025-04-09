import pygame
from settings import *
import random
import math
from paddle import Paddle

class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, radius, paddles, groups):
        super().__init__(groups)
        self.x = x 
        self.y = y
        self.radius = radius

        self.paddles = paddles
        self.last_paddle = None

        self.image = pygame.Surface((2*radius, 2*radius))
        self.image.set_colorkey((0,0,0))
        self.colour = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        pygame.draw.circle(self.image, self.colour, (radius,radius), radius)

        self.rect = self.image.get_frect(center=(x,y))
        angle = random.random() * 2 * math.pi
        self.direction = pygame.Vector2(math.cos(angle), -math.sin(angle))


    def update(self):
        self.rect.center = self.rect.center + self.direction

        if self.rect.right >= SCREEN_WIDTH and self.direction.x >= 0:
            self.die()
        if self.rect.left <= 0 and self.direction.x <= 0:
            self.die()
        if self.rect.bottom >= SCREEN_HEIGHT and self.direction.y >= 0:
            self.direction.y *= -1
        if self.rect.top <= 0 and self.direction.y <= 0:
            self.direction.y *= -1

        for paddle in self.paddles:
            if self.rect.colliderect(paddle.rect):
                self.last_paddle = paddle
                if self.rect.centerx > paddle.rect.centerx and self.direction.x < 0:
                    self.direction.x *= -1
                if self.rect.centerx < paddle.rect.centerx and self.direction.x > 0:
                    self.direction.x *= -1

    def die(self):
        if self.last_paddle:
            self.last_paddle.give_points(1)
        self.kill()