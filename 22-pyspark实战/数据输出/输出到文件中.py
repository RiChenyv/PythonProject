import os

from pyspark import SparkContext, SparkConf

os.environ['PYSPARK_DRIVER_PYTHON'] = r"C:\Users\SCX\AppData\Local\Python\pythoncore-3.14-64\python.exe"

conf = SparkConf().setMaster("local[*]").setAppName("pyspark")
# 全局设置分区为1
# conf.set("spark.default.parallelism", "1")

sc = SparkContext(conf=conf)

rdd1 = sc.parallelize([1, 2, 3, 4], 1)

rdd2 = sc.parallelize(["richenyv", "chunriyang", "shichenxiang"], numSlices=1)

rdd1.saveAsTextFile(r"D:\PythonProject\test2")
rdd2.saveAsTextFile(r"D:\PythonProject\test1")

sc.stop()
