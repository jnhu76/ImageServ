FROM python:3.8.1-slim

ENV PYTHONUNBUFFERED 1

EXPOSE 8000
WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends python3-dev python3-pip && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY requirements.txt ./
RUN pip3 install --upgrade pip && \
    pip3 install -r requirements.txt

RUN mkdir -p /app/images

COPY . ./

CMD uvicorn --host=0.0.0.0 serv.main:app