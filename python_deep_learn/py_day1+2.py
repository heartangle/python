

'''
import sys

print(sys.version_info)
print(sys.version)
'''



'''
import turtle

turtle.pensize(4)
turtle.pencolor('red')
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.mainloop()
'''

'''
a = 321
b = 123
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
'''

'''
a = int(input('a = '))
b = int(input('b = '))
print('%d + %d = %d' % (a, b, a + b))
print('%d // %d = %d' % (a, b, a // b))
print('%d ** %d = %d' % (a, b, a ** b))
'''
'''
a = 100
b = 12.345
c = 1 + 5j
d = 'hello world'
e = True

print(type(a))
print(type(int(b))
print(type(c))
print(type(d))
print(type(e))
'''

'''
a = 5
b = 10
a /= b
print('a = ', a)
'''
'''
flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not flag1
print("flag1 = ", flag1)
print("flag3 = ", flag3)
print("flag4 = " , flag4)
print("flag5 = ", flag5)
print(flag1 is True)
print(flag2 is not False)
'''

'''
# 华氏温度转为摄氏温度
f = float(input('请输入华氏温度：'))
c = (f-32)/1.8
print('%.1f华氏度 = %.1f摄氏度' %(f, c))
'''

'''
# 输入半径计算园的周长和面积
import math

while True:
	
	radius = float(input('请输入园的半径：'))
	perimetr = 2*math.pi*radius
	area = math.pi*radius*radius
	print('周长：%.2f' % perimetr)
	print('面积：%.2f' % area)
'''

'''
# 输入的年份判断是不是闰年

year = int(input('请输入年份：'))
is_leap = (year%4==0 and year%100!=0 or year%400==0)
print(is_leap)
'''















