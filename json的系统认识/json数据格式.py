"""
演示json数据与python的转化
"""
import json

data = [{"name": "日辰羽", "age": 18}, {"name": "richenyv", "age": 19}]
# 不使用ASCII码全部转换中文
json_str = json.dumps(data, ensure_ascii=False)
print(json_str)
# json本质上为字符串
print(type(json_str))
d = {"name": "日辰羽", "age": 18}
json_str_02 = json.dumps(d, ensure_ascii=False)
print(json_str_02)
print(type(json_str_02))
# json幻化为py
new_data = json.loads(json_str)
new_d = json.loads(json_str_02)
print(new_data)
print(new_d)
print(type(new_data))
print(type(new_d))
