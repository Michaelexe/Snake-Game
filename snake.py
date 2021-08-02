import pygame as pg
from snakeclasses import*

pg.init()

clock = pg.time.Clock()

window = pg.display.set_mode((690,510))
pg.display.set_caption("snake game")

apple = apple()

mainloop = True
run = True
restart_menu = False

circlex = 345
circley = 355
circle_radius = 25

def drawrestart(window):
	global circlex
	global circley
	global circle_radius
	global run
	global mainloop
	global restart_menu

	deadfont = pg.font.SysFont('comicsans', 60, True)
	dead = deadfont.render("YOU DIED!", True, (255,255,255))

	restartfont = pg.font.SysFont('comicsans', 30, True)
	restart = restartfont.render("restart?", True, (255,255,255))

	optionfont = pg.font.SysFont('comicsans', 30, True)
	yes = optionfont.render("YES", True, (255,255,255))
	no = optionfont.render("NO", True, (255,255,255))

	scorefont = pg.font.SysFont('comicsans', 40, True)
	score = scorefont.render("Your score was : " + str(snake.score_value), True, (255,255,255))


	keys = pg.key.get_pressed()

	if keys[pg.K_LEFT]:
		circlex -= 5

	if keys[pg.K_RIGHT]:
		circlex += 5

	if circlex <= 260:
		run = True
		restart_menu = False
		snake.score_value = 0
		circlex = 345

	if circlex >= 440:
		run = False
		restart_menu =  False
		mainloop = False


	window.fill((0,0,0))
	window.blit(dead, (220, 120))
	window.blit(score, (200, 180))
	window.blit(restart, (300, 230))
	window.blit(yes, (200, 350))
	window.blit(no, (460, 350))
	pg.draw.circle(window, (0, 255, 255), (circlex, circley), circle_radius)


def death_check():
	global restart_menu
	global run 

	if snake.position[0][0] == 690 or snake.position[0][0] < 0 or snake.position[0][1] < 0 or snake.position[0][1] == 510:
		run = False
		restart_menu = True
		snake.position = [[60,0,2],[30,0,2],[0,0,2]]
		apple.position = [330,270]
		snake.turnleft = []
		snake.turnright = []
		snake.turnup = []
		snake.turndown = []

	for blocks in snake.position[1:]:
		if [snake.position[0][0], snake.position[0][1]] == [blocks[0], blocks[1]]:
			run = False
			restart_menu = True
			snake.position = [[60,0,2],[30,0,2],[0,0,2]]
			apple.position = [330,270]
			snake.turnleft = []
			snake.turnright = []
			snake.turnup = []
			snake.turndown = []

while mainloop:

	while run:

		for event in pg.event.get():
			if event.type == pg.QUIT:
				run = False
				mainloop = False

		clock.tick(3)

		snake.user_input()
		snake.move()
		apple.eat()
		snake.draw(window)
		apple.draw(window)
		snake.draw_score(window)
		death_check()
		pg.display.update()


	while restart_menu:

		for event in pg.event.get():
			if event.type == pg.QUIT:
				restart_menu = False
				mainloop = False

		clock.tick(20)

		drawrestart(window)
		pg.display.update()

pg.quit()