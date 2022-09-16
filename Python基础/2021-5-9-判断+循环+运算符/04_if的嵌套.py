"""
tab键：批量缩进4空格
shift+tab：批量取消缩进4空格
if嵌套：在之前条件成立的前提下,在增加额外的条件判断.
语法：
if 条件判断：
    if 条件判断：
        条件成立要执行的代码
"""
while True:
    has_ticket = input('有票请输入1,否则请输入0:\n')
    knife_length = int(input('所携带刀具的长度为(cm)：\n'))
    try:
        if int(has_ticket):
            print('车票检查通过,准备开始安检！！！')
            if knife_length <= 20:
                print('刀具符合规定长度,可以进站.')
                break
            else:
                print('携带刀具长度超标，不能进站！！！')
                break
        else:
            print('您没有车票,不能进站,请先去买票！！')
    except ValueError:
        print('您输入的数字有误,请重新输入！！')