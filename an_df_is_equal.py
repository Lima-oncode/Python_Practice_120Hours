import findspark
findspark.init()

import pyspark
from pyspark.sql import SparkSession
spark = SparkSession.builder.master("local[1]").appName("is_equal").getOrCreate()

# Create DataFrame 1
data1 = [('Alice', 25), ('Bob', 30), ('Charlie', 35)]
df1 = spark.createDataFrame(data1, ['name', 'age'])

# Create DataFrame 2
data2 = [('Bob', 30), ('Eve', 28)]
df2 = spark.createDataFrame(data2, ['name', 'age'])

# Compare the DataFrames
df1_except_df2 = df1.exceptAll(df2)
df2_except_df1 = df2.exceptAll(df1)

# Print the results
print('Rows present in df1 but not in df2:')
df1_except_df2.show()
print('Rows present in df2 but not in df1:')
df2_except_df1.show()
