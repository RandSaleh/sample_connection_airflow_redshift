from airflow.operators.dummy_operator import DummyOperator
import datetime
import logging
from airflow import DAG
from airflow.providers.amazon.aws.hooks.base_aws import AwsBaseHook
from airflow.hooks.postgres_hook import PostgresHook
from airflow.operators.postgres_operator import PostgresOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def load_data_from_redshift(*args,**kwargs):
    hook = AwsBaseHook(client_type='secretsmanager',aws_conn_id="aws_credentials")
    test= hook.get_conn()
    logging.info(f"test ... {test}")
    credential = hook.get_credentials()
    redshift_hook = PostgresHook("redshift")
    sql = "select * from users limit 10;"
    res = redshift_hook.get_records(sql)

    for i in res : 
        logging.info(i)

    logging.info(f"test credentials, {credential}")
     

with DAG(dag_id="ConnectToRedshift",
        start_date=datetime(2021,1,1),
        schedule_interval="@hourly",
        catchup=False) as dag:

    start = DummyOperator(task_id = "Start")
    
    list_task = PythonOperator(
                task_id = "list_task",
                python_callable=load_data_from_redshift)

    end = DummyOperator(task_id = "End")

start >> list_task >> end





