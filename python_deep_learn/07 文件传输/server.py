import socket
import subprocess
import struct
import json
import os

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
			res = conn.recv(8096) # b 'get a.txt'
			if not res: # 适用于Linux系统
				break
			
			# 2 解析命令， 提取响应的参数
			cmds = res.decode('utf-8').split() # ['get', 'a.txt']
			filename = cmds[1]
			
			# 3 以读的方式打开文件， 读取文件内容， 发送给客户端
				
			# 第一步： 制作固定长度的报头
			header_dict = {
				'filename' : r'C:\Users\爱心天使\Desktop\1606990532.jpg',
				'md5' : 'xxxfxx',
				'filesize' : os.path.getsize(filename)
			}
			header_json = json.dumps(header_dict)
			header_bytes = header_json.encode('utf-8')
			
			# 第二步： 先发送报头的长度
			conn.send(struct.pack('i', len(header_bytes)))
			
			# 第三步：再发送报头	
			conn.send(header_bytes) 
			
			# 第四步：在发真实的数据
			with open(filename, 'rb') as f:
				# conn.send(f.read())
				for line in f:
					conn.send(line)
					
		except	ConnectionResetError:  #使用于windows系统
			break
	conn.close()

phone.close()
