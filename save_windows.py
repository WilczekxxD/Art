import os
import pygame


def save(window):
    f = open(os.path.join(os.getcwd(), "saved", "last.txt"), "r+")
    number = int(f.readline())
    print(number)
    f.truncate(0)
    f.write(str(number+1))
    f.close()

    path = os.path.join(os.getcwd(), "saved", f"save{number}.png")
    pygame.image.save(window, path)
