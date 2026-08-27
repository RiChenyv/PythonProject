import json
import os

from pyspark import SparkContext, SparkConf

os.environ['PYSPARK_DRIVER_PYTHON'] = r"C:\Users\SCX\AppData\Local\Python\pythoncore-3.14-64\python.exe"

conf = SparkConf().setMaster("local[*]").setAppName("Spark")
sc = SparkContext(conf=conf)

rdd_init = sc.textFile(r"D:\PythonProject\14-json原始数据\原始数据\2026年2月销售数据.txt")

json_rdd = rdd_init.filter(lambda line: line.strip() not in ["[", "]", ""]).map(
    lambda line: json.loads(line.strip().rstrip(",")))

dict_rdd = json_rdd.map(lambda line: (line["销售省份"], round(line["销售额"], 2)))

city_with_money_rdd = dict_rdd.reduceByKey(lambda x, y: x + y)

print([(p, f"{m:.2f}") for p, m in city_with_money_rdd.collect()])

sc.stop()
