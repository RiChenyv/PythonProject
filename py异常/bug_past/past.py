def funco1():
    print("1")
    1 / 0
    print("2")


def funco2():
    print("3")
    funco1()
    print("4")


def main():
    funco2()


main()
'''
Traceback (most recent call last):
  File "D:\PythonProject\py异常\bug_past\past.py", line 17, in <module>
    main()
    ~~~~^^
  File "D:\PythonProject\py异常\bug_past\past.py", line 14, in main
    funco2()
    ~~~~~~^^
  File "D:\PythonProject\py异常\bug_past\past.py", line 9, in funco2
    funco1()
    ~~~~~~^^
  File "D:\PythonProject\py异常\bug_past\past.py", line 3, in funco1
    1 / 0
    ~~^~~
ZeroDivisionError: division by zero
'''
