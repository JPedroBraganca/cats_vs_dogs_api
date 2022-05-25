FROM python:3.8.10

COPY requirements.txt  ./
COPY app/main.py ./app/
COPY app/models ./app/models/
COPY app/components ./app/components/

RUN apt update &&\
#    apt install ffmpeg libsm6 libxext6  -y &&\
    pip install --upgrade pip &&\
    pip install -r requirements.txt

#CMD ["python", "main.py"]
#CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
CMD ["uvicorn", "app.main:app"]