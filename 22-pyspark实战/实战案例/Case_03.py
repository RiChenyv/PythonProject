import os

from pyspark import SparkContext, SparkConf

os.environ['PYSPARK_DRIVER_PYTHON'] = r"C:\Users\SCX\AppData\Local\Python\pythoncore-3.14-64\python.exe"

conf = SparkConf().setMaster("local[*]").setAppName("pyspark")
# 全局限定设置分区为1
conf.set("spark.default.parallelism", "1")
sc = SparkContext(conf=conf)
# 读取文件,获取rdd数据
file_rdd = sc.textFile(r"D:\PythonProject\14-json原始数据\原始数据\搜索引擎日志.txt")
#  需求1，热门词汇搜索
"""
先通过map将数据中的时间取出并与1组成数组，便于reducebykey统计；
再通过reducebykey聚合
sortby按降序排列
take取出前三组数据合成list
"""
result = file_rdd.map(lambda line: (line.split("\t")[0][11:13], 1)). \
    reduceByKey(lambda x, y: x + y). \
    sortBy(lambda x: x[1], ascending=False, numPartitions=1). \
    take(3)
# 输出结果
print(f"最热门搜索时间段为{result[0][0]}，有{result[0][1]}次搜索在此时间段完成")
print(f"top2热门搜索时间段为{result[1][0]}，有{result[1][1]}次搜索在此时间段完成")
print(f"top3热门搜索时间段为{result[2][0]}，有{result[2][1]}次搜索在此时间段完成")

#  需求2，热门搜索词top3
result_word = file_rdd.map(lambda line: (line.split("\t")[1], 1)). \
    reduceByKey(lambda x, y: x + y). \
    sortBy(lambda x: x[1], ascending=False, numPartitions=1). \
    take(3)
# 输出结果
print(f"热门词top3依次为{result_word[0][0]}, {result_word[1][0]}, {result_word[2][0]}")
#  需求3，统计关键字在哪个时间段被搜索最多
"""
通过map形成元组((搜索词，时段),1)；
reducebykey统计；
重构元组为(搜索词(时段，count))；
reducebykey按搜索词聚合，对比不同元组里的(时段，count)中的count，count大的留下
"""
result_get_all = file_rdd.map(lambda x: x.split("\t")). \
    map(lambda x: ((x[1], x[0][11:13]), 1)). \
    reduceByKey(lambda x, y: x + y). \
    map(lambda x: (x[0][0], (x[0][1], x[1]))). \
    reduceByKey(lambda x, y: x if x[1] > y[1] else y)
for line in result_get_all.collect():
    print(f"搜索词{line[0]}一天中，在{line[1][0]}时分被搜索的最多")

#  需求4，并输出json格式的数据
"""
通过map初步处理数据
map构造字典
saveAstextfile写出文件
"""
result_total = file_rdd.map(lambda x: x.split("\t")). \
    map(lambda x: {"time": x[0], "word": x[1], "ip": x[2]}). \
    saveAsTextFile(r"D:\PythonProject\14-json原始数据\搜索引擎json数据处理返回")

sc.stop()
