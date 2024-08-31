import pygame
import random

class Field:

    def __init__(self, size, snake):
        self.size = size
        self.snake = snake

    def setUp(self):
        self.field = [["ceil" for i in range(self.size[1])] for j in range(self.size[0])]
        self.apple = (random.randint(0, self.size[0]-1), random.randint(0, self.size[1]-1))
        self.snake = [(self.size[0] // 2, self.size[1] // 2)]
        self.field[self.apple[0]][self.apple[1]] = "apple"
        self.field[self.snake[0][0]][self.snake[0][1]] = "snake"

    def eventHandler(self, speed):
        snake_step_x = self.snake[-1][0] + speed[0]
        snake_step_y = self.snake[-1][1] + speed[1]
        self.snake.append((snake_step_x, snake_step_y))

        if snake_step_x == self.size[0] or snake_step_y == self.size[1] or snake_step_x < 0 or snake_step_y < 0:
            self.setUp()

        snake_head_x = self.snake[-1][0]
        snake_head_y = self.snake[-1][1]
        snake_tail_x = self.snake[0][0]
        snake_tail_y = self.snake[0][1]
        cur_ceil = self.field[snake_head_x][snake_head_y]
        self.field[snake_head_x][snake_head_y] = "snake"

        if cur_ceil != "apple" and cur_ceil != "snake":
            self.field[snake_tail_x][snake_tail_y] = "ceil"
            self.snake.remove(self.snake[0])
        elif cur_ceil == "snake":
            self.setUp()
        else:
            self.apple = (random.randint(0, self.size[0]-1), random.randint(0, self.size[1]-1))
            while self.field[self.apple[0]][self.apple[1]] != "ceil":
                self.apple = (random.randint(0, self.size[0]-1), random.randint(0, self.size[1]-1))
            self.field[self.apple[0]][self.apple[1]] = "apple"

class Game:

    def __init__(self, screen, exmField, ceil_size, ceil_border, HFPS, FPS, colors):
        self.screen = screen
        self.exmField = exmField
        self.ceil_size = ceil_size
        self.ceil_border = ceil_border
        self.HFPS = HFPS
        self.FPS = FPS
        self.colors = colors

    def rendering(self):
        self.screen.fill((0, 0, 0))
        for cx in range(self.exmField.size[0]):
            for cy in range(self.exmField.size[1]):
                if self.exmField.field[cx][cy] == "snake":
                    pygame.draw.rect(self.screen, self.colors["snake"], (cx * self.ceil_size, cy * self.ceil_size, self.ceil_size, self.ceil_size))
                elif self.exmField.field[cx][cy] == "apple":
                    pygame.draw.rect(self.screen, self.colors["apple"], (cx * self.ceil_size, cy * self.ceil_size, self.ceil_size, self.ceil_size))
                else:
                    pygame.draw.rect(self.screen, self.colors["ceil"], (cx * self.ceil_size, cy * self.ceil_size, self.ceil_size, self.ceil_size),
                                     self.ceil_border)







