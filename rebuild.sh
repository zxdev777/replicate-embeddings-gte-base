#!/bin/bash

CONTAINER_NAME="sentence-transformer-gte-base"
IMAGE_NAME="sentence-transformer-gte-base"

# Check if the container exists
if docker ps -a --format '{{.Names}}' | grep -Eq "^$CONTAINER_NAME$"; then
    echo "Stopping and removing container: $CONTAINER_NAME"
    docker stop $CONTAINER_NAME
    docker rm $CONTAINER_NAME
fi

echo "Building the new Docker image: $IMAGE_NAME"
cog build -t $IMAGE_NAME

echo "Starting a new container from the new image: $IMAGE_NAME"
docker run -d --name $CONTAINER_NAME -p 5000:5000 $IMAGE_NAME

echo "Container rebuild completed."
