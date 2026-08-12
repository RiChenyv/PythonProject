my_str = "itrichenyv itcunriyang scx"
count = my_str.count("it")
print(f"字符串{my_str}中有：{count}个it字符")
new_str = my_str.replace(" ", "|")
print(f"字符串{my_str}，被替换空格后，结果为{new_str}")
new_str = new_str.split("|")
print(f"字符串{my_str}被按照 | 分割后，得到{new_str}")
