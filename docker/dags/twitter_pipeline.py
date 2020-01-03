from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import date, timedelta, datetime

import twitterETL.getOldTweets as getOldTweets
import twitterETL.loadbdTweets as loadbdTweets

import twitterETL.getOldTweets

DAG_DEFAULT_ARGS = {
	'owner': 'airflow',
	'depends_on_past': False,
	'retries': 1,
	'retry_dalay': timedelta(minutes=1)
}

with DAG('twitter_dag_v1', start_date=datetime(2018, 10, 1), schedule_interval='*/10 * * * *', default_args=DAG_DEFAULT_ARGS, catchup=False) as dag:
    getOldTweets_task = PythonOperator(task_id='getOldTweets_task', python_callable=getOldTweets.main)
    loadbdTweets_task = PythonOperator(task_id='loadbdTweets_task', python_callable=loadbdTweets.main)
    
    getOldTweets_task >> loadbdTweets_task



    
