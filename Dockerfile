FROM python:3.8.1-slim

ENV PYTHONUNBUFFERED 1

EXPOSE 8000
WORKDIR /serv


RUN  sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN  apt-get clean

RUN apt-get update && \
    apt-get install -y --no-install-recommends netcat python3-dev python3-pip && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY poetry.lock pyproject.toml ./
RUN pip3 install poetry==1.1 && \
    poetry config virtualenvs.in-project true && \
    poetry install --no-dev

COPY . ./

ADD .env.example .env

CMD poetry run alembic upgrade head && \
    poetry run uvicorn --host=0.0.0.0 serv.main:app