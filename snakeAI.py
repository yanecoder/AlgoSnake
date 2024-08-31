import pygame
import random

class Algorithms:

    count = 0
    field = None

    @staticmethod
    def test(head):
        if Algorithms.count == 0:
            Algorithms.count += 1
            return (-1, 0)
        elif Algorithms.count == 1:
            Algorithms.count = 0
            return (0, 1)

    @staticmethod
    def BFS(head):

        def checkCeil(x, y, list, visited, prev_ceil):
            cur_ceil = Algorithms.field.field
            if (x >= 0 and x < len(cur_ceil)) and (y >= 0 and y < len(cur_ceil[0])):
                if visited[x][y] == "not visited" and (cur_ceil[x][y] == "ceil" or cur_ceil[x][y] == "apple"):
                    list.append((x, y))
                    visited[x][y] = prev_ceil

        list = [head]
        cur_ceil = Algorithms.field.field
        visited = [["not visited" for i in range(len(cur_ceil[0]))] for i in range(len(cur_ceil))]
        visited[head[0]][head[1]] = "start"

        while len(list) > 0:
            current = list[0]
            checkCeil(current[0]-1, current[1], list, visited, current)
            checkCeil(current[0], current[1]-1, list, visited, current)
            checkCeil(current[0]+1, current[1], list, visited, current)
            checkCeil(current[0], current[1]+1, list, visited, current)
            list.pop(0)

            cur_ceil = Algorithms.field.field
            x = current[0]
            y = current[1]
            if cur_ceil[x][y] == "apple":
                cur_ceil_rev = (x, y)
                path = []
                while visited[cur_ceil_rev[0]][cur_ceil_rev[1]] != "start":
                    path.append(cur_ceil_rev)
                    cur_ceil_rev = visited[cur_ceil_rev[0]][cur_ceil_rev[1]]
                return (path[-1][0] - head[0], path[-1][1] - head[1])





class Snake:

    def __init__(self, body, speed, algorithm):
        self.body = body
        self.algorithm = algorithm
        self.speed = speed

    def movement(self):
        try:
            self.speed = self.algorithm(self.body[-1])
            snake_step_x = self.body[-1][0] + self.speed[0]
            snake_step_y = self.body[-1][1] + self.speed[1]
            self.body.append((snake_step_x, snake_step_y))
        except Exception:
            self.speed = (1, 0)
            snake_step_x = self.body[-1][0] + self.speed[0]
            snake_step_y = self.body[-1][1] + self.speed[1]
            self.body.append((snake_step_x, snake_step_y))


class Field:

    def __init__(self, size, snake):
        self.size = size
        self.snake = snake

    def setUp(self):
        self.field = [["ceil" for i in range(self.size[1])] for j in range(self.size[0])]
        self.apple = (random.randint(0, self.size[0]-1), random.randint(0, self.size[1]-1))
        self.snake.body = [(self.size[0] // 2, self.size[1] // 2)]
        self.field[self.apple[0]][self.apple[1]] = "apple"
        self.field[self.snake.body[0][0]][self.snake.body[0][1]] = "snake"

    def eventHandler(self):
        self.snake.movement()

        if self.snake.body[-1][0] == self.size[0] or self.snake.body[-1][1] == self.size[1] or self.snake.body[-1][0] < 0 or self.snake.body[-1][1] < 0:
            self.setUp()

        snake_head_x = self.snake.body[-1][0]
        snake_head_y = self.snake.body[-1][1]
        snake_tail_x = self.snake.body[0][0]
        snake_tail_y = self.snake.body[0][1]
        cur_ceil = self.field[snake_head_x][snake_head_y]
        self.field[snake_head_x][snake_head_y] = "snake"

        if cur_ceil != "apple" and cur_ceil != "snake":
            self.field[snake_tail_x][snake_tail_y] = "ceil"
            self.snake.body.remove(self.snake.body[0])
        elif cur_ceil == "snake":
            self.setUp()
        else:
            self.apple = (random.randint(0, self.size[0]-1), random.randint(0, self.size[1]-1))
            while self.field[self.apple[0]][self.apple[1]] != "ceil":
                self.apple = (random.randint(0, self.size[0]-1), random.randint(0, self.size[1]-1))
            self.field[self.apple[0]][self.apple[1]] = "apple"


class Game:

    def __init__(self, screen, exmField, ceil_size, ceil_border, H_FPS, FPS, colors):
        self.screen = screen
        self.exmField = exmField
        self.ceil_size = ceil_size
        self.ceil_border = ceil_border
        self.H_FPS = H_FPS
        self.FPS = FPS
        self.colors = colors
        self.clock = pygame.time.Clock()

    def EventListener(self):
        for frame in range(round(self.H_FPS / self.FPS)):
            self.clock.tick(self.H_FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()


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







