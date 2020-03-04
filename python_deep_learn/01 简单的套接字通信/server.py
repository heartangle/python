import socket

# 1 买手机
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2 插手机卡
phone.bind(('127.0.0.1', 9094)) # bind传入的是一个元祖

# 3 开机
phone.listen(5) # 代表最大挂起的链接数

# 4 等电话
print("start....")
conn, client_addr = phone.accept()
print(client_addr)

# 5 收发消息
while True: # 通信循环
	data = conn.recv(1024) # 1 单位: bytes 2 1024代表最大接收1024个字节
	print('客户端数据', data)

	conn.send(data.upper())

conn.close()

phone.close()
