#FROM tiangolo/uwsgi-nginx-flask
FROM python:3.7.3-stretch

ADD . /app 

#WORKDIR /app/flask_lesson_3/
WORKDIR /app/what_was_on_the_lesson/

EXPOSE 5000
RUN pip install -r requirements.txt
CMD flask run --host=127.0.0.1
#RUN flask run
#RUN flask run
#ENTRYPOINT ["python"]
#CMD ["app.py"]
