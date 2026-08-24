# 使用面向对象的思想完成
from pyecharts.charts import Bar
from pyecharts.options import ToolboxOpts, TitleOpts, LabelOpts

from File_define import *
from data_define import *

"""
读取数据
"""
text_filereader = TextReader(r"D:\PythonProject\14-json原始数据\原始数据\2026年1月销售数据.txt")
json_reader = JsonReader(r"D:\PythonProject\14-json原始数据\原始数据\2026年2月销售数据.txt")

jan_data: list[Record] = text_filereader.read_data()
feb_data: list[Record] = json_reader.read_data()

all_data: list[Record] = jan_data + feb_data

data_dict = {}

for record in all_data:
    if record.date in data_dict:
        data_dict[record.date] += record.money
    else:
        data_dict[record.date] = record.money

"""
可视化
"""
bar = Bar()

x_data = data_dict.keys()
y_data = [round(value, 1) for value in data_dict.values()]

bar.add_xaxis(list(x_data))
bar.add_yaxis("日销售额", y_data, label_opts=LabelOpts(is_show=False))

bar.set_global_opts(
    title_opts=TitleOpts(title=f"2026年全球1、2月销售额柱状图", pos_left="center", pos_top="0%"),
    toolbox_opts=ToolboxOpts(is_show=True),
)

bar.render("2026年1、2月销售额柱状统计图.html")
