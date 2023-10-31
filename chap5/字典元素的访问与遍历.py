d = {'hello':10, 'world':20, 'python':30}
#访问字典中的元素
#使用d[key]
print(d['hello'])
#d.get(key)
print(d.get('hello'))

#二者之间是有区别的。如果key不存在，d[key]报错，d.get(key)可以指定默认值
print(d.get('java','不存在'))

#字典的遍历
for item in d.items():
    print(item)  #key=value组成的一个元素

#使用for循环遍历时，分别获取key,value
for key,value in d.items():
    print(key,'--->',value)