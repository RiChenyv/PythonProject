"""
包含标题配置项TitleOpts,LegendOpts图例配置项，ToolboxOpts工具箱配置项，VisualMapOpts视觉映射配置项，DataZoomOpts区域映射配置项，TooltipOpts提示框配置项
"""
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts

line = Line()
line.add_xaxis(["中国", "美国", "英国"])
line.add_yaxis("GDP", [30, 20, 10])
# 配置
line.set_global_opts(
    title_opts=TitleOpts(title="GDP展示", pos_left="center", pos_top="0%"),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True),
)
line.render()
