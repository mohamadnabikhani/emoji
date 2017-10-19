
# -*- coding: utf-8 -*-
from PIL import Image
from PIL import ImageFont
from PIL import ImageOps
from PIL import ImageDraw
import arabic_reshaper
import textwrap
from bidi.algorithm import get_display
s = u'that\u2019s \U0001f63b'
import emojipy
# image = Image.new("RGBA", (100, 100), (255, 255, 255))
img = Image.open("a.jpg")
a, b = img.size
size = a, b
frame = Image.open('frame2.png')

aa, bb = frame.size
print aa, bb

# frame.thumbnail(size, Image.ANTIALIAS)
frame = frame.resize((a,b))
#
# frame.save('test.png')
# frame = Image.open('test.png')
img_dest = img.copy().convert('RGBA')
img_dest.paste(frame, (0, 0), frame)

# img_dest = img_dest.convert('RGB')
img_dest.save('fraaaaaame.png')


# word_number = a / 10
if a > 1100:
    word_number = a / 6
else:
    word_number = a/8
# print word_number
# print a,b
if b < 500:
    dist = 250
else:
    dist = 50
size = (1000 - dist)/ (88/2 - 88/7)
print size
font = ImageFont.truetype("IRANSans_Medium.ttf", size, encoding='unic')


text =" تقدیم به فلانی   :kissing_closed_eyes::sweat_smile:"

sig = False
emojis = []
new_emoji = ""
for i in text:
    # print i
    if i == ':' and not sig:
        new_emoji += ":"
        print i
        sig = True
        continue
    if sig:
        new_emoji += i
        print i

    if i == ":" and sig:
        # new_emoji += ":"
        sig = False
        print i
        emojis.append(new_emoji)
        new_emoji = ''
print emojis
for i in emojis:
    # print i
    text = text.replace(i, "")
print text


# from pyemojify import emojify
# tex1 = emojify("Life is short :smile: , use :sparkles: Python :sparkles:")
import emoji
# tex1 = emoji.emojize('Python is :thumbsup:', use_aliases=True)
# tex1 = emojify("Life is short :smile: , use :sparkles: Python :sparkles:")

draw = ImageDraw.Draw(img_dest)
# w, h = draw.multiline_textsize(text, font=font)
FOREGROUND = (255, 255, 255)

lines = textwrap.wrap(text, width=word_number)
# print lines
# for i in lines:
#     print i
# print len(text)
# lis = text.split(" ")
# lens = len(lis)
# print lens
# new_lis = []
# sd = 0

# print a
# print b
# word_number = a/88
# for i in lis:
#     new_lis.append(i)
#     sd += 1
#     if sd % word_number == 0:
#         new_lis.append('\n')
# print new_lis
# ff = ''
# x = 0
# maxi = 0
#
# for i in new_lis:
#     x += len(i)
#     if i == '\n' and x > maxi:
#         maxi = x
#         x = 0
#
#     ff += i
#     ff += " "
#     x += 1
# print "maxi"
# print maxi
#
# print len(ff)
# print ff
#
# text = ff.decode('utf-8')
# from bidi.algorithm import get_display
# text = arabic_reshaper.reshape(text)
# bidi_text = get_display(text)
#
#
#
# draw = ImageDraw.Draw(img)
# font = ImageFont.truetype("IRANSans_Medium.ttf", b / 14, encoding='unic')
# w, h = draw.textsize(text, font=font)
# print w
#
# print h
# font = ImageFont.truetype("IRANSans_Medium.ttf", b / 30, encoding='unic')

# print w
#
# print h
# draw.multiline_text((a / 2 - w / 2, b - h - h/5), bidi_text, (20, 255, 255), font=font)
# img.save('sampleff-out.jpg')


# img = Image.open("ff.jpg")


print a,b
i = 0
for line in lines:
    text = line.decode('utf-8')
    # width, height = font.getsize(text)
    width, height = draw.textsize(text, font=font)
    # print width
    text = arabic_reshaper.reshape(text)
    bidi_text = get_display(text)
    # print a/2 - height/2
    # print "/////"
    # print a, width
    # print a / 2 - width/2
    draw.multiline_text((a / 2 - width/2 + width/10, b - (82 - size)*len(lines) + (40 + size/3) * i), bidi_text, font=font, fill=FOREGROUND)
    i += 1
import json
with open('/home/mohammad/untitled1/Output.json') as data_file:
    data = json.load(data_file)

files = {}
for i in data:
    if i['code'] in emojis:
        files[i['code']] = i['file']
#     if :) in emojis then implement
h = 0
for i in emojis:
    new_emoji = Image.open('/home/mohammad/untitled1/emoji-data-master/img-apple-160/{0}'.format(files[i]))
    new_emoji = new_emoji.resize((30, 30))
    img_dest.paste(new_emoji, (120 + h*50, 120 +h*50), new_emoji)
    h += 1
name = "heeeee.png" #.format(datetime.datetime.now())
img_dest.save(name)
