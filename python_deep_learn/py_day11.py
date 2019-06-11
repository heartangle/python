# 文件和异常
"""
在实际开发中，常常需要对程序中的数据进行持久化操作，而实现数据持久化最简单的方式就是将
数据保存到文件中。说到"文件"这个词，需要先了解一下文件系统，这个自行了解

在python中实现文件的读写操作非常简单，通过python内置的open函数，我们可以指定文件名，
操作模式，编码信息等来获得操作文件的对象，接下来就可以对文件进行读写操作了。这里的操作
模式指要打开的文件(字符文件还是二进制文件)以及做什么样的操作(读，写还是追加)。

操作模式	具体含义
'r'	读取 （默认）
'w'	写入（会先截断之前的内容）
'x'	写入，如果文件已经存在会产生异常
'a'	追加，将内容写入到已有文件的末尾
'b'	二进制模式
't'	文本模式（默认）
'+'	更新（既可以读又可以写）
"""

# 读文本文件
"""
读取文本文件时，需要在使用open函数时指定好带路劲的文件名(可以使用相对路径或绝对路径)
并将文件模式设置为"r"(如果不指定，默认值是"r"),然后通过 encoding 参数指定编码(如果
不指定，默认是None，那么在读取文件时使用的是操作系统默认的编码)，如果不能保证文件使用的
编码方式与encoding参数指定的编码方式一致，那么就可能无法解码字符而导致读取失败。
下面的例子演示如何读取一个纯文本文件
"""
'''
def main():
	f = open('致橡树.txt', 'r', encoding='utf-8')
	print(f.read())
	f.close()
main()
'''

""""
请注意上面的代码，如果open函数指定的文件并不存在或者无法打开，那么将引发异常状况导致
程序崩溃。为了让代码有一定的健壮性和容错性，我们可以使用Python的异常机制
对可能在运行时发生状况的代码进行适当的处理，如下所示。
"""
'''
def main():
	f = None
	try:
		f= open('致橡树.txt', 'r', encoding='utf-8')
		print(f.read())
	except FileNotFoundError:
		print('无法打开指定文件')
	except LookupError:
		print('指定了位置的编码')
	except UnicodeDecodeError:
		print('读取文件时解码错误')
	finally:
		if f:
			f.close()
main()
'''
"""
在Python中，我们可以将那些在运行时可能会出现状况的代码放在try代码块中，在try代码块的后面可以跟上
个或多个except来捕获可能出现的异常状况。例如在上面读取文件的过程中，文件找不到会引发
FileNotFoundError，指定了未知的编码会引发LookupError，而如果读取文件时无法按指定方式解码会引发
UnicodeDecodeError，我们在try后面跟上了三个except分别处理这三种不同的异常状况。
最后我们使用finally代码块来关闭打开的文件，释放掉程序中获取的外部资源，由于finally块的代码不论程序正常还是异
常都会执行到（甚至是调用了sys模块的exit函数退出Python环境，finally块都会被执行，因为exit函数
实质上是引发了SystemExit异常），因此我们通常把finally块称为“总是执行代码块”，它最适合用来做释放外
部资源的操作。如果不愿意在finally代码块中关闭文件对象释放资源，也可以使用上下文语法，通过with关键
字指定文件对象的上下文环境并在离开上下文环境时自动释放文件资源，代码如下所示
"""
'''
def main():
	try:
		with open('致橡树.txt','r', encoding='utf-8') as f:
			print(f.read())
	except FileNotFoundError:
			print('无法打开指定文件')
	except LookupError:
			print('指定了未知的编码')
	except UnicodeDecodeError:
			print('读取文件时解码错误')
main()
'''
"""
除了使用文件对象的read方法读取文件之外，还可以使用for-in循环逐行读取或者使用readlines方法
将文件按行读取到一个列表容器中。
"""
'''
import time
def main():
	# 一次性读取整个文件内容
	with open('致橡树.txt','r',encoding='utf-8') as f:
		print(f.read())
	# 通过for-in循环逐行读取
	with open('致橡树.txt',mode='r',encoding='utf-8') as f:
		for line in f:
			print(line,end='')
			time.sleep(0.5)
	print()
	# 读取文件按行读取到列表中
	with open('致橡树.txt',encoding='utf-8') as f:
		lines = f.readlines()
	print(lines)

main()
'''

"""
要将文本信息写入文件也非常简单，在使用open函数时指定好文件名字并将文件模式设置为'w',
注意需要对文件内容进行追加写入，应该讲模式设置为'a'。如果要写入的文件不存在会自动创建
文件而不是引发一场。
下面的例子演示了如何将1-9999之间的素数分别写入三个文件中（1-99之间的素数保存在a.txt中，
100-999之间的素数保存在b.txt中，1000-9999之间的素数保存在c.txt中）。
"""
'''
from math import sqrt
def is_prime(n):
	"""判断素数的函数"""
	assert n > 0
	for factor in range(2,int(sqrt(n))+1):
		if n % factor == 0:
			return False
	return True if n != 1 else False
def main():
	filenames = ('a.txt','b.txt','c.txt')
	fs_list = []
	try:
		for filename in filenames:
			fs_list.append(open(filename,'w',encoding='utf-8'))
		for number in range(1,10000):
			if is_prime(number):
				if number < 100:
					fs_list[0].write(str(number)+'\n')
				elif number < 1000:
					fs_list[1].write(str(number)+'\n')
				else:
					fs_list[2].write(str(number)+'\n')
	except IOError as ex:
		print(ex)
		print('写文件时发生错误')
	finally:
		for fs in fs_list:
			fs.close()
	print('操作完成')
main()
'''

