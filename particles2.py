import random
import time
from perlin_noise import PerlinNoise
import pygame
from pygame import draw, transform
from time import sleep
from random import randint
from math import sqrt
from save_windows import save

clock = pygame.time.Clock()
pygame.init()

win_side = 700
win_width = 1250
win_height = win_side
size = (win_width, win_height)
win = pygame.display.set_mode(size)

black = (0, 0, 0)
frame_rate = 10


class Particle:
    def __init__(self):
        self.y = 0
        self.x = random.random()*win_width
        self.v = [0, 3]

    def move(self):
        self.x += self.v[0]
        self.y += self.v[1]

    def draw(self, win, color):
        pygame.draw.circle(win, color, (self.x, self.y), 1)


def noise_gen():
    noise = PerlinNoise(3.5, random.seed())
    return noise


def r_color():
    return randint(0, 255), randint(0, 255), randint(0, 255)


def check_color(color1, color2):
    difx = color1[0] - color2[0]
    dify = color1[1] - color2[1]
    difz = color1[2] - color2[2]
    distance = sqrt(difx**2 + dify**2 + difz**2)
    print(distance)
    if distance > 300:
        return True
    else:
        return False


def choose_color():
    chosen = False
    color1, color2 = [0, 0]
    while not chosen:
        color1 = r_color()
        color2 = r_color()
        chosen = check_color(color1, color2)

    return color1, color2


def paint(n):
    win.fill((0, 0, 0))
    particles = [Particle() for _ in range(n)]
    noise_x = noise_gen()
    noise_y = noise_gen()

    colors = choose_color()
    color1 = colors[0]
    color2 = colors[1]

    step = (-(color1[0] - color2[0]) / (win_width + win_height - 1),
            -(color1[1] - color2[1]) / (win_width + win_height - 1),
            -(color1[2] - color2[2]) / (win_width + win_height - 1))
    adjustment = 0
    counter = 0
    end = False
    while not end:
        # win.fill((0, 0, 0))
        clock.tick(frame_rate)
        counter += 1
        if counter == frame_rate * 30:
            end = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE]:
            end = True
            time.sleep(0.2)

        if pressed[pygame.K_p]:
            time.sleep(1)

        if pressed[pygame.K_UP]:
            adjustment += 0.1
            time.sleep(0.2)

        if pressed[pygame.K_DOWN]:
            adjustment -= 0.1
            time.sleep(0.2)

        for x, particle in enumerate(particles):
            force_x = noise_x([particle.x/win_width, particle.y/win_height])
            force_y = noise_y([particle.x/win_width, particle.y/win_height])
            particle.v[0] += force_x + adjustment
            particle.v[1] += force_y + adjustment
            particle.move()

            if particle.y < 0 or particle.x < 0 or particle.x > win_width or particle.y > win_height:
                particles.pop(x)
                particles.append(Particle())
            else:
                multiplayer = (particle.x + particle.y)
                color = (color1[0] + step[0] * multiplayer,
                         color1[1] + step[1] * multiplayer,
                         color1[2] + step[2] * multiplayer)
                particle.draw(win, color)
        pygame.display.update()

    if counter == frame_rate * 30:
        save(win)


def main():
    close = False
    n = 200
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
        sleep(0.2)
        paint(n)


if __name__ == "__main__":
    main()
