"""
eval函数--可以将字符串当成有效的表达式来求值并返回计算结果
注意：不要使用eval函数直接转化input函数
"""

input_str = input('请输入算术题:')
print(eval(input_str))
