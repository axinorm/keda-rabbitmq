#!/usr/bin/env python
import pika
import os

rabbitmq_username = os.getenv('RMQ_USERNAME')
rabbitmq_password = os.getenv('RMQ_PASSWORD')
rabbitmq_queue = os.getenv('RMQ_QUEUE')

# Step #1: Connect to RabbitMQ using the default parameters
credentials = pika.PlainCredentials(rabbitmq_username, rabbitmq_password)
connection = pika.BlockingConnection(
  pika.ConnectionParameters(
    "rabbitmq.default.svc.cluster.local",
    5672,
    '/',
    credentials
  )
)

# Connect to RabbitMQ using the default parameters
channel = connection.channel()
channel.queue_declare(queue=rabbitmq_queue)

for i in range(100):

  # Publish message
  channel.basic_publish(
    exchange='',
    routing_key=rabbitmq_queue,
    body='Hello World!'
  )

  print("[x] Sent 'Hello World!' : ", i)

# Gracefully close the connection
connection.close()