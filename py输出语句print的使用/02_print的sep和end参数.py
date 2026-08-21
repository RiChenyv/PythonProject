# print() 的两个进阶参数：sep 和 end

# 1. sep 参数：指定多个内容之间的分隔符（默认是空格）
print("a", "b", "c")
print("a", "b", "c", sep="-")
print("a", "b", "c", sep="喵")
print("2026", "08", "21", sep="/")
print("————————————————————————")

# 2. end 参数：指定结尾字符（默认是换行符 \n）
print("hello", end="")
print("world")                # 结果：helloworld（不换行）
print("————————————————————————")

# 3. end 搭配其他字符
print("第一行", end="---")
print("第二行", end="\n\n")
print("————————————————————————")

# 4. 经典应用：用 end 打印进度条效果
import time

for i in range(1, 6):
    print("=" * i, end="\r")
    time.sleep(0.5)
print("下载完成！")
print("————————————————————————")

# 5. sep 和 end 可以一起使用
print("apple", "banana", "orange", sep=" | ", end=" 喵！\n")
