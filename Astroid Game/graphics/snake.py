import pygame
from sys import exit
from random import randint

pygame.init()

screen_width = 1200
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

snake_pos_x = randint(50, 1000)
snake_pos_y = randint(50, 600)
snake_size = 20

snake = pygame.Rect(snake_pos_x, snake_pos_y, snake_size, snake_size)

velocity_x = 0
velocity_y = 0

speed = 10
snake_length = 1
snake_list = []

food_x = randint(50, 1000)
food_y = randint(50, 600)
food = pygame.Rect(food_x, food_y, snake_size, snake_size)


def plot_snake(snake_list, color, snk_size):
    for x, y in snake_list:
        pygame.draw.rect(screen, color, pygame.Rect(x, y, snk_size, snk_size))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                velocity_x = 0
                velocity_y = speed

            if event.key == pygame.K_UP:
                velocity_x = 0
                velocity_y = -speed

            if event.key == pygame.K_RIGHT:
                velocity_x = speed
                velocity_y = 0

            if event.key == pygame.K_LEFT:
                velocity_x = -speed
                velocity_y = 0

    screen.fill('black')
    pygame.draw.rect(screen, 'red', food)

    if abs(snake_pos_x-food_x) < 10 and abs(snake_pos_y - food_y) < 10:
        # if snake.colliderect(food):
        food_x = randint(50, 1000)
        food_y = randint(50, 600)
        food = pygame.Rect(food_x, food_y, snake_size, snake_size)
        snake_length += 5

    snake_pos_x += velocity_x
    snake_pos_y += velocity_y

    snake_head = []
    snake_head.append(snake_pos_x)
    snake_head.append(snake_pos_y)

    if snake_head in snake_list[:-1]:
        screen.fill('blue')

    snake_list.append(snake_head)
    if len(snake_list) > snake_length:
        del snake_list[0]
    plot_snake(snake_list, 'green', snake_size)

    pygame.display.update()
    clock.tick(60)
