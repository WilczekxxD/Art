import time
from perlin_noise import PerlinNoise
import pygame
from pygame import draw, transform
from time import sleep
from random import randint

clock = pygame.time.Clock()
pygame.init()

win_side = 500
win_width = win_side
win_height = win_side
size = (win_width, win_height)
win = pygame.display.set_mode(size)

black = (0, 0, 0)
r_color = (randint(0, 255), randint(0, 255), randint(0, 255))


class Particle:
    def __init__(self):
        self.y = 0
        self.x = randint(0, win_side)
        self.v = [0, 2]

    def move(self):
        self.x += self.v[0]
        self.y += self.v[1]

    def draw(self, win):
        pygame.draw.circle(win, (255, 255, 255), (self.x, self.y), 2)


def noise_gen():
    noise = PerlinNoise(10, randint(0, 100))
    return noise


def paint(n):
    win.fill((0, 0, 0))
    particles = [Particle() for _ in range(n)]
    noise_x = noise_gen()
    noise_y = noise_gen()
    end = False
    while not end:
        win.fill((0, 0, 0))
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE]:
            end = True

        for x, particle in enumerate(particles):
            force_x = noise_x([particle.x/win_width, particle.y/win_height])
            force_y = noise_y([particle.x/win_width, particle.y/win_height])
            particle.v[0] += force_x
            particle.v[1] += force_y
            particle.move()
            particle.draw(win)
            if particle.y < 0 or particle.x < 0 or particle.x > win_width or particle.y > win_height:
                particles.pop(x)
                particles.append(Particle())
        pygame.display.update()


def main():
    close = False
    n = 500
    paint(n)
    while not close:
        clock.tick(18)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close = True
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE]:
            close = True
        if pressed[pygame.K_n]:
            paint(n)
            sleep(0.5)


if __name__ == "__main__":
    main()
