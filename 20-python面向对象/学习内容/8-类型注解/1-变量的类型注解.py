import json
import random


def func():
    return random.randint(1, 10)


# 常规变量注解
number: int = 10
float_number: float = 3.14
Bool: bool = True
Str: str = "str"
# 数据容器注解
my_dict: dict = {"richenyv": "girl", "chunriyang": "little girl"}  # 简略注解
my_list: list[int] = [1, 2, 3]
my_tuple: tuple[str, int, bool] = ("richenyv", 2, True)  # 详细注解
# 在注释中进行类型注解
var_1 = random.randint(1, 10)  # type: int
var_2 = json.loads('{"richenyv": "girl", "chunriyang": "little girl"}')  # type: dict[str,str]
var_3 = func()  # type: int
# 类型注解的限制
var_4: int = "richenyv"
var_5: str = 123  # 可见，类型注解仅起到标注作用，是提示性作用，并非直接限制变量的类型的决定性作用
