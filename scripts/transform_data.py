from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date

# initializing spark session
spark = SparkSession.builder\
        .appName("COVID 19 Data Transformation")\
        .getOrCreate()

# config
s3_bucket_name = 'covid-19-data-bucket-57ff8653-e9e6-430c-b576-8cd83ac9d64f'
raw_data_path = f's3a://{s3_bucket_name}/owid-covid-data.csv'
transform_data_path = f's3a://{s3_bucket_name}/transformed/owid-covid-data.parquet'

# load raw data from s3
df = spark.read.csv(raw_data_path, header=True, inferSchema=True)

# transform
df_transformed = df.withColumn('date', to_date(col('date'), 'yyyy-MM-dd'))

# filter out null values
df_transformed = df_transformed.na.drop()

df_transformed.write.mode('overwrite').parquet(transform_data_path)

spark.stop()