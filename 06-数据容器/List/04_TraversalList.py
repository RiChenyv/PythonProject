def list_while_func(my_list):
    index = 0
    while index < len(my_list):
        if index != len(my_list) - 1:
            print(my_list[index], end=",")
            index = index + 1
        else:
            print(my_list[index])
            index = index + 1


def list_for_func(list):
    for item in list:
        if item != list[len(list) - 1]:
            print(item, end=",")
        else:
            print(item)


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_for_func(my_list)
list_while_func(my_list)
