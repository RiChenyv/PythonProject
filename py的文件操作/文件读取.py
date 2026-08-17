from datetime import time

f = open("D:/python.txt", "r", encoding="UTF-8")
print(f"输出10个字节：{f.read(10)}")
print(f"输出全部内容：{f.read()}")
lines = f.readlines()
# 由于read已经读取完成，readlines会接着读，造成无输出元素
print(type(lines))
print(lines)
# readline
line1 = f.readline()
print(type(line1))
print(line1)
# for循环读取
for line in f:
    print(line)
# 关闭文件
time.sleep(500000)
f.close()
