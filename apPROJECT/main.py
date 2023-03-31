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
import time

sourceFileDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(sourceFileDir)

pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()
pygame.init()

#define colors
red = (255, 0, 0)
green = (0, 255, 0)
black = (0,0,0)
#define fps
clock = pygame.time.Clock()
fps = 60


screen_width = 696
screen_height = 564
buildingRows = 4
buildingCols = 4 
junctionRows = 3
junctionCols = 3

bg = pygame.image.load("img/bg.png")

def draw_bg():
	screen.blit(bg, (0, 0))


screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('CopRun')


class buildings(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("img/building.png")
		self.rect = self.image.get_rect()
		self.rect.left = x
		self.rect.y = y
	def update(self):
		return

class intersections(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("img/intersection.png")
		self.rect = self.image.get_rect()
		self.rect.left = x
		self.rect.y = y
	def update(self):
		return


class Vehicle(pygame.sprite.Sprite):
	def __init__(self, x, y, health):
		pygame.sprite.Sprite.__init__(self)
		img = pygame.image.load("img/Escape.png")
		self.image = pygame.transform.scale(img, (17, 17))
		self.rect = self.image.get_rect()
		self.rect.center = [x, y]
		self.health_start = health
		self.health_remaining = health
		self.last_shot = pygame.time.get_ticks()
		self.speed = 4
	def update(self):
		#game_over = 0
		#get key press
		speed = 4
		key = pygame.key.get_pressed()
		
		if key[pygame.K_LEFT] and self.rect.left > 0:
			self.rect.x -= speed
			if pygame.sprite.spritecollide(self, buildings_group, False): #stops vheicle from crossing buildings
				while(pygame.sprite.spritecollide(self, buildings_group, False)):
					self.rect.x += speed
		if key[pygame.K_RIGHT] and self.rect.right < screen_width:
			self.rect.x += speed
			if pygame.sprite.spritecollide(self, buildings_group, False): #stops vheicle from crossing buildings
				while(pygame.sprite.spritecollide(self, buildings_group, False)):
					self.rect.x -= speed	
		if key[pygame.K_DOWN] and self.rect.y < screen_height-25:
			self.rect.y += speed
			if pygame.sprite.spritecollide(self, buildings_group, False): #stops vheicle from crossing buildings
				while(pygame.sprite.spritecollide(self, buildings_group, False)):
					self.rect.y -= speed	
		if key[pygame.K_UP] and self.rect.y > 0: 
			self.rect.y -= speed
			if pygame.sprite.spritecollide(self, buildings_group, False): #stops vheicle from crossing buildings
				while(pygame.sprite.spritecollide(self, buildings_group, False)):
					self.rect.y += speed
		#update mask
		self.mask = pygame.mask.from_surface(self.image)

		#draw health bar
		return 

class cops(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		img = pygame.image.load("img/whoop-whoop.png")
		self.image = pygame.transform.scale(img, (20, 20))
		self.rect = self.image.get_rect()
		self.rect.center = [x, y]
		self.xspeed = 2
		self.yspeed = 0
	def update(self):
		self.rect.x += self.xspeed
		self.rect.y += self.yspeed
		if self.rect.left <= 0:
			self.xspeed = 2
		if self.rect.right > screen_width:
			self.xspeed = -2
		if self.rect.y >= screen_height -25:
			self.yspeed = -2
		if self.rect.y < 0:
			self.yspeed = 2
		if pygame.sprite.spritecollide(self, buildings_group, False) and self.yspeed > 0: #stops vheicle from crossing buildings
			while(pygame.sprite.spritecollide(self, buildings_group, False)):
				self.rect.y -= self.yspeed
		if pygame.sprite.spritecollide(self, buildings_group, False) and self.yspeed < 0: #stops vheicle from crossing buildings
			while(pygame.sprite.spritecollide(self, buildings_group, False)):
				self.rect.y += self.yspeed
		if pygame.sprite.spritecollide(self, buildings_group, False) and self.xspeed > 0: #stops vheicle from crossing buildings
			while(pygame.sprite.spritecollide(self, buildings_group, False)):
				self.rect.x -= self.xspeed
		if pygame.sprite.spritecollide(self, buildings_group, False) and self.xspeed < 0: #stops vheicle from crossing buildings
			while(pygame.sprite.spritecollide(self, buildings_group, False)):
				self.rect.x += self.xspeed
		if pygame.sprite.spritecollide(self, intersections_group, False):
			direction = random.randint(1,4)
			if direction == 1:
				self.xspeed = 2
				self.yspeed = 0
			if direction == 2:
				self.xspeed = 0
				self.yspeed = 2
			if direction == 3:
				self.xspeed = -2
				self.yspeed = 0
			if direction == 4:
				self.xspeed = 0
				self.yspeed = -2 
		



#create sprite groups
vehicle_group = pygame.sprite.Group()
cops_group = pygame.sprite.Group()
buildings_group = pygame.sprite.Group()
intersections_group = pygame.sprite.Group()

#create player
vehicle = Vehicle(int(screen_width / 2), screen_height - 100, 3)
vehicle_group.add(vehicle)

police = cops(15, int(screen_height/2))
cops_group.add(police)

def create_buildings():
	#generate buildings
	for row in range(buildingRows):
		for item in range(buildingCols):
			building = buildings(item * 187, row * 154)
			buildings_group.add(building)
def create_intersections():
	#create hidden junctions of roads
	for row in range(junctionRows):
		for item in range(junctionCols):
			intersection = intersections(137*(row+1) + 50*(row), 104*(item+1) + 50*(item))
			intersections_group.add(intersection)




create_buildings()
create_intersections()





run = True
while run:

	
	clock.tick(fps)
	
	draw_bg()
	
	#draw background

	
	buildings_group.update()
	intersections_group.update()
	vehicle.update()
	police.update()
		
	

	#draw sprite groups
	buildings_group.draw(screen)
	intersections_group.draw(screen)
	cops_group.draw(screen)
	vehicle_group.draw(screen)
	#bg_group.draw(screen)
	#event handlers
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()

pygame.quit()
