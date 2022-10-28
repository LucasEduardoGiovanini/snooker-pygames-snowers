
import pygame

pygame.init()


class Ball:
    radius = 7

    def init(self, position_x, position_y, color=(255, 0, 0)):
        self.position_x = position_x
        self.position_y = position_y
        self.color = color

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.position_x, self.position_y), self.radius)


class Table:
    height = 300
    width = 500
    color = (0, 255, 0)

    def init(self):
        self.table = pygame.Rect(0, 0, self.height, self.width)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.table)


screen_size_x = 800
screen_size_y = 800
screen = pygame.display.set_mode([screen_size_x, screen_size_y])
running = True

table = Table()
table.table.centerx = screen_size_x / 2
table.table.centery = screen_size_y / 2
ball = Ball(position_x=table.table.topleft[0], position_y=table.table.topleft[1])

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))

    table.draw(screen)
    ball.draw(screen)

    pygame.display.flip()
pygame.quit()
