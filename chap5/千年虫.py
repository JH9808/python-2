lst= [88, 89, 90, 98, 00, 99] # 表示员工的两位整数出生年份
print(lst)
#遍历列表的方式
for index in range(len(lst)):
    if str(lst[index]) != '0':
        lst[index] = '19' + str(lst[index]) #拼接年份，在赋值
    else:
        lst[index] = '200' + str(lst[index])

print('修改后的年份列表：',lst)

#使用enumerate()函数
for index,value in enumerate(lst):
    if str(value) !='0':
        lst[index] = '19' + str(value)
    else:
        lst[index] = '200' + str(value)

print('修改后的年份列表：',lst)

import tkinter as tk

# 创建主窗口
window = tk.Tk()

# 设置窗口标题
window.title("Python GUI示例")

# 创建一个标签
label = tk.Label(window, text="欢迎使用Python GUI!")
label.pack()

# 运行主循环
window.mainloop()
