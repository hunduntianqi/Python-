import random
play_name = 0  # 定义变量统计玩家获胜次数
computer_name = 0  # 定义变量统计电脑获胜次数
number = int(input('请输入要比赛的局数:\n')) # 通过Input函数来设定要进行多少次比赛
for i in range(number): # for循环实现循环比赛
    try:
        player = int(input('请输入您要出的拳石头（1）/剪刀（2）/布（3）：\n')) # 玩家输入要出的拳
        computer = random.randint(1,3) # 根据随机生成数字来代表电脑的出拳
        print(computer)
        if ((player == 3 and computer == 1)
                or (player == 1 and computer == 2)
                or (player == 2 and computer == 3)):  # 玩家获胜条件判断

            print('恭喜你赢了一局！！！')
            play_name +=1
        elif ((player == 1 and computer == 3)  # 电脑获胜条件判断
                or (player == 2 and computer == 1)
                or (player == 3 and computer == 2)):

            print('你输了,请再接再厉！！')
            computer_name += 1
        else:
            print('比赛结果:平局')
    except ValueError:
        print('请输入正确的数字！！！')
draw = number - (play_name + computer_name) # 获取平局次数
# 判断最终胜负情况：
if play_name > computer_name:
    print('恭喜玩家获得了最终胜利,电脑弱爆了！！')
elif computer_name > play_name:
    print('对不起,你输了,连电脑都不如！！')
else:
    print('你和电脑打成了平局！！')
print('胜负明细:你赢了{}局,输了{}局，平局{}局.'.format(play_name,computer_name,draw))