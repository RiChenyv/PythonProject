def create_list(part1, part2):
    my_list = [part1, part2]
    return my_list


def create_tuple(part1, part2, part3):
    my_tuple = (part1, part2, part3)
    return my_tuple


def serach_TulpeAgeIndex(tuple):
    return tuple.index(age)


def search_TulpeName(tuple):
    return tuple[0]


print("请输入姓名：")
name = input()
print("请输入您的年龄:")
age = int(input())
print("请输入您的两个爱好：")
hobby_1 = input()
hobby_2 = input()
list = create_list(hobby_1, hobby_2)
my_tulpe = create_tuple(name, age, list)
print(f"元组内容为{my_tulpe}")
print(f"年龄的下标为{serach_TulpeAgeIndex(my_tulpe)}")
print(f"学生名为{search_TulpeName(my_tulpe)}")
my_tulpe[2].pop(0)
print(f"删除兴趣1后，元组内容为{my_tulpe}")
my_tulpe[2].append('coding')
print(f"元组内容为{my_tulpe}")
