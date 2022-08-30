FROM python:3.8

ENV PYTHONUNBUFFERED 1
WORKDIR /kombat
COPY . .
COPY ./requirements.txt /kombat/requirements.txt
RUN python -m pip install --upgrade pip
RUN pip install -r /requirements.txt