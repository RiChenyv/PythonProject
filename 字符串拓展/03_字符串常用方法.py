# 字符串常用方法大全

my_str = "  Hello Python Project  "
print(f"原字符串：'{my_str}'")
print("————————————————————————")

# 1. 大小写转换
print(f"全部大写：{my_str.upper()}")
print(f"全部小写：{my_str.lower()}")
print(f"首字母大写：{my_str.strip().title()}")
print("————————————————————————")

# 2. 去除空白
print(f"去左右空格：'{my_str.strip()}'")
print(f"去左空格：'{my_str.lstrip()}'")
print(f"去右空格：'{my_str.rstrip()}'")
print("————————————————————————")

# 3. 查找与替换
text = "python is fun, python is powerful"
print(f"'python'第一次出现的下标：{text.find('python')}")
print(f"'python'最后一次出现的下标：{text.rfind('python')}")
print(f"'python'出现的次数：{text.count('python')}")
print(f"替换后的字符串：{text.replace('python', 'Python')}")
print("————————————————————————")

# 4. 分割与拼接
words = "apple,banana,orange"
word_list = words.split(",")
print(f"分割后的列表：{word_list}")
print(f"重新拼接：{' | '.join(word_list)}")
print("————————————————————————")

# 5. 判断开头和结尾
url = "https://github.com/RiChenyv"
print(f"是否以https开头：{url.startswith('https')}")
print(f"是否以.com结尾：{url.endswith('.com')}")
