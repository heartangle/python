# python中的字符串、列表、元祖、集合、字典

'''
def main():
	# 字符串操作
	str1 = "hello, world!"
	# 通过len函数计算字符串的长度
	print(len(str1))
	# 获取字符串首字母大写的拷贝
	print(str1.capitalize())
	# 获取字符串变大写后的拷贝
	print(str1.upper())
	# 在字符串中查找字串所在的位置
	print(str1.find('or'))
	print(str1.find('shit'))
	# 与find类似但找不到字串时会引发异常
	#print(str1.index('or'))
	#print(str1.index('shit'))
	# 检查字符串是否以指定的字符串开头
	print(str1.startswith('He'))
	print(str1.startswith('hel'))
	# 检查字符串是否以指定字符串结尾
	print(str1.endswith('!'))
	# 将字符串以指定的宽度居中并在两侧填充指定的字符
	print(str1.center(50,' '))
	# 指定字符串以指定的宽度靠右放置左侧填充指定字符
	print(str1.rjust(50,' '))
'''
	
'''
	str2 = 'abc123456'
	# 从字符串中取出指定位置的字符(下标运算)
	print(str2[2])      # c
	# 字符串切片(从指定的开始索引到指定的结束索引)
	print(str2[2:5]) # c12
	print(str2[2:])  # c123456
	print(str2[2::2])  # c246
	print(str2[::2])   # ac246
	print(str2[::-1]) # 654321cba
	print(str2[::-2]) # 642ca
	print(str2[-3:-1]) # 45
	# 检查字符串是否由数字构成
	print(str2.isdigit()) # False
	# 检查字符串是否以字母构成 
	print(str2.isalpha()) # False
	# 检查字符串是否以数字和字母构成
	print(str2.isalnum()) # True
'''

'''
	str3 = '   jackfrued@126.com'
	print(str3)
	# 获得字符串修建左右两侧空格的拷贝
	print(str3.strip())
'''

'''
	# 列表及其操作
def main():
	list1 = [1, 3, 5 ,7, 100]
	print(list1)
	list2 = ['hello'] * 5
	print(list2)
	# 计算列表长度
	print(len(list1))
	# 下标索引运算
	print(list1[0])
	print(list1[4])
	# print(list1[5]) # IndexError: list index out of range
	print(list1[-1])
	print(list1[-3])
	list1[2] = 300
	print(list1)
	# 添加元素
	list1.append(200)
	print(list1)
	list1.insert(1,400) # 在1的位置插入400，把所有数据向后挪动
	print(list1)
	list1 += [1000, 2000]
	# list1 = [] # python是一个边解释边运行的语言，后面定义的list1会把之前的覆盖，不会像C/C++的语言报错
	print(list1)
	# 删除元素
	list1.remove(3) # 删除是如果元素在列表中不存在，会报异常
	print(list1)
	if 1234 in list1:
		list1.remove(1234)
	print(list1)
	del list1[0]
	print(list1)
	# 清空列表元素
	list1.clear()
	print(list1)
'''

'''
和字符串一样，列表也可以做切片操作，通过切片操作，我们可以实现对列表的复制
或者将列表中的一部分取出来创建出新的列表
'''
'''
def main():
	fruits = ['grape', 'apple', 'strawberry', 'waxberry']
	# print(fruits)
	fruits += ['pitaya', 'pear', 'mango']
	# print(fruits)
	# 循环遍历列表元素
	for fruit in fruits:
		print(fruit.title(), end=' ')
	print()
	# 列表切片
	fruits2 = fruits[1:4]
	print(fruits2)
	fruit3 = fruits # 没有复制列表，只是创建了新的引用
	# 可以通过完整的切片操作来复制列表
	fruits3 = fruits[:]
	print(fruits3)
	fruits4 = fruits[-3:-1]
	print(fruits4)
	# 可以通过反向切片操作来获得翻转后的列表的拷贝
	fruits5 = fruits[::-1]
	print(fruits5)
'''

