# 图形用户界面和游戏开发
"""
基于tkinter模块的GUI
GUI是图形用户界面的缩写，图形化的用户界面对使用过计算机的人来说应该都不陌生，在此无须进行
赘述.python默认的GUI开发模块是tkinter（在Python 3以前的版本中名为Tkinter），
从这个名字就可以看出它是基于Tk的，Tk是一个工具包，最初是为Tcl设计的，后来被移植到很多
其他的脚本语言中，它提供了跨平台的GUI控件。当然Tk并不是最新和最好的选择，
也没有功能特别强大的GUI控件，事实上，开发GUI应用并不是Python最擅长的工作，
如果真的需要使用Python开发GUI应用，wxPython、PyQt、PyGTK等模块都是不错的选择。

基本上使用tkinter来开发GUI应用需要以下五个步骤:
	1、导入tkinter模块
	2、创建一个顶层窗口对象并用它来承载整个GUI应用
	3、在顶层窗口对象上添加GUI组件
	4、通过代码将这些GUI组件的功能组织起来
	5、进入主事件循环(main loop)
"""
'''
import tkinter
import tkinter.messagebox

def main():
	flag = True
	# 修改标签上的文字
	def change_label_text():
		nonlocal flag
		flag = not flag
		color,msg = ('red','hello world!') if flag else ('blue','goodbye world!')
		label.config(text=msg,fg=color)
	# 确认退出
	def confirm_to_quit():
		if tkinter.messagebox.askokcancel('温馨提示','确定要退出吗?'):
			top.quit()
	# 创建顶层窗口
	top = tkinter.Tk()
	# 设置窗口大小
	top.geometry('240x160')
	# 设置窗口标题
	top.title('小游戏')
	# 创建标签对象并添加到顶层窗口
	label = tkinter.Label(top,text='hello world!',font='Arial -32',fg='red')
	label.pack(expand=1)
	# 创建一个装按钮的容器
	panel = tkinter.Frame(top)
	# 创建按钮对象 指定添加到那个容器 通过command参数绑定事件回调函数
	button1 = tkinter.Button(panel,text='修改',command=change_label_text)
	button1.pack(side='left')
	button2 = tkinter.Button(panel,text='退出',command=confirm_to_quit)
	button2.pack(side='right')
	panel.pack(side='bottom')
	tkinter.mainloop()
main()
'''
"""
需要说明的是，GUI应用通常是事件驱动式的，之所以要进入事件循环就是要监听鼠标，键盘等
各种事件的发生并执行相应的代码事件处理，因为事件会持续发生，所以需要这样的一个循环一直
运行着等待下一个事件的发生。另一方面，Tk为控件的摆放提供了三种布局管理器，通过布局管理器
可以对控件进行定位，这三种布局管理器分别是：Placer(开发者提供控件的大小和摆放位置),
Packer(自动将控件填充到合适的位置) 和 Grid(基于网络坐标来摆放控件)
"""

# 使用pygame进行游戏开发
"""
pygame是一个开源的python模块，专门用于多媒体应用(如电子游戏)的开发，其中包括对图像、
声音、视频、事件、碰撞等的支持。pygame建立在SDL的基础上，SDL是一套跨平台的多媒体开发库
用C语言实现，被广泛的应用于游戏、模拟器、播放器等的开发。而pygame让游戏开发者不再被底层
语言束缚，可以更多的关注游戏的功能和逻辑。

下面我们来完成一个简单的小游戏，游戏的名字叫“大球吃小球”，当然完成这个游戏并不是重点，
学会使用Pygame也不是重点，最重要的我们要在这个过程中体会如何使用前面讲解的
面向对象程序设计，学会用这种编程思想去解决现实中的问题。
"""

# 制作游戏窗口
'''
import pygame
def main():
	# 初始化导入的pygame模块
	pygame.init()
	# 初始化用于显示的窗口并设置窗口尺寸
	screen = pygame.display.set_mode((800,600))
	# 设置当前窗口的标题
	pygame.display.set_caption('大球吃小球')
	running = True
	# 开启一个事件循环处理发生的事件
	while running:
		# 从消息队列中获取事件并对事件进行处理
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
'''

