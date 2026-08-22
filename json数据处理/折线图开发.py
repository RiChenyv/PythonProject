# 导包
import json

from pyecharts.charts import Line, Tab
from pyecharts.options import TitleOpts, ToolboxOpts, LegendOpts

# 将所有的path与名字存储到一个字典
files = {
    "美国": "D:/PythonProject/json数据处理/原始数据/covid19_2022_美国.txt",
    "日本": "D:/PythonProject/json数据处理/原始数据/covid19_2022_日本.txt",
    "印度": "D:/PythonProject/json数据处理/原始数据/covid19_2022_印度.txt",
}
# 创建按钮
tab = Tab()
# 以下操作为批量处理
for country, path in files.items():
    # 用列表的path将json数据传递
    with open(path, "r", encoding="utf-8") as f:
        data = json.loads(f.read())["data"]
    # 初步处理原始数据
    x_date = data["日期"]
    y_data_now = data["num"]["确诊"]
    y_data_add = data["num"]["新增"]
    y_data_dead = data["num"]["死亡"]
    # 创建表格，添加数据
    line = Line()
    line.add_xaxis(x_date)
    line.add_yaxis("新增", y_data_add)
    line.add_yaxis("确诊", y_data_now)
    line.add_yaxis("死亡", y_data_dead)

    # 全局设置表格
    line.set_global_opts(
        title_opts=TitleOpts(title=f"{country} 2022年度新冠数据统计", pos_left="center", pos_top="0%"),
        legend_opts=LegendOpts(is_show=True),
        toolbox_opts=ToolboxOpts(is_show=True),
    )
    # 将表格和国家名字加入按钮中
    tab.add(line, country)

# 建表
line_now = Line()
line_now.add_xaxis(x_date)
line_add = Line()
line_add.add_xaxis(x_date)
line_dead = Line()
line_dead.add_xaxis(x_date)
# 读取数据
with open(r"D:\PythonProject\json数据处理\原始数据\totallynum.txt", "r", encoding="utf-8") as f:
    totally_num = json.loads(f.read())
    data_usa = totally_num["num_usa"]
    data_jp = totally_num["num_jp"]
    data_pi = totally_num["num_pi"]
# 添加数据
line_now.add_yaxis("美国", data_usa["确诊"])
line_now.add_yaxis("日本", data_jp["确诊"])
line_now.add_yaxis("印度", data_pi["确诊"])

line_add.add_yaxis("美国", data_usa["新增"])
line_add.add_yaxis("日本", data_jp["新增"])
line_add.add_yaxis("印度", data_pi["新增"])

line_dead.add_yaxis("美国", data_usa["死亡"])
line_dead.add_yaxis("日本", data_jp["死亡"])
line_dead.add_yaxis("印度", data_pi["死亡"])
# 全局设置
line_now.set_global_opts(
    title_opts=TitleOpts(title="美、日、印三国2022年度新冠确诊数据统计", pos_left="center", pos_top="0%"),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
)

line_add.set_global_opts(
    title_opts=TitleOpts(title="美、日、印三国2022年度新冠新增数据统计", pos_left="center", pos_top="0%"),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
)

line_dead.set_global_opts(
    title_opts=TitleOpts(title="美、日、印2022年度新冠死亡数据统计", pos_left="center", pos_top="0%"),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
)

tab.add(line_now, "确诊")
tab.add(line_add, "新增")
tab.add(line_dead, "死亡")
# 生成图像
tab.render()
