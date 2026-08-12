# 定义元组
my_tulpe = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(my_tulpe)
# 定义空元组
print("——————————————————————————————————————")
my_tulpe2 = tuple()
print(f"空元组的内容是：{my_tulpe2}")
# 定义单个元素的元组
print("——————————————————————————————————————")
my_tulpe3 = ('hello')
print(f"元组内容为{my_tulpe3}，类型为{type(my_tulpe3)}")
my_tulpe3 = ('hello',)
print(f"元组内容为{my_tulpe3}，类型为{type(my_tulpe3)}")
# 元组的嵌套
print("——————————————————————————————————————")
my_tulpe4 = ((1, 2, 3, 4), (5, 6, 7, 8))
print(f"元组内容为{my_tulpe4}，类型为{type(my_tulpe4)}")
# 下标索引取出元素
print("——————————————————————————————————————")
print(my_tulpe4[1][1])
# 查找下标索引
print("——————————————————————————————————————")
index = my_tulpe4.index((1, 2, 3, 4))
print(index)
# count统计操作
print("——————————————————————————————————————")
my_tulpe5 = (1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5)
print(my_tulpe5.count(5))
# len统计元组长度
print("——————————————————————————————————————")
length = len(my_tulpe5)
print(length)
# 元组的遍历:while
print("——————————————————————————————————————")
index = 0
while index < len(my_tulpe5):
    print(my_tulpe5[index], end=" ")
    index += 1
print()
# 元组的遍历：for
print("——————————————————————————————————————")
for element in my_tulpe5:
    print(element, end=" ")
print()
# 修改元组内的list
"""
元组的内容不支持修改，但特例的是，元组内的list可以通过下标修改
"""
print("——————————————————————————————————————")
my_tulpe6 = (1, 2, ["itrichenyv", "itSCX"])
print(f"内容为{my_tulpe6}")
my_tulpe6[2][0] = "RICHENYV"
my_tulpe6[2][1] = "CUNRIYANG"
print(f"内容为{my_tulpe6}")