'''
# 下面的代码实现了对列表的排序操作
def main():
	list1 = ['orange', 'apple', 'zoo', 'pear', 'blueberry']
	list2 = sorted(list1)
	print(list1)
	print(list2)
	# sorted函数返回列表排序后的拷贝不会修改传入的列表
	# 函数的设计就应该像sorted一样尽可能不产生副作用
	list3 = sorted(list1, reverse=True)
	print(list3)
	# 通过key关键字参数指定根据字符串长度进行排序，而不是默认的字母表顺序
	list4 = sorted(list1, key=len)
	print(list4)
	# 给列表对象发出排序消息直接在列表对象上进行排序
	list1.sort(reverse=True)
	print(list1)
'''

# 使用列表的生成语法来创建列表
'''
import sys

def main():
	f = [x for x in range(1,10)]
	print(f)
	f = [x + y for x in 'ABCDE' for y in '123456']
	print(f)
	# 使用列表的生成表达式语法创建列表容器
	# 用这种语法创建列表之后元素已经准备就绪所以需要耗费较多的内存空间
	f = [x ** 2 for x in range(1,1000)]
	print(sys.getsizeof(f)) # 查看对象占用内存的字节数
	print(f)
	# 请注意下面的代码创建的不是一个列表而是一个生成器对象
	# 通过生成器对象可以获取到数据，但它不占用额外的空间存储数据
	# 每次需要数据的时候就通过内部的运算得到数据(需要花额外的时间)
	f = (x ** 2 for x in range(1,1000))
	print(sys.getsizeof(f)) # 相比生成器不占用存储数据的空间
	print(f)
	for val in f:
		print(val,end=' ')
'''

'''
除了上面的生成器语法，python中还有另外一种定义生成器的方式，就是通过yield关键字
将一个普通函数改造成生成器函数。下面的代码演示了如何生成一个斐波那锲数列的生成器。
'''
'''
def fib(n):
	a,b = 0,1
	for _ in range(n):
		a,b = b,a+b
		yield a

def main():
	for val in fib(20):
		print(val)
'''
'''
def main1():
	list1 = ['123',3, True]
	print(list1)
'''

# 元祖
'''
python的元祖与列表类似，不同之处在于元祖的元素不能修改
顾名思义，我们把多个元素组合到一起就形成了一个元祖，所以它和列表一样可以保存多条数据。
'''
'''
def main():
	# 定义元祖
	t = ('王朝阳','23',True,'陕西西安')
	print(t)
	# 获取元祖中的元素
	print(t[0])
	print(t[3])
	# 遍历元祖中的值
	for member in t:
		print(member)
	# 重新给元祖赋值
	# t[0] = '王大锤' # TypeError: 'tuple' object does not support item assignment
	# 变量t重新引用了新的元祖，原来的元祖将被垃圾回收
	t = ('王大锤',20,True, '广州深圳')
	print(t)
	# 将元祖转换成列表
	person = list(t)
	print(person)
	# 列表是可以修改它的元素的
	person[0] = '李小龙'
	person[1] = 25
	print(person)
	# 将列表转化为元祖
	fruits_list = ['apple', 'banana', 'orange']
	fruits_tuple = tuple(fruits_list)
	print(fruits_tuple)
'''

'''
这里有一个非常值得探讨的问题，我们已经有了列表这种数据结构，为什么还需要元祖这种类型呢
1、元祖中的元素是无法修改的，事实上我们在项目中，尤其是多线程环境中可能更喜欢使用的是那些
不变对象(一方面的因为对象状态不能更改，所以可以避免由此引起的不必要的程序错误，简单的
说就是一个不可变的对象要比一个可变的对象更加容易维护；另一方面是因为没有一个线程能够修改
不变对象的内部状态，一个不变对象自动就是线程安全的，这样就可以省掉处理同步化的开销。一个
不变对象可以方便的被共享访问)。所以结论就是：如果不需要对元素进行添加，删除，修改的时候，
可以考虑使用元祖，当然如果一个方法要返回多个值，使用元祖也是不错的选择.
2、元祖在创建时间和占用的空间上面都优于列表。我们可以使用sys模块的getsizeof函数来检查
存储同样的元素的元祖和列表各自占用了多少的内存空间。我们也可以在ipython中使用魔法指令
%timeit来分析创建同样内容的元祖和列表所花费的时间。
'''
'''
def main() :
	import sys
	tuple1 = (1,2,3,4,5,6) # 52
	print(sys.getsizeof(tuple1))	
	list1 = [1,2,3,4,5,6] # 60
	print(sys.getsizeof(list1))
'''

