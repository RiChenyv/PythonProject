my_list = ['itrichenyv', 'itcast', 'python']
index = my_list.index('itrichenyv')
print(f"'itrichenyv'在列表中的下标索引为{index}")
# 修改元素的下标值
print("——————————————————————————————————")
my_list[0] = 'XXXX'
print(my_list[0])
print("——————————————————————————————————")
# 插入元素
my_list.insert(1, 'XXXX')
print(my_list)
print("——————————————————————————————————")
# 追加元素
my_list.append('CUNRIYANG')
print(my_list)
# 追加列表
print("——————————————————————————————————")
my_list2 = ['S', 'C', 'X']
my_list.extend(my_list2)
print(my_list)
print("——————————————————————————————————")
# 删除元素
del my_list[0]
print(my_list)
print("——————————————————————————————————")
my_list.pop(0)
print(my_list)
print("——————————————————————————————————")
# 删除某元素在列表中的第一个匹配项
print(my_list)
my_list.remove('CUNRIYANG')
print(my_list)
print("——————————————————————————————————")
# 清空列表
my_list.clear()
print(my_list)
print("——————————————————————————————————")
# 统计列表中某元素的数量
my_list3 = [1, 2, 2, 3, 3, 3]
print(my_list3.count(3))
print("——————————————————————————————————")
# 统计列表中总元素的数量
print(len(my_list3))