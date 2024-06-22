import pygame
from sys import exit
import time
# from random import randint


pygame.init()

# basic setup
screen_widht = 640
screen_height = 700
screen = pygame.display.set_mode((screen_widht, screen_height))
pygame.display.set_caption('Brick Game by Coder Aditya')
clock = pygame.time.Clock()

# font work
font = pygame.font.Font('subatomic.ttf', 40)


def display_score():
    score_surf = font.render(
        f'SCORE : {score - len(brick_list)}', True, 'white')
    score_rect = score_surf.get_rect(
        center=(screen_widht/2, screen_height/2))

    screen.blit(score_surf, score_rect)
    pygame.draw.rect(screen, 'white', score_rect.inflate(30, 30), 3, 14)


brick_list = []
for i in range(5):
    for j in range(8):
        brick_size = []
        brick_size.append(j*80)
        brick_size.append(i*30)

        brick = pygame.Rect(brick_size[0], brick_size[1], 80, 30)
        brick_list.append(brick)


score = len(brick_list)


def Plot_brick(brick_list):
    for bricks in brick_list:

        pygame.draw.rect(screen, 'green', bricks, 1)


Paddle_x = screen_widht/2
paddle_y = screen_height
paddle_widht = 200
paddle_height = 20
paddle = pygame.Rect(Paddle_x-paddle_widht/2, paddle_y -
                     paddle_height, paddle_widht, paddle_height)

paddle_speed_x = 0
speed = 7

ball_size = 30
ball_x = screen_widht/2 - ball_size/2
ball_y = screen_height/2 - ball_size/2
ball = pygame.Rect(ball_x, ball_y, ball_size, ball_size)
ball_speed_x = 10
ball_speed_y = 10


def player_animation():
    paddle.x += paddle_speed_x

    if paddle.left <= 0:
        paddle.left = 0
    if paddle.right >= screen_widht:
        paddle.right = screen_widht


def ball_animation():
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.right >= screen_widht or ball.left <= 0:
        ball_speed_x *= -1

    if ball.colliderect(paddle) or ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1

    for brick in brick_list:
        if ball.colliderect(brick):
            brick_list.remove(brick)
            ball_speed_y *= -1


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                paddle_speed_x -= speed
            if event.key == pygame.K_RIGHT:
                paddle_speed_x += speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                paddle_speed_x += speed
            if event.key == pygame.K_RIGHT:
                paddle_speed_x -= speed

    if len(brick_list) > 0:

        screen.fill('black')

        display_score()

        pygame.draw.rect(screen, 'white', paddle, 1)

        Plot_brick(brick_list)
        player_animation()

        pygame.draw.ellipse(screen, 'red', ball)
        ball_animation()

    else:
        screen.fill('white')
        time.sleep(3)
        pygame.quit()
        exit()

    pygame.display.update()
    clock.tick(60)
