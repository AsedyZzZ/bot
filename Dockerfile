FROM python:3.11

ENV PYTHONDONTWRITEBYCODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apt-get -y update
RUN apt-get -y upgrade

COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY . /app

CMD [ "python", "run.py" ]
