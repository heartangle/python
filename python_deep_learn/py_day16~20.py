# Python语言进阶

# 1、数据结构与算法
"""
算法：解决问题的方法和步骤
评价算法的好坏：渐进时间复杂度和空间复杂度。
渐进时间复杂度的大O标记：
	
	- 常量时间复杂度 - 布隆过滤器 / 哈希存储
	- 对数时间复杂度 - 折半查找（二分查找）
	- 线性时间复杂度 - 顺序查找 / 桶排序
	- 对数线性时间复杂度 - 高级排序算法（归并排序、快速排序）
	- 平方时间复杂度 - 简单排序算法（选择排序、插入排序、冒泡排序）
	- 立方时间复杂度 - Floyd算法 / 矩阵乘法运算
	- 几何级数时间复杂度 - 汉诺塔
	- 阶乘时间复杂度 - 旅行经销商问题 - NP
"""

"""排序算法(选择，冒泡，归并)和查找算法(顺序和折半)"""

"""简单选择排序"""
'''
def select_sort(origin_items,comp=lambda x,y: x < y):
	""""每次都去剩余的部分找最小的往前放"""
	items = origin_items[:]
	for i in range(len(items)-1):
		min_index = i
		for j in range(i+1, len(items)):
			if comp(items[j],items[min_index]):
				min_index = j
		items[i],items[min_index] = items[min_index],items[i]
	return items
def main():
	a = [9,8,7,6,5,4,3,2,1]
	b = select_sort(a)
	print(a)
	print(b)
'''

"""高质量冒泡排序(搅拌排序)"""
'''
def bubble_sort(origin_items, comp=lambda x,y: x>y):
	items = origin_items[:]
	for i in range(len(items)-1):
		swapped = False
		for j in range(i, len(items)-1-i):
			if comp(items[j], items[j+1]):
				items[j],items[j+1] = items[j+1],items[j]
				swapped = True
		if swapped:
			swapped = False
			for j in range(len(items)-2-i, i,-1):
				if comp(items[j-1],items[j]):
					items[j],items[j-1] = items[j-1],items[j]
					swapped = True
		if not swapped:
			break
	return items

import datetime
from random import randint

def main():
	a = []
	for i in range(1,10000):
		a.append(randint(1,1000))
	start = datetime.datetime.now()
	b = select_sort(a)
	b = bubble_sort(a)
	end = datetime.datetime.now()
	print(end-start)
main()
'''

"""归并排序(分治法)"""
'''
def merge_sort(items,comp=lambda x,y : x >= y):
	if len(items) < 2:
		return items[:]
	mid = len(items) // 2
	left = merge_sort(items[:mid],comp)
	right = merge_sort(items[mid:],comp)
	return merge(left,right,comp)

def merge(items1,items2,comp):
	items = []
	index1,index2 = 0,0
	while index1 < len(items1) and index2 < len(items2):
		if comp(items1[index1],items2[index2]):
			items.append(items1[index1])
			index1 += 1
		else:
			items.append(items2[index2])
			index2 += 1
	items += items1[index1:]
	items += items2[index2:]
	return items

def main():
	l = [4,3,2,1]
	ll = merge_sort(l,lambda x,y : x <= y)
	print(ll)
main()
'''

"""顺序查找"""
'''
def seq_search(items,key):
	for index,item in enumerate(items):
		if item == key:
			return index
	return -1
'''

"""折半查找"""
'''
def bin_search(items,key):
	start,end = 0,len(items)-1
	while start <= end:
		mid = (start + end) // 2
		if key > items[mid]:
			start = mid + 1
		elif key < items[mid]:
			end = mid - 1
		else:
			return mid
	return -1
'''

"""使用生成式(推导式)语法"""
'''
prices = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
}
# 用股票价格大于100元的股票构造一个新的字典
prices2 = {key: value for key,value in prices.items() if value > 100}
print(prices2)
"""说明：生成式(推导式)可以用来生成列表，集合和字典"""
'''

"""嵌套的列表"""
'''
names= ['关羽','张飞','赵云','马超','黄忠']
courses = ['语文','数学','英语']
"""录入五个学生三门课的成绩"""
sorces = [[None] * len(courses) for _ in range(len(names))]
# print(sores)
for row,name in enumerate(names):
	for col,course in enumerate(courses):
		sorces[row][col] = float(input(f'请输入{name}的{course}成绩：'))
		print(sorces)
'''

