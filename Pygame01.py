'''
前景图跟随鼠标移动
'''
import pygame
from pygame.locals import *
from sys import exit

background_image_filename = './Images/bg.png'
mouse_image_file = './Images/home.jpg'

pygame.init()

screen = pygame.display.set_mode((1920,1080),0,32)
pygame.display.set_caption("I love you")

background = pygame.image.load(background_image_filename).convert()
mouse_cursor = pygame.image.load(mouse_image_file).convert_alpha()

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			exit()

	screen.blit(background,(0,0))
	x,y = pygame.mouse.get_pos()
	x -= mouse_cursor.get_width() / 2
	y -= mouse_cursor.get_height() / 2
	screen.blit(mouse_cursor,(x,y))
	pygame.display.update()