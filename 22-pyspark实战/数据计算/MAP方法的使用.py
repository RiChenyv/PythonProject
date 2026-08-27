import os

from pyspark import SparkContext, SparkConf

os.environ['PYSPARK_PYTHON'] = r"C:\Users\SCX\AppData\Local\Python\pythoncore-3.14-64\python.exe"

conf = SparkConf().setAppName("map").setMaster(
    "local[*]")
sc = SparkContext(conf=conf)
# 创建rdd对象
rdd = sc.parallelize([1, 2, 3, 4, 5, 6])

# 使用map方法

rdd2 = rdd.map(lambda x: x * 10)

print(rdd2.collect())

sc.stop()
