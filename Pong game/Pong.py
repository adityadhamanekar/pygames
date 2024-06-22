import pygame
from sys import exit
from random import randint

# from pongGame import opponent_ai

pygame.init()

screen_width = 800
screen_height = 400

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Ping pong Game With Aditya ')

clock = pygame.time.Clock()


def player_animation():
    Player.y += Player_speed_y

    if Player.top <= 0:
        Player.top = 0

    if Player.bottom >= screen_height:
        Player.bottom = screen_height


def ball_dir():
    if randint(0, 1):
        return 1
    else:
        return -1


ball_speed_y = 7 * ball_dir()
ball_speed_x = 7 * ball_dir()


def ball_animation():

    global ball_speed_x, ball_speed_y

    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.bottom >= screen_height or ball.top <= 0:
        ball_speed_y *= -1

    if ball.left <= 0 or ball.right >= screen_width:
        ball.x = screen_width/2 - ball_width/2
        ball.y = screen_height/2 - ball_width/2

        ball_speed_y = 7 * ball_dir()
        ball_speed_x = 7 * ball_dir()

    if ball.colliderect(Player) or ball.colliderect(Opponent):
        ball_speed_x *= -1


def Opponent_game():
    if ball.top <= Opponent.top:
        Opponent.top -= opponent_speed_y

    if ball.bottom >= Opponent.bottom:
        Opponent.bottom += opponent_speed_y


opponent_speed_x = 0
opponent_speed_y = 7


Player_width = 20
player_height = 140

Player_speed_y = 0
Player_speed_x = 0

Player = pygame.Rect(screen_width-Player_width, screen_height /
                     2 - player_height/2, Player_width, player_height)

Opponent = pygame.Rect(0, screen_height/2 - player_height /
                       2, Player_width, player_height)

ball_width = 30
ball = pygame.Rect(screen_width/2 - ball_width/2,
                   screen_height/2 - ball_width/2, ball_width, ball_width)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                Player_speed_y += 7

            if event.key == pygame.K_UP:
                Player_speed_y -= 7

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                Player_speed_y -= 7

            if event.key == pygame.K_UP:
                Player_speed_y += 7

    screen.fill('black')

    pygame.draw.rect(screen, 'red', Player)
    pygame.draw.rect(screen, 'red', Opponent)
    pygame.draw.ellipse(screen, 'green', ball)

    player_animation()
    Opponent_game()
    ball_animation()
    # player_animation()
    pygame.display.update()
    clock.tick(60)
