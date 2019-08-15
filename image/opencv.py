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
import cv2

img = cv2.imread('F:/py/pic/butterfly.jpg', cv2.IMREAD_COLOR)    # 打开文件
font = cv2.FONT_HERSHEY_DUPLEX  # 设置字体
# 图片对象、文本、像素、字体、字体大小、颜色、字体粗细
imgzi = cv2.putText(img, "FONT_HERSHEY_DUPLEX ", (1100, 1164), font, 5.5, (0, 0, 0), 2,)
cv2.imshow('lena', img)
cv2.imwrite('F:/py/pic/5.png', img)    # 写磁盘

cv2.destroyAllWindows()     # 毁掉所有窗口
# cv2.destroyWindow(wname)    # 销毁指定窗口
