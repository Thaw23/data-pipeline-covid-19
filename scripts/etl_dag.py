from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

# Define default arguments
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
dag = DAG(
    'covid19_data_pipeline',
    default_args=default_args,
    description='ETL pipeline for COVID-19 data',
    schedule_interval=timedelta(days=1),
)

def download_and_upload():
    import download_and_upload
    download_and_upload.main()

def transform_data():
    import transform_data
    transform_data.main()

def load_to_redshift():
    import load_to_redshift
    load_to_redshift.main()

# Define tasks
download_task = PythonOperator(
    task_id='download_and_upload',
    python_callable=download_and_upload,
    dag=dag,
)

transform_task = PythonOperator(
    task_id='transform_data',
    python_callable=transform_data,
    dag=dag,
)

load_task = PythonOperator(
    task_id='load_to_redshift',
    python_callable=load_to_redshift,
    dag=dag,
)

# Set task dependencies
download_task >> transform_task >> load_task
