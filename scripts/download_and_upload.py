import os
import requests
import boto3
from botocore.exceptions import NoCredentialsError
import uuid
# Configuration

s3_bucket_name = 'covid-19-data-bucket-57ff8653-e9e6-430c-b576-8cd83ac9d64f' # uuid used to make bucket-name unique
data_url = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'
local_file_name = 'owid-covid-data.csv'
s3 = boto3.client('s3')
def download_data(url, local_file_name):
    response = requests.get(url)
    with open(local_file_name, 'wb') as file:
        file.write(response.content)

def upload_to_s3(local_file_name, bucket_name, s3_file_name):
    
    try:
        if not s3_check_bucket_exists(bucket_name):
            s3.create_bucket(Bucket=bucket_name)
        s3.upload_file(local_file_name, bucket_name, s3_file_name)
        print(f"Upload Successful: {s3_file_name}")
    except FileNotFoundError:
        print("The file was not found")
    except NoCredentialsError:
        print("Credentials are not available")

def s3_check_bucket_exists(bucket_name):
    try:
        response = s3.list_buckets()
        for bucket in response['Buckets']:
            if bucket_name == bucket:
                return True
        return False
    except Exception as e:
        print(e)
        
if __name__ == "__main__":
    # download data from url
    download_data(data_url, local_file_name)

    # upload to s3
    upload_to_s3(local_file_name, s3_bucket_name, local_file_name)

