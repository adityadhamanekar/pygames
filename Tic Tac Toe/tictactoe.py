import pygame
from sys import exit
import time

pygame.init()
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Tic Tac Toe')
clock = pygame.time.Clock()

win = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],
    [0, 3, 6], [1, 4, 7], [2, 5, 8],
    [0, 4, 8], [2, 4, 6]
]


def check_win_o():
    global turn
    for i in win:
        try:
            if (o_dict[i[0]] == 'o' and o_dict[i[1]] == 'o' and o_dict[i[2]] == 'o'):
                turn = 'o'
                return True
            else:
                return False
        except:
            pass


def check_win_x():
    global turn
    for i in win:
        try:
            if (x_dict[i[0]] == 'x' and x_dict[i[1]] == 'x' and x_dict[i[2]] == 'x'):
                turn = 'x'
                return True
            else:
                return False
        except:
            pass


turn = 'x'


def change_turn(turn):
    if turn == 'x':
        return 'o'
    else:
        return 'x'


font = pygame.font.Font('subatomic.ttf', 200)
x_text = font.render('X', True, 'white')
o_text = font.render('O', True, 'white')


x_dict = {}
o_dict = {}


def draw_x_o():
    for square in square_list:
        if pygame.mouse.get_pressed()[0]:
            if square.collidepoint(pygame.mouse.get_pos()):
                x_rect = x_text.get_rect(center=(square.center))
                screen.blit(x_text, x_rect)


def draw_x():
    for x_rect in x_text_list:
        screen.blit(x_text, x_rect)


def draw_o():
    for o_rect in o_text_list:
        screen.blit(o_text, o_rect)


square_list = []
x_text_list = []
o_text_list = []

won = False


for i in range(3):
    for j in range(3):
        square_rect = pygame.Rect(j*200, i*200, 200, 200)

        square_list.append(square_rect)


def draw_square():
    for square in square_list:
        pygame.draw.rect(screen, 'blue', square, 4)


num_list = []


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            for i, square in enumerate(square_list):
                if square.collidepoint(pygame.mouse.get_pos()) and not i in num_list:
                    num_list.append(i)
                    if turn == 'x':

                        turn = change_turn(turn)
                        x_dict[i] = 'x'
                        x_rect = x_text.get_rect(center=(square.center))
                        x_text_list.append(x_rect)
                        won = check_win_x()

                    else:
                        turn = change_turn(turn)
                        o_dict[i] = 'o'
                        o_rect = o_text.get_rect(center=(square.center))
                        o_text_list.append(o_rect)
                        won = check_win_o()

    if not won:

        screen.fill('black')

        draw_square()
        # draw_x_o()
        draw_x()
        draw_o()

    else:
        screen.fill('black')
        font = pygame.font.Font('subatomic.ttf', 20)
        message_surf = font.render(f'{turn} won the match', True, 'white')
        message_rect = message_surf.get_rect(
            center=(screen_width/2, screen_height/2))
        screen.blit(message_surf, message_rect)

    pygame.display.update()
    clock.tick()
