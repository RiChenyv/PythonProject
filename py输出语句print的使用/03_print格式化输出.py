# print() 格式化输出：把变量嵌入到字符串中

name = "richenyv"
age = 18
score = 95.5

# 1. % 格式化（老方法）
# %s 字符串、%d 整数、%f 小数
print("我的名字是%s，今年%d岁" % (name, age))
print("成绩是%.1f分" % score)
print("————————————————————————")

# 2. format() 方法
print("我的名字是{}，今年{}岁".format(name, age))
print("我的名字是{0}，今年{1}岁，再次叫{0}".format(name, age))
print("我的名字是{n}，今年{a}岁".format(n=name, a=age))
print("————————————————————————")

# 3. f-string（最推荐，Python3.6+）
print(f"我的名字是{name}，今年{age}岁")
print(f"明年我就{age + 1}岁了")
print(f"成绩保留两位：{score:.2f}")
print("————————————————————————")

# 4. 对齐与补零
print(f"学号：{7:03d}")
print(f"|{'居中':^10}|")
print(f"|{'左对齐':<10}|")
print(f"|{'右对齐':>10}|")
