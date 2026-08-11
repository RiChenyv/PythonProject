def list_for_func(list):
    list2 = []
    for item in list:
        if item % 2 == 0:
            list2.append(item)
    return list2


def list_while_func(list):
    list2 = []
    index = 0
    while index < len(list):
        if list[index] % 2 == 0:
            list2.append(list[index])
        index += 1
    return list2


data_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
data_list2 = list_while_func(data_list)
print(data_list2)
data_list3 = list_for_func(data_list)
print(data_list3)
