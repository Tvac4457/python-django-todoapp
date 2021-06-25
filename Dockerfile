FROM python:3.6.1-alpine

RUN https://github.com/taebk2838/python-django-todoapp/raw/master/test.py
RUN python test.py