# 集合
# python中的集合跟数学上的集合上一致的，不允许有重复元素，而且可以进行交集、并集、差集的运算
'''
def main():
	# 集合可以类比c++中的set理解，会对插入的数据进行排序+去重
	set1 = {1,2,3,3,3,2}
	print(set1)
	print('lengrh =',len(set1))
	set2 = set(range(1,10))
	print(set2)
	set1.add(4)
	set1.add(5)
	set2.update([11,12])
	print(set1)
	print(set2)
	set2.discard(100) # 删除，没有不会抛异常
	print(set2)
	# remove的元素如果不存在会引发keyError
	if 4 in set2:
		set2.remove(4)
	print(set2)
	# 遍历集合容器
	for elem in set2:
		print(elem ** 2,end=' ')
	print()
	# 将元祖转换成集合
	set3 = set((1,2,3,3,2,1))
	print(set3.pop())
	print(set3)
	'''
	
	'''
	set1 = {1,2,3,3}
	set2 = {1,2,3,4,5}
	# 集合的交集、并集、差集、对称差运算
	print(set1 & set2)
	print(set1 | set2)
	print(set1 - set2)
	print(set1 ^ set2)
	# 判断子集和超集
	print(set1 <= set2)
	print(set1 >= set2)
	print(set3)
	'''
	
# 字典
'''
def main():
	sorces = {'小A':95, '小B':78, '小C':82}
	print(sorces)
	# 通过键可以获取字典中对应的值
	print(sorces['小A'])
	# 对字典进行遍历(遍历的其实是键在通过键取对应的值)
	for elem in sorces:
		print('%s ---> %d' % (elem,sorces[elem]))
	# 更新字典中的元素
	sorces['小B'] = 65
	print(sorces)
	sorces['小D'] = 71
	print(sorces)
	sorces.update(小E=67,小F=85)
	print(sorces)
	if '小G' in sorces:
		print(sorces['小G'])
	print(sorces.get('小G'))
	# get方法也是通过键获取对应的的值，但是可以设置默认值
	print(sorces.get('小G',False))
	# 删除字典中的元素
	print(sorces.popitem())
	print(sorces.popitem())
	print(sorces)
	print(sorces.pop('小A',1000))
	# 清空字典
	sorces.clear()
	print(sorces)
'''

########################################################################

# 练习1：在屏幕上显示跑马灯文字
'''
def main():
	import os
	import time
	
	content = '北京欢迎你，为你开天辟地......'
	while True:
		# 清理出屏幕上输出
		os.system('cls') # os.system('clear')
		print(content)
		# 休眠200毫秒
		time.sleep(0.2)
		content = content[1:] + content[0]
'''

# 练习2：设计一个函数产生制定长度的验证码，验证码由大小写字母和数字构成
'''
def generate_code(code_len=4):
	"""
	生成制定长度的验证码
	:param code_len:验证码的长度(默认四个字符)
	:return:由大小写因为字母和数字构成的随机验证码
	"""
	import random
	
	all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
	last_pos = len(all_chars) - 1
	code = ''
	for _ in range(code_len):
		index = random.randint(0,last_pos)
		code += all_chars[index]
	return code
print(generate_code(10))
'''

# 练习3：设计一个函数返回给定文件名的后缀名
'''
def get_suffix(filename, has_dot=False):
	"""
	获取文件名的后缀
	:param filename: 文件名
	:param has_dot: 返回的后缀名是否需要带点
	:return: 文件的后缀名
	"""
	pos = filename.rfind('.')
	if 0 < pos < len(filename) -1:
		index = pos if has_dot else pos + 1;
		return filename[index:]
	else:
		return ''
		
print(get_suffix('简历.pdf',True))
'''

# 练习4：设计一个函数返回传入的列表中最大和第二大的元素
'''
def max2(x):
	m1,m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])
	for index in range(2, len(x)):
		if x[index] > m1:
			m2 = m1
			m1 = x[index]
		elif x[index] > m2:
			m2 = x[index]
	return m1, m2
print(max2([1,2,3,4,5,6,7,8]))
'''

