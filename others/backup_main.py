import pygame
import random

pygame.init()
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("SnakeAI")
clock = pygame.time.Clock()
H_FPS = 120
FPS = 7

COLORS = {
    "ceil": (10, 10, 10),
    "snake": (50, 118, 0),
    "apple": (188, 14, 14)
}
CEIL_SIZE = 20
CEIL_BORDER = 1
FIELD_X = window_size[0] // CEIL_SIZE
FIELD_Y = window_size[1] // CEIL_SIZE
FIELD_SIZE = (FIELD_X, FIELD_Y)
SPEED = (1, 0)


def restart():
    screen.fill((0, 0, 0))
    global field
    global snake
    field = [["ceil" for i in range(FIELD_SIZE[1])] for j in range(FIELD_SIZE[0])]
    snake = [(FIELD_X // 2, FIELD_Y // 2)]
    apple = [(random.randint(0, FIELD_X - 1), random.randint(0, FIELD_Y - 1))]
    field[apple[0][0]][apple[0][1]] = "apple"
    field[snake[0][0]][snake[0][1]] = "snake"


# np.full() не работал, сделали свою матрицу
field = [["ceil" for i in range(FIELD_SIZE[1])] for j in range(FIELD_SIZE[0])]
snake = [(FIELD_X // 2, FIELD_Y // 2)]
apple = [(random.randint(0, FIELD_X - 1), random.randint(0, FIELD_Y - 1))]
field[apple[0][0]][apple[0][1]] = "apple"
field[snake[0][0]][snake[0][1]] = "snake"

snake_mover = 0
flag = True
while True:
    clock.tick(H_FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and SPEED != (0, 1) and flag:
                SPEED = (0, -1)
                flag = False
            elif event.key == pygame.K_s and SPEED != (0, -1) and flag:
                SPEED = (0, 1)
                flag = False
            elif event.key == pygame.K_a and SPEED != (1, 0) and flag:
                SPEED = (-1, 0)
                flag = False
            elif event.key == pygame.K_d and SPEED != (-1, 0) and flag:
                SPEED = (1, 0)
                flag = False

    snake_mover += 1

    if snake_mover == round(H_FPS / FPS):
        flag = True

        # Сложение двух элементов в кортеже
        snake_step_x = snake[-1][0] + SPEED[0]
        snake_step_y = snake[-1][1] + SPEED[1]
        snake.append((snake_step_x, snake_step_y))

        if snake_step_x == FIELD_X or snake_step_y == FIELD_Y or snake_step_x < 0 or snake_step_y < 0:
            restart()

        snake_head_x = snake[-1][0]
        snake_head_y = snake[-1][1]
        snake_tail_x = snake[0][0]
        snake_tail_y = snake[0][1]
        snake_tail = snake[0]
        cur_ceil = field[snake_head_x][snake_head_y]
        field[snake_head_x][snake_head_y] = "snake"

        if cur_ceil != "apple" and cur_ceil != "snake":
            field[snake_tail_x][snake_tail_y] = "ceil"
            snake.remove(snake_tail)
        elif cur_ceil == "snake":
            restart()
        else:
            apple = [(random.randint(0, FIELD_X - 1), random.randint(0, FIELD_Y - 1))]
            while field[apple[0][0]][apple[0][1]] != "ceil":
                apple = [(random.randint(0, FIELD_X - 1), random.randint(0, FIELD_Y - 1))]
            field[apple[0][0]][apple[0][1]] = "apple"

        screen.fill((0, 0, 0))
        for cx in range(FIELD_SIZE[0]):
            for cy in range(FIELD_SIZE[1]):
                if field[cx][cy] == "snake":
                    pygame.draw.rect(screen, COLORS["snake"], (cx * CEIL_SIZE, cy * CEIL_SIZE, CEIL_SIZE, CEIL_SIZE))
                elif field[cx][cy] == "apple":
                    pygame.draw.rect(screen, COLORS["apple"], (cx * CEIL_SIZE, cy * CEIL_SIZE, CEIL_SIZE, CEIL_SIZE))
                else:
                    pygame.draw.rect(screen, COLORS["ceil"], (cx * CEIL_SIZE, cy * CEIL_SIZE, CEIL_SIZE, CEIL_SIZE),
                                     CEIL_BORDER)
        snake_mover = 0

        pygame.display.flip()

# Сделать респавн яблок, которые спавнятся не там где нужно ✅
# Сделать, чтобы яблоко не могло заспавниться в яблоке ✅
# Сделать, чтобы нельзя было развернуться на ходу в противоположную сторону ✅