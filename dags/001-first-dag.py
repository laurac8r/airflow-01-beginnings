from airflow import DAG
from airflow.operators.empty import EmptyOperator

with DAG('lauras-first-DAG', description='A simple tutorial DAG',):
    EmptyOperator(task_id='first_task')