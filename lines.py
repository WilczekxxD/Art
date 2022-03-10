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


def paint(tiles):
    win.fill((255, 255, 255))
    side = 500 / tiles
    for x in range(tiles):
        for y in range(tiles):
            a = randint(0, 1)
            if a == 0:
                draw.line(win, black,
                          (0 + x * side, 0 + y * side), (side * (x + 1), side * (y + 1)), width=4)
            else:
                draw.line(win, black,
                          (0 + x * side, side * (y + 1)), (side * (x + 1), 0 + y * side), width=4)

    pygame.display.update()


def main():
    close = False
    side = 50
    paint(side)
    while not close:
        clock.tick(18)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close = True

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE]:
            close = True
        if pressed[pygame.K_n]:
            paint(side)
            sleep(0.2)


if __name__ == "__main__":
    main()
