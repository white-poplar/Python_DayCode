#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-19 10:08:55
# @Author  : poplar. (BYH5566@gmail.com)
# @Link    : https://white-poplar.github.io
# @Version : $Id$

import os
import PIL
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


# 居中
def clipiamge(size):
    width = int(size[0])
    height = int(size[1])
    box = ()
    if(width > height):
        dx = width - height
        box = (dx / 2, 0, height + dx / 2, height)
    else:
        dx = height - width
        box = (0, dx / 2, width, width + dx / 2)
    return box


# 缩略图
def thumb_photo(file_path, file_name, thumb_size):
    if not os.path.exists(file_path):
        return

    with Image.open(file_path) as __img:
        __img = Image.open(file_path)
        box = clipiamge(__img.size)
        print(box)
        region = __img.crop(box)
        region.thumbnail(thumb_size, Image.ANTIALIAS)
        newdir = './temp/'
        if not os.path.exists(newdir):
            os.mkdir(newdir)
        saveToPath = os.path.join(newdir, file_name)
        region.save(saveToPath, 'jpeg')


# 裁剪
def cat_photo(file_path, file_name, size_width):
    if not os.path.exists(file_path):
        return

    __img = Image.open(file_path)
    print(__img.format, __img.size, __img.mode)
    if __img.size[0] > size_width:
        # 根据宽度裁剪
        newWidth = size_width
        newHeight = float(size_width) / __img.size[0] * __img.size[1]
        __img.thumbnail((newWidth, newHeight), Image.ANTIALIAS)

    newdir = './temp/'
    if not os.path.exists(newdir):
        os.mkdir(newdir)
    saveToPath = os.path.join(newdir, file_name)
    __img.save(saveToPath, 'jpeg')


# 水印
def water_photo(file_path, file_name, water_text):
    if not os.path.exists(file_path):
        return

    __img = Image.open(file_path)
    w, h = __img.size

    # _font = ImageFont.load_default().font
    _font = ImageFont.truetype(
        'C:\Windows\Fonts\HYHalloweenJ.ttf', int(h / 20))
    _draw = ImageDraw.Draw(__img)

    f_w, f_h = _font.getsize(water_text)
    print('f_w=%s,f_h=%s' % (f_w, f_h))

    _draw.text((w - f_w - 10, h - f_h - 10),
               water_text, (129, 41, 145), font=_font)

    newdir = './temp/'
    if not os.path.exists(newdir):
        os.mkdir(newdir)
    saveToPath = os.path.join(newdir, file_name)
    __img.save(saveToPath, 'jpeg')


# 角标
def mark_photo(file_path, file_name, mark_text, mark_position=9):
    if not os.path.exists(file_path):
        return

    __img = Image.open(file_path)
    w, h = __img.size

    # _font = ImageFont.load_default().font
    _font = ImageFont.truetype(
        'C:\Windows\Fonts\HYHalloweenJ.ttf', int(h / 20))
    _draw = ImageDraw.Draw(__img)

    f_w, f_h = _font.getsize(mark_text)
    print('f_w=%s,f_h=%s' % (f_w, f_h))

    _margin = 5
    _position = (_margin, _margin)

    if mark_position == 1:
        # 左1
        _position = (_margin, _margin)
    elif mark_position == 2:
        # 中1
        _position = (w / 2 - f_w / 2, _margin)
    elif mark_position == 3:
        # 右1
        _position = (w - f_w - _margin, _margin)
    elif mark_position == 4:
        # 左2
        _position = (_margin, h / 2 - f_h / 2)
    elif mark_position == 5:
        # 中2
        _position = (w / 2 - f_w / 2, h / 2 - f_h / 2)
    elif mark_position == 6:
        # 右2
        _position = (w - f_w - _margin, h / 2 - f_h / 2)
    elif mark_position == 7:
        # 左3
        _position = (_margin, h - f_h - _margin)
    elif mark_position == 8:
        # 中3
        _position = (w / 2 - f_w / 2, h - f_h - _margin)
    elif mark_position == 9:
        # 右3
        _position = (w - f_w - _margin, h - f_h - _margin)

    print(_position)
    _draw.text(_position,
               mark_text, (129, 41, 145), font=_font)

    newdir = './temp/'
    if not os.path.exists(newdir):
        os.mkdir(newdir)
    saveToPath = os.path.join(newdir, file_name)
    __img.save(saveToPath, 'jpeg')


if __name__ == '__main__':
    # thumbanail
    with Image.open('logo.png') as img:
        w, h = img.size
        print("w=%s,h=%s" % (w, h))
        img.thumbnail((w // 2, h // 2), resample=Image.LANCZOS)  # 缩放
        img.save("A.jpg", format="jpeg")

    # resize
    with Image.open('logo.png') as img:
        w, h = img.size
        print("w=%s,h=%s" % (w, h))
        resized = img.resize((w // 2, h // 2), resample=Image.ANTIALIAS)
        resized.save("B.jpg", format="jpeg")

    # crop
    with Image.open('logo.png') as img:
        w, h = img.size
        print("w=%s,h=%s" % (w, h))
        region = (0, 0, 800, 800)  # 0,0 左上角
        crop = img.crop(region)
        crop.save('C.jpg')

    thumb_photo('logo.png', 'D.jpg', (80, 80))

    cat_photo('logo.png', 'E.jpg', 100)

    # list = os.listdir('.')  # 目录下的所有文件和目录
    # print(list)

    water_photo('logo.png', 'F.jpg', u'黑莓糖专属城堡')

    mark_photo('logo.png', 'G.jpg', u'9', 3)
