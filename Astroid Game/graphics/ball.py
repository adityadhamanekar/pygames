import pygame
from sys import exit
pygame.init()

screen_widht = 1280
screen_height = 700

screen = pygame.display.set_mode((screen_widht, screen_height))

clock = pygame.time.Clock()

ball_size = 30
ball_game = pygame.Rect(screen_widht/2, screen_height/2, ball_size, ball_size)

speed = 10

velocity_y = speed
velocity_x = speed

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill('black')

    ball_game.x += velocity_x
    ball_game.y += velocity_y

    if ball_game.bottom >= screen_height or ball_game.top <= 0:
        velocity_y *= -1

    if ball_game.left <= 0 or ball_game.right >= screen_widht:
        velocity_x *= -1
    pygame.draw.ellipse(screen, 'green', ball_game)

    pygame.display.update()
    clock.tick(60)
