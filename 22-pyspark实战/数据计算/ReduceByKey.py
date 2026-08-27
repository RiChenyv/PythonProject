import os

from pyspark import SparkContext, SparkConf

os.environ['PYSPARK_PYTHON'] = r"C:\Users\SCX\AppData\Local\Python\pythoncore-3.14-64\python.exe"

con = SparkConf().setMaster(
    "local[*]").setAppName(
    "FlatMap")

sc = SparkContext(conf=con)

rdd1 = sc.parallelize([("girl", 42), ("man", 21), ("girl", 22), ("man", 22), ("girl", 23)])

rdd = rdd1.reduceByKey(lambda a, b: a + b)

print(rdd.collect())

sc.stop()
