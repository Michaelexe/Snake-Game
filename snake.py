import pygame as pg
from snakeclasses import*

pg.init()

clock = pg.time.Clock()

window = pg.display.set_mode((690,510))
pg.display.set_caption("snake game")

apple = apple()

run = True

def death_check():

	global run 

	if snake.position[0][0] == 690 or snake.position[0][0] < 0 or snake.position[0][1] < 0 or snake.position[0][1] == 510:
		run = False

	for blocks in snake.position[1:]:
		if [snake.position[0][0], snake.position[0][1]] == [blocks[0], blocks[1]]:
			run = False

while run:

	for event in pg.event.get():
		if event.type == pg.QUIT:
			run = False

	clock.tick(3)

	snake.user_input()
	snake.move()
	apple.eat()
	snake.draw(window)
	apple.draw(window)
	death_check()
	pg.display.update()

pg.quit()