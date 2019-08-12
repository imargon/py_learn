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
    print
    "hello"


if __name__ == "__main__":
    run()    
