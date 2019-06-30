FROM ubuntu:18.04

RUN apt update
RUN apt install -y python3 python3-dev python3-pip
RUN pip3 install flask

COPY . /flask_lesson_3/
WORKDIR /flask_lesson_3/

#RUN pip3 install -r requirements.txt

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

EXPOSE 5000
EXPOSE 5432
#CMD flask run --host=0.0.0.0

