from time import sleep
import pika
credentials = pika.PlainCredentials('admin', 'admin')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost',credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='hello')
for i in range(10):
    channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
    print(" [x] Sent 'Hello World!'")
    sleep(3)
connection.close()