"""heapq,itertools等的用法"""
"""
从列表中找出最大的或最小的N个元素
堆结构(大根堆，小根堆)
"""
'''
import heapq

list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
list2 = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
print(heapq.nlargest(3,list1))
print(heapq.nsmallest(3,list1))
print(heapq.nlargest(2,list2,key=lambda x: x['price']))
print(heapq.nsmallest(2,list2,key=lambda x: x['shares']))
'''

"""迭代工具-排列/组合/笛卡尔积"""
'''
import itertools
print(list(itertools.permutations('ABCD')))
print(list(itertools.combinations('ABCDE',3)))
print(list(itertools.product('ABCD','123')))
'''

"""collections模块下的工具类"""
'''
from collections import Counter

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
    'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
    'look', 'into', 'my', 'eyes', "you're", 'under'
]
counter = Counter(words)
print(counter.most_common(3))
# [('eyes', 8), ('the', 5), ('look', 4)]
'''

"""常用算法"""
"""
1、穷举法-又又称暴力破解法。对所有的可能性进行验证，直到找到正确答案
2、贪婪发-在对问题求解时，总是做出在当前看来最好的选择，不追求最优解，快速找到满意解
3、分治法-把一个复杂的问题分成两个或更多的相同或相似的子问题，在把子问题分成更小的子问题
		直到可以直接求解的程度，最后将子问题的解进行合并得到原问题的解
4、回溯法-回溯法又称试探法，按选优条件向前搜索，当搜索到某一步发现原先选择并不优或达不到
		目标时，就退一步重新选择
5、动态规划-基本思想是将带求解问题分成若干个子问题，先求解并保存这些子问题的解，避免产生
		大量的重复计算
"""

"""穷举法例子"""
'''
# 公鸡5元一只 母鸡3元一只 小鸡1元三只
# 用100元买100只鸡 问公鸡/母鸡/小鸡各多少只
for x in range(20):
	for y in range(33):
		z = 100-x-y
		if 5*x + 3*y + z//3 == 100 and z%3 == 0:
			print(x,y,z)
'''

'''
# A、B、C、D、E五人在某天夜里合伙捕鱼 最后疲惫不堪各自睡觉
# 第二天A第一个醒来 他将鱼分为5份 扔掉多余的1条 拿走自己的一份
# B第二个醒来 也将鱼分为5份 扔掉多余的1条 拿走自己的一份
# 然后C、D、E依次醒来也按同样的方式分鱼 问他们至少捕了多少条鱼

fish = 6

while True:
	total = fish
	enough = True
	for _ in range(5):
		if(total-1)%5 == 0:
			total = (total-1)//5*4
		else:
			enough = False
			break
	if enough:
		print(fish)
		break
	fish += 5
'''

"""贪婪法例子"""
"""
假设小偷有一个背包，最多能装20公斤赃物，他闯入一户人家，发现如下表所示的物品。很显然，
他不能把所有物品都装入背包，所以确定拿走那些物品，留下哪些

名称	  价格（美元）	重量（kg）
电脑	  200	        20
收音机 20	        4
钟	  175	        10
花瓶	  50	        2
书	  10	        1
油画	  90	        9
______________________________________________________________________
贪婪法在求解问题时，总是做出在当前看来最好的选择，不追求最优解，快速找到满意解，。
"""
"""
class Thing(object):
	# 物品
	def __init__(self,name,price,weight):
		self.name = name
		self.price = price
		self.weight = weight
	@property
	def value(self):
	# 价格重量比
		return self.price / self.weight

def input_thing():
	# 输入物品信息
	name_str,price_str,weight_str = input().split()
	return name_str,int(price_str),int(weight_str)

def main():
	# 主函数
	max_weight,num_of_things = map(int, input().split())
	all_things = []
	for _ in range(num_of_things):
		all_things.append(Thing(*input_thing()))
	all_things.sort(key=lambda x: x.value,reverse=True)
	total_weight = 0
	total_price = 0
	for thing in all_things:
		if total_weight + thing.weight <= max_weight:
			print(f'小偷拿走了{thing.name}')
			total_weight += thing.weight
			total_price += thing.price
	print(f'总价值:{total_price}美元')
main()
"""

