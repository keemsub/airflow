from datetime import datetime
import json
from airflow import DAG
from pandas import json_normalize

# operation import
from airflow.providers.sqlite.operators.sqlite import SqliteOperator
from airflow.providers.http.sensors.http import HttpSensor
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

import sqlite3
from airflow.operators.python import PythonOperator

def run_sqlite_query():
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS my_table (id INTEGER PRIMARY KEY, name TEXT)')
    conn.commit()
    conn.close()

sqlite_task = PythonOperator(
    task_id="sqlite_task",
    python_callable=run_sqlite_query
)

#default create
default_args = {
    "start_date":datetime(2022,1,1) #현재날짜보다 작아서 무조건 한번은 실행 성공
}

NAVER_CLI_ID = "ID"
NAVER_CLI_SECRET = "PW"

#Dag setting
with DAG(
    dag_id="naver-search-pipline",
    schedule_interval="@daily",
    default_args=default_args,
    tags=["naver","search","local","api","pipline"],
    catchup=False) as dag: # catchup True면 start date부터 현재까지 못돌린 날들을 채움
    pass