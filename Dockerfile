FROM python:3.8.1-slim

ENV PYTHONUNBUFFERED 1

EXPOSE 80

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends netcat python3-dev python3-pip && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY ./serv /app/serv

COPY .env.example /app/.env

COPY requirements.txt /app/requirements.txt

RUN pip3 install -r requirements.txt && \
    pip3 instal -e .

CMD ["uvicorn", "serv.main:app", "--host", "0.0.0.0", "--port", "80"]
