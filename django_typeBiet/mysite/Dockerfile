FROM python:3.7
#MAINTAINER ss wreck out

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /iyap
WORKDIR /iyap
COPY ./iyap /iyap

RUN adduser -D user
USER user