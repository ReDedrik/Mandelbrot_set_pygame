import pygame
import sys
import math


pygame.init()

height, width = 900, 1400
size = (width, height)
screen = pygame.display.set_mode(size)
black = (0, 0, 0)
white = (255, 255, 255)
blue = (36, 84, 247)
green = (36, 84, 36)
pygame.display.set_caption("Mandelbrot Set")
screen.fill(black)

pygame.display.update()
x_coord, y_coord = 0, 0
def convert_coords(coords):
    x = (coords[0] - (width / 2) - 300) * 0.0024
    y = (-coords[1] + (height / 2)) * 0.0024
    return (x, y)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    for a in range(height):
        for b in range(width):
            x_coord, y_coord = b, a
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
            coords = convert_coords((x_coord, y_coord))
            c = complex(coords[0], coords[1])
            z = 0
            set = True
            for j in range(1000):
                z = z**2 + c
                if math.sqrt(abs((z**2).real)) >= 2:
                    set = False
                    break

            if math.sqrt(abs((z**2).real)) < 2:
                set = True
            if set:
                pygame.draw.circle(screen, white, (x_coord, y_coord), 1)


            pygame.display.update()
    print('done')