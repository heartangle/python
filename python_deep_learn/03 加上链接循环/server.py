import socket

# 1 买手机
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

phone.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# 2 插手机卡
phone.bind(('127.0.0.1', 9094)) # bind传入的是一个元祖

# 3 开机
phone.listen(5) # 代表最大挂起的链接数

# 4 等电话
print("start....")

while True: # 链接循环
	conn, client_addr = phone.accept()
	print(client_addr)

	# 5 收发消息

	while True: # 通信循环
		# 客户端单方面断开链接，会导致服务端死循环
		try:
			data = conn.recv(1024) # 1 单位: bytes 2 1024代表最大接收1024个字节
			if not data: # 适用于Linux系统
				break
			print('客户端数据', data)

			conn.send(data.upper())
		except	ConnectionResetError:  #使用于windows系统
			break
	conn.close()

phone.close()
