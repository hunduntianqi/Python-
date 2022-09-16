card_list = []


def card_add():
    """TODO(混沌天炁) 新增名片"""
    global card_list
    card_dict = {}
    card_dict['name'] = input('请输入名字:')
    card_dict['phone'] = input('请输入联系方式:')
    card_dict['qq'] = input('请输入qq号码:')
    card_dict['email'] = input('请输入常用邮箱地址:')
    card_list.append(card_dict)


def card_find_all():
    """查看所有名片信息"""
    global card_list
    for card in card_list:
        for data in card:
            print("{}: {}".format(data, card[data]), end='\t')
        print()
    # TODO 该判断还可以使用len函数,len(card_list) == 0
    # TODO not card_list也可以实现
    if bool(card_list) == False:
        print('现在还没有任何名片信息！！！')


def card_find():
    """查找指定人员名片信息"""
    global card_list
    name_card = input()
    for card in card_list:
        if card['name'] == name_card:
            for data in card:
                print("{}:{}".format(data, card[data]), end='\t')
            print()
            break

    else:
        print('系统中没有这个人的名片！！！')


def card_change():
    """修改指定人员名片信息"""
    global card_list
    name_change = input('请输入要修改的名片姓名:')
    for card in card_list:
        if card['name'] == name_change:
            first_name = card['name']
            for data in card:
                save = card[data]
                card[data] = input('请输入新的{}(回车不修改):'.format(data))
                if card[data] == '':
                    card[data] = save
            print('已成功修改{}的名片！！'.format(first_name))
            break
    else:
        print('系统中没有这个人的名片！！！')


def card_del():
    """删除指定人员名片信息"""
    global card_list
    name_del = input('请输入要删除的名片姓名:')
    for card in card_list:
        if card['name'] == name_del:
            # 此处还可以使用list.remove(元素)直接删除
            card_index = card_list.index(card)
            del card_list[card_index]
            print('已成功删除{}的名片！！'.format(card['name']))
            break
    else:
        print('系统中没有这个人的名片！！！')
