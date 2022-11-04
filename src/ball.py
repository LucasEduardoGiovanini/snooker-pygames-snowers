
import pygame


class Ball:
    radius = 7

    def __init__(
            self, x=0, y=0,
            vx=0, vy=0,
            color=(255, 0, 0)
                 ):
        self.x = x
        self.x_old = x
        self.y = y
        self.y_old = y
        self.vx = vx
        self.vy = vy
        self.ax, self.ay = 0, 0
        self.color = color

    def calculate_position(self, dt=1/60):
        self.x_old = self.x
        self.y_old = self.y

        self.x = self.x + self.vx * dt + self.ax * (dt * dt)
        self.y = self.y + self.vy * dt + self.ay * (dt * dt)

    def calculate_speed(self, dt=1/60):
        self.vx = (self.x - self.x_old) / dt
        self.vy = (self.y - self.y_old) / dt

    def check_collision_table(self, table=None):
        if self.x + self.radius > table.table.topright[0] or self.x - self.radius < table.table.topleft[0]:
            self.vx = -self.vx
        if self.y - self.radius < table.table.topright[1] or self.y + self.radius > table.table.bottomright[1]:
            self.vy = -self.vy

    def update(self, dt=1/60, table=None):
        self.calculate_position(dt=dt)
        self.calculate_speed(dt=dt)
        self.check_collision_table(table=table)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
