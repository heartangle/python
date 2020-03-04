import socket
import struct

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
	# 第一步：先拿到报头
	header = phone.recv(4)
	total_size = struct.unpack('i', header)[0]
	# 第二步：从报头中解析出对真实数据的描述信息
	
	# 第三步：接收真实的数据
	recv_size = 0
	recv_data=b''
	while recv_size < total_size:
		res= phone.recv(1024)  # 1024是一个坑
		recv_data += res
		recv_size += len(res)
		
	print(recv_data.decode('gbk'))

# 4 关闭
phone.close()
