from tkinter import N
from pyspark import SparkSession

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL") \
    .getOrCreate()

columnNames = ["name","license","gender","salary"] 
driverData = [ ('Alice', 'A224455', 'Female', 3000), ('Bryan','B992244','Male',4000), ('Catherine','C887733','Female',4000) ]
 
df = spark.createDataFrame(data= driverData, schema = columnNames)
 
df.write.option("compression", "gzip").parquet("adls://path/to/output")
