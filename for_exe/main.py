import pygame
import time
import math
from random import randint
from pygame.locals import *

pygame.init()

scrW = 1000
scrH = 700
tileWidth = 50
tileHeight = 50
win = pygame.display.set_mode((scrW,scrH))
pygame.display.set_caption("Open_World_Prj")
text_list = ""

#controller.py
def turn(c = 'N'):
	if c == 'w':
		P.back = True
		P.front = False
		P.left = False
		P.right = False

	elif c == 'a':
		P.back = False
		P.front = False
		P.left = True
		P.right = False

	elif c == 's':
		P.back = False
		P.front = True
		P.left = False
		P.right = False

	elif c == 'd':
		P.back = False
		P.front = False
		P.left = False
		P.right = True

def go_north():
	P.idle = False
	turn('w')
	P.y -= P.runSpeed
	print("P1.x : " + str(P.x) + ", P1.y : " + str(P.y))
	print("player x : " + str(P.x/50) + "player y : " + str(P.y/50))

def go_south():
	P.idle = False
	turn('s')
	P.y += P.runSpeed
	print("P1.x : " + str(P.x) + ", P1.y : " + str(P.y))
	print("player x : " + str(P.x/50) + "player y : " + str(P.y/50))

def go_west():
	P.idle = False
	turn('a')
	P.x -= P.runSpeed
	print("P1.x : " + str(P.x) + ", P1.y : " + str(P.y))
	print("player x : " + str(P.x/50) + "player y : " + str(P.y/50))

def go_east():
	P.idle = False
	turn('d')
	P.x += P.runSpeed
	print("P1.x : " + str(P.x) + ", P1.y : " + str(P.y))
	print("player x : " + str(P.x/50) + "player y : " + str(P.y/50))

def control():
	keys = pygame.key.get_pressed()

	P.idle = True
	if keys[pygame.K_w]:
		turn('w')
	elif keys[pygame.K_a]:
		turn('a')
	if keys[pygame.K_s]:
		turn('s')
	elif keys[pygame.K_d]:
		turn('d')

	if keys[pygame.K_w] and P.y / 50 > 0:
		if walkable(new_map.Geo[(P.y / 50) - 1][P.x / 50], new_map.env[(P.y / 50) - 1][P.x / 50]):
			if P.y % 50 != P.runSpeed:
				go_north()
		else:
			go_north()

	elif keys[pygame.K_s] and P.y / 50 < new_map.max_y - 1:
		if walkable(new_map.Geo[(P.y / 50) + 1][P.x / 50], new_map.env[(P.y / 50) + 1][P.x / 50]):
			if P.y % 50 != 50 - P.runSpeed:
				go_south()
		else:
			go_south()

	if keys[pygame.K_a] and P.x / 50 > 0:
		if walkable(new_map.Geo[P.y / 50][(P.x / 50) - 1], new_map.env[P.y / 50][(P.x / 50) - 1]):
			if P.x % 50 != P.runSpeed:
				go_west()
		else:
			go_west()

	elif keys[pygame.K_d] and P.x / 50 < new_map.max_x - 1:
		if walkable(new_map.Geo[P.y / 50][(P.x / 50) + 1], new_map.env[P.y / 50][(P.x / 50) + 1]):
			if P.x % 50 != 50 - P.runSpeed:
				go_east()
		else:
			go_east()
		
def walkable(geo, env):
	if geo == water[0] or geo == water[1] or geo == stone_bl[0] or geo == stone_bl[1] or geo == wood_bl[0] or geo == wood_bl[1] or env != None:
		return True

	else:
		return False

#text_box
def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def txt(text, color = (10, 10, 10), fsize = 30, x = 0, y = 0):
    largeText = pygame.font.Font('freesansbold.ttf',fsize)
    TextSurf, TextRect = text_objects(text, largeText, color)
    TextRect.center = (x, y)
    win.blit(TextSurf, TextRect)

    pygame.display.update()

def MainMenu_tb():
	rectW = 710
	rectH = 50
	pygame.draw.rect(win, (180, 180, 180), (((scrW/2) - (rectW/2)), ((scrH/2) - (rectH/2)), rectW, rectH))
	rectW = 700
	rectH = 40
	pygame.draw.rect(win, (100, 100, 100), (((scrW/2) - (rectW/2)), ((scrH/2) - (rectH/2)), rectW, rectH))
	EntrUrNm = "Enter your name"
	txt(EntrUrNm, (100, 100, 100), 50, (scrW/2), (scrH/2) - 70)
	txt(text_list, (10, 10, 10), 30, (scrW/2), (scrH/2))

def typing(text_list):
	keys = pygame.key.get_pressed()
	if len(text_list) < 20:
		if keys[pygame.K_a]:
			text_list += "a"
		if keys[pygame.K_b]:
			text_list += "b"
		if keys[pygame.K_c]:
			text_list += "v"
		if keys[pygame.K_d]:
			text_list += "d"
		if keys[pygame.K_e]:
			text_list += "e"
		if keys[pygame.K_f]:
			text_list += "f"
		if keys[pygame.K_g]:
			text_list += "g"
		if keys[pygame.K_h]:
			text_list += "h"
		if keys[pygame.K_i]:
			text_list += "i"
		if keys[pygame.K_j]:
			text_list += "j"
		if keys[pygame.K_k]:
			text_list += "k"
		if keys[pygame.K_l]:
			text_list += "l"
		if keys[pygame.K_m]:
			text_list += "m"
		if keys[pygame.K_n]:
			text_list += "n"
		if keys[pygame.K_o]:
			text_list += "o"
		if keys[pygame.K_p]:
			text_list += "p"
		if keys[pygame.K_q]:
			text_list += "q"
		if keys[pygame.K_r]:
			text_list += "r"
		if keys[pygame.K_s]:
			text_list += "s"
		if keys[pygame.K_t]:
			text_list += "t"
		if keys[pygame.K_u]:
			text_list += "u"
		if keys[pygame.K_v]:
			text_list += "v"
		if keys[pygame.K_w]:
			text_list += "w"
		if keys[pygame.K_x]:
			text_list += "x"
		if keys[pygame.K_y]:
			text_list += "y"
		if keys[pygame.K_z]:
			text_list += "z"
		#if keys[pygame.K_]:

	return text_list

#update_display
def test_refresh(index, t_list = text_list):
	x = 10
	y = 10

	pygame.draw.rect(win, (0, 0, 0), (0, 0, scrW, scrH))
	win.blit(stand_F[index], (x, y))
	x += tileWidth + 20
	win.blit(stand_B[index], (x, y))
	x += tileWidth + 20
	win.blit(stand_L[index], (x, y))
	x += tileWidth + 20
	win.blit(stand_R[index], (x, y))
	x += tileWidth + 20
	win.blit(run_F[index], (x, y))
	x += tileWidth + 20
	win.blit(run_B[index], (x, y))
	x += tileWidth + 20
	win.blit(run_L[index], (x, y))
	x += tileWidth + 20
	win.blit(run_R[index], (x, y))
	x = 10
	y += tileHeight + 20
	win.blit(stone_bl[0], (x, y))
	x += tileWidth + 20
	win.blit(stone_bl[1], (x, y))
	x += tileWidth + 20
	win.blit(wood_bl[0], (x, y))
	x += tileWidth + 20
	win.blit(wood_bl[1], (x, y))
	x += tileWidth + 20
	win.blit(rock, (x, y))
	x += tileWidth + 20
	win.blit(tree, (x, y))
	x += tileWidth + 20
	win.blit(grass[0], (x, y))
	x += tileWidth + 20
	win.blit(grass[1], (x, y))
	x = 10
	y += tileHeight + 20
	win.blit(rocky[0], (x, y))
	x += tileWidth + 20
	win.blit(rocky[1], (x, y))
	x += tileWidth + 20
	win.blit(water[0], (x, y))
	x += tileWidth + 20
	win.blit(water[1], (x, y))
	x += tileWidth + 20
	win.blit(soil[0], (x, y))
	x += tileWidth + 20
	win.blit(soil[1], (x, y))
	x += tileWidth + 20
	win.blit(soil[2], (x, y))
	x += tileWidth + 20
	win.blit(soil[3], (x, y))
	x += tileWidth + 20
	win.blit(soil[4], (x, y))
	x += tileWidth + 20
	win.blit(soil[5], (x, y))
	MainMenu_tb()
	pygame.display.update()

def refresh():
	new_map.update(P.x, P.y)
	#P.update()
	pygame.display.update()

