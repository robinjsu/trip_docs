FROM ubuntu:18.04

LABEL "author"="robisu@pdx.edu"

COPY ./app_files /app

WORKDIR /app
 
RUN apt-get update --allow-releaseinfo-change -y && apt-get install curl -y && apt-get install gnupg2 -y && curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - && apt-get install -y python3-pip && pip3 install -r requirements.txt

CMD exec gunicorn --bind=:$PORT --workers 1 --threads 8 app:app