from PythonPackage.my_package import READMODE

f = READMODE.ReadMode("D:/PythonProject/test.txt")
print(f.readline())
f.close()
