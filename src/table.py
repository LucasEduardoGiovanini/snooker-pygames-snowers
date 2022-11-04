
import pygame


class Table:
    height = 300
    width = 500
    color = (0, 255, 0)

    def __init__(self):
        self.table = pygame.Rect(0, 0, self.height, self.width)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.table)
