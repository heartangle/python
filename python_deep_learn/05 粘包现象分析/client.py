import socket
import time

# 1 买手机
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2 拨号
client.connect(('127.0.0.1', 9094))

client.send('hello'.encode('utf-8'))
time.sleep(5)
client.send('world'.encode('utf-8'))