#sources.py
stand_F = [	pygame.transform.scale(pygame.image.load("img/character/stand_front/0.png"), (tileWidth, tileHeight)),
			pygame.transform.scale(pygame.image.load("img/character/stand_front/1.png"), (tileWidth, tileHeight)),
			pygame.transform.scale(pygame.image.load("img/character/stand_front/2.png"), (tileWidth, tileHeight)),
			pygame.transform.scale(pygame.image.load("img/character/stand_front/3.png"), (tileWidth, tileHeight)) ]

stand_B = [	pygame.transform.scale(pygame.image.load("img/character/stand_back/0.png"), (tileWidth, tileHeight)),
			pygame.transform.scale(pygame.image.load("img/character/stand_back/1.png"), (tileWidth, tileHeight)),
			pygame.transform.scale(pygame.image.load("img/character/stand_back/2.png"), (tileWidth, tileHeight)),
			pygame.transform.scale(pygame.image.load("img/character/stand_back/3.png"), (tileWidth, tileHeight)) ]

stand_L = [	pygame.transform.scale(pygame.image.load("img/character/stand_left/0.png"), (tileWidth, tileHeight)),
			pygame.transform.scale(pygame.image.load("img/character/stand_left/1.png"), (tileWidth, tileHeight)),
			pygame.transform.scale(pygame.image.load("img/character/stand_left/2.png"), (tileWidth, tileHeight)),
			pygame.transform.scale(pygame.image.load("img/character/stand_left/3.png"), (tileWidth, tileHeight)) ]

stand_R = [	pygame.transform.scale(pygame.image.load("img/character/stand_right/0.png"), (tileWidth, tileHeight)),
			pygame.transform.scale(pygame.image.load("img/character/stand_right/1.png"), (tileWidth, tileHeight)),
			pygame.transform.scale(pygame.image.load("img/character/stand_right/2.png"), (tileWidth, tileHeight)),
			pygame.transform.scale(pygame.image.load("img/character/stand_right/3.png"), (tileWidth, tileHeight)) ]

run_F = [	pygame.transform.scale(pygame.image.load("img/character/run_front/0.png"), (tileWidth, tileHeight)),
			pygame.transform.scale(pygame.image.load("img/character/run_front/1.png"), (tileWidth, tileHeight)),
			pygame.transform.scale(pygame.image.load("img/character/run_front/2.png"), (tileWidth, tileHeight)),
			pygame.transform.scale(pygame.image.load("img/character/run_front/3.png"), (tileWidth, tileHeight)) ]

run_B = [	pygame.transform.scale(pygame.image.load("img/character/run_back/0.png"), (tileWidth, tileHeight)),
			pygame.transform.scale(pygame.image.load("img/character/run_back/1.png"), (tileWidth, tileHeight)),
			pygame.transform.scale(pygame.image.load("img/character/run_back/2.png"), (tileWidth, tileHeight)),
			pygame.transform.scale(pygame.image.load("img/character/run_back/3.png"), (tileWidth, tileHeight)) ]

run_L = [	pygame.transform.scale(pygame.image.load("img/character/run_left/0.png"), (tileWidth, tileHeight)),
			pygame.transform.scale(pygame.image.load("img/character/run_left/1.png"), (tileWidth, tileHeight)),
			pygame.transform.scale(pygame.image.load("img/character/run_left/2.png"), (tileWidth, tileHeight)),
			pygame.transform.scale(pygame.image.load("img/character/run_left/3.png"), (tileWidth, tileHeight)) ]

run_R = [	pygame.transform.scale(pygame.image.load("img/character/run_right/0.png"), (tileWidth, tileHeight)),
			pygame.transform.scale(pygame.image.load("img/character/run_right/1.png"), (tileWidth, tileHeight)),
			pygame.transform.scale(pygame.image.load("img/character/run_right/2.png"), (tileWidth, tileHeight)),
			pygame.transform.scale(pygame.image.load("img/character/run_right/3.png"), (tileWidth, tileHeight)) ]

stone_bl = [	pygame.transform.scale(pygame.image.load("img/blocks/stone_block_link.png"), (tileWidth, tileHeight)),
				pygame.transform.scale(pygame.image.load("img/blocks/stone_block_end.png"), (tileWidth, tileHeight)) ]

wood_bl = [	pygame.transform.scale(pygame.image.load("img/blocks/wood_block_link.png"), (tileWidth, tileHeight)),
			pygame.transform.scale(pygame.image.load("img/blocks/wood_block_end.png"), (tileWidth, tileHeight)) ]

