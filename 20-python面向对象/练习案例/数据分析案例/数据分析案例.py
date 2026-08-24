# 使用面向对象的思想完成
from pyecharts.charts import Bar
from pyecharts.options import ToolboxOpts, TitleOpts, LabelOpts, InitOpts

from File_define import *
from data_define import *

"""
读取数据
"""
# 创建对象
text_filereader = TextReader(r"D:\PythonProject\14-json原始数据\原始数据\2026年1月销售数据.txt")
json_reader = JsonReader(r"D:\PythonProject\14-json原始数据\原始数据\2026年2月销售数据.txt")
# 调用接口方法读取数据，得到一个record对象列表
jan_data: list[Record] = text_filereader.read_data()
feb_data: list[Record] = json_reader.read_data()
# 整合所有数据
all_data: list[Record] = jan_data + feb_data
"""
数据处理
"""
# 我们需要日期和销售额来制作图表，单独取出这两元素，用字典表示
# 准备空字典来接收数据
data_dict = {}
# for循环取出每个对象，来计算日总销售额
for record in all_data:
    # 判断当天日期是否已成为keys
    if record.date in data_dict:
        # 已存有keys，算总销售额
        data_dict[record.date] += record.money
    else:
        # 未存有keys，录入本次销售额
        data_dict[record.date] = record.money

"""
可视化
"""
# 创建柱状图对象
bar = Bar(init_opts=InitOpts(width="100%", height="80vh"))
# 添加数据
x_data = data_dict.keys()
y_data = [round(value, 1) for value in data_dict.values()]  # 保留一位小数
"""
上一行等价于：
y_data = []                       # 先建一个空列表
for v in data_dict.values():      # 遍历每一天的销售额
    y_data.append(round(v, 1))    # 四舍五入到1位小数，再放进列表
"""
bar.add_xaxis(list(x_data))
bar.add_yaxis("日销售额", y_data, label_opts=LabelOpts(is_show=False))
# 全局设置
bar.set_global_opts(
    title_opts=TitleOpts(title=f"2026年全球1、2月销售额柱状图", pos_left="center", pos_top="0%"),
    toolbox_opts=ToolboxOpts(is_show=True),
)
# 代码生成图像
bar.render("2026年1、2月销售额柱状统计图.html")
