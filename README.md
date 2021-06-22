# SE-technical-challenge
Mock application to be used in the hiring process for support engineers

This is a Flask application running along a postgresql database that is populated with random data.

## How to use it?
Follow these steps to build and run the docker container to deploy the app:

Run docker build from the folder containing the dockerfile  
```bash
sudo docker build -t addi-assesment .  
```
Run the bash file "run.sh"  
```bash
- bash run.sh  
```
Open the docker's bash:  
```bash
- sudo docker exec -it addi-app /bin/bash  
```
Alternatively use the more friendly bash file:  
```bash
- bash enter_docker_bash.sh  
```
Inside the docker's bash you're placed in a folder containing the necessary bash file with the commands to run the app:  
```bash
- bash run_flask.sh  
```
