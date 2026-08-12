"""
语法： 序列[起始下标:结束下标:步长]
"""
# 对list进行切片
my_list = [0, 1, 2, 3, 4, 5, 6]
result1 = my_list[1:4:1]
print(result1)
print("————————————————————————————")
my_tuple = (0, 1, 2, 3, 4, 5, 6)
result2 = my_tuple[:]
print(result2)
print("————————————————————————————")
my_str = "0123456"
result3 = my_str[::2]
print(result3)
result4 = my_str[::-2]
print(result4)
print("————————————————————————————")
my_list = [0, 1, 2, 3, 4, 5, 6]
result5 = my_list[3:1:-1]
print(result5)
