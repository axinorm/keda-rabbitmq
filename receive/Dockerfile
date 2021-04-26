FROM python:3.10.0a7-alpine3.12

RUN pip install pika

ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

COPY receive.py .

CMD ["python", "/usr/src/app/receive.py"]
