# 导包
import json

from pyecharts.charts import Line, Tab
from pyecharts.options import TitleOpts, ToolboxOpts, LegendOpts

# 将所有的path与名字存储到一个字典
files = {
    "美国": "D:/PythonProject/14-json原始数据/原始数据/covid19_2022_美国.txt",
    "日本": "D:/PythonProject/14-json原始数据/原始数据/covid19_2022_日本.txt",
    "印度": "D:/PythonProject/14-json原始数据/原始数据/covid19_2022_印度.txt",
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
    # 读取数据
    with open(r"D:\PythonProject\14-json原始数据\原始数据\totallynum.txt", "r", encoding="utf-8") as f:
        totally_num = json.loads(f.read())
        data_usa = totally_num["num_usa"]
        data_jp = totally_num["num_jp"]
        data_pi = totally_num["num_pi"]
# 指标 → 标题
metrics = {
    "确诊": "美、日、印三国2022年度新冠确诊数据统计",
    "新增": "美、日、印三国2022年度新冠新增数据统计",
    "死亡": "美、日、印三国2022年度新冠死亡数据统计",
}
countries = [("美国", data_usa), ("日本", data_jp), ("印度", data_pi)]
# 添加数据
for metric, title in metrics.items():
    line = Line()
    line.add_xaxis(x_date)
    for country, data in countries:
        line.add_yaxis(country, data[metric])
        # 全局设置
        line.set_global_opts(
            title_opts=TitleOpts(title=title, pos_left="center", pos_top="0%"),
            legend_opts=LegendOpts(is_show=True),
            toolbox_opts=ToolboxOpts(is_show=True),
        )
        # 生成图像
    tab.add(line, metric)
    tab.render()
