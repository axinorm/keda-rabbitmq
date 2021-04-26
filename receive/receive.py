#!/usr/bin/env python
import pika
import os
import time

rabbitmq_username = os.getenv('RMQ_USERNAME')
rabbitmq_password = os.getenv('RMQ_PASSWORD')
rabbitmq_queue = os.getenv('RMQ_QUEUE')

# Create a global channel variable to hold our channel object in
channel = None

# Step #2
def on_connected(connection):
  """Called when we are fully connected to RabbitMQ"""
  # Open a channel
  connection.channel(on_open_callback=on_channel_open)

# Step #3
def on_channel_open(new_channel):
  """Called when our channel has opened"""
  global channel
  channel = new_channel
  channel.queue_declare(queue=rabbitmq_queue, durable=False, exclusive=False, auto_delete=False, callback=on_queue)

# Step #4
def on_queue(frame):
  """Callback when we have successfully declared the queue"""
  channel.basic_qos(prefetch_count=1, callback=on_qos)

# Step #5
def on_qos(frame):
  """Callback when we have set the channel prefetch limit"""
  channel.basic_consume(rabbitmq_queue, handle_delivery)

# Step #6
def handle_delivery(channel, method, header, body):
  """Called when we receive a message from RabbitMQ"""
  print(body)
  channel.basic_ack(method.delivery_tag)
  time.sleep(1) # Add pause for simulate actions

# Step #1: Connect to RabbitMQ using the default parameters
credentials = pika.PlainCredentials(rabbitmq_username, rabbitmq_password)
parameters = pika.ConnectionParameters(
  "rabbitmq.default.svc.cluster.local",
  5672,
  '/',
  credentials
)
connection = pika.SelectConnection(parameters, on_open_callback=on_connected)

try:
  # Loop so we can communicate with RabbitMQ
  connection.ioloop.start()
except KeyboardInterrupt:
  # Gracefully close the connection
  connection.close()
  # Loop until we're fully closed, will stop on its own
  connection.ioloop.start()