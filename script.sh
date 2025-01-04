#!/bin/bash

# This script will manage your Docker Compose setup for MySQL and Airflow

# Define the docker-compose file location (if needed)
COMPOSE_FILE=docker-compose.yml

# Function to start the services
start_services() {
    echo "Starting MySQL and Airflow containers..."
    docker-compose -f $COMPOSE_FILE up -d
    if [ $? -eq 0 ]; then
        echo "Services started successfully!"
    else
        echo "Failed to start services."
        exit 1
    fi
}

# Function to stop the services
stop_services() {
    echo "Stopping MySQL and Airflow containers..."
    docker-compose -f $COMPOSE_FILE down
    if [ $? -eq 0 ]; then
        echo "Services stopped successfully!"
    else
        echo "Failed to stop services."
        exit 1
    fi
}

# Function to view logs of both services
view_logs() {
    echo "Viewing logs for MySQL and Airflow..."
    docker-compose -f $COMPOSE_FILE logs -f
}

# Function to restart the services
restart_services() {
    echo "Restarting MySQL and Airflow containers..."
    stop_services
    start_services
}

# Function to check the status of services
check_status() {
    echo "Checking the status of MySQL and Airflow containers..."
    docker-compose -f $COMPOSE_FILE ps
}

# Main menu
while true; do
    clear
    echo "Choose an option:"
    echo "1. Start Services (MySQL + Airflow)"
    echo "2. Stop Services"
    echo "3. View Logs"
    echo "4. Restart Services"
    echo "5. Check Status"
    echo "6. Quit"
    read -p "Enter the number corresponding to your choice: " choice

    case $choice in
        1)
            start_services
            ;;
        2)
            stop_services
            ;;
        3)
            view_logs
            ;;
        4)
            restart_services
            ;;
        5)
            check_status
            ;;
        6)
            exit 0
            ;;
        *)
            echo "Invalid option. Please try again."
            sleep 2
            ;;
    esac
done
