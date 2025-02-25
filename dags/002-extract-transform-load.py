import json
from typing import Dict, Any

from airflow import DAG
from airflow.models import TaskInstance
from airflow.operators.python import PythonOperator

with DAG('lauras-extract-transform-load-DAG', description='A simple tutorial DAG', ):
    def extract(**kwargs) -> None:
        """
        Extracts sample data.
        Args:
            **kwargs: Python callable arguments

        Returns:
            None
        """
        kwargs: Dict[str, Any]
        ti: TaskInstance = kwargs.get('ti')
        data_string = '{"1001": 301.27, "1002": 433.21, "1003": 502.22}'
        ti.xcom_push(key='order_data', value=data_string)


    def transform(**kwargs) -> None:
        """
        Transforms sample data.
        Args:
            **kwargs: Python callable arguments

        Returns:
            None
        """
        kwargs: Dict[str, Any]
        ti = kwargs['ti']

        order_data_str = ti.xcom_pull(key='order_data', task_ids='extract')
        order_data = json.loads(order_data_str)

        total_amount = sum(order_data.values())

        total_value = {'total_order_value': total_amount}
        total_value_str = json.dumps(total_value)

        ti.xcom_push(key='total_amount', value=total_value_str)


    def load(**kwargs) -> None:
        """
        Load sample data.
        Args:
            **kwargs: Python callable arguments

        Returns:
            None
        """
        kwargs: Dict[str, Any]
        ti = kwargs['ti']
        total_value_str = ti.xcom_pull(key='total_amount', task_ids='transform')
        total_order_value = json.loads(total_value_str)

        print(total_order_value)


    extract_task = PythonOperator(task_id='extract', python_callable=extract)

    transform_task = PythonOperator(task_id='transform', python_callable=transform)

    load_task = PythonOperator(task_id='load', python_callable=load)

    extract_task >> transform_task >> load_task
