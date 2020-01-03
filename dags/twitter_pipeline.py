from airflow import DAG
from datetime import date, timedelta, datetime

DAG_DEFAULT_ARGS = {
	'owner': 'airflow',
	'depends_on_past': False,
	'retries': 1,
	'retry_dalay': timedelta(minutes=1)
}

with DAG('twitter_dag_v1', start_date=datetime(2018, 10, 1), schedule_interval='*/10 * * * *', default_args=DAG_DEFAULT_ARGS, catchup=False) as dag:
	None
