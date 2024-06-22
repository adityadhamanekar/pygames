# from re import S
import pygame
from sys import exit


def draw_mario():
    global mario, mario_jump, mario_index,  mario_rect
    if mario_rect.bottom < 300:
        return mario_jump
    else:
        mario_index += 0.3
        if mario_index >= len(mario):
            mario_index = 1
        return mario[int(mario_index)]


screen_width = 800
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()


sky = pygame.image.load('bg.png').convert_alpha()
sky_rect = sky.get_rect(topleft=(0, 0))

ground = pygame.Surface((screen_width, 100))
ground.fill('brown')

mario_walk = pygame.image.load('Mario/mario1.png').convert_alpha()
mario_walk1 = pygame.image.load('Mario/mario1_move0.png').convert_alpha()
mario_walk2 = pygame.image.load('Mario/mario1_move1.png').convert_alpha()
mario_walk3 = pygame.image.load('Mario/mario1_move2.png').convert_alpha()
mario_jump = pygame.image.load('Mario/mario1_jump.png').convert_alpha()
mario_index = 0
mario = [mario_walk, mario_walk1, mario_walk2, mario_walk3]
mario_surf = mario[mario_index]
mario_rect = mario_surf.get_rect(midbottom=(100, 300))
mario_gravity = 0


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and mario_rect.bottom >= 300:
                mario_gravity = -20

            if event.key == pygame.K_RIGHT:
                mario_rect.right += 1

    screen.blit(sky, sky_rect)
    screen.blit(ground, (0, 300))
    mario_rect.right += 3
    mario_gravity += 1
    mario_rect.bottom += mario_gravity
    if mario_rect.bottom >= 300:
        mario_rect.bottom = 300
    mario_surf = draw_mario()
    screen.blit(mario_surf, mario_rect)

    pygame.display.update()
    clock.tick(60)
