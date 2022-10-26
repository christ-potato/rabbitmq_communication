import pika
import config

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=config.host, port=config.port, virtual_host=config.virtual_host,
                              credentials=config.credentials))
# 创建一个链接对象

channel = connection.channel()  # 创建一个频道
channel.queue_declare(queue="helloworld",durable=True)  # 声明队列，不存在则创建
channel.basic_publish(exchange='', routing_key='helloworld', body=b'Hello,world')
print("[x] Sent 'Hello Wolrd!'")
connection.close()
