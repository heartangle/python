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

# 排序算法(选择，冒泡，归并)和查找算法(顺序和折半)

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
