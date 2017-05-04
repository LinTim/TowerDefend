# -*- coding: utf8 -*-

# import os
# import pygame
from modules.create_window import *
# from modules.key_control_move import *
from modules.color_name import *
from pics import *
import copy



# The first and the second number are the start position (x,y).
# r,l,u,d = right,left,up,down
# The number after english word is how many block it moves.
monster_walk_path = "81r3d10l2u8l5u1l2d9r2u6r2d1r1d2l1d2"
def translateMonsterWalkPath(data):
	"""
	Translate the monster_walk_path to a list and return it.
	"""
	path = []
	pos = [0,0]
	for i in range(len(data)):
		if i == 0:
			pos[0] = 50*(int(data[i])-1)
		elif i == 1:
			pos[1] = 50*(int(data[i])-1)
			path.append(copy.copy(pos))
		else:
			move = [0,0]
			if data[i] == "l":
				move = [-50,0]
			elif data[i] == "r":
				move = [50,0]
			elif data[i] == "u":
				move = [0,-50]
			elif data[i] == "d":
				move = [0,50]
			if move != [0,0]:
				rang = int(data[i+1])
				if i+2 < len(data):
					if data[i+2] in "0123456789":
						rang = int(data[i+1:i+3])
				for t in range(rang):
					pos[0] += move[0]
					pos[1] += move[1]
				path.append(copy.copy(pos))
	return path

def showMonsterWalkPath(data_list):
	"""
	showMonsterWalkPath(data_list)
	The data_list should be a 2D list. 
	"""
	pos = [0,0]
	for i in range(len(data_list)):
		if i == 0:
			pos = copy.copy(data_list[i])
			gameDisplay.blit(monster_walk, pos)
		else:
			monster_move = False
			num_cal = [1,0,0]
			dx = (data_list[i][0] - pos[0])/50
			dy = (data_list[i][1] - pos[1])/50
			if dx < 0 or dy < 0:
				num_cal[0] = -1
			if dx != 0:
				monster_move = True
				num_cal[1] = 1
			elif dy != 0:
				monster_move = True
				num_cal[2] = 1
			if monster_move:
				for t in range(abs(dx+dy)):
					pos[0] += num_cal[0]*num_cal[1]*50
					pos[1] += num_cal[0]*num_cal[2]*50
					gameDisplay.blit(monster_walk, pos)

def createMonsterWalkPath(data_list, init_pos):
	"""
	createMonsterWalkPath(data_list, init_pos)
	"""
	path = []
	pos = copy.copy(init_pos)
	path.append(copy.copy(pos))
	monster_size = 20
	side_d = (50-monster_size)/2

	for i in data_list:
		pos_temp = [0,0]
		pos_temp[0] = pos[0]-side_d
		pos_temp[1] = pos[1]-side_d

		dx = i[0] - pos_temp[0]
		dy = i[1] - pos_temp[1]

		move_info = [1,0,0]
		if dx < 0 or dy < 0:
			move_info[0] = -1
		if dx != 0:
			move_info[1] = 1
		elif dy != 0:
			move_info[2] = 1
		for t in range(abs(dx+dy)):
			pos[0] += move_info[0]*move_info[1]
			pos[1] += move_info[0]*move_info[2]
			path.append(copy.copy(pos))

	dx = (250+side_d) - pos[0]
	dy = (500+side_d) - pos[1]
	move_info = [1,0,0]
	if dx < 0 or dy < 0:
		move_info[0] = -1
	if dx != 0:
		move_info[1] = 1
	elif dy != 0:
		move_info[2] = 1
	for t in range(abs(dx+dy)-side_d):
		pos[0] += move_info[0]*move_info[1]
		pos[1] += move_info[0]*move_info[2]
		path.append(copy.copy(pos))

	return path


def showMonster(monster, pos):
	gameDisplay.blit(monster, pos)



