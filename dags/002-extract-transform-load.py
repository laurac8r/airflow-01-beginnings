from airflow import DAG
from airflow.operators.python import PythonOperator

with DAG('lauras-extract-transform-load-DAG', description='A simple tutorial DAG',):
    def extract(**kwargs):
        """
        Extracts the sample data.
        :param kwargs:
        :return:
        """
        ti = kwargs['ti']
        data_string = '{"1001": 301.27, "1002": 433.21, "1003": 502.22}'
        ti.xcom_push(key='order_data', value=data_string)

    extract_task = PythonOperator(task_id='extract', python_callable=extract)