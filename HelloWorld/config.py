import pika

host = "127.0.0.1"
port = 5672
virtual_host = "/ems"
credentials = pika.PlainCredentials('ems', '123')
