# 写入新文件
f = open("D:/PythonProject/12-文件操作/write/write.py", "w", encoding="utf-8")
f.write("print('hello world')")

# close方法内置了flush

f.close()
# 写入旧文件
with open("D:/PythonProject/12-文件操作/write/write.py", "w", encoding="utf-8") as f:
    f.write('print("byebye world which had never belong me")')
