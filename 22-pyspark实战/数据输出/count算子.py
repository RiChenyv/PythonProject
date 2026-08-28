import os

from pyspark import SparkContext, SparkConf

os.environ['PYSPARK_DRIVER_PYTHON'] = r"C:\Users\SCX\AppData\Local\Python\pythoncore-3.14-64\python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_PySpark")

sc = SparkContext(conf=conf)

rdd1 = sc.parallelize([1, 2, 3, 4])

print(rdd1.count())

sc.stop()
