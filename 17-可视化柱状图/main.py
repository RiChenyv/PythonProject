# 导包
from pyecharts.charts import Bar, Timeline
from pyecharts.globals import ThemeType
from pyecharts.options import LabelOpts, TitleOpts, ToolboxOpts

"""
原始数据处理
"""
# 按行读取数据
with open(r"D:\PythonProject\14-json原始数据\原始数据\各国GDP_1960-2026.txt", "r", encoding="utf-8") as f:
    data_lines = f.readlines()
# 删除第一行的无用数据
data_lines.pop(0)
# 建立空字典以便于后续存储
data_dict = {}
# for循环批量处理数据
for line in data_lines:
    # 去除原始数据尾部的换行符
    line = line.strip()
    # 把字符串按逗号分割为列表，批量对列表取固定位置的元素进行赋值
    year = int(line.split(",")[0])
    country = line.split(",")[3]
    GDP = float(line.split(",")[1])
    # 把国家与GDP添加到字典中
    try:
        # 以年份为key，将国家和GDP添加到列表year中
        data_dict[year].append([country, GDP])
    # year初次加入字典时会由于无year_key而报错
    except KeyError:
        # 创建year列表
        data_dict[year] = []
        # 添加
        data_dict[year].append([country, GDP])
# 对字典的key进行从小到大排序
sorted_year_list = sorted(data_dict.keys())
# 设置时间线并设置主题
time = Timeline({"theme": ThemeType.LIGHT})
# 批量化处理每一年的前八数据
for year in sorted_year_list:
    # 对当年的year列表中下标为1的数据进行由大到小的排序
    data_dict[year].sort(key=lambda x: x[1], reverse=True)
    # 取出每年的year列表中前八的数据并创建柱状图
    year_data = data_dict[year][0:8]
    # 创建x、y轴数据空列表用于接收数据
    x_data = []
    y_data = []
    for country_gdp in year_data:
        # x加入国家name，y加入gdp数值
        x_data.append(country_gdp[0])
        y_data.append(country_gdp[1])

    # 创建柱状图
    bar = Bar()
    # 由于为横向柱状图，应逆置数据
    x_data.reverse()
    y_data.reverse()
    # 添加数据
    bar.add_xaxis(x_data)
    bar.add_yaxis("GDP(亿美元)", y_data, label_opts=LabelOpts(position="right"))
    # 组成横向柱状图
    bar.reversal_axis()
    # 柱状图全局设置
    bar.set_global_opts(
        title_opts=TitleOpts(title=f"{year}年全球前八GDP排行榜", pos_left="center", pos_top="0%"),
        toolbox_opts=ToolboxOpts(is_show=True),
    )
    # 将柱状图按时间添加进时间线
    time.add(bar, str(year))
    # 时间线设置
    time.add_schema(
        play_interval=1000,  # 视图更换间隔
        is_timeline_show=True,  # 是否展示时间线
        is_auto_play=True,  # 是否自动播放
        is_loop_play=True,  # 是否循环播放
    )
# 代码转试图
time.render("GDP图标.html")
