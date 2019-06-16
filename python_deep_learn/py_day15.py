# 图形和办公文档处理

"""
用程序来处理图像和办公文档经常出现在实际开发中，Python的标准库中虽然没有直接支持这些操作的模块，
但我们可以通过Python生态圈中的第三方模块来完成这些操作。

用pillow操作图象
Pillow是由从著名的Python图像处理库PIL发展出来的一个分支，通过Pillow可以实现图像压缩和
图像处理等各

Pillow中最为重要的是Image类，读取和处理图像都要通过这个类来完成。
"""
'''
from PIL import Image

def main():
	image = Image.open('./timg.jpg')
	print(image.format,image.size,image.mode)
	image.show()
main()
'''

# 1、裁剪图片
'''
from PIL import Image

image = Image.open('timg.jpg')
rect = 80,20,310,360
image.crop(rect).show()
'''

# 2、生成缩略图
'''
from PIL import Image

image = Image.open('timg.jpg')
size = 128,128
image.thumbnail(size)
image.show()
'''

# 3、缩放和黏贴图片
'''
from PIL import Image

image1 = Image.open('timg.jpg')
image2 = Image.open('猪妹.jpg')
rect = 100,20,200,260
pikaqiu_head = image2.crop(rect)
width,height = pikaqiu_head.size
image1.paste(pikaqiu_head.resize((int(width/1.5), int(height/1.5))),(172,40))
image1.show()
'''

# 4、旋转和翻转
'''
from PIL import Image

image = Image.open('猪妹.jpg')
image.rotate(180).show()
image.transpose(Image.FLIP_LEFT_RIGHT).show()
'''

# 5、操作像素
'''
from PIL import Image

image = Image.open('timg.jpg')
for x in range(80,310):
	for y in range(20,360):
		image.putpixel((x,y),(128,128,128))
image.show()
'''

# 6、滤镜效果
'''
from PIL import Image,ImageFilter

image = Image.open('timg.jpg')
image.filter(ImageFilter.CONTOUR).show() # 这里把图片变黑白了
'''

# 处理Excel电子表格
"""
Python的openpyxl模块让我们可以在Python程序中读取和修改Excel电子表格，当然实际工作中，我们可能会
用LibreOffice Calc和OpenOffice Calc来处理Excel的电子表格文件，这就意味着openpyxl模块也能处理来自这
些软件生成的电子表格。关于openpyxl的使用手册和使用文档可以查看它的官方文档。
链接：https://openpyxl.readthedocs.io/en/stable/#
"""

# 处理Word文档
"""
利用python-docx模块，Pytho 可以创建和修改Word文档，当然这里的Word文档不仅仅是指通过微软的
Office软件创建的扩展名为docx的文档，LibreOffice Writer和OpenOffice Writer都是免费的字处理软件。
"""

# 处理PDF文档
"""
PDF是Portable Document Format的缩写，使用.pdf作为文件扩展名。接下来我们就研究一下如何通过Python
实现从PDF读取文本内容和从已有的文档生成新的PDF文件。
"""
