import pygame.gfxdraw
import pygame
from pygame import draw, transform
from time import sleep
from random import randint
clock = pygame.time.Clock()
pygame.init()

win_side = 1000
win_width = win_side
win_height = win_side
size = (win_width, win_height)
win = pygame.display.set_mode(size)

black = (0, 0, 0)


def r_color():
    return randint(0, 255), randint(0, 255), randint(0, 255)


def paint(tiles, curvature):
    win.fill(black)
    side = int(win_side/tiles)
    color1 = r_color()
    color2 = r_color()
    step = (-(color1[0]-color2[0])/(2*tiles-1), -(color1[1]-color2[1])/(2*tiles-1), -(color1[2]-color2[2])/(2*tiles-1))
    for x in range(tiles):
        for y in range(tiles):
            color = r_color()
            complementary = (int(abs(color2[0]-step[0]*(x+y))), int(abs(color2[1]-step[1]*(x+y))), int(abs(color2[2]-step[2]*(x+y))))
            pygame.draw.rect(win, complementary, (x*side, y*side, side, side))
            a = randint(0, 1)
            points = [(randint(x * side, (x+1)*side), randint(y*side, (y+1)*side)) for _ in range(curvature)]
            if a == 0:
                points = tuple([(side * (x + 1), y * side)] + points + [(x * side, side * (y + 1))])
                pygame.gfxdraw.bezier(win, points,
                                      2, (abs(color1[0]+step[0]*(x+y)), abs(color1[1]+step[1]*(x+y)), abs(color1[2]+step[2]*(x+y))))
            else:
                points = tuple([(side * x, y * side)] + points + [((x + 1) * side, side * (y + 1))])
                pygame.gfxdraw.bezier(win, points,
                                      2, (abs(color1[0]+step[0]*(x+y)), abs(color1[1]+step[1]*(x+y)), abs(color1[2]+step[2]*(x+y))))

    pygame.display.update()


def main():
    close = False
    side = 50
    curvature = 1
    paint(side, curvature)
    while not close:
        clock.tick(18)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close = True

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE]:
            close = True
        if pressed[pygame.K_n]:
            paint(side, curvature)
            sleep(0.5)


if __name__ == "__main__":
    main()
