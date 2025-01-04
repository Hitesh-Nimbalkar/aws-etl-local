# Use the official Apache Airflow image as the base image
FROM apache/airflow:2.10.4

# Install additional Python dependencies from requirements.txt
COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt
