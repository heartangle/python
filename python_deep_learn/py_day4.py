# 循环结构


"""
or-in循环
如果明确的知道循环执行的次数或者是要对一个容器进行迭代，那么我们推荐使用for-in循环，
"""

# 用for循环实现1-100求和

'''
sum = 0
for x in range(101):
	sum += x
print(sum)
# 上面代码中的range类型，range可以用来产生一个不变的数值序列，而且这个序列通常都是用在循环中
# range(101) 可以产生一个0-100的整数序列
# range(1,100)可以产生一个1-99的整数序列
# range(1,100,2)可以产生一个1到99的奇数序列，其中的2是步长，即数值序列的增量
'''

# 用for循环实现1-100之间的偶数求和

'''
sum = 0
for x in range(2,101,2):
	sum += x
print(sum)
'''
'''
sum = 0
for x in range(1,101):
	if x % 2 == 0:
		sum += x
print(sum)
'''

# while 循环

# 猜数字游戏
'''
import random

answer = random.randint(1,101)
counter = 0
while True:
	counter += 1
	number = int(input('请输入：'))
	if number < answer:
		print('大一点')
	elif number > answer:
		print('小一点')
	else:
		print('恭喜你猜对了！')
		break
print('你总共猜了%f' % counter)
if counter > 7:
	print('你的智商余额明显不足')
'''

# 输出乘法口诀表
'''
for i in range(1,10):
	for j in range(1,i+1):
		print('%d*%d=%d' %(i,j,i*j),end = '\t')
	print()
'''

# 练习1：判断一个数是不是素数
'''
from math import sqrt

num = int(input('请输入一个整数：'))
end = int(sqrt(num))
is_prime = True
for x in range(2,end+1):
	if num % x == 0:
		is_prime = False
		break
if is_prime and num != 1:
	print('%d是素数' % num)
else:
	print('%d不是素数' % num)
'''

# 练习2：输入两个整数，计算最大公约数和最小公倍数
'''
x = int(input('x = '))
y = int(input('y = '))
if x > y:
	x,y = y,x
for factor in range(x,0,-1):
	if x % factor == 0 and y % factor == 0:
		print('%d和%d的最大公约数是%d' % (x, y, factor))
		print('%d和%d的最小公倍数是%d' % (x, y, x * y//factor))
		break
'''

# 练习3：打印三角形图案
"""
打印各种三角形图案

*
**
***
****
*****

    *
   **
  ***
 ****
*****

    *
   ***
  *****
 *******
*********

Version: 0.1
Author: 骆昊
"""

'''
row = int(input('请输入行数：'))
for i in range(row):
	for _ in range(i+1):
		print('*',end='')
	print()

for i in range(row):
	for j in range(row):
		if j < row -i - 1:
			print(' ',end='')
		else:
			print('*', end='')
	print()

for i in range(row):
	for _ in range(row - i -1):
		print(' ',end='')
	for _ in range(2* i + 1):
		print('*',end='')
	print()
'''
