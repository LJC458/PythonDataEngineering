import datetime as dt
from datetime import timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
import pandas as pd

def CSVToJson():
    df=pd.read_CSV('C:/Users/LiamTower/Desktop/PythonDataEngineering/CSV_JSON flow/data.CSV')
    for i,r in df.iterrows():
        print(r['name'])
    df.to_JSON('fromAirflow.JSON',orient='records')

default_args = {
 'owner': 'liamcochrane',
 'start_date': dt.datetime(2021, 11, 14),
 'retries': 1,
 'retry_delay': dt.timedelta(minutes=5),
}

#The DAG is created with the following code:
with DAG('MyCSVDAG',
    default_args=default_args,
    schedule_interval=timedelta(minutes=5), 
    # '0 * * * *',
    ) as dag:

    print_starting = BashOperator(task_id='starting',bash_command='echo "I am reading the CSV now....."')
    CSVJson = PythonOperator(task_id='convertCSVtoJson',python_callable=CSVToJson)
    print_starting >> CSVJson
