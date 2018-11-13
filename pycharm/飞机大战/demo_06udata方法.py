import pygame

pygame.init()

#创建游戏窗口
screen = pygame.display.set_mode((480, 700))

#绘制背景图像
bg = pygame.image.load(r'.\images\background.png')
screen.blit(bg, (0, 0))

#绘制英雄飞机
hero = pygame.image.load(r'.\images\me1.png')
screen.blit(hero, (200, 500))
pygame.display.update()

while True:
    pass

pygame.quit()