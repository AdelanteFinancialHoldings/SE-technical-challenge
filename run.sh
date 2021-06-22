#!/bin/sh
#Here we wrap the whole DB local deployment.
sudo docker kill $(sudo docker ps -q)
sudo docker system prune
sudo docker run --name addi-app -e POSTGRES_PASSWORD=1234 -p 5432:5432 -p 5000:5000 -d addi-assesment
