"""
演示pyecharts入门
"""
# 导包
from pyecharts.charts import Line

# 创建line对象
line = Line()
# x,y轴添加数据
line.add_xaxis(["中国", "美国", "英国"])
line.add_yaxis("GDP", [30, 20, 10])
# 通过render方法将代码生成为图像
line.render()
