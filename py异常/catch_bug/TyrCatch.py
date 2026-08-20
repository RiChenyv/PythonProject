try:
    f = open("D:/PythonProject/666.txt", "r", encoding="utf-8")
except:
    print("请确认文件读写形式")

try:
    print(name)
    # 1 / 0
except NameError as e:
    print("name未定义")

try:
    print(name)
    1 / 0
except (NameError, ZeroDivisionError) as e:
    print("变量未定义或除零异常")

try:
    print(name)
    1 / 0
    fr = open("D:/PythonProject/666.txt", "r", encoding="utf-8")
except Exception as e:
    print("错误")

try:
    print("1")
    print("wuyichang")
except Exception as e:
    print(e)

try:
    f = open("D:/PythonProject/py异常/catch_bug/666.txt", "r", encoding="utf-8")
except Exception as e:
    print("错误")
    f = open("D:/PythonProject/py异常/catch_bug/666.txt", "w", encoding="utf-8")
else:
    print("开心呢，没有异常")
finally:
    print("执行完毕")
    f.close()
