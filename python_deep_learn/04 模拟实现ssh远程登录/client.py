import socket

# 1 买手机
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2 拨号
phone.connect(('127.0.0.1', 9094))

# 3 发、收消息
while True:
	# 1 发命令
	cmd = input('>> ').strip() # ls 
	if not cmd:
		continue
	phone.send(cmd.encode('utf-8'))
	
	# 2 拿到命令的结果， 并打印  
	data = phone.recv(1024)  # 1024是一个坑
	print(data.decode('gbk'))

# 4 关闭
phone.close()
