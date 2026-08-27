import os

from pyspark import SparkContext, SparkConf

os.environ['PYSPARK_DRIVER_PYTHON'] = r"C:\Users\SCX\AppData\Local\Python\pythoncore-3.14-64\python.exe"

conf = SparkConf().setMaster("local[*]").setAppName("Octopus")

sc = SparkContext(conf=conf)

rdd1 = sc.parallelize([1, 2, 3, 3, 3, 4, 4, 5, 5, 5, 6, 6, 6, 6, 6])

rdd2 = rdd1.distinct()

print(rdd2.collect())

sc.stop()
