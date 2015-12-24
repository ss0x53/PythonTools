import pygame
from pygame.locals import *
from sys import exit

pygame.init()

background_image_filename = "./Images/bg.png"
sprite_image_filename = './Images/fish.png'

SCREEN_SIZE = (640,480)

screen = pygame.display.set_mode(SCREEN_SIZE,0,32)
background = pygame.image.load(background_image_filename).convert()
sprite = pygame.image.load(sprite_image_filename)

x = 0

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			exit()
	screen.blit(background,(0,0))
	screen.blit(sprite,(x,100))
	x -= 0.2
	print("x = " + str(x) + "    " + str(SCREEN_SIZE[0]))

	if x < 0 - sprite.get_width():
		x = SCREEN_SIZE[0]

	pygame.display.update()