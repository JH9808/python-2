t = (i for i in range(1,4))
print(t)
t = tuple(t)
print(t)

#遍历
for item in t:
    print(item)

print('--------------')
t = (i for i in range(1,4))
print(t)
print(t.__next__())
print(t.__next__())
print(t.__next__())
