import pika
import config

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=config.host, port=config.port, virtual_host=config.virtual_host,
                              credentials=config.credentials))
# 创建一个链接对象
channel = connection.channel()  # 创建一个频道
channel.queue_declare(queue="helloworld",durable=True)  # 声明队列，不存在则创建

def callback(ch,method,properties,body):
    print("[x] Received %r"%body)
channel.basic_consume('helloworld',callback,auto_ack=True)
print('[*] Waiting for message.To exit press CTRL+C')
channel.start_consuming()