rock = pygame.transform.scale(pygame.image.load("img/resources/stone1.png"), (tileWidth, tileHeight))

tree = pygame.transform.scale(pygame.image.load("img/resources/tree1.png"), (tileWidth, tileHeight))

grass = [	pygame.transform.scale(pygame.image.load("img/tiles/grass/0.png"), (tileWidth, tileHeight)),
			pygame.transform.scale(pygame.image.load("img/tiles/grass/1.png"), (tileWidth, tileHeight)) ]

rocky = [	pygame.transform.scale(pygame.image.load("img/tiles/rocky/0.png"), (tileWidth, tileHeight)),
			pygame.transform.scale(pygame.image.load("img/tiles/rocky/1.png"), (tileWidth, tileHeight)) ]

water = [	pygame.transform.scale(pygame.image.load("img/tiles/water/deep.png"), (tileWidth, tileHeight)),
			pygame.transform.scale(pygame.image.load("img/tiles/water/shallow.png"), (tileWidth, tileHeight)) ]

soil = [	pygame.transform.scale(pygame.image.load("img/tiles/soil/normal.png"), (tileWidth, tileHeight)),
			pygame.transform.scale(pygame.image.load("img/tiles/soil/tiled.png"), (tileWidth, tileHeight)),
			pygame.transform.scale(pygame.image.load("img/tiles/soil/wet_tiled.png"), (tileWidth, tileHeight)),
			pygame.transform.scale(pygame.image.load("img/tiles/soil/wet_planted.png"), (tileWidth, tileHeight)),
			pygame.transform.scale(pygame.image.load("img/tiles/soil/planted.png"), (tileWidth, tileHeight)),
			pygame.transform.scale(pygame.image.load("img/tiles/soil/ripe.png"), (tileWidth, tileHeight)) ]

DN_cycle = [pygame.transform.scale(pygame.image.load("img/day_night_cycle/midnight_shade_none.png"), (scrW, scrH)),
			pygame.transform.scale(pygame.image.load("img/day_night_cycle/midnight_shade_torch.png"), (scrW, scrH)) ]

#player.py
class player():
	def __init__(self, max_x, max_y):
		self.x = randint(1, (max_x) - 1) * 50
		self.y = randint(1, (max_y) - 1) * 50
		self.idle = True
		self.front = True
		self.left = False
		self.right = False
		self.back = False
		self.index = 0
		self.runSpeed = 5

	def update(self):
		if self.index < 3:
			self.index += 1

		else:
			self.index = 0

		if self.idle == True:
			if self.front == True:
				win.blit(stand_F[self.index], (scrW / 2, (scrH / 2) - 20))

			elif self.left == True:
				win.blit(stand_L[self.index], (scrW / 2, (scrH / 2) - 20))

			elif self.right == True:
				win.blit(stand_R[self.index], (scrW / 2, (scrH / 2) - 20))

			elif self.back == True:
				win.blit(stand_B[self.index], (scrW / 2, (scrH / 2) - 20))

		else:
			if self.front == True:
				win.blit(run_F[self.index], (scrW / 2, (scrH / 2) - 20))

			elif self.left == True:
				win.blit(run_L[self.index], (scrW / 2, (scrH / 2) - 20))

			elif self.right == True:
				win.blit(run_R[self.index], (scrW / 2, (scrH / 2) - 20))

			elif self.back == True:
				win.blit(run_B[self.index], (scrW / 2, (scrH / 2) - 20))

# make_map.py
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
		river = True
		for y in range(self.max_y):
			li[y] = {}
			for x in range(self.max_x):
				tmp = randint(1, 10)
				if tmp % 4 == 0:
					li[y][x] = water[1]
				else:
					tmp = randint(0,1)
					li[y][x] = grass[tmp]

		while river:
			river = False
			pass

		self.Geo = li

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
						win.blit(self.env[y][x], (coord_x, coord_y - 15))

				if x == center_x+1 and y == center_y:
					P.update()

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

# main.py & init.py

clock = pygame.time.Clock()
fps = 7
new_map = map()
P = player(100, 70)
index = 0
while(True):
	clock.tick(fps)
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			break
	#control()
	text_list = typing(text_list)
	test_refresh(index)
	if index == 3:
		index = 0
	else:
		index += 1
	#refresh()
	#cycles()

pygame.quit()