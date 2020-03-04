import socket

# 1 买手机
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2 拨号
phone.connect(('127.0.0.1', 9094))

# 3 发、收消息
while True:
	msg = input('>> ').strip()
	phone.send(msg.encode('utf-8'))

	data = phone.recv(1024)
	print(data)

# 4 关闭
phone.close()
