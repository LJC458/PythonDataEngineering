import datetime as dt
from datetime import timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
import pandas as pd
import os

file ="/mnt/c/Users/liamTower/Desktop/PythonDataEngineering/CSV_JSON/data.CSV"

def CSVToJson():
    df=pd.read_csv(file)
    for i,r in df.iterrows():
        print(r['name'])
        df.to_json('fromAirflow.JSON',orient='records')

default_args = {
 'owner': 'liamcochrane',
 'start_date': dt.datetime(2021, 11, 14),
 'retries': 1,
 'retry_delay': dt.timedelta(minutes=5),
}

#The DAG is created with the following code:
# default_args = {
#     'owner': 'paulcrickard',
#     'start_date': dt.datetime(2020, 3, 18),
#     'retries': 1,
#     'retry_delay': dt.timedelta(minutes=5),
# }


with DAG('MyCSVDAG',default_args=default_args,schedule_interval=timedelta(minutes=5),      # '0 * * * *',
) as dag:

    print_starting = BashOperator(task_id='starting',bash_command='echo "I am reading the CSV now....."')
    
    csvJson = PythonOperator(task_id='convertCSVtoJson',python_callable=CSVToJson)


print_starting >> csvJson
