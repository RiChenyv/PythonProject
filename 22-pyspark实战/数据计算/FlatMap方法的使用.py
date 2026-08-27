import os

from pyspark import SparkContext, SparkConf

os.environ['PYSPARK_PYTHON'] = r"C:\Users\SCX\AppData\Local\Python\pythoncore-3.14-64\python.exe"

con = SparkConf().setMaster("local").setAppName("FlatMap")

sc = SparkContext(conf=con)

rdd1 = sc.parallelize(["richenyv cunriyang 9178", "chunriyang", "python", "yuki"])
# flatmap解嵌套
rdd2 = rdd1.flatMap(lambda x: x.split(" "))

print(rdd2.collect())
