import pygame
from pygame.locals import *
from sys import exit
from gameobjects.vector2 import Vector2

background_image_filename = './Images/bg.png'
sprite_image_filename = './Images/fish.png'
SCREEN_SIZE = (640,480)

pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE,0,32)

background = pygame.image.load(background_image_filename).convert()
sprite = pygame.image.load(sprite_image_filename).convert_alpha()

clock = pygame.time.Clock()
position = Vector2(100.0,100.0)
heading = Vector2()


#-----------------------------------------------
def HandleKeyBoardEvent():
	for event in pygame.event.get():
		if event.type == QUIT:
			exit()



while True:
	HandleKeyBoardEvent()

	screen.blit(background,(0,0))
	screen.blit(sprite,position)
	time_passed = clock.tick()
	time_passed_seconds = time_passed / 1000.0

	destination = Vector2(*pygame.mouse.get_pos()) - Vector2(*sprite.get_size())
	vector_to_mouse = Vector2.from_points(position,destination)
	vector_to_mouse.normalize()

	heading = heading + (vector_to_mouse * .6)
	position += heading * time_passed_seconds
	pygame.display.update()




