import pygame
from snakeAI import Snake, Field, Game, Algorithms
from deployment import Deploy

deployment = Deploy()

snake = Snake([(deployment.field_size[0] // 2, deployment.field_size[1] // 2)], deployment.speed, Algorithms.BFS)
field = Field(deployment.field_size, snake)
field.setUp()
Algorithms.field = field
game = Game(deployment.screen, field, deployment.ceil_size, deployment.ceil_border, deployment.H_FPS, deployment.FPS, deployment.colors)

while True:
        game.EventListener()
        field.eventHandler()
        game.rendering()
        pygame.display.flip()


#TODO
# 1. Перенести HFPS функцию в класс ✅
# 2. Начинать делать алгоритм ✅
# 3. Перенести все данные в базу в отдельный файл ✅
# 4. Сделать функцию для развертывания pygame ✅
# 5. Сделать названия без капса ✅
# 5Algo. Сделать чтобы алгоритм мог видеть преграды на поле, яблоки, границы поля, и восстановление маршрута. ✅
# 6Algo. Продумать обучение для змейки, чтобы она не загоняла себя в г-образную ловушку у границы
# 7. А*