"""分治法例子：快速排序"""
"""
快速排序 - 选择枢轴元素进行划分，左边都比枢轴小，右边都比枢轴大
"""
"""
def quick_sort(origin_items,comp=lambda x,y: x <= y):
	items = origin_items[:]
	_quick_sort(items,0,len(items)-1,comp)
	return items

def _quick_sort(items,start,end,comp):
	if start < end:
		pos = _partition(items,start,end,comp)
		_quick_sort(items,start,pos-1,comp)
		_quick_sort(items,pos+1,end,comp)

def _partition(items,start,end,comp):
	pivot = items[end]
	i = start -1
	for j in range(start,end):
		if comp(items[j],pivot):
			i += 1
			items[i],items[j] = items[j],items[i]
	items[i+1],items[end] = items[end],items[i+1]
	return i+1
def main():
	import random
	l = []
	for _ in range(1,1000001):
		l.append(random.randint(1,1000))
	res = quick_sort(l)
	print(res)
main()
"""

"""回溯法：骑士巡逻"""
"""
递归回溯法：叫试探法，按选优条件向前搜索，当搜索到某一步，发现原来选择并不优或达不到
"""
"""
import sys
import time

SIZE = 5
total = 0

def print_board(board):
	for row in board:
		for col in row:
			print(str(col).center(4),end='')
		print()

def patrol(board,row,col,step=1):
	if row >= 0 and row < SIZE and col >= 0 and col < SIZE and board[row][col] == 0:
		board[row][col] = step
		if step == SIZE*SIZE:
			global total
			total += 1
			print(f'第{total}种走法')
			print_board(board)
		patrol(board,row-2,col-2,step+1)
		patrol(board,row-1,col-2,step+1)
		patrol(board,row+1,col-2,step+1)
		patrol(board,row+2,col-1,step+1)
		patrol(board,row+2,col+1,step+1)
		patrol(board,row+1,col+2,step+1)
		patrol(board,row-1,col+2,step+1)
		patrol(board,row-2,col+1,step+1)
		board[row][col] = 0
def main():
	board = [[0] * SIZE for _ in range(SIZE)]
	patrol(board,SIZE-1,SIZE-1)
main()
"""

"""动态规划例子1：斐波拉契数列(不使用动态规划将会是几何级数复杂度)"""
"""
动态规划 - 适用于有重叠子问题和最优子结构性质的问题
使用动态规划方法所耗费时间往往远少于朴素解法(用空间换时间)
"""
"""
def fib(num,temp={}):
	# 用递归计算Fibonacci数
	if num in (1,2):
		return 1
	try:
		return temp[num]
	except KeyError:
		temp[num] = fib(num-1) + fib(num-2)
		return temp[num]
def main():
	print(fib(905))
	print(len(str(fib(750))))
main()
"""

"""动态规划例子2：子列表元素之和的最大值(可使用动态规划避免二重循环)"""
"""
def main():
	items = list(map(int,input().split()))
	size = len(items)
	overall,partial = {},{}
	overall[size-1] = partial[size-1] = items[size-1]
	for i in range(size-2,-1,-1):
		partial[i] = max(items[i],partial[i+1]+items[i])
		overall[i] = max(partial[i],overall[i+1])
	print(overall[0])
main()
"""

# 2、函数的使用方法
"""
1、将函数视为“一等公民”
	函数可以赋值给变量
	函数可以作为函数的参数
	函数可以作为函数的返回值

2、高阶函数的用法(filter,map以及它们的替代品)
"""
"""
filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。
该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判，
然后返回 True 或 False，最后将返回 True 的元素放到新列表中。
"""
"""
items1 = list(map(lambda x: x ** 2, filter(lambda x:x % 2,range(1,10))))
print(items1)
items2 = [x ** 2 for x in range(1,10) if x % 2] # 奇数%2余1，
print(items2)
"""

"""
3、位置参数、可变参数、关键字参数、命名关键字参数

4、参数的元信息(代码可读性问题)

5、匿名函数和内联函数的用法(lambda函数)

6、闭包和作用域问题
	python中搜索变量的LEGB顺序(Local--> Embeded--> Global--> Built-in)
	global 和 nonlocal 关键字的作用
		global:声明或定义全局变量(要么使用现有的全局作用域的变量，要么定义一个变量放到全局作用域)
		nonllocal：声明使用嵌套作用域的变量(嵌套作用域必须存在该变量，否则报错)

7、装饰器函数(使用装饰器和取消装饰器)
"""
# 例子：输出函数执行时间的装饰器
from functools import wraps
from time import time

def main(num):
	while num:
		print("hello world")
		num = num - 1

def record_time(func):
	"""自定义装饰函数的装饰器"""
	@wraps(func)
	def wrapper(*args,**kwargs):
		start = time()
		result = func(*args,**kwargs)
		print(f'{func.__name__}:{time()-start}秒')
		return result
	return wrapper
record_time(main(1000))
