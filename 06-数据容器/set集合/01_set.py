# 集合中无法存储重复元素
my_set = {"RICHENYV", "CUNRIYANG", "HACKER", "RICHENYV", "CUNRIYANG", "HACKER"}
my_set_empty = set()
print(my_set, type(my_set))
print(my_set_empty, type(my_set_empty))
# add（添加新元素）方法
print("————————————————————————————————")
my_set.add("PYTHON")
my_set.add("CUNRIYANG")
print(my_set, type(my_set))
# remove（移除元素）方法
print("————————————————————————————————")
my_set.remove("RICHENYV")
print(my_set, type(my_set))
# pop（随机取出元素）方法
print("————————————————————————————————")
element = my_set.pop()
print(element, type(element))
print(f"取出元素后，my_set还剩{my_set}")
# 清空集合
print("————————————————————————————————")
my_set.clear()
print(my_set, type(my_set))
# 取两个集合的差集
print("————————————————————————————————")
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set3 = set1.difference(set2)
set4 = set2.difference(set1)
print(set3, type(set3))
print(set4, type(set4))
print(f"取差集后，原集合set1、set2为{set1}, {set2}")
# 消除差集
print("————————————————————————————————")
set1.difference_update(set2)
print(set1, type(set1))
# 两个集合合并为一个
print("————————————————————————————————")
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set3 = set1.union(set2)
print(set3, type(set3))
# 统计元素数量
print("————————————————————————————————")
count = len(my_set)
print(count, type(count))
count = len(set1)
print(count, type(count))
