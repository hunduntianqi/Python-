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
enemy = GameSprite(image_name=r'.\游戏素材\enemy1.png', speed=random.randint(1,30))
enemy1 = GameSprite(image_name=r'.\游戏素材\enemy1.png', speed=random.randint(1,15))
enemy2 = GameSprite(image_name=r'.\游戏素材\enemy1.png', speed=random.randint(1,25))
enemy3 = GameSprite(image_name=r'.\游戏素材\enemy1.png', speed=random.randint(1,20))
enemy4 = GameSprite(image_name=r'.\游戏素材\enemy1.png', speed=random.randint(1,40))
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

"""

import pygame
from plane_sprites import *

pygame.init()


class PlaneGame(object):
    """飞机大战主游戏"""

    def __init__(self):
        # 创建矩形区域,记录英雄初始位置
        self.hero_rect = pygame.Rect(189, 574, 102, 126)
        print('游戏初始化')
        # 创建游戏的窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 创建游戏的时钟
        self.clock = pygame.time.Clock()
        # 调用私有方法,创建精灵和精灵组
        self.__create_sprites()
        # 定义创建敌机定时器事件 - 1s
        pygame.time.set_timer(CREAT_ENEMY_EVENT, 1000)
        # 定义创建发射子弹事件
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)

    def __create_sprites(self):
        # 创建背景精灵和精灵组
        bg1 = BackGround()
        bg2 = BackGround(is_alt=True)
        self.back_group = pygame.sprite.Group(bg1, bg2)
        # 创建敌机精灵组
        self.enemy_group = pygame.sprite.Group()
        # 创建英雄精灵和精灵组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def __check_collide(self):
        # 子弹摧毁敌机
        pygame.sprite.groupcollide(self.enemy_group, self.hero.bullet_group, True, True)
        # 敌机撞毁英雄
        hero_die_list = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        if len(hero_die_list):
            print('英雄牺牲...')
            # 从英雄精灵组删除精灵..
            self.hero.kill()
            # 结束游戏
            PlaneGame.__game_over()

    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        self.hero_group.update()
        self.hero_group.draw(self.screen)
        self.hero.bullet_group.update()
        self.hero.bullet_group.draw(self.screen)

    def __event_handler(self):

        for event in pygame.event.get():

            # 判断是否退出游戏
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREAT_ENEMY_EVENT:
                print('敌机出场....')
                # 创建敌机精灵
                enemy = Enemy()
                # 将敌机精灵添加到敌机精灵组
                self.enemy_group.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()
            """
            # 移动英雄方法一：
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                self.hero.rect.x += 10
                print('向右移动...')
                if self.hero.rect.x == SCREEN_RECT.width - self.hero.rect.width:
                    self.hero.rect.x = SCREEN_RECT.width - self.hero.rect.width
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                self.hero.rect.x -= 10
                print('向左移动...')
                if self.hero.rect.x == 0:
                    self.hero.rect.x = 0
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                self.hero.rect.y -= 10
                print('向上移动...')
                if self.hero.rect.y == 0:
                    self.hero.rect.y = 0
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                self.hero.rect.y += 10
                print('向下移动...')
                if self.hero.rect.y == SCREEN_RECT.height:
                    self.hero.rect.y = SCREEN_RECT.height - self.hero.rect.height
            """
        # 移动英雄方法二：
        # 使用键盘提供的方法获取键盘按键-按键元组
        keys_pressed = pygame.key.get_pressed()
        # 判断按键索引值是否为1,1则表示按下按键
        if keys_pressed[pygame.K_RIGHT]:
            self.hero.speed = 3
            print('向右移动...')
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -3
            print('向左移动...')
        else:
            self.hero.speed = 0

    def start_game(self):
        print('游戏开始...')

        while True:
            # 设置刷新帧率
            self.clock.tick(FRAME_PER_SEC)
            # 事件监听
            self.__event_handler()
            # 碰撞检测
            self.__check_collide()
            # 更新/绘制精灵组
            self.__update_sprites()
            # 更新显示屏幕
            pygame.display.update()

    @staticmethod
    def __game_over():
        print('游戏结束...')

        pygame.quit()
        exit()


if __name__ == '__main__':
    # 创建游戏对象
    game = PlaneGame()
    # 启动游戏
    game.start_game()

pygame.quit()
