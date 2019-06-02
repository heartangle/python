# 分支结构



'''
username = input('请输入用户名：')
password = input('请输入口令：')
# 如果希望输入口令时，终端没有回显，可以使用getpass模块的getpass函数
# import getpass
# password = getpass.getpass('请输入口令：')

if username == 'admin' and password == '123456':
	print('身份验证成功！')
else:
	print('身份验证失败！')
'''

'''
import getpass
username = input('请输入用户名：')
password = getpass.getpass('请输入口令：')
if username == 'admin' and password == '123456':
	print('身份验证成功！')
else:
	print('身份验证失败！')
'''

'''
x = float(input('x = '))
if x > 1:
	y = 3 * x - 5
elif x < -1:
	y = x + 2
else:
	y = 5 * x + 3
print('x = %.2f : y =  %.2f' % (x, y))
'''

'''
x = float(input('x = '))
if x >= -1 and x <=1:
	y = x + 2
else:
	if x > 1:
		y = 3 * x - 5
	else:
		5 * x + 3
print('x = %.2f, y = %.2f' %(x, y))
'''

"""
 大家可以自己感受一下这两种写法到底是哪一种更好。
 在之前我们提到的Python之禅中有这么一句话“Flat is better than nested.”，
 之所以提出这个观点是因为嵌套结构的嵌套层次多了之后会严重的影响代码的可读性，
 如果可以使用扁平化的结构就不要去用嵌套，因此之前的写法是更好的做法。
"""

# 练习1：英制单位和公制单位转换
'''
value = float(input('请输入长度：'))
unit = input('请输入单位：')
if unit == 'in' or unit == '英寸':
	print('%f英寸 = %f厘米' %(value, value*2.54))
elif unit == 'cm' or unit == '厘米':
	print('%d厘米 = %f英寸' %(value, value/2.54))
else:
	print('请输入有效的单位')
'''


# 练习2：掷色子决定做什么
'''
from random import randint

face = randint(1,6)
if face == 1:
	result = '唱歌'
elif face == 2:
	result = '跳个舞'
elif face == 3:
	result = '学狗叫'
elif face == 4:
	result = '做俯卧撑'
elif face == 5:
	result = '念绕口令'
else:
	result = '讲笑话'
print(result)
'''

# 练习3：百分制成绩转等级

"""
百分制成绩转等级制成绩
90分以上    --> A
80分~89分    --> B
70分~79分	   --> C
60分~69分    --> D
60分以下    --> E

Version: 0.1
Author: 骆昊
"""

'''
sorce = float(input('请输入成绩：'))
if sorce >= 90:
	grade = 'A'
elif sorce >= 80:
	grade = 'B'
elif sorce >= 70:
	grade = 'C'
elif sorce >= 60:
	grade = 'D'
else:
	grade = 'E'
print('对应的等级是',grade)
'''

# 练习4：输入三条边如果能构成三角形就计算周长和面积
'''
import math

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a + b > c and a + c > b and b + c > a:
	print('周长：%f' %(a+b+c))
	p = (a + b + c)/2
	area = math.sqrt(p*(p-a)*(p-b)*(p-c))
	print('面积：%f' %(area))
else:
	print('不能构成三角形')
'''

# 练习5：个人所得税计算器
'''
salary = float(input('本月收入：'))
insurance = float(input('五险一金：'))
diff = salary - insurance - 3500
if diff <= 0:
	rate = 0
	deduction = 0
elif diff < 1500:
	rate = 0.03
	deduction = 0
elif diff < 4500:
	rate = 0.01
	deduction = 105
elif diff < 9000:
	rate = 0.2
	deduction = 555
elif diff < 35000:
	rate = 0.25
	deduction = 1005
elif deii < 55000:
	rate = 0.3
	deduction = 2755
elif diff < 80000:
	rate = 0.35
	deduction = 5500
else:
	rate = 0.45
	deduction = 13505
tax = abs(diff*rate - deduction)
print('个人所得税：%.2f' % tax)
print('实际到手收入：%.2f' % (diff + 3500-tax))
'''













