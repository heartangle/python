import socket
import time

# 1 买手机
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# 2 插手机卡
server.bind(('127.0.0.1', 9094)) # bind传入的是一个元祖

# 3 开机
server.listen(5) # 代表最大挂起的链接数

conn, addr = server.accept()

res1 = conn.recv(1)
print('第一次', res1)

time.sleep(6)
res2 = conn.recv(1024)
print('第二次', res2)
