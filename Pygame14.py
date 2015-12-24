background_image_filename = './Images/bg.png'
sprite_image_filename = './Images/fish.png'

import pygame
from pygame.locals import *
from sys import exit

pygame.init()
SCREEN_SIZE = (640,480)

screen = pygame.display.set_mode(SCREEN_SIZE,0,32)
background = pygame.image.load(background_image_filename).convert()
sprite = pygame.image.load(sprite_image_filename)

clock = pygame.time.Clock()
x = 0
speed = 250

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			exit()
	screen.blit(background,(0,0))
	screen.blit(sprite,(x,100))

	time_passed = clock.tick()
	time_passed_seconds = time_passed / 1000.0
	
	distance_moved = time_passed_seconds * speed
	x += distance_moved
	print(str(time_passed) + "    " + str(time_passed_seconds) + "    " + str(x))

	if x > SCREEN_SIZE[0]:
		x -= 640
	pygame.display.update()