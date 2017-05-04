from setting import *



def keyControlMove(event, dx_dy, speed = 5):

	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_LEFT or event.key == pygame.K_a:
			dx_dy[0] = -speed
		elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
			dx_dy[1] = speed
		elif event.key == pygame.K_UP or event.key == pygame.K_w:
			dx_dy[2] = -speed
		elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
			dx_dy[3] = speed

	if event.type == pygame.KEYUP:
		if event.key == pygame.K_LEFT or event.key == pygame.K_a:
			dx_dy[0] = 0
		elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
			dx_dy[1] = 0
		elif event.key == pygame.K_UP or event.key == pygame.K_w:
			dx_dy[2] = 0
		elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
			dx_dy[3] = 0

	return dx_dy


def moveTo(location, dx_dy, unit_size = (0, 0) ):
	if location[0] >= 0 and location[0] <= window_size[0] - unit_size[0]:
		location[0] += dx_dy[0] + dx_dy[1]
	elif location[0] < 0:
		location[0] = 0
	elif location[0] >= window_size[0] - unit_size[0]:
		location[0] = window_size[0] - unit_size[0]
	if location[1] >= 0 and location[1] <= window_size[1] - unit_size[1]:
		location[1] += dx_dy[2] + dx_dy[3]
	elif location[1] < 0:
		location[1] = 0
	elif location[1] >= window_size[1] - unit_size[1]:
		location[1] = window_size[1] - unit_size[1]

	return location
