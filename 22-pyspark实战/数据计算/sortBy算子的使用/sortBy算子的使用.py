import os

from pyspark import SparkContext, SparkConf

os.environ['PYSPARK_DRIVER_PYTHON'] = r"C:\Users\SCX\AppData\Local\Python\pythoncore-3.14-64\python.exe"

conf = SparkConf().setMaster("local[*]").setAppName("PySpark")

sc = SparkContext(conf=conf)

rdd = sc.textFile(r"D:\PythonProject\14-json原始数据\原始数据\2026年1月销售数据.txt")

world_rdd = rdd.flatMap(lambda x: x.split(","))

world_with_one_rdd = world_rdd.map(lambda word: (word, 1))

result_rdd = world_with_one_rdd.reduceByKey(lambda x, y: x + y)

final_rdd = result_rdd.sortBy(lambda x: x[1], ascending=True, numPartitions=1)

print(final_rdd.collect())

sc.stop()
