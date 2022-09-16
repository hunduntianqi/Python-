"""
目标
1.项目准备
2.使用pygame创建图形窗口
3.理解图像并实现图像绘制
4.理解游戏循环和游戏时钟
5.理解精灵和精灵组
"""
import pygame, random
import time
from plane_sprites import *

# 导入并初始化所有pygame模块
pygame.init()

# 游戏初始化-加载图像,创建游戏窗口等
# 创建游戏主窗口
screen = pygame.display.set_mode(size=(480, 700))
# 创建矩形区域,记录英雄初始位置
hero_rect = pygame.Rect(189, 574, 102, 126)
# 加载背景图像,将返回结果赋值给图像变量
bg = pygame.image.load(r'D:\PyCharm Community Edition 2020.3.4\Python基础\2021-5\2021-5-30\游戏素材\background.png')
me2 = pygame.image.load(r'D:\PyCharm Community Edition 2020.3.4\Python基础\2021-5\2021-5-30\游戏素材\me1.png')
# 将背景图像绘制在屏幕的(0, 0)位置
screen.blit(bg, (0, 0))
screen.blit(me2, hero_rect)
# 调用update方法更新屏幕显示
pygame.display.update()
time.sleep(0.015)
# time.sleep(10)
# 创建时钟对象
clock = pygame.time.Clock()
# 创建敌机的精灵
enemy = GameSprite(image_name=r'.\游戏素材\enemy1.png', speed=random.randint(1, 30))
enemy1 = GameSprite(image_name=r'.\游戏素材\enemy1.png', speed=random.randint(1, 15))
enemy2 = GameSprite(image_name=r'.\游戏素材\enemy1.png', speed=random.randint(1, 25))
enemy3 = GameSprite(image_name=r'.\游戏素材\enemy1.png', speed=random.randint(1, 20))
enemy4 = GameSprite(image_name=r'.\游戏素材\enemy1.png', speed=random.randint(1, 40))
# 创建敌机的精灵组
enemy_group = pygame.sprite.Group(enemy, enemy1, enemy2, enemy3, enemy4)
# 游戏循环->意味着游戏的正式开始
while True:
    clock.tick(10)
    event_list = pygame.event.get()
    if len(event_list) > 0:
        print(event_list)
    for event in event_list:
        # 判断用户是否点击关闭按钮
        if event.type == pygame.QUIT:
            print('退出游戏...')
            pygame.quit()
            exit()
    if hero_rect.y + hero_rect.height <= 0:
        hero_rect.y = 700
    # 修改影响在屏幕的绘制位置
    hero_rect.y -= 10
    # # 将背景图像绘制在屏幕的(0, 0)位置
    screen.blit(bg, (0, 0))
    screen.blit(me2, hero_rect)

    # 让精灵组调用两个方法
    # update方法-让组中的所有精灵更新位置
    enemy_group.update()
    # draw方法-在screen上绘制所有的精灵
    enemy_group.draw(screen)
    # 调用update方法更新屏幕显示
    pygame.display.update()

# 游戏结束,卸载所有pygame模块
pygame.quit()
