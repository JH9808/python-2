# 直接使用【】创建列表
lst = ['hello', 'world', 98, 100.5]
print(lst)

#可以使用内置的函数list()创建列表
list2 = list('helloworld')
list3 = list(range(1, 10, 2))  #从1开始到10结束，步长为2，不包含10
print(list2)
print(list3)

#列表是序列中的一种，对序列的操作符，运算符，函数均可以使用
print(lst + list2 + list3)  #序列中的相加操作
print(lst * 3)  #序列的相乘操作
print(len(lst))
print(max(list3))
print(min(list3))
print(list2.count('o'))  # 统计o的个数
print(list2.index('o'))  #o在列表list2中第一次出现的位置

#列表的删除操作
list4 = [10, 20, 30]
print(list4)
#删除列表
del list4
