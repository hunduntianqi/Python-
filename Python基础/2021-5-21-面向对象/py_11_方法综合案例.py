"""
需求：
1.设计一个Game类
2.属性：
 2.1 定义一个类属性top_score记录游戏的历史最高分
 2.2 定义一个实例属性player_name记录当前游戏的玩家姓名
3.方法：
 3.1 静态方法show_help显示游戏帮助信息
 3.2 类方法show_top_score显示历史最高分
 3.3 实例方法start_game开始当前玩家的游戏
4.主程序步骤：
 4.1 查看帮助信息
 4.2 查看历史最高分
 4.3 创建游戏对象,开始游戏
"""


class Game(object):
    # 历史最高分
    top_score = 0

    def __init__(self, player_name):
        self.player_name = player_name

    @staticmethod
    def show_help():
        print('帮助信息:让僵尸进入大门！！！')
        pass

    @classmethod
    def show_top_score(cls):
        print('历史记录最高分:{}'.format(cls.top_score))

    def start_game(self):
        print('{}开始游戏了...'.format(self.player_name))


# 1.查看游戏帮助信息
Game.show_help()

# 2.查看历史最高分
Game.show_top_score()

# 创建游戏对象
player = Game('gpt')
player.start_game()

"""
案例小结：
1.实例方法--方法内部需要访问实例属性
 1.1 实例方法内部可以使用类名.访问类属性
2.类方法--方法内部只需要访问类属性和调用类方法
3.静态方法--方法内部不需要访问类属性和实例属性
"""
