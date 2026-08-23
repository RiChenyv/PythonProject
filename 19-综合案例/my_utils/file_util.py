def print_file_info(file_name):
    file = None
    try:
        file = open(file_name, "r", encoding="utf-8")
        print(file.read())
    except Exception as e:
        print(f"存在异常为{e}的报错问题，请注意")
    finally:
        if file is not None:
            file.close()


def append_to_file(file_name, content):
    file = None
    try:
        file = open(file_name, "a", encoding="utf-8")
        file.write(content)
    except Exception as e:
        print(f"存在错误{e},无法进行追加")
    finally:
        if file is not None:
            file.close()


if __name__ == "__main__":
    print_file_info("D:/PythonProject/test.txt")
    print_file_info("D:/PythonProject/test_bug.txt")
    append_to_file("D:/PythonProject/test.txt",
                   "这是一条来自my_utils测试中的函数追加\n")
    append_to_file("D:/PythonProject/test_bug.txt",
                   "这是一条来自my_utils测试中的函数追加\n")
