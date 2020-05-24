import pygame
from pygame.locals import *
from random import randint
from sources import *
from player import *

class map():
	def __init__(self):
		self.max_x = 100
		self.max_y = 70
		self.Geo = {}
		self.makeMap()
		self.env = {}
		self.treemax = 2000
		self.treeCount = 0
		self.makeEnv()

	def makeMap(self):
		li = {}
		for y in range(self.max_y):
			li[y] = {}
			for x in range(self.max_x):
				tmp = randint(1, 10)
				if tmp % 7 == 0:
					li[y][x] = water[1]

				else:
					li[y][x] = grass[randint(0, 1)]

		self.Geo = li

	#Backup
	# def update(self, player_x, player_y):
	# 	if (player_x % 100 > 50):
	# 		coord_x = 0 - ((player_x % 100) - 50)
	# 		start_x = 11
	# 		end_x = 10
	# 	else:
	# 		coord_x = -100 + (player_y % 50)
	# 		start_x = 10
	# 		end_x = 11

	# 	tmpx = coord_x

	# 	if (player_y % 100 > 50):
	# 		coord_y = -100 + (player_y % 50)
	# 		start_y = 8
	# 		end_y = 7

	# 	else:
	# 		coord_y = (player_y % 100) - 50
	# 		start_y = 7
	# 		end_y = 8

	# 	center_x = (player_x) / 10
	# 	center_y = (player_y) / 10

	# 	for y in range(center_y - start_y, center_y + end_y):
	# 		for x in range(center_x - start_x, center_x + end_x):
	# 			#print("x : " + str(x) + "\ny : " + str(y))
	# 			if x < 0 or y < 0 or x > (self.max_x - 1) or y > (self.max_y - 1):
	# 				if y == -1 and x > -1 and x < 100:
	# 					win.blit(stone_bl[1], (coord_x, coord_y))

	# 				else:
	# 					win.blit(stone_bl[0], (coord_x, coord_y))

	# 			else:
	# 				win.blit(self.Geo[y][x], (coord_x, coord_y))
	# 				if self.env[y][x] == None:
	# 					pass
	# 				else:
	# 					win.blit(self.env[y][x], (coord_x, coord_y - 25))

	# 			coord_x += tileWidth
	# 		coord_y += tileHeight
	# 		coord_x = tmpx

	def update(self, player_x, player_y):

		coord_x = - ((player_x % 50) + 22)
		coord_y = - ((player_y % 50) + 22)
		tmpx = coord_x
		center_x = player_x / 50
		center_y = player_y / 50

		for y in range(center_y - 8, center_y + 8):
			for x in range(center_x - 11, center_x + 11):
				#print("x : " + str(x) + "\ny : " + str(y))
				if x < 0 or y < 0 or x > (self.max_x - 1) or y > (self.max_y - 1):
					if y == -1 and x > -1 and x < 100:
						win.blit(stone_bl[1], (coord_x, coord_y))

					else:
						win.blit(stone_bl[0], (coord_x, coord_y))

				else:
					win.blit(self.Geo[y][x], (coord_x, coord_y))
					if self.env[y][x] == None:
						pass
					else:
						win.blit(self.env[y][x], (coord_x, coord_y - 25))

				coord_x += tileWidth
			coord_y += tileHeight
			coord_x = tmpx

	def makeEnv(self):
		li = {}
		for y in range(self.max_y):
			li[y] = {}
			for x in range(self.max_x):
				tmp = randint(1, 10)
				if tmp % 4 == 0 and self.treeCount < self.treemax and (self.Geo[y][x] == grass[0] or self.Geo == grass[1]):
					tmp = randint(0, 3)
					if tmp == 2:
						li[y][x] = rock

					else:
						li[y][x] = tree
				else:
					li[y][x] = None

		self.env = li


new_map = map()