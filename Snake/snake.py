# from turtle import speed
# from inspect import iscode
# import enum
import pygame
from sys import exit
from random import randint


def isCollide():
    global snake_speed_x, snake_speed_y, snake_pos_y, snake_pos_x, snk_length, snk_list
    if snake_pos_x <= 0 or snake_pos_x >= screen_width or snake_pos_y <= 0 or snake_pos_y >= screen_height:

        snake_pos_x = randint(100, 700)
        snake_pos_y = randint(100, 500)
        snake_speed_x = 0
        snake_speed_y = 0
        # snk_length = 1


pygame.init()
clock = pygame.time.Clock()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

snake_pos_x = 300
snake_pos_y = 200
# snake = pygame.Rect(snake_pos_x, snake_pos_y, 20, 20)

snake_speed_x = 0
snake_speed_y = 0
initial_speed = 5

food_x_pos = randint(150, 650)
food_y_pos = randint(100, 500)

snk_list = []
snk_length = 1


def plot_snake(screen, color, snk_list):
    for x, y in snk_list:
        # print(x, y)
        pygame.draw.rect(screen, color, (x, y, 20, 20))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                snake_speed_x = 0
                snake_speed_y = initial_speed

            if event.key == pygame.K_UP:
                snake_speed_x = 0
                snake_speed_y = -initial_speed

            if event.key == pygame.K_RIGHT:
                snake_speed_x = initial_speed
                snake_speed_y = 0

            if event.key == pygame.K_LEFT:
                snake_speed_x = -initial_speed
                snake_speed_y = 0

    screen.fill('black')
    isCollide()

    pygame.draw.rect(screen, 'red', [food_x_pos, food_y_pos, 20, 20])

    if abs(food_x_pos-snake_pos_x) < 7 and abs(food_y_pos-snake_pos_y) < 7:
        food_x_pos = randint(150, 650)
        food_y_pos = randint(100, 500)
        snk_length += 5

    snake_pos_x += snake_speed_x
    snake_pos_y += snake_speed_y

    snk_head = []
    snk_head.append(snake_pos_x)
    snk_head.append(snake_pos_y)

    snk_list.append(snk_head)

    if len(snk_list) > snk_length:
        del snk_list[0]

    plot_snake(screen, 'green', snk_list)
    pygame.draw.rect(screen, 'green', [snake_pos_x, snake_pos_y, 20, 20])

    pygame.display.update()
    clock.tick(60)
