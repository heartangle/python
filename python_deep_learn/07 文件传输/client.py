import socket
import struct
import json

# 1 买手机
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2 拨号
phone.connect(('127.0.0.1', 9094))

# 3 发、收消息
while True:
	# 1 发命令
	cmd = input('>> ').strip() # get a.txt
	if not cmd:
		continue
	phone.send(cmd.encode('utf-8'))
	
	# 2 接收文件的内容，以写的方式打开一个新文件，接收服务端发来的文件内容，写入客户端的新文件
	
	# 第一步：先收报头的长度
	obj = phone.recv(4)
	header_size = struct.unpack('i', obj)[0]
	
	# 第二步： 在收报头
	header_bytes = phone.recv(header_size)
	
	# 第三步：从报头中解析出对真实数据的描述信息
	header_json = header_bytes.decode('utf-8')
	header_dict = json.loads(header_json)
	print(header_dict)
	total_size = header_dict['filesize']
	filename = header_dict['filename']
	
	# 第四步：接收真实的数据
	with open(filename, 'wb') as f:
		recv_size = 0
		while recv_size < total_size:
			line= phone.recv(1024)  # 1024是一个坑
			f.write(line)
			recv_size += len(line)

# 4 关闭
phone.close()
