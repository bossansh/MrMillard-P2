#############################################################################
# Name: Anshul Prabu #221                                                   #
# Project: AP CSP Project												    #
#                                                                           #
# Description: Creates vehicle class, and gives it two attributes. Makes a  #
# bus class and copies its attributes. Prints out attributes.				#                        #                   #
#############################################################################

import pygame
from pygame import mixer
from pygame.locals import *
import random
import os

sourceFileDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(sourceFileDir)

pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()
pygame.init()


#define fps
clock = pygame.time.Clock()
fps = 60


screen_width = 696
screen_height = 564
bg = pygame.image.load("img/bg.png")

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('KidsGTA')

run = True
while run:

	clock.tick(fps)

	#draw background
	draw_bg()
