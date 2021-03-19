# 导入相关模块
import random
import pygame
import sys
from pygame.locals import *

snake_speed = 5  # 贪吃蛇的速度
windows_width = 800
windows_height = 600  # 游戏窗口的大小
cell_size = 20  # 贪吃蛇身体方块大小,注意身体大小必须能被窗口长宽整除

# 贪吃蛇是有大小尺寸的, 因此地图的实际尺寸是相对于贪吃蛇的大小尺寸而言的
map_width = int(windows_width / cell_size)
map_height = int(windows_height / cell_size)

# 颜色定义
white = (255, 255, 255)
black = (0, 0, 0)
gray = (230, 230, 230)
dark_gray = (40, 40, 40)
Green = (0, 255, 0)
Red = (255, 0, 0)
body_color1 = (0, 100, 200)
body_color2 = (0, 124, 255)

# 定义方向
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

my_font = 'myfont.ttf'


def main():
    pygame.init()
    snake_speed_clock = pygame.time.Clock()
    screen = pygame.display.set_mode((windows_width, windows_height))
    screen.fill(black)
    pygame.display.set_caption('Snake')
    show_start_info(screen)

    while True:
        running_game(screen, snake_speed_clock)
        show_gameover_info(screen)


def running_game(screen, snake_speed_clock):
    snake_body = [(15, 15), (14, 15), (13, 15)]  # 初始贪吃蛇位置
    direction = RIGHT  # 初始向右
    food = get_food_location(snake_body)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if (event.key == K_LEFT or event.key == K_a) and direction != RIGHT:
                    direction = LEFT
                elif (event.key == K_RIGHT or event.key == K_d) and direction != LEFT:
                    direction = RIGHT
                elif (event.key == K_UP or event.key == K_w) and direction != DOWN:
                    direction = UP
                elif (event.key == K_DOWN or event.key == K_s) and direction != UP:
                    direction = DOWN
                elif event.key == K_ESCAPE:
                    terminate()

        move_snake(direction, snake_body)

        if not snake_is_alive(snake_body):
            break
        food = snake_is_eat_food(snake_body, food)  # 判断蛇是否吃到食物

        screen.fill(black)
        draw_grid(screen)
        draw_snake(screen, snake_body)
        draw_food(screen, food)
        draw_score(screen, len(snake_body) - 3)
        pygame.display.update()
        snake_speed_clock.tick(snake_speed)


def draw_food(screen, food):
    x = food[0] * cell_size
    y = food[1] * cell_size
    apple = pygame.Rect(x, y, cell_size, cell_size)
    pygame.draw.rect(screen, Red, apple)


def draw_snake(screen, snake_body):
    for body in snake_body:
        x = body[0] * cell_size
        y = body[1] * cell_size
        body1 = pygame.Rect(x, y, cell_size, cell_size)
        pygame.draw.rect(screen, body_color1, body1)
        body2 = pygame.Rect(x + 4, y + 4, cell_size - 8, cell_size - 8)
        pygame.draw.rect(screen, body_color2, body2)


def draw_grid(screen):
    for x in range(0, windows_width, cell_size):
        pygame.draw.line(screen, dark_gray, (x, 0), (x, windows_height))
    for y in range(0, windows_height, cell_size):
        pygame.draw.line(screen, dark_gray, (0, y), (windows_width, y))


def move_snake(direction, snake_body):
    x = snake_body[0][0]
    y = snake_body[0][1]
    if direction == UP:
        new_head = (x, y - 1)
    elif direction == DOWN:
        new_head = (x, y + 1)
    elif direction == RIGHT:
        new_head = (x + 1, y)
    else:
        new_head = (x - 1, y)

    snake_body.insert(0, new_head)


def snake_is_alive(snake_body):
    if snake_body[0][0] == -1 or snake_body[0][0] >= map_width \
            or snake_body[0][1] == -1 or snake_body[0][1] >= map_height \
            or snake_body[0] in snake_body[1:]:
        return False
    return True


def snake_is_eat_food(snake_body, food):
    if snake_body[0] == food:
        food = get_food_location(snake_body)
    else:
        del snake_body[-1]  # 如果没有吃到实物, 就向前移动, 那么尾部一格删掉

    return food


# 获取食物位置
def get_food_location(snake_body):
    while True:
        location = (random.randint(0, map_width - 1), random.randint(0, map_height - 1))
        if location not in snake_body:
            return location


def draw_score(screen, score):
    font = pygame.font.Font(my_font, 30)
    screen.blit(font.render('Score: %s' % score, True, Green), (20, 20))


def terminate():
    pygame.quit()
    sys.exit()


def show_start_info(screen):
    font = pygame.font.Font(my_font, 40)
    screen.blit(font.render('Press any key to start ~~~', True, (65, 105, 225)), (200, 350))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or event.type == K_ESCAPE:
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()
                else:
                    return


def show_gameover_info(screen):
    font = pygame.font.Font(my_font, 40)
    word1 = font.render('Press Q or ESC to exit ', True, (65, 105, 225))
    word2 = font.render('Press any key to restart~~~', True, (65, 105, 225))
    screen.blit(word1, (80, 300))
    screen.blit(word2, (80, 350))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE or event.key == K_q:
                    terminate()
                else:
                    return


if __name__ == '__main__':
    main()
