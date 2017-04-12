# boilerplate.py
# boilerplate for starting spark context locally

def startSparkCtx():

	print "Initializing Spark and SQL context"

	import os
	import sys

	spark_path = "/Users/weizhong/stk/spark-1.6.0-bin-hadoop2.6"

	os.environ['SPARK_HOME'] = spark_path
	os.environ['HADOOP_HOME'] = spark_path

	sys.path.append(spark_path + "/bin")
	sys.path.append(spark_path + "/python")
	sys.path.append(spark_path + "/python/pyspark/")
	sys.path.append(spark_path + "/python/lib")
	sys.path.append(spark_path + "/python/lib/pyspark.zip")
	sys.path.append(spark_path + "/python/lib/py4j-0.9-src.zip")

	from pyspark import SparkContext
	from pyspark import SparkConf
	from pyspark.sql import SQLContext
	from pyspark.sql.types import *

	#sc = SparkContext("local")
	sc = SparkContext()
	sqlCtx = SQLContext(sc)

	print "Done"