# 在窗口中绘图
"""
可以使用pygame中的draw模块的函数在窗口上进行绘图，可以绘制的图形包括:线条、矩形、多边形
园、椭圆、圆弧等。需要说明的是，屏幕坐标系是将屏幕左上角设置为坐标原点(0,0)，向右x轴的
正向，向下是y轴的正向，在表示位置或者设置尺寸时，我们默认的单位都是像素。所谓像素就是屏幕
上的一个点，你可以用浏览器的软件将一张图片放大若干倍，就可以看到这些点。pygame中表示颜色
用的是色光三原色表示法，即通过一个元祖或列表来表示颜色的RGB值，每个值都在0-255之间，因为
是每种原色都用一个8位(bit)的值来表示，三种颜色相当于一共24位构成，这也就是常说的"24位
颜色表示法"
"""
'''
import pygame
def main():
	# 初始化导入的pygame模块
	pygame.init()
	# 初始化用于显示的窗口并设置窗口尺寸
	screen = pygame.display.set_mode((800,600))
	# 设置当前窗口的标题
	pygame.display.set_caption('大球吃小球')
	# 设置窗口的背景色(颜色是由红绿蓝三原色构成的元祖)
	screen.fill((242,242,242))
	# 绘制一个圆(参数分别是：屏幕，颜色，圆心位置，半径，0表示填充圆)
	pygame.draw.circle(screen,(250,0,0),(100,100),30,0)
	# 刷新当前窗口(渲染窗口将绘制的图象展示出来)
	pygame.display.flip()
	running = True
	# 开启一个事件循环处理发生的事件
	while running:
		# 从消息队列中获取事件并对事件进行处理
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
main()
'''

# 加载图象
"""
如果需要直接加载图象到窗口上，可以使用pygame中image模块的函数来加载图象，在通过之前的
窗口对象的 blie 方法渲染图象
"""
'''
import pygame
def main():
	# 初始化导入的pygame模块
	pygame.init()
	# 初始化用于显示的窗口并设置窗口尺寸
	screen = pygame.display.set_mode((800,600))
	# 设置当前窗口的标题
	pygame.display.set_caption('大球吃小球')
	# 设置窗口的背景色(颜色是由红绿蓝三原色构成的元祖)
	screen.fill((255,255,255))
	# 通过指定的文件名加载图象
	ball_image = pygame.image.load('./timg.jpg')
	# 在窗口上渲染图象
	screen.blit(ball_image,(50,50))
	# 刷新当前窗口(渲染窗口将绘制的图象展示出来)
	pygame.display.flip()
	running = True
	# 开启一个事件循环处理发生的事件
	while running:
		# 从消息队列中获取事件并对事件进行处理
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
main()
'''

# 实现动画效果
"""
说到动画这个词大家都不会陌生事实上要实现动画效果，本身的原理也非常简单，就是将不连续的
图片连续的播放，只要每秒达到了一定的帧数，那么就可以做出比较流畅的动画效果。如果要让上面
代码中的小球动起来，可以将小球的位置用变量来表示，并在循环中修改小球的位置在刷新整个窗口
"""
'''
import pygame
def main():
	# 初始化导入的pygame模块
	pygame.init()
	# 初始化用于显示的窗口并设置窗口尺寸
	screen = pygame.display.set_mode((800,600))
	# 设置当前窗口的标题
	pygame.display.set_caption('大球吃小球')
	# 定义变量来表示小球在屏幕上的位置
	x,y = 50,50
	running = True
	# 开启一个事件循环处理发生的事件
	while running:
		# 从消息队列中获取事件并对事件进行处理
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
		screen.fill((255,255,255)) # 设置窗口背景色
		# 绘制一个圆(参数分别是：屏幕，颜色，圆心位置，半径，0表示填充圆)
		pygame.draw.circle(screen,(250,0,0),(x,y),30,0)
		pygame.display.flip() # 刷新当前窗口(渲染窗口将绘制的图象展示出来)
		# 每隔50毫秒就改变小球的位置在刷新窗口
		pygame.time.delay(50)
		x,y = x + 5,y + 5
main()
'''

