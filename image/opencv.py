from __future__ import unicode_literals
import sys

import cv2

img1 = cv2.imread('linuxidc.com.jpg',cv2.IMREAD_COLOR)
text = 'www.linuxidc.com'
pos = (10,150)
font_type = 4
font_size = 2
color = (255,0,0)
bold = 1


#图片，文字，位置，字体，字号，颜色，厚度
cv2.putText(img1,text,pos, font_type, font_size, color,bold)
cv2.imshow('www.linuxidc.com',img1)
cv2.waitKey(0)


import cv2
from PIL import Image, ImageFont, ImageDraw
import numpy as np

img1 = cv2.imread('linuxidc.com.jpg',cv2.IMREAD_COLOR)

pil_image = Image.fromarray(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))

font = ImageFont.truetype('NotoSerifCJK-Regular.ttc', 40)
color = (0,0,255)
pos = (10,150)
text = u"Linux公社www.linuxidc.com"

draw = ImageDraw.Draw(pil_image)
draw.text(pos,text,font=font,fill=color)

cv_img = cv2.cvtColor(np.asarray(pil_image),cv2.COLOR_RGB2BGR)

cv2.imshow('www.linuxidc.com',cv_img)

cv2.waitKey(0)


from PIL import Image
im = Image.open("linuxidc.com.jpg")
mark = Image.open("linuxidc.png")
layer = Image.new('RGBA', im.size, (0,0,0,0))
layer.paste(mark, (im.size[0]-220,im.size[1]-520))
out = Image.composite(layer,im,layer)
out.show()

def run():
    print "hello"
    
if __name__ == "__main__":
    run()
   
#https://docs.opencv.org/3.3.0/da/d6e/tutorial_py_geometric_transformations.html   
    
import cv2
import numpy as np
img = cv2.imread('messi5.jpg')
res = cv2.resize(img,None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)
#OR
height, width = img.shape[:2]
res = cv2.resize(img,(2*width, 2*height), interpolation = cv2.INTER_CUBIC)

import cv2
import numpy as np
img = cv2.imread('messi5.jpg',0)
rows,cols = img.shape
M = np.float32([[1,0,100],[0,1,50]])
dst = cv2.warpAffine(img,M,(cols,rows))
cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()


img = cv2.imread('sudoku.png')
rows,cols,ch = img.shape
pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(img,M,(300,300))
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()

###
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import cv2
import numpy
from PIL import Image, ImageDraw, ImageFont

image_dir = "F:/py/pic/image/"
image_path = os.path.join(image_dir)
image_list = os.listdir(image_path)
n = 0

for image_name in image_list:
    n = n+1
    image_name = image_dir + image_name
    image_cv2 = cv2.imread(image_name, cv2.IMREAD_COLOR)    # 打开文件
    height, width, colors = image_cv2.shape
    image_PIL = Image.fromarray(cv2.cvtColor(image_cv2, cv2.COLOR_BGR2RGB))
    print(height, width, colors)
    x = width - 620
    y = height - 400
    watermark_position = (x, y)

    # image_font = cv2.FONT_HERSHEY_DUPLEX  # cv2 设置字体

    image_font = ImageFont.truetype('C:/Windows/Fonts/SIMLI.TTF', 200)
    image_color = (255, 255, 25, 20)
    image_text = '蝴 蝶'

    # cv2 待处理的图片、待添加的文字、添加位置坐标（文字左下角）、文字、大小、颜色、文字粗细
    # imgzi = cv2.putText(image_cv2, image_text, watermark_position, image_font, 5.5, image_color, 2,)
    # 左上角为画布坐标（0,0）点
    draw = ImageDraw.Draw(image_PIL)
    draw.text(watermark_position, image_text, image_color, image_font)

    # 重新转换为opencv格式

    image_cv2 = cv2.cvtColor(numpy.asarray(image_PIL), cv2.COLOR_BGR2RGB)
    cv2.imshow('demo', image_cv2)
    cv2.imwrite(image_dir+'image_'+str(n)+'.jpg', image_cv2)    # 写磁盘
    cv2.waitKey(0)
    cv2.destroyAllWindows()     # 毁掉所有窗口
    # cv2.destroyWindow(demo)    # 销毁指定窗口
