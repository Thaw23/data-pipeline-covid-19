from pyspark.sql import SparkSession

# Configuration
s3_bucket_name = 'covid-19-data-bucket-57ff8653-e9e6-430c-b576-8cd83ac9d64f'
transformed_data_path = f's3a://{s3_bucket_name}/transformed/owid-covid-data.parquet'
redshift_jdbc_url = 'jdbc:redshift://redshift-cluster-url:5439/covid-database'
redshift_user = 'username'
redshift_password = 'password'
table_name = 'covid_data'

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("COVID19 Data Load to Redshift") \
    .getOrCreate()

# Load transformed data from S3
df = spark.read.parquet(transformed_data_path)

# Load data into Redshift
df.write \
    .format("jdbc") \
    .option("url", redshift_jdbc_url) \
    .option("dbtable", table_name) \
    .option("user", redshift_user) \
    .option("password", redshift_password) \
    .option("driver", "com.amazon.redshift.jdbc.Driver") \
    .mode("overwrite") \
    .save()

spark.stop()
