import pygame
from math import pi, sin, cos

pygame.init()

dimension = 500

scr = pygame.display.set_mode((dimension, dimension))
naranja = (255, 165, 0)
azul_marino = (0,0,128)
rosa = (255, 192, 203)
radio = dimension / 3
centro = (dimension / 2, dimension/ 2)

x1 = centro[0]
x2 = radio * cos(11 * pi / 6) + centro[0]
x3 = radio * cos(7 * pi / 6) + centro[0]
y1 = -radio + centro[1]

y2 = radio/2 + centro[1]
y3 = radio/2 + centro[1]

puntos = [(x1,y1),(x2,y2),(x3,y3)]

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        pygame.draw.circle(scr,naranja,centro,radio)
        pygame.draw.polygon(scr,azul_marino,puntos,5)
        pygame.draw.circle(scr,rosa,centro,3)

        #Lineas para ver el centro de la ventana
        pygame.draw.line(scr, rosa, (centro[0], 0), (centro[0], dimension), 2)
        pygame.draw.line(scr, rosa, (0, centro[1]), (dimension, centro[1]), 2)

        pygame.display.flip()
pygame.quit()