# 读写二进制文件
"""知道了如何读写文本文件要读写二进制文件也就很简单了，下面的代码实现了复制图片文件的功能"""
'''
def main():
	try:
		with open('timg.jpg','rb') as fs1:
			data = fs1.read()  # <class 'bytes'>
			print(type(data))
		with open('皮卡丘jpg','wb') as fs2:
			fs2.write(data)
	except FileNotFoundError as e:
		print('指定的文件无法打开')
	except IOError as e:
		print('读写文件时出现错误')
	print('程序结束')
main()
'''

# 读取json文件
"""
如果希望吧一个列表或者一个字典中的数据保存到文件中该怎么做呢？答案是将数据以json格式保存，
JSON是“JavaScript Object Notation”的缩写，它本来是JavaScript语言中创建对象的一种字面量语法，
现在已经被广泛的应用于跨平台跨语言的数据交换，原因很简单，因为JSON也是纯文本，任何系统任何编程语
言处理纯文本都是没有问题的。目前JSON基本上已经取代了XML作为异构系统间交换数据的事实标准。
关于JSON的知识，更多的可以参考JSON的官方网站，从这个网站也可以了解到每种语言处理JSON数据格式
可以使用的工具或三方库，下面是一个JSON的简单例子。
"""
'''
{
	"name":"爱心天使",
	"age":23,
	"qq":123456,
	"friends":["蔡文姬","曹操"],
	"cars":[
		{"brand":"BYD","max_speed":1800},
		{"brand":"Audi","max_speed":280},
		{"brand":"Benz","max_speed":320}
	]
}
可能大家已经注意到了，上面的JSON跟Python中的字典其实是一样一样的，
事实上JSON的数据类型和Python的数据类型是很容易找到对应关系的，如下面两张表所示。
'''
"""
JSON			Python
---------------------------------------------------------
object			dict
array	        list
string			str
number 			(int / real)	int / float
true / false	True / False
null			None
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Python										JSON
----------------------------------------------------------
dict										object
list, tuple									array
str											string
int, float, int- & float-derived Enums		number
True / False								true / false
None										null
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""

"""我们可以使用Python中的json模块就可以将字典或列表以json格式保存到文件中"""
'''
import json

def main():
	mydict = {
		"name":"爱心天使",
		"age":23,
		"qq":123456,
		"friends":["蔡文姬","曹操"],
		"cars":[
			{"brand":"BYD","max_speed":1800},
			{"brand":"Audi","max_speed":280},
			{"brand":"Benz","max_speed":320}
		]
	}
	try:
		with open('data.json','w',encoding='utf-8') as fs:
			json.dump(mydict,f)
	except IOError as e:
		print(e)
	print("数据保存完成")
main()
'''
"""
json 模块有四个比较重要的函数，分别是：
	dump-将python对象按照json格式序列化到文件中
	dumps-将python对象处理成json格式的字符串
	load-将文件中的json数据反序列化成对象
	loads-将字符串的内容反序列化成python对象
"""
"""
这里出现了两个概念，一个叫序列化，一个叫反序列化。自由的百科全书维基百科上对这两个概念是这样解
释的：“序列化（serialization）在计算机科学的数据处理中，是指将数据结构或对象状态转换为可以存储或
传输的形式，这样在需要的时候能够恢复到原先的状态，而且通过序列化的数据重新获取字节时，可以利用
这些字节来产生原始对象的副本（拷贝）。与这个过程相反的动作，即从一系列字节中提取数据结构的操
作，就是反序列化（deserialization）”。

目前绝大多数网络数据服务（或称之为网络API）都是基于HTTP协议提供JSON格式的数据，关于HTTP协议
的相关知识，可以看看阮一峰老师的《HTTP协议入门》，如果想了解国内的网络数据服务，可以看看聚合
数据和阿凡达数据等网站，国外的可以看看{API}Search网站。下面的例子演示了如何使用requests模块（封
三方网络访问模块）访问网络API获取国内新闻，如何通过json模块解析JSON数据并显示新闻标题，这个例子使
用了天行数据提供的国内新闻数据接口，其中的APIKey需要自己到该网站申请
"""
'''
import requests
import json
def main():
	resp = requests.get('http://api.tianapi.com/guonei/?key=4832634ad9dcd75eb187cb66f8bb9738&num=11')
	data_model = json.loads(resp.text)
	for news in data_model['newslist']:
		print(news['title'])
main()
'''
'''
另外，如果要了解更多的关于Python异常机制的知识，可以看看segmentfault上面的文章《总结：Python中的异常处理》
，这篇文章不仅介绍了Python中异常机制的使用，还总结了一系列的最佳实践，很值得一读。
链接：https://segmentfault.com/a/1190000007736783
'''
