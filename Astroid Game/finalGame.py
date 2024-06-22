import pygame
from sys import exit
from random import randint, uniform

pygame.init()

screen_widht = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_widht, screen_height))
clock = pygame.time.Clock()
pygame.display.set_caption('Space Game')

ship_surf = pygame.image.load('graphics/ship.png').convert_alpha()
ship_rect = ship_surf.get_rect(center=(screen_widht/2, screen_height/2))

bg_surf = pygame.image.load('graphics/background.png').convert_alpha()

laser_surf = pygame.image.load('graphics/laser.png').convert_alpha()
laser_list = []
can_shoot = True
laser_timer = pygame.time.get_ticks()
laser_speed = 400


shoot_sound = pygame.mixer.Sound('sounds/laser.ogg')
collide_sound = pygame.mixer.Sound('sounds/explosion.wav')


def move_laser(laser_list, laser_speed):
    for laser_rect in laser_list:
        laser_rect.top -= laser_speed * dt

        if laser_rect.bottom < 0:
            laser_list.remove(laser_rect)


def laser_interval(can_shoot, duration=200):
    if not can_shoot:
        current_time = pygame.time.get_ticks()
        if current_time - laser_timer > duration:
            can_shoot = True
        return can_shoot


# text for the game
font = pygame.font.Font('graphics/subatomic.ttf', 50)


def display_font():
    score = f'SCORE : {pygame.time.get_ticks()//1000}'
    text_surf = font.render(score, True, 'white')
    text_rect = text_surf.get_rect(
        midbottom=(screen_widht/2, screen_height-80))
    screen.blit(text_surf, text_rect)
    pygame.draw.rect(screen, 'white', text_rect.inflate(
        30, 30), width=2, border_radius=5)


meteor_timer = pygame.event.custom_type()
pygame.time.set_timer(meteor_timer, 500)
meteor_surf = pygame.image.load('graphics/meteor.png')
meteor_list = []
meteor_speed = 400


def move_meteor(meteor_list):
    for meteor_tuple in meteor_list:
        meteor_rect = meteor_tuple[0]
        direction = meteor_tuple[1]
        meteor_rect.center += meteor_speed * direction * dt

        if meteor_rect.top > screen_height:
            meteor_list.remove(meteor_tuple)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN and can_shoot:
            laser_timer = pygame.time.get_ticks()
            laser_rect = laser_surf.get_rect(midbottom=(ship_rect.midtop))
            laser_list.append(laser_rect)
            can_shoot = False
            shoot_sound.play()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                laser_timer = pygame.time.get_ticks()
                laser_rect = laser_surf.get_rect(midbottom=(ship_rect.midtop))
                laser_list.append(laser_rect)
                can_shoot = False
                shoot_sound.play()

        if event.type == meteor_timer:
            direction = pygame.math.Vector2(uniform(-0.5, 0.5), 1)
            m_x = randint(-100, screen_widht+100)
            m_y = randint(-100, -50)
            meteor_rect = meteor_surf.get_rect(center=(m_x, m_y))
            meteor_list.append((meteor_rect, direction))

    dt = clock.tick(120) / 1000

    # displaying images
    screen.blit(bg_surf, (0, 0))
    screen.blit(ship_surf, ship_rect)

    ship_rect.center = pygame.mouse.get_pos()
    move_laser(laser_list, laser_speed)
    display_font()
    can_shoot = laser_interval(can_shoot, 1)
    for laser_rect in laser_list:
        screen.blit(laser_surf, laser_rect)

    move_meteor(meteor_list)
    for meteor_tuple in meteor_list:
        screen.blit(meteor_surf, meteor_tuple[0])

        if ship_rect.colliderect(meteor_tuple[0]):
            collide_sound.play()
            pygame.quit()
            exit()

        for laser_rect in laser_list:
            if laser_rect.colliderect(meteor_tuple[0]):
                meteor_list.remove(meteor_tuple)
                laser_list.remove(laser_rect)

    pygame.display.update()
