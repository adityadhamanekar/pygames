from PIL import Image, ImageGrab
# from numpy import asarray
import pyautogui
import time
import pygame

clock = pygame.time.Clock()


def hit(key):
    pyautogui.keyDown(key)


def isCollide(data):
    # print(asarray(image))
    for i in range(740, 770):
        for j in range(270, 310):
            if data[i, j] < 100:
                hit('up')
                return True
    return False


# def screen_shot():

#     # image.show()
#     return image


if __name__ == "__main__":
    print('hey... the dino game is about to start')

    time.sleep(3)
    hit('up')
    hit('up')
    while True:
        image = ImageGrab.grab().convert('L')

        data = image.load()
        isCollide(data)

        clock.tick(90)

        # print(asarray(image))
        # for i in range(735, 750):
        #     for j in range(270, 305):
        #         data[i, j] = 0

        # image.show()
        # break