# 碰撞检测
"""
通常一个游戏中会有很多对对象出现，而这些对象之间的"碰撞"在所难免，比如炮弹击中飞机，箱子
撞到了地面等。碰撞检测在绝大多数的游戏中都是一个必须处理的至关重要的问题，pygame的sprite
(动画精灵)模块就提供了对碰撞检测的支持，这里不做介绍，因为要检测两个小球有没有碰撞只需要
检查球心的距离有没有小于两个球的半径之和。为了制造出更多的小球，我们可以通过对鼠标事件的
处理，在点击鼠标的位置创建颜色，大小和移动速度都随机的小球，当然要做到这一点需要把之前的
面向对象的知识应用起来
"""
'''

from enum import Enum
from math import sqrt
from random import randint
import pygame

# @uinque
class Color(Enum):
	"""颜色"""
	RED = (250,0,0)
	GREEN = (0,250,0)
	BLUE = (0,0,250)
	BLACK = (0,0,0)
	WHITE = (255,255,255)
	GRAY = (242,242,242)
	@staticmethod
	def random_color():
		"""获得随机颜色"""
		r = randint(0,255)
		g = randint(0,255)
		b = randint(0,255)
		return (r,g,b)
class Ball(object):
	"""球"""
	def __init__(self,x,y,radius,sx,sy,color=Color.RED):
		"""初始化方法"""
		self.x = x
		self.y = y
		self.radius = radius # 球的半径
		self.sx = sx
		self.sy = sy
		self.color = color
		self.alive = True
	def move(self,screen):
		"""移动"""
		self.x += self.sx
		self.y += self.sy
		if self.x - self.radius <= 0 or self.x - self.radius >= screen.get_width():
			self.sx = -self.sx
		if self.y - self.radius <= 0 or self.y + self.radius >= screen.get_height():
			self.sy = -self.sy
	def eat(self,other):
		"""吃其他球"""
		if self.alive and other.alive and self != other:
			dx,dy = self.x - other.x,self.y - other.y
			distance = sqrt(dx**2 + dy**2)
			if distance < self.radius + other.radius and self.radius > other.radius:
				other.alive = False
				self.radius = self.radius + int(other.radius*0.146)
	def draw(self,screen):
		"""在窗口上绘制球"""
		pygame.draw.circle(screen,self.color,(self.x,self.y),self.radius,0)


# 事件处理
"""
可以在事件循环中对鼠标事件进行处理，通过事件对象的 type 属性可以判定事件类型，在通过
pos 属性就可以获得鼠标点击的位置。如果要处理键盘事件也是在这个地方，做法和处理鼠标事件
类似
"""
def main():
	# 定义用来装所有球的容器
	balls = []
	# 初始化导入的pygam模块
	pygame.init()
	# 初始化用于显示的窗口并设置窗口尺寸
	screen = pygame.display.set_mode((800,600))
	# 设置当前窗口的标题
	pygame.display.set_caption('大球吃小球')
	running = True
	# 开启一个事件循环处理发生的事件
	while running:
		# 从消息队列中获取事件并对事件进行处理
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			# 处理鼠标事件的代码
			if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
				# 获得点击鼠标的位置
				x,y = event.pos
				radius = randint(10,100)
				sx,sy = randint(-10,10),randint(-10,10)
				color = Color.random_color()
				# 在点击鼠标的位置创建一个球(大小，速度和颜色随机)
				ball = Ball(x,y,radius,sx,sy,color)
				# 将球添加到列表容器中
				balls.append(ball)
		screen.fill((255,255,255))
		# 取出容器中的球 如果没被吃掉就绘制 被吃掉了就移除
		for ball in balls:
			if ball.alive:
				ball.draw(screen)
			else:
				balls.remove(ball)
		pygame.display.flip() # 刷新当前窗口(渲染窗口将绘制的图象展示出来)
		# 每隔50毫秒就改变球的位置在刷新窗口
		pygame.time.delay(50)
		for ball in balls:
			ball.move(screen)
			# 检查有没有吃到其他的球
			for other in balls:
				ball.eat(other)
main()
'''
			




