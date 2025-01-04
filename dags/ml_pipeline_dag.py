from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import psycopg2

# Placeholder function for training the ML model
def train_ml_model():
    print("Training the ML model...")  # Add your training logic here

# Function for fetching and processing data from PostgreSQL
def fetch_data_from_postgres():
    try:
        # Connection details for the PostgreSQL container
        conn_params = {
            "dbname": "ml_data",
            "user": "ml_user",
            "password": "ml_password",
            "host": "ml_postgres",  # PostgreSQL service name in docker-compose
            "port": 5432
        }
        # Connect to PostgreSQL
        with psycopg2.connect(**conn_params) as conn:
            with conn.cursor() as cur:
                # Fetch all rows from the table
                cur.execute("SELECT * FROM sample_data;")
                rows = cur.fetchall()
                print("Data fetched from PostgreSQL:")
                for row in rows:
                    print(row)

                # Calculate the average of the 'value' column
                cur.execute("SELECT AVG(value) FROM sample_data;")
                avg_value = cur.fetchone()[0]
                print(f"Average value in the 'value' column: {avg_value}")

        # Save the processed data to a file
        with open('/opt/airflow/logs/processed_data.txt', 'w') as f:
            f.write(f"Average value: {avg_value}\n")
            f.write("Full Data:\n")
            for row in rows:
                f.write(str(row) + '\n')

    except Exception as e:
        print(f"Error connecting to PostgreSQL: {e}")


# Placeholder function for evaluating the ML model
def evaluate_ml_model():
    print("Evaluating the ML model...")  # Add your evaluation logic here

# Placeholder function for deploying the ML model
def deploy_ml_model():
    print("Deploying the ML model...")  # Add your deployment logic here

# Define the default_args for the DAG
default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'start_date': datetime(2025, 1, 4),  # Set your start date here
}

# Initialize the DAG
dag = DAG(
    'ml_pipeline',
    default_args=default_args,
    description='A simple ML pipeline DAG',
    schedule_interval=None,  # Set the schedule interval as needed
    catchup=False,
)

# Define the PythonOperator for fetching data from PostgreSQL
fetch_data_task = PythonOperator(
    task_id='fetch_data_from_postgres',
    python_callable=fetch_data_from_postgres,
    dag=dag,
)

# Define the PythonOperator for running the ML model training
train_model_task = PythonOperator(
    task_id='train_ml_model',
    python_callable=train_ml_model,  # Calling the custom ML function
    dag=dag,
)

# Define the PythonOperator for evaluating the ML model
evaluate_model_task = PythonOperator(
    task_id='evaluate_ml_model',
    python_callable=evaluate_ml_model,  # Placeholder for evaluation function
    dag=dag,
)

# Define the PythonOperator for deploying the ML model
deploy_model_task = PythonOperator(
    task_id='deploy_ml_model',
    python_callable=deploy_ml_model,  # Placeholder for deployment function
    dag=dag,
)

# Set the task order (task dependencies)
fetch_data_task >> train_model_task >> evaluate_model_task >> deploy_model_task
