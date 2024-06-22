import pygame
from sys import exit
from random import randint


pygame.init()
screen_width = 800
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake Game by Aditya')

Clock = pygame.time.Clock()


snake_pos_x = 45
snake_pos_y = 67
snake_size = 20
snk_len = 1

velocity_x = 0
velocity_y = 0

speed = 5

food_x = randint(100, 700)
food_y = randint(100, 300)


def plot_food(screen, foodx, foody, color, size):
    food = pygame.Rect(foodx, foody, size, size)
    pygame.draw.rect(screen, color, food)


snk_list = []


def Plot_snake(screen, snk_list, color, snake_size):
    i = 0
    for x, y in snk_list:
        snk = pygame.Rect(x, y, snake_size, snake_size)
        if i < len(snk_list)-2:
            pygame.draw.rect(screen, color, snk)
        else:
            pygame.draw.rect(screen, 'yellow', snk)
        i += 1


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                velocity_x = 0
                velocity_y = -speed

            if event.key == pygame.K_DOWN:
                velocity_x = 0
                velocity_y = speed

            if event.key == pygame.K_RIGHT:
                velocity_x = speed
                velocity_y = 0

            if event.key == pygame.K_LEFT:
                velocity_x = -speed
                velocity_y = 0

    screen.fill('black')

    plot_food(screen, food_x, food_y, 'red', snake_size)

    if abs(snake_pos_x - food_x) < 7 and abs(snake_pos_y - food_y) < 7:

        food_x = randint(100, 700)
        food_y = randint(100, 300)
        snk_len += 4

    snake_pos_x += velocity_x
    snake_pos_y += velocity_y
    snk_head = []
    snk_head.append(snake_pos_x)
    snk_head.append(snake_pos_y)

    snk_list.append(snk_head)
    Plot_snake(screen, snk_list, 'green', snake_size)

    if len(snk_list) > snk_len:
        del snk_list[0]

    if snk_head in snk_list[:-1]:
        print('hello world')

    pygame.display.update()
    Clock.tick(50)
