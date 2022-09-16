"""
派生精灵子类
1.新建plane_speites.py文件
2.定义GameSprite类继承自pygame.sprite.Sprite
注意：
如果一个类的父类不是object
在重写初始化方法时,一定要先super()以一下父类的__init__方法
保证父类中实现的__init__代码能够被正常运行
GameSprite类属性和方法：
属性：
image：精灵图像,使用image_name加载
rect：精灵大小,默认使用图片大小
speed：精灵移动速度,默认为1
方法：
初始化方法__init__(self, image_name, speed = 1)
update(self)方法：每次更新屏幕时在游戏循环内调用

提示：image的get_rect()方法,可以返回pygame.Rect(0, 0, 图像宽, 图像高)的对象
"""
import random

import pygame

# 定义屏幕大小的常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 定义刷新帧率
FRAME_PER_SEC = 60
# 创建敌机的定时器常量
CREAT_ENEMY_EVENT = pygame.USEREVENT
# 英雄发射子弹事件
HERO_FIRE_EVENT = pygame.USEREVENT + 1


class GameSprite(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""

    def __init__(self, image_name, speed=1):
        # 调用父类初始化方法
        super().__init__()
        # 定义对象属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        """在屏幕的垂直方向上移动"""
        self.rect.y += self.speed
        if self.rect.y == 700:
            self.rect.y = 0


class BackGround(GameSprite):
    """游戏背景精灵类"""

    def __init__(self, is_alt=False):

        # 调用父类方法实现精灵的创建(image/rect/speed)
        super().__init__('./游戏素材/background.png')
        # 判断是否是交替图像,如果是,需要设置初始位置
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        # 调用父类的方法实现
        super().update()
        # 判断背景图片是否移出屏幕,如果移出屏幕,将图像设置到屏幕上方
        # 背景图像高度等于屏幕高度
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):
    """敌机精灵类"""

    def __init__(self):
        # 调用父类方法,调用敌机精灵,指定敌机图片
        super().__init__('/游戏素材/enemy1.png')
        # 指定敌机的初始随机速度
        self.speed = random.randint(1, 3)
        # 指定敌机的初始位置
        self.rect.bottom = 0
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):
        # 调用父类方法,保持垂直方向的飞行
        super().update()

        # 判断是否飞出屏幕,飞出屏幕从精灵组删除敌机精灵
        if self.rect.y >= SCREEN_RECT.height:
            # 调用kill()方法销毁敌机精灵,kill()方法可以将精灵从所有精灵组移除
            self.kill()
            print('敌机飞出屏幕,需要从精灵组删除...')

    def __del__(self):
        print('销毁敌机在{}'.format(self.rect))


class Hero(GameSprite):
    """英雄精灵类"""

    def __init__(self):
        # 调用父类方法,设置image和speed
        super().__init__('./游戏素材/me1.png', speed=0)
        # 设置英雄的初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120
        # 定义子弹精灵组保存子弹
        self.bullet_group = pygame.sprite.Group()

    def update(self):
        # 控制英雄不能离开屏幕
        if self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right
        elif self.rect.x < 0:
            self.rect.x = 0
        # 英雄在水平方向移动
        else:
            self.rect.x += self.speed
        pass

    def fire(self):
        print('发射子弹...')
        for i in range(3):
            # 创建子弹精灵
            bullet = Bullet()
            # 设置子弹初始位置
            bullet.rect.y = self.rect.y - 10 * i
            bullet.rect.centerx = self.rect.centerx
            # 将子弹添加到子弹精灵组
            self.bullet_group.add(bullet)


class Bullet(GameSprite):
    """子弹精灵类"""

    def __init__(self):
        # 调用父类方法,设置子弹图片和初始速度
        super().__init__('./游戏素材/bullet1.png', speed=-2)

    def update(self):
        # 调用父类方法,让子弹沿垂直方向向上方飞行
        super().update()
        if self.rect.bottom < 0:
            self.kill()
            print('子弹已经飞出屏幕...')

    def __del__(self):
        print('子弹被销毁...')
