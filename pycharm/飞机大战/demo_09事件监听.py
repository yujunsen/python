import pygame
from  plane_sprites import *

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

#创建时钟对象
clock = pygame.time.Clock()

#1 定义rect变量记录飞机初始位置
hero_rect = pygame.Rect(150, 300, 102, 126)

#创建敌机的精灵
enemy = GameSprite(r'.\images\enemy1.png')
enemy1 = GameSprite(r'.\images\enemy1.png', 2)

#创建敌机的精灵组
enemy_group = pygame.sprite.Group(enemy, enemy1)


ifg = True
while True:
    clock.tick(60)
    #捕获事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('退出游戏')
            #pygame.quit()
            quit()

    #2 修改飞机位置
    hero_rect.y -= 1
    if hero_rect.y <= -126:
        hero_rect.y = 700

    #3 调用blit绘制图像
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)

    #让精灵组调用两个方法
    #update
    enemy_group.update()
    #draw
    enemy_group.draw(screen)

    #4 调用uodata更新
    pygame.display.update()



pygame.quit()