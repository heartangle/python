import socket
import subprocess
import struct
import json

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
			cmd = conn.recv(8096) # 1 单位: bytes 2 1024代表最大接收1024个字节
			if not cmd: # 适用于Linux系统
				break
			
			# 2 执行命令， 拿到结果
			obj = subprocess.Popen(cmd.decode('utf-8'), shell=True,
									stdout=subprocess.PIPE, 
									stderr=subprocess.PIPE)
			stdout = obj.stdout.read()
			stderr = obj.stderr.read()
			
			# 3 把命令的结果返回给客户端
			
			# 第一步： 制作固定长度的报头
			header_dict = {
				'filename' : 'a.txt',
				'md5' : 'xxxfxx',
				'total_size' : len(stdout) + len(stderr)
			}
			header_json = json.dumps(header_dict)
			header_bytes = header_json.encode('utf-8')
			
			# 第二步： 先发送报头的长度
			conn.send(struct.pack('i', len(header_bytes)))
			
			# 第三步：再发送报头	
			conn.send(header_bytes) 
			
			# 第四步：在发真实的数据
			conn.send(stdout)
			conn.send(stderr)
		except	ConnectionResetError:  #使用于windows系统
			break
	conn.close()

phone.close()
