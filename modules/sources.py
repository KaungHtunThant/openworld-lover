import pygame
from pygame.locals import *


pygame.init()

#Sources of images and audios
scrW = 1000
scrH = 700
tileWidth = 50
tileHeight = 50
win = pygame.display.set_mode((scrW,scrH))
pygame.display.set_caption("Open_World_Prj")

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