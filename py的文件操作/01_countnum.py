with open("D:\PythonProject\py的文件操作\write.txt", "w", encoding="utf-8") as f:
    f.write("itrichenyv itcast pythn ")
    f.write("itrihenyv itcst python ")
    f.write("itricheyv itcas python ")
    f.write("itricheny icast python ")

with open("D:\PythonProject\py的文件操作\write.txt", "r", encoding="utf-8") as f:
    num = f.read().count("python")
    print(type(f.read()))
print(num)