def run():
	font = pygame.font.SysFont("colonna", 40)
	font_live = pygame.font.SysFont("colonna", 40, True)
	font_start = pygame.font.SysFont("colonna", 110)

	text_1 = font_start.render("-+-[Tower", 1, (0, 0, 0))
	text_2 = font_start.render("Defend]-+-", 1, (0, 0, 0))
	text_line = font_start.render("____", 1, (0, 0, 0))
	text_line_1 = font_start.render("/", 1, (0, 0, 0))
	text_line_2 = font_start.render("\\", 1, (0, 0, 0))

	level_now = "00"
	money_now = "00000"
	live_now = "20"

	sell_price = 0

	# location = [window_size[0] * 0.5, window_size[1] * 0.5]

	# dx_dy = [0,0,0,0]

	clock = pygame.time.Clock()

	playing = False
	drop_it = False
	tower_type_num = 0
	tower_type = [leading_role, \
								myst_array, \
								tower_wall, \
								tower_arrow]
	tower_type_size = [leading_role_size, \
										 myst_array_size, \
										 tower_size, \
										 tower_size]
	builded_towers = [leading_role, \
										myst_array, \
										myst_array]
	builded_towers_pos = [[(250,500), 0], \
												[(250,0), 1], \
												[(300,0), 1]]
	stop = False

	monster_init_pos_0 = [265,15]
	monster_init_pos_1 = [315,15]
	monsters_pos = {}

	monster_path_corner_list = translateMonsterWalkPath(monster_walk_path)
	monster_path_point_list = createMonsterWalkPath(monster_path_corner_list, monster_init_pos_1)

	crashed = False

	while not crashed:
		mouse_pos = pygame.mouse.get_pos()
		mouse_pos_re = (mouse_pos[0]-25,mouse_pos[1]-25)
		text_live = font_live.render(live_now, 1, white, black)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				crashed = True
				break

			# print event

			if event.type == pygame.KEYDOWN:
				if playing:
					if event.key == pygame.K_ESCAPE:
						if stop:
							stop = False
						elif drop_it:
							drop_it = False
						elif not stop and not drop_it:
							stop = True

			if stop:
				pass
			else:
				if event.type == pygame.MOUSEBUTTONUP:
					if playing:
						#-- Right frame:
						# Tools
						if pygame.Rect((676, 135), sell_0_size).collidepoint(mouse_pos):
							money_temp = int(money_now) + sell_price
							if money_temp > 99999:
								money_temp = 99999
							money_now = money_now[0:5-len(str(money_temp))] + str(money_temp)

						# Towers
						if pygame.Rect((612, 192), tower_size).collidepoint(mouse_pos):
							drop_it = True
							tower_type_num = 2
						if pygame.Rect((675, 192), tower_size).collidepoint(mouse_pos):
							drop_it = True
							tower_type_num = 3

						#--------------------

						#-- Left frame:
						# Build tower
						if drop_it:
							build_pos = ((mouse_pos[0]//50)*50,(mouse_pos[1]//50)*50)
							no_prob = True
							if pygame.Rect(600, 0, 200, 600).collidepoint(build_pos):
								continue
							for i in builded_towers_pos:
								if pygame.Rect(i[0], tower_type_size[i[1]]).collidepoint(build_pos):
									no_prob = False
									break
							if no_prob:
								builded_towers.append(tower_type[tower_type_num])
								builded_towers_pos.append([build_pos, tower_type_num])

						#--------------------

					else:
						if pygame.Rect((300, 350), play_size).collidepoint(mouse_pos):
							playing = True


			# end event


		if stop:
			pass
		else:
			gameDisplay.fill(white) # background

			if playing:
				#-- background:
				showMonsterWalkPath(monster_path_corner_list)
				gameDisplay.blit(shading, (0, 0))

				#--------------------


				#-- Right frame:
				gameDisplay.blit(right_table, (600, 0))

				# Infomations
					# Level
				gameDisplay.blit(level, (613, 13))
				gameDisplay.blit(number[int(str(level_now)[0])], (733, 13))
				gameDisplay.blit(number[int(str(level_now)[1])], (758, 13))
					# Money
				gameDisplay.blit(money, (613, 74))
				gameDisplay.blit(number[int(str(money_now)[0])], (655, 74))
				gameDisplay.blit(number[int(str(money_now)[1])], (680, 74))
				gameDisplay.blit(number[int(str(money_now)[2])], (705, 74))
				gameDisplay.blit(number[int(str(money_now)[3])], (730, 74))
				gameDisplay.blit(number[int(str(money_now)[4])], (755, 74))

				# Tools
				if not pygame.Rect((739, 135), upgrade_0_size).collidepoint(mouse_pos):
					gameDisplay.blit(upgrade_0, (739, 135))
				else:
					gameDisplay.blit(upgrade_1, (739, 135))

				if not pygame.Rect((613, 135), repair_0_size).collidepoint(mouse_pos):
					gameDisplay.blit(repair_0, (613, 135))
				else:
					gameDisplay.blit(repair_1, (613, 135))

				if not pygame.Rect((676, 135), sell_0_size).collidepoint(mouse_pos):
					gameDisplay.blit(sell_0, (676, 135))
				else:
					gameDisplay.blit(sell_1, (676, 135))

				# Towers
				gameDisplay.blit(tower_wall, (612, 192))
				if pygame.Rect((612, 192), tower_size).collidepoint(mouse_pos):
					gameDisplay.blit(tower_select, (612, 192))

				gameDisplay.blit(tower_arrow, (675, 192))
				if pygame.Rect((675, 192), tower_size).collidepoint(mouse_pos):
					gameDisplay.blit(tower_select, (675, 192))

				#--------------------


				#-- object

				# Towers on map
				for i in range(len(builded_towers_pos)):
					gameDisplay.blit(builded_towers[i], builded_towers_pos[i][0])

				# Live
				gameDisplay.blit(text_live, (280, 550))

				# Show the block mouse on it
				if pygame.Rect((0, 0), (600, 600)).collidepoint(mouse_pos):
					gameDisplay.blit(tower_select, (mouse_pos[0]//50*50, mouse_pos[1]//50*50))

				# Drop the tower that you want to build
				if drop_it:
					gameDisplay.blit(tower_type[tower_type_num], mouse_pos_re)

				# Monsters
				if 0 not in monsters_pos:
					monsters_pos[0] = {}
					monsters_pos[0]["move_times"] = 0
					monsters_pos[0]["pos"] = monster_init_pos_1
				showMonster(monster, monsters_pos[0]["pos"])

				cannot_move = False
				for i in builded_towers_pos:
					if pygame.Rect(i[0], tower_type_size[i[1]]).colliderect(pygame.Rect(monsters_pos[0]["pos"],monster_size)) and not i[1] == 1:
						cannot_move = True
						break
				if not cannot_move:
					monsters_pos[0]["move_times"] += 1
					monsters_pos[0]["pos"] = monster_path_point_list[monsters_pos[0]["move_times"]]
				elif pygame.Rect(builded_towers_pos[0][0], leading_role_size).colliderect(pygame.Rect(monsters_pos[0]["pos"],monster_size)):
					live_now = str(int(live_now)-1)
					del monsters_pos[0]

				#--------------------

			else:
				# Menu page
				gameDisplay.blit(text_1, (81, 121))
				gameDisplay.blit(text_1, (80, 120))
				gameDisplay.blit(text_2, (251, 191))
				gameDisplay.blit(text_2, (250, 190))

				gameDisplay.blit(text_line, (290, 260))
				gameDisplay.blit(text_line, (290, 360))
				gameDisplay.blit(text_line_1, (240, 340))
				gameDisplay.blit(text_line_2, (240, 370))
				gameDisplay.blit(text_line_1, (506, 370))
				gameDisplay.blit(text_line_2, (506, 340))

				gameDisplay.blit(play, (300, 350))
				if pygame.Rect(300, 350, play_size[0], play_size[1]).collidepoint(mouse_pos):
					gameDisplay.blit(text_line, (290, 270))
					gameDisplay.blit(text_line, (290, 350))
					gameDisplay.blit(text_line_1, (230, 320))
					gameDisplay.blit(text_line_2, (230, 390))
					gameDisplay.blit(text_line_1, (516, 390))
					gameDisplay.blit(text_line_2, (516, 320))



		pygame.display.update()
		clock.tick(game_speed)



if __name__ == "__main__":
  run()
  pygame.quit()