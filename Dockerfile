FROM python:3.8.10

COPY requirements.txt  ./
COPY app/main.py ./app/
COPY app/models ./app/models/
COPY app/components ./app/components/

RUN apt update &&\
    pip install --upgrade pip &&\
    pip install -r requirements.txt

#CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
#CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app.main:app
CMD exec gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.main:app