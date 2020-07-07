FROM python:3.8.3
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
COPY requirements.txt /code/requirements.txt
WORKDIR /code
RUN pip install -r requirements.txt
COPY . /code/
