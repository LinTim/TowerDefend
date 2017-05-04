import pygame

# Load your pictures
#-- Background:
shading = pygame.image.load('pics/16x12_shading.png')

#--------------------


#-- frame:
right_table = pygame.image.load('pics/right_table.png')

level = pygame.image.load('pics/level.png')

money = pygame.image.load('pics/money.png')


number = []
for i in range(10):
	number.append(pygame.image.load('pics/number/%d.png' % i))

#--------------------


#-- Unit:
# Menu page
play = pygame.image.load('pics/play.png')
play_size = play.get_size()

# Tools
upgrade_0 = pygame.image.load('pics/upgrade_0.png')
upgrade_0_size = upgrade_0.get_size()
upgrade_1 = pygame.image.load('pics/upgrade_1.png')

repair_0 = pygame.image.load('pics/repair_0.png')
repair_0_size = repair_0.get_size()
repair_1 = pygame.image.load('pics/repair_1.png')

sell_0 = pygame.image.load('pics/sell_0.png')
sell_0_size = sell_0.get_size()
sell_1 = pygame.image.load('pics/sell_1.png')

# Initial stage
leading_role = pygame.image.load('pics/leading_role.png')
leading_role_size = leading_role.get_size()

myst_array = pygame.image.load('pics/myst_array.png')
myst_array_size = myst_array.get_size()

# Towers
tower_size = (50,50)
tower_select = pygame.image.load('pics/tower_select.png')

tower_arrow = pygame.image.load('pics/tower_arrow.png')

tower_wall = pygame.image.load('pics/tower_wall.png')

# Enemys
monster = pygame.image.load('pics/monster.png')
monster_size = monster.get_size()

monster_walk = pygame.image.load('pics/monster_walk.png')
monster_walk_size = monster_walk.get_size()

#--------------------
