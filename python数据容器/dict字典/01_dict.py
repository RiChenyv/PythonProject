# 定义字典
my_dict = {
    "SCX": 150,
    "RICHENYV": 98,
    "CUNCHENYV": 67
}
# 定义空字典：
empty_dict = {}
empty_dict = dict()
print(my_dict, type(my_dict))
print(empty_dict, type(empty_dict))
# 定义重复key的字典
print("————————————————————————————————————————")
my_dict = {
    "SCX": 150,
    'SCX': 98,
    "CUNCHENYV": 67
}
print(my_dict, type(my_dict))
# 基于字典的key获取value
print("————————————————————————————————————————")
score = my_dict["SCX"]
print(score)
# 字典的嵌套
print("————————————————————————————————————————")
student_dict = {
    "SCX": {
        "语文": 112,
        "数学": 140,
        "英语": 125
    },
    "RICHENYV": {
        "chinese": 141,
        "math": 121,
        "English": 122
    },
    "CUNRIUANG": {
        "chinese": 117,
        "math": 111,
        "English": 131
    }
}
print(student_dict["SCX"]["语文"])
print(student_dict["RICHENYV"])
print(student_dict["CUNRIUANG"])
