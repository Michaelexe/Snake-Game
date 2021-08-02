import pygame as pg
from time import sleep
from random import randrange

#1 = left
#2 = right
#3 = up
#4 = down

class snake():
	def __init__(self):
		self.position = [[60,0,2],[30,0,2],[0,0,2]]
		self.score_value = len(self.position) - 2
		
		self.turnleft = []
		self.turnright = []
		self.turnup = []
		self.turndown = []

	def user_input(self):
		keys = pg.key.get_pressed()

		if keys[pg.K_LEFT]:
			self.turnleft.append([self.position[0][0], self.position[0][1]])

		if keys[pg.K_RIGHT]:
			self.turnright.append([self.position[0][0], self.position[0][1]])

		if keys[pg.K_UP]:
			self.turnup.append([self.position[0][0], self.position[0][1]])

		if keys[pg.K_DOWN]:
			self.turndown.append([self.position[0][0], self.position[0][1]])

	def move(self):
		for block in self.position:
			if [block[0], block[1]] in self.turnleft and block[2] != 2:
				block[2] = 1

			if [block[0], block[1]] in self.turnright and block[2] != 1:
				block[2] = 2

			if [block[0], block[1]] in self.turnup and block[2] != 4:
				block[2] = 3

			if [block[0], block[1]] in self.turndown and block[2] != 3:
				block[2] = 4



		for block in self.position:
			if block[2] == 1:
				block[0] -= 30

			if block[2] == 2:
				block[0] += 30

			if block[2] == 3:
				block[1] -= 30

			if block[2] == 4:
				block[1] += 30


		

		if [self.position[-1][0], self.position[-1][1]] in self.turnleft:
			self.turnleft.remove([self.position[-1][0], self.position[-1][1]])
			self.position[-1][2] = self.position[-2][2]

		if [self.position[-1][0], self.position[-1][1]] in self.turnright:
			self.turnright.remove([self.position[-1][0], self.position[-1][1]])
			self.position[-1][2] = self.position[-2][2]

		if [self.position[-1][0], self.position[-1][1]] in self.turnup:
			self.turnup.remove([self.position[-1][0], self.position[-1][1]])
			self.position[-1][2] = self.position[-2][2]

		if [self.position[-1][0], self.position[-1][1]] in self.turndown:
			self.turndown.remove([self.position[-1][0], self.position[-1][1]])
			self.position[-1][2] = self.position[-2][2]

	def draw(self, window):
		window.fill((0,0,0))
		for block in self.position:
			pg.draw.rect(window, (255,0,0), (block[0], block[1], 30, 30))

	def draw_score(self, window):
		font = pg.font.SysFont('comicsans', 30, True)
		score = font.render("score : " + str(self.score_value), True, (255,255,255))
		window.blit(score, (570, 10))

				



snake = snake()


class apple():
	def __init__(self):
		self.position = [330,270]

	def eat(self):
		if [snake.position[0][0], snake.position[0][1]] == self.position:
			self.position = [randrange(0,690,30), randrange(0,510,30)]
			snake.score_value += 1

			if snake.position[-1][2] == 1:
				snake.position.append([snake.position[-1][0] + 30, snake.position[-1][1], 1])

			if snake.position[-1][2] == 2:
				snake.position.append([snake.position[-1][0] - 30, snake.position[-1][1], 2])

			if snake.position[-1][2] == 3:
				snake.position.append([snake.position[-1][0], snake.position[-1][1] + 30, 3])

			if snake.position[-1][2] == 4:
				snake.position.append([snake.position[-1][0], snake.position[-1][1] - 30, 4])

	def draw(self, window):
		pg.draw.rect(window, (0,255,0), (self.position[0], self.position[1], 30, 30))
