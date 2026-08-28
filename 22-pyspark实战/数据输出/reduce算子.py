import os

from pyspark import SparkContext, SparkConf

os.environ['PYSPARK_DRIVER_PYTHON'] = r"C:\Users\SCX\AppData\Local\Python\pythoncore-3.14-64\python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_PySpark")

sc = SparkContext(conf=conf)
# 写入内容
rdd = sc.parallelize([1, 2, 3, 4, 5, 6, 7])

rdd_list = rdd.reduce(lambda x, y: x + y)

print(rdd_list)

sc.stop()
