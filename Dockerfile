FROM python:3.8.5
ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get install gettext -y
RUN mkdir /code
COPY requirements.txt /code/requirements.txt
WORKDIR /code
RUN pip install -r requirements.txt
COPY . /code/
