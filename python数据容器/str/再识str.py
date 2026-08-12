my_str = "ITRICHENYV AND ITCUNRIYANG"
# 通过下标索引
value = my_str[2]
value2 = my_str[-16]
"""
字符串是一个无法修改的数据容器
无法进行insert、pop、append、extend操作
"""
# index方法
value = my_str.index('ITRICHENYV')
print(f"查找ITRICHENYV下标为{value}")
# replace操作
print("————————————————————————————————————————————————")
new_str = my_str.replace("IT", "程序")
print(my_str)
print(new_str)
# split操作
print("————————————————————————————————————————————————")
my_str = "hello python itrichenyv"
my_str_list = my_str.split(" ")
print(f"将字符串{my_str}分割后得到{my_str_list},类型为{type(my_str_list)}")
# strip（去前后空格\去前后指定字母）操作
print("————————————————————————————————————————————————")
my_str = "  itrichenyv and itcunriyang   "
new_my_str = my_str.strip(" ")
print(f"字符串{my_str}被strip后变为：{new_my_str}")
my_str = "12ITRICHENYV and ITCUNRIYANG21"
new_my_str = my_str.strip("12")
print(f"字符串{my_str}被strip后变为：{new_my_str}")
# count方法
print("————————————————————————————————————————————————")
my_str = "KSKBLZDJD"
COUNT = my_str.count("D")
print(COUNT)
print("————————————————————————————————————————————————")
# len方法
length = len(my_str)
print(length)
