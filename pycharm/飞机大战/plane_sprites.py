import random
import pygame


#屏幕大小常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
#刷新的帧率
FRAME_PER_SEC = 60
#创建敌机定时器
CREATE_ENEMY_EVENT = pygame.USEREVENT
#英雄发射子弹事件
HERO_FIRE_EVENT = pygame.USEREVENT + 1

class GameSprite(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""
    def __init__(self, img_name, speed = 1):
        """调用父类方法"""
        super().__init__()
        """定义对象属性"""
        self.image = pygame.image.load(img_name)
        self.rect = self.image.get_rect()
        self.speed = speed;
    def update(self):
        #在屏幕的垂直方向移动
        self.rect.y += self.speed

class Background(GameSprite):
    """游戏背景精灵"""

    def __init__(self, is_alt = False):
        #1 调用父类方法实现精灵创建
        super().__init__(r'.\images\background.png')
        #2 判断是否是交替
        if is_alt:
            self.rect.y = -self.rect.height
    def update(self):
        # 1 调用父类方法实现
        super().update()
        # 2 判断是否移出屏幕
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height

class Enemy(GameSprite):
    """敌机精灵"""
    def __init__(self):
        #1 调父类方法 创建敌机精灵 指定图片

        super().__init__(r'.\images\enemy1.png')

        #2 指定敌机的随机速度
        self.speed = random.randint(1, 3)
        #3 指定敌机的随机位置
        self.rect.bottom = 0
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)
    def __del__(self):
        pass

    def update(self):
        #1 调用父类方法 保持垂直飞行
        super().update()
        #2 判读是否飞出屏幕 是否从精灵组删除敌机
        if self.rect.y >= SCREEN_RECT.height:
            self.kill()

class Hero(GameSprite):
    """英雄精灵"""
    def __init__(self):
        # 1 调用父类方法 设置image&speed
        super().__init__(r'.\images\me1.png', 0)
        # 2 设置英雄初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom -120
        # 3 子弹精灵组
        self.bullets = pygame.sprite.Group()

    def update(self):
        self.rect.x += self.speed
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right
    def fire(self):
        print('发射子弹')
        for i in (0, 1, 2):
            #创建子弹精灵
            bullet = Bullet()
            #设置位置
            bullet.rect.bottom = self.rect.y - i * 20
            bullet.rect.centerx = self.rect.centerx
            #添加精灵组
            self.bullets.add(bullet)

class Bullet(GameSprite):
    """子弹精灵"""
    def __init__(self):
        #调用父类方法
        super().__init__(r'.\images\bullet1.png', -2)

    def update(self):
        #调用父类
        super().update()
        #边界检查
        if self.rect.bottom < 0:
            self.kill()



    def __del__(self):
        print('子弹销毁')