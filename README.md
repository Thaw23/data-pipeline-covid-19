# COVID-19 Data Pipeline

This repository contains a data engineering project that builds a data pipeline to extract, transform, and load COVID-19 data into a data warehouse for analysis.

## Objective

The objective of this project is to demonstrate the following data engineering skills:
- Extracting data from a public dataset.
- Transforming raw data to improve quality and usability.
- Loading transformed data into a data warehouse.
- Orchestrating the entire ETL process.
- Optionally, visualizing the data for insights.

## Dataset

COVID-19 Data:
- Link: [COVID-19 Data from Our World in Data](https://github.com/owid/covid-19-data/tree/master/public/data)
- Description: This dataset contains COVID-19 data including daily new cases, deaths, testing data, and vaccinations for countries around the world.

## Architecture

1. Data Extraction:
   - The dataset is extracted from the [Our World in Data GitHub repository](https://github.com/owid/covid-19-data/tree/master/public/data).
   - A Python script is used to download the dataset and upload it to an AWS S3 bucket.

2. Data Transformation:
   - Apache Spark is used to clean and transform the data.
   - Transformations include removing null values, converting data types, and aggregating data by country and date.

3. Data Loading:
   - The transformed data is loaded into Amazon Redshift.

4. Orchestration:
   - Apache Airflow is used to schedule and monitor the ETL pipeline.

## Tools and Technologies

- Python: For data extraction and scripting.
- Apache Spark: For data transformation.
- AWS S3: For data storage.
- Amazon Redshift: For data warehousing.
- Apache Airflow: For pipeline orchestration.

## Setup Instructions

### Prerequisites

- AWS account with access to S3 and Redshift.
- Python installed.
- Apache Spark installed.
- Apache Airflow installed.
