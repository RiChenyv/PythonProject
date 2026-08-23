# 目录加了数字前缀后，`from 11-包与导入.my_package import READMODE` 这种写法是语法错误
# （模块名不能以数字开头、不能含连字符），所以改用 importlib 动态导入；
# 同时把项目根目录加入 sys.path，保证从任何位置运行都能找到这个包：
import os
import sys
import importlib

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
READMODE = importlib.import_module("11-包与导入.my_package.READMODE")

f = READMODE.ReadMode("D:/PythonProject/test.txt")
print(f.readline())
f.close()
