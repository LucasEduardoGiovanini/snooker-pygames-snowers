
import pygame
import numpy as np

from src.table import Table
from src.ball import Ball

pygame.init()


def create_balls(n : int = 10, table=None):
    balls = []
    for _ in range(n):
        ball = Ball(
            x=table.table.topleft[0] + (table.table.centerx / 2) * np.random.rand(),
            y=table.table.topleft[1] + table.table.centery * np.random.rand(),
            vx=10*np.random.rand(),
            vy=10*np.random.rand(),
            color=255 * np.random.rand(3)
        )
        balls.append(ball)

    return balls


screen_size_x = 800
screen_size_y = 800
screen = pygame.display.set_mode([screen_size_x, screen_size_y])
running = True

table = Table()
table.table.centerx = screen_size_x / 2
table.table.centery = screen_size_y / 2
balls = create_balls(n=100, table=table)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))

    table.draw(screen)
    for ball in balls:
        ball.update(dt=1/60, table=table)
        ball.draw(screen)

    pygame.display.flip()

pygame.quit()
