import pygame

hero_rect = pygame.Rect(100, 500, 120, 125)

print('英雄的原点 x:%d y:%d' %(hero_rect.x, hero_rect.y))
print('英雄的尺寸 width:%d height:%d' %(hero_rect.width, hero_rect.height))

print('%d %d' %hero_rect.size)