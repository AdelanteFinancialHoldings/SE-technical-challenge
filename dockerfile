FROM postgres
#Set env variables
ENV PYTHONUNBUFFERED=1 
ENV FLASK_APP=challenge_app
ENV FLASK_ENV=development
# Install python/pip
RUN apt-get update -y
RUN apt-get install -y python
RUN apt-get -y install python3-pip
# Setting the app inside the container
COPY ./app/requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip3 install -r requirements.txt
COPY . /app
EXPOSE 5000
# Copying deployment script
COPY run_flask.sh /app/run_flask.sh 
RUN chmod +x /app/run_flask.sh 
