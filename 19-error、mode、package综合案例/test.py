import my_utils

my_utils.file_util.print_file_info(r"D:\PythonProject\12-文件操作\bill.txt")
my_utils.file_util.append_to_file(r"D:\PythonProject\12-文件操作\bill.txt", "\n日辰羽记录")
print("————————————————————————————————————————————————————————————————")
my_utils.file_util.print_file_info(r"D:\PythonProject\12-文件操作\bill.txt")
honey = my_utils.str_util.str_reverse("ikuY")
print(honey)
lover = my_utils.str_util.substr(honey, 1, 2)
print(lover)
