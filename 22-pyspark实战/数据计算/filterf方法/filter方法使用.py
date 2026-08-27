import os

from pyspark import SparkContext, SparkConf

os.environ['PYSPARK_DRIVER_PYTHON'] = r"C:\Users\SCX\AppData\Local\Python\pythoncore-3.14-64\python.exe"

conf = SparkConf().setAppName("filter").setMaster("local[*]")
sc = SparkContext(conf=conf)

rdd = sc.parallelize([1, 2, 3, 4, 5, 6])
# 过滤
rdd_new = rdd.filter(lambda x: x % 2 == 0)

print(rdd_new.collect())

sc.stop()
