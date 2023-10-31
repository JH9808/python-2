#创建字典
d = {10:'cat',20:'dag',30:'pet',20:'zoo'}
print(d)   ##key相同是，value值进行覆盖

#zip函数
lst1 = [10, 20, 30, 40]
lst2 = ['cat', 'dog', 'pet', 'zoo', 'car']
zipobj = zip(lst1, lst2)
print(zipobj)
d = dict(zipobj)
print(d)

#使用参数创建字典
d = dict(cat=10, dao=20)  # 左侧cat是key，右侧是value
print(d)

t = (10, 20, 30)
print({t:10})  #t是key，10是value，元组是可以作为字典中的key

#字典属于序列
print('max:',max(d))
print('min:',min(d))
print('len',len(d))
#字典的删除
del d