import socket
import subprocess

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
			# 1 接收命令
			cmd = conn.recv(1024) # 1 单位: bytes 2 1024代表最大接收1024个字节
			if not cmd: # 适用于Linux系统
				break
			
			# 2 执行命令， 拿到结果
			obj = subprocess.Popen(cmd.decode('utf-8'), shell=True,
									stdout=subprocess.PIPE, 
									stderr=subprocess.PIPE)
			stdout = obj.stdout.read()
			stderr = obj.stderr.read()
			
			# 3 把命令的结果返回给客户端
			print(len(stdout+stderr)) 
			conn.send(stdout+stderr) # + 是一个可以优化的点
		except	ConnectionResetError:  #使用于windows系统
			break
	conn.close()

phone.close()
