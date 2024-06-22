# from tkinter.tix import Tree
import pygame
from sys import exit
pygame.init()


# def display_brick():

def draw_brick():
    for i in range(5):
        for j in range(10):
            global brick
            brick = pygame.Rect(
                (brick_width*j, brick_height*i, brick_width, brick_height))
            brick_list.append(brick)

    for index, item in enumerate(brick_list):
        # print(index)
        if index is not 0:
            pygame.draw.rect(screen, 'blue', item, 1)
        else:
            pygame.draw.rect(screen, 'yellow',  item, 1)


screen_width = 640
screen_height = 750
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('BRICK BREAKER')
clock = pygame.time.Clock()

brick_width = 64
brick_height = 30
brick_list = []
# brick = pygame.Surface((brick_width, brick_height))

paddle = pygame.Rect(200, screen_height-30, 250, 30)
paddle_speed = 0


def paddle_animation(paddle):
    paddle.x += paddle_speed
    if paddle.right >= screen_width:
        paddle.right = screen_width
    if paddle.left <= 0:
        paddle.left = 0

    pygame.draw.rect(screen, 'green', paddle)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                paddle_speed -= 7

            if event.key == pygame.K_RIGHT:
                paddle_speed += 7

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                paddle_speed += 7

            if event.key == pygame.K_RIGHT:
                paddle_speed -= 7

            if event.type == pygame.MOUSEBUTTONDOWN:
                if brick.collidepoint(event):
                    print('hello world')

    screen.fill('black')
    # display_brick()
    draw_brick()

    paddle_animation(paddle)

    pygame.display.update()
    clock.tick(60)
