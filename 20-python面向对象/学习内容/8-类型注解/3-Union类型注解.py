from typing import Union


# 联合类型注解可广泛适用  Union[type,type...]
def showData(data: Union[int, str]) -> Union[int, str]:
    return data


my_list: list[Union[int, str]] = [1, 2, "richenyv", "xiaonanniang"]

my_dict: dict[str, Union[int, str]] = {"xiaonan": "richenyv", "xiangruannanniang": 18}

print(showData("xiaonanniang"))
print(my_list)
print(my_dict)
