import pygame
from sys import exit
from random import randint

pygame.init()

screen_width = 289
screen_height = 511
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Flappy bird')
clock = pygame.time.Clock()

bg_surf = pygame.image.load('images/background.png').convert_alpha()
bg_rect = bg_surf.get_rect(topleft=(0, 0))

base_surf = pygame.image.load('images/base.png').convert_alpha()
base_rect = base_surf.get_rect(bottom=(screen_height))

upper_pipe = pygame.transform.rotozoom(
    pygame.image.load('images/pipe.png').convert_alpha(), 180, 1)
lower_pipe = pygame.image.load('images/pipe.png').convert_alpha()

pipe_timer = pygame.event.custom_type()
pygame.time.set_timer(pipe_timer, 3000)

bird1 = pygame.image.load('images/bird.png').convert_alpha()
bird2 = pygame.image.load('images/bird.png').convert_alpha()
bird = [bird1, bird2]
bird_index = 0
bird_surf = bird[bird_index]
bird_rect = bird_surf.get_rect(center=(100, screen_height/2))

gravity = 1

pipes = []


def bird_animation():
    global bird_index
    bird_index += 0.05
    if bird_index >= 2:
        bird_index = 0

    return bird[int(bird_index)]


def draw_pipes():
    for pipe in pipes:
        pipe[0].left -= 1
        pipe[1].left -= 1
        screen.blit(upper_pipe, pipe[0])
        screen.blit(lower_pipe, pipe[1])


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pipe_timer:
            pipe_y = randint(-240, -100)
            pipe_x = 300
            upper_pipe_rect = upper_pipe.get_rect(topleft=(pipe_x, pipe_y))
            lower_pipe_rect = lower_pipe.get_rect(
                topleft=(pipe_x, upper_pipe_rect.bottom + 100))
            pipes.append((upper_pipe_rect, lower_pipe_rect))

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                gravity = -3

    screen.blit(bg_surf, bg_rect)
    draw_pipes()
    screen.blit(base_surf, base_rect)

    bird_surf = bird_animation()
    screen.blit(bird_surf, bird_rect)
    gravity += 0.2
    bird_rect.bottom += gravity

    base_rect.left -= 2
    if base_rect.right <= screen_width:
        base_rect.left = 0

    pygame.display.update()
    clock.tick(60)
