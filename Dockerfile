FROM ubuntu:latest

RUN apt-get update
RUN apt-get install wget -y
RUN apt-get install python -y
RUN wget https://github.com/taebk2838/python-django-todoapp/raw/master/test.py
RUN python test.py
