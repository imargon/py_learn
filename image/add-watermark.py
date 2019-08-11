#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import glob
from PIL import Image, ImageDraw, ImageFont
import imghdr

image_dir = "F:/zhen/df/尿素箱盖/"
image_path = os.path.join(image_dir)
image_text = "东风商用车配件 186 7198 3115"
image_font = ImageFont.truetype('C:\Windows\Fonts\msyh.ttf', 40)
image_logo = Image.open("F:/zhen/df/logo4.jpg")
image_list = os.listdir(image_path)
ind = 0


def pic_addwatermark(image_name, image_text, image_font):

    # 指定使用字体
    original_image = Image.open(image_name)
    layer = original_image.convert('RGBA')

    # 生成同等大小的图片
    text_overlay = Image.new('RGBA', layer.size, (255, 255, 255, 0))
    image_draw = ImageDraw.Draw(text_overlay)

    # 获取文本大小
    text_size_x, text_size_y = image_draw.textsize(text=image_text, font=image_font)

    # 设置文本文字位置
    text_xy = (layer.size[0] - text_size_x, layer.size[1] - 280)

    # 设置文本颜色和透明度 和 位置
    image_draw.text(text_xy, text=image_text, font=image_font, fill=(20, 20, 20, 120))

    # 将新生成的图片覆盖到需要加水印的图片上
    layer_add = Image.alpha_composite(layer, text_overlay)
    original_image = Image.open(image_name)

    # 设置图层
    original_layer = Image.new('RGBA', original_image.size, (255, 255, 255, 0))
    original_layer.paste(image_logo, (original_image.size[0]-original_layer.size[0], original_image.size[1] - original_layer.size[1]))

    # 图层覆盖
    layer_add.save(str(image_name)+'.png')


# 增加logo

def pic_addlogo(image_name, image_logo):
    original_image = Image.open(image_name)

    # 设置图层
    original_layer = Image.new('RGBA', original_image.size, (255, 255, 255, 0))
    original_layer.paste(image_logo, (original_image.size[0]-original_layer.size[0], original_image.size[1] - original_layer.size[1]))

    # 图层覆盖
    image_add = Image.composite(original_layer, original_image, original_layer)

    # image_add.show()
    image_add.save(str(image_name)+'.png')


def img_batchamark():
    for image_name in image_list:
        image_name = image_dir+image_name
        pic_addwatermark(image_name, image_text, image_font)


def img_batchlogo():
    for image_name in glob.glob(os.path.join(image_dir, '*.png')):
        pic_addlogo(image_name, image_logo)


if __name__ == "__main__":
    img_batchamark()
    img_batchlogo()