# 练习5：计算指定的年月日是这一年的第几天
'''
def is_leap_year(year):
	"""
	判断指定年是不是闰年
	：param year: 年份
	:return: 闰年返回True 平年返回False
	"""
	return year%4==0 and year%100!=0 or year%400==0
	
def which_day(year,month,date):
	"""
	计算传入的日期是这一年的第几天
	:param year: 年
	:param month: 月
	:param date: 日
	:return: 第几天
	"""
	days_of_month = [
		[31,28,31,30,31,30,31,31,30,31,30,31],
		[31,29,31,30,31,30,31,31,30,31,30,31]
		][is_leap_year(year)]
	total = 0
	for index in range(month-1):
		total += days_of_month[index]
	return total + date
def main():
	print(which_day(1980,11,29))
	print(which_day(1981,12,31))
	print(which_day(2018,1,1))
	print(which_day(2018,3,1))
main()
'''

# 练习6：打印杨辉三角
'''
def main():
	num = int(input('Number of rows:'))
	yh = [[]] * num
	for row in range(len(yh)):
		yh[row] = [None] * (row + 1)
		for col in range(len(yh[row])):
			if col == 0 or col == row:
				yh[row][col] = 1
			else:
				yh[row][col] = yh[row-1][col] + yh[row-1][col-1]
			print(yh[row][col],end='\t')
		print()
main()
'''

# 综合案例

# 案例1：双色球选号
'''
from  random import randrange,randint,sample
# 使用random模块中的sample函数来实现从列表中选择不重复的N个元素
# enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，
# 同时列出数据和数据下标，一般用在 for 循环当中。

def display(balls):
	"""
	输出列表中的双色球号码
	"""
	for index,ball in enumerate(balls):
		if index == len(balls) - 1:
			print('|',end=' ')
		print('%-2d' % ball, end=' ')
	print()

def random_select():
	"""
	随机选择一组号码
	"""
	red_balls = [x for x in range(1, 34)]
	selected_balls = []
	selected_balls = sample(red_balls, 6)
	selected_balls.sort()
	selected_balls.append(randint(1, 16))
	return selected_balls

def main():
	n = int(input('机选几注： '))
	for _ in range(n):
		display(random_select())

main()
'''

# 案例二：约瑟夫环问题
"""
《幸运的基督徒》
有15个基督徒和15个非基督徒在海上遇险，为了能让一部分人或下来，不得不将其中15个人扔到
海里面去，有个人想了个办法就是大家围城一圈，由某个人从1报数，报到9的人就扔到海里面，
他后面的人接着从一开始报数，报到9的人继续扔到海里面，直到扔掉15个人。
由于上帝的保佑，15个基督徒都幸免于难，问这些人最开始是怎末站的，那些位置是基督徒，
那些位置是非基督徒。
"""
'''
def main():
	persons = [True] * 30
	counter, index, number = 0, 0, 0
	while counter < 15:
		if persons[index]:
			number += 1
			if number == 9:
				persons[index] = False
				counter += 1
				number = 0
		index += 1
		index %= 30
	tmp = 0
	for person in persons:
		tmp += 1
		print(('%d->基' if person else '%d->非')% tmp,end='  ')

main()
'''

# 案例三：井字棋游戏
'''
import os

def print_board(board):
	print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
	print('-+-+-')
	print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])
	print('-+-+-')
	print(board['BL'] + '|' + board['BM'] + '|' + board['BR'])

def main():
	init_board = {
		'TL':' ','TM':' ','TR':' ',
		'ML':' ','MM':' ','MR':' ',
		'BL':' ','BM':' ','BR':' '
	}
	begin = True
	while begin:
		curr_board = init_board.copy()
		begin = False
		turn = 'x'
		counter = 0
		os.system('clear')
		print_board(curr_board)
		while counter < 9:
			move = input('轮到%s走棋,请输入位置：' % turn)
			if curr_board[move] == ' ':
				counter += 1
				curr_board[move] = turn
				if turn == 'x':
					turn = 'o'
				else:
					turn = 'x'
			os.system('clear')
			print_board(curr_board)
		choice = input('在玩一局?(yes|no)')
		begin = choice == 'yes'

main()
'''
