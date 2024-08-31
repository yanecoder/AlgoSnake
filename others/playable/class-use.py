import pygame
import playable_snakeAI

pygame.init()
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("SnakeAI")
clock = pygame.time.Clock()
H_FPS = 120
FPS = 7
COLORS = {
    "ceil": (10,10,10),
    "snake": (50,118,0),
    "apple": (188,14,14)
}
CEIL_SIZE = 20
CEIL_BORDER = 1
FIELD_X = window_size[0] // CEIL_SIZE
FIELD_Y = window_size[1] // CEIL_SIZE
FIELD_SIZE = (FIELD_X, FIELD_Y)
SPEED = (1,0)
snake = [(FIELD_X // 2, FIELD_Y // 2)]

field = playable_snakeAI.Field(FIELD_SIZE, snake)
field.setUp()
game = playable_snakeAI.Game(screen, field, CEIL_SIZE, CEIL_BORDER, H_FPS, FPS, COLORS)

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

        field.eventHandler(SPEED)
        game.rendering()

        snake_mover = 0
        pygame.display.flip()

# Сделать респавн яблок, которые спавнятся не там где нужно ✅
# Сделать, чтобы яблоко не могло заспавниться в яблоке ✅
# Сделать, чтобы нельзя было развернуться на ходу в противоположную сторону ✅
