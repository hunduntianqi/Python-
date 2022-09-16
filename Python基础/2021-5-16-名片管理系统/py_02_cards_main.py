import py_03_cards_tools


def main():
    # TODO(混沌天炁) 主界面显示！！
    print('*' * 50)
    print('欢迎使用【名片管理系统】V1.0')
    print()
    print('0.退出系统')
    print('1.新增名片')
    print('2.查询指定名片')
    print('3.查询全部名片')
    print('4.修改名片')
    print('5.删除名片')
    print('6.回主界面')
    print()
    print('*' * 50)
    # TODO(混沌天炁) While循环保证用户循环操作！！
    while True:
        try:
            card_action = int(input('请选择需要执行的操作(输入对应数字)：'))
            # TODO 退出系统
            if card_action == 0:
                print('欢迎您下次使用！！')
                break
            # TODO 新增名片
            if card_action == 1:
                print('您选择的操作是【新增名片】,请输入名片信息：')
                py_03_cards_tools.card_add()
                print('已成功添加名片！！')
            # TODO 查询特定人员名片
            if card_action == 2:
                print('您选择的操作是【查询名片】,请输入要查询的名片姓名：')
                py_03_cards_tools.card_find()
            # TODO 查询所有人员名片
            if card_action == 3:
                print('您选择的操作是【查询全部名片】,查询结果如下：')
                py_03_cards_tools.card_find_all()
            # TODO 修改特定人员名片
            if card_action == 4:
                print('您选择的操作是修改名片,请按提示进行修改：')
                py_03_cards_tools.card_change()
            # TODO 删除指定人员名片
            if card_action == 5:
                print('您选择的操作是删除名片,请输入要删除的名片姓名：')
                py_03_cards_tools.card_del()
            # TODO 回主界面
            if card_action == 6:
                main()
                break
        except:
            print('请输入正确的数字！！！')


main()
