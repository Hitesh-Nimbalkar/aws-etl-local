#!/bin/bash

# Define variables
CONTAINER_NAME="ml_postgres_container"
DB_USER="ml_user"
DB_NAME="ml_data"

# Check if the container is running
if ! docker ps --filter "name=$CONTAINER_NAME" | grep -q "$CONTAINER_NAME"; then
  echo "Error: Container '$CONTAINER_NAME' is not running."
  exit 1
fi

# Log into the PostgreSQL container
echo "Logging into PostgreSQL database '$DB_NAME' as user '$DB_USER'..."
docker exec -it $CONTAINER_NAME psql -U $DB_USER -d $DB_NAME
