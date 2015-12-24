'''
按F在不同的窗口模式之间切换
按x键退出
'''

import pygame
from pygame.locals import *
from sys import exit

pygame.init()

background_image_filename = './Images/home.jpg'
screen = pygame.display.set_mode((640,480),0,32)
background = pygame.image.load(background_image_filename).convert()

Fullscreen = False

while True:
	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == K_x:
				exit()
			if event.key == K_f:
				Fullscreen = not Fullscreen
				if Fullscreen:
					screen = pygame.display.set_mode((640,480),NOFRAME,32)
				else:
					screen = pygame.display.set_mode((640,480),0,32)

	screen.blit(background,(0,0))
	pygame.display.update()