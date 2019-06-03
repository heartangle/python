# 函数和模块的使用


# 上面的问题等同于将8个苹果分成四组每组至少一个苹果有多少种方案
# 求阶乘
'''
def factorial(num):
	result = 1
	for n in range(1,num + 1):
		result *= n
	return result

m = int(input('m = '))
n = int(input('n = '))

print(factorial(m) // factorial(n) // factorial(m-n))
'''

# 定义函数
"""
在Python中可以使用def关键字来定义函数，和变量一样每个函数也有一个响亮的名字，
而且命名规则跟变量的命名规则是一致的。在函数名后面的圆括号中可以放置传递给
函数的参数，这一点和数学上的函数非常相似，程序中函数的参数就相当于是数学上
说的函数的自变量，而函数执行完成后我们可以通过return关键字来返回一个值，
这相当于数学上说的函数的因变量。
"""

# 函数的参数
"""
在Python中，函数的参数可以有默认值，也支持使用可变参数，
所以Python并不需要像其他语言一样支持函数的重载，因为我们在定义一个函数
的时候可以让它有多种不同的使用方式，下面是两个小例子。
"""

# 摇筛子 param n:色子的个数 return: n颗色子点数之和
'''
from random import randint

def roll_dice(n=2):
	total = 0
	for _ in range(n):
		total += randint(1, 6)
	return total

def add(a=0, b=0, c=0):
	return a + b + c
	
# 如果没有使用参数 使用默认值摇筛子
print(roll_dice())
# 摇三颗
print(roll_dice(3))
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
#传递参数时可以不按照设定的顺序进行传递
print(add(c=50, a=100, b=200))
'''

# 可变参数
# 在参数名前面的*表示args是一个可变参数
# 即在调用add函数时可以传入0个或多个参数
'''
def add(*args):
	total = 0
	for val in args:
		total += val
	return total

print(add())
print(add(1))
print(add(1,2,3,4))
print(add(1,3,5,7,9))
'''

# 用模块管理函数
"""
因为我们会遇到命名冲突这种尴尬的情况。
最简单的场景就是在同一个.py文件中定义了两个同名函数，由于Python没有函数重载的概念，
那么后面的定义会覆盖之前的定义，也就意味着两个函数同名函数实际上只有一个是存在的。

def foo():
    print('hello, world!')


def foo():
    print('goodbye, world!')


# 下面的代码会输出什么呢？
foo()

当然上面的这种情况我们很容易就能避免，但是如果项目是由多人协作进行团队开发的时候，
团队中可能有多个程序员都定义了名为foo的函数，那么怎么解决这种命名冲突呢？
答案其实很简单，Python中每个文件就代表了一个模块（module），我们在不同的模块中可以
有同名的函数，在使用函数的时候我们通过import关键字导入指定的模块就可以区分到底要
使用的是哪个模块中的foo函数，代码如下所示。

module1.py

def foo():
    print('hello, world!')
module2.py

def foo():
    print('goodbye, world!')
test.py

from module1 import foo

# 输出hello, world!
foo()

from module2 import foo

# 输出goodbye, world!
foo()

也可以按照如下所示的方式来区分到底要使用哪一个foo函数。

test.py

import module1 as m1
import module2 as m2

m1.foo()
m2.foo()

但是如果将代码写成了下面的样子，那么程序中调用的是最后导入的那个foo，
因为后导入的foo覆盖了之前导入的foo。

test.py

from module1 import foo
from module2 import foo

# 输出goodbye, world!
foo()

test.py

from module2 import foo
from module1 import foo

# 输出hello, world!
foo()

需要说明的是，如果我们导入的模块除了定义函数之外还中有可以执行代码，
那么Python解释器在导入这个模块时就会执行这些代码，事实上我们可能并不希望如此，
因此如果我们在模块中编写了执行代码，最好是将这些执行代码放入如下所示的条件中
，这样的话除非直接运行该模块，if条件下的这些代码是不会执行的，
因为只有直接执行的模块的名字才是“__main__”。

module3.py

def foo():
    pass


def bar():
    pass


# __name__是Python中一个隐含的变量它代表了模块的名字
# 只有被Python解释器直接执行的模块的名字才是__main__
if __name__ == '__main__':
    print('call foo()')
    foo()
    print('call bar()')
    bar()
test.py

import module3

# 导入module3时 不会执行模块中if条件成立时的代码 因为模块的名字是module3而不是__main__
"""


# 练习
# 实现计算求最大公约数和最小公倍数的函数
'''
def gcd(x, y):
	(x, y) = (y, x) if x > y else (x, y)
	# 从x到0(左闭右开)->[x 0) 每次减1
	for factor in range(x,0,-1):  
		if x % factor == 0 and y %factor == 0:
			return factor

def lcm(x, y):
	return x*y // gcd(x,y)
'''	
# 实现判断一个数是不是回文数的函数
'''
def is_palindrome(num):
	temp = num
	total = 0
	while temp > 0:
		total = total * 10 + temp % 10
		temp //= 10
	return total == num
'''

# 实现判断一个数是不是素数
'''
def is_prime(num):
	for factor in range(2,num):
		if num % factor == 0:
			return False
	return True if num != 1 else False
'''

# 实现一个程序判断输入的正整数是不是回文素数
'''
if __name__ == '__main__':
	num = int(input('请输入整数：'))
	if is_palindrome(num) and is_prime(num):
		print("%d是回文素数" % num)
'''





