FROM python:3.8.10

COPY requirements.txt  ./
COPY app/main.py ./app/
COPY app/models ./app/models/
COPY app/components ./app/components/

RUN apt update &&\
    pip install --upgrade pip &&\
    pip install -r requirements.txt

CMD exec gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.main:app