my_dict = {"周杰伦": 99, "林俊杰": 88, "张学友": 77}
# 新增元素
my_dict["张信哲"] = 66
print(f"After the add operation,my_dict: {my_dict}")
# 更新元素
my_dict["周杰伦"] = 91
print(f"After the reload operation,my_dict: {my_dict}")
# 删除元素
score = my_dict.pop("周杰伦")
print(f"After the pop operation,my_dict: {my_dict},\nthe grade of him is {score}")
# 清空元素
my_dict.clear()
print(f"After the clear operation,my_dict: {my_dict}")
# get all the keys
print("——————————————————————————————————————————————————————————————————————————————————————————————")
my_dict = {"周杰伦": 99, "林俊杰": 88, "张学友": 77}
keys = my_dict.keys()
print(keys, type(keys))
# 遍历字典
print("——————————————————————————————————————————————————————————————————————————————————————————————")
for key in keys:
    print(f"字典的key是：{key}")
    print(f"字典的value为{my_dict[key]}")
print("——————————————————————————————————————————————————————————————————————————————————————————————")
for key in my_dict:
    print(f"字典的key是：{key}")
    print(f"字典的value为{my_dict[key]}")
# 统计字典内元素个数
print("——————————————————————————————————————————————————————————————————————————————————————————————")
length = len(my_dict)
print(length)
