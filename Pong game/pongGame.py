from cmath import rect
import pygame
from sys import exit
from random import randint


def ball_animation():
    global ball_speed_x, ball_speed_y

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= 600:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball.x = 7
        ball.y = 7

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1


def player_animation():

    player.y += player_speed_y
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height


def opponent_ai():
    if opponent.top <= ball.y:
        opponent.y += opponent_speed
    if opponent.bottom >= ball.y:
        opponent.y -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height


pygame.init()
clock = pygame.time.Clock()

screen_width = 1050
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong Game')

ball = pygame.Rect(screen_width/2-15,  screen_height/2-15, 30, 30)
player = pygame.Rect(screen_width-18, screen_height/2-100, 18, 200)
opponent = pygame.Rect(0, screen_height/2-100, 18, 200)

ball_speed_x = 7
ball_speed_y = 7

player_speed_x = 0
player_speed_y = 0

opponent_speed = 7

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_speed_y -= 7
            if event.key == pygame.K_DOWN:
                player_speed_y += 7

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_speed_y += 7
            if event.key == pygame.K_DOWN:
                player_speed_y -= 7

    ball_animation()
    player_animation()
    opponent_ai()

    # player.draw.rect('blue')
    screen.fill('black')
    pygame.draw.rect(screen, 'gray', player)
    pygame.draw.rect(screen, 'gray', opponent)
    pygame.draw.ellipse(screen, 'gray', ball)

    pygame.display.update()
    clock.tick(60)
