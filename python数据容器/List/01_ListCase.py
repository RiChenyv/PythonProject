my_list = [21,25,21,23,22,20]
print(my_list)
my_list.append(31)
print(my_list)
my_list2 = [29,33,30]
my_list.extend(my_list2)
print(my_list)
print(my_list[0])
length = len(my_list)
print(my_list[length-1])
index = my_list.index(31)
print(index)