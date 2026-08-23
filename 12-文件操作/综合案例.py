fr = open("D:/PythonProject/12-文件操作/bill.txt", "r", encoding="utf-8")
fw = open("D:/PythonProject/12-文件操作/bill.txt.bak", "w", encoding="utf-8")
fw2 = open("D:/PythonProject/12-文件操作/bill_test.txt.", "w", encoding="utf-8")
for line in fr:
    # 去掉换行符号
    line = line.strip()
    # 以逗号分割为列表，取每行的第五个元素判断
    if line.split(",")[4] == "正式":
        fw.write(line)
        fw.write("\n")
    else:
        fw2.write(line)
        fw2.write("\n")
fw.close()
fr.close()
