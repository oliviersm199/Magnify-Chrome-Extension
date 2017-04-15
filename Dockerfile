FROM tiangolo/uwsgi-nginx-flask:flask
COPY ./app /app

RUN pip install -r requirements.txt
