import pygame

pygame.init()

#创建游戏窗口
screen = pygame.display.set_mode((480, 700))
#绘制背景图像
#1 加载图像数据
bg = pygame.image.load(r'D:\code\python\pycharm\飞机大战\images\background.png')
#2 blit绘制图像
screen.blit(bg, (0, 0))
#3 更新屏幕显示
pygame.display.update()

while True:
    pass

pygame.quit()