# -*- coding:utf-8 -*-
from PIL import Image,ImageDraw,ImageFont
import time
import os

def render(im,filename):
    now =time.strftime("%Y-%m-%d-%H_%M_%S")
    str1='./result/'+filename[:-4]+now+'result.jpg'
    myfont = ImageFont.truetype("C:/Files/Lydia Puente.ttf",size=200)
    draw = ImageDraw.Draw(im)
    (w,h) = im.size
    #logo_x,logo_y
    fillcolor = "#F8F8FF"
    draw.text((0.77*w,0.78*h),'MCRain',font=myfont, fill=fillcolor)
    print str1
    im.save(str1,'jpeg')


if __name__ == '__main__':
    i=0
    for filename in os.listdir(r"./IMG"):
        print filename
        im = Image.open('C:/Files/IMG/'+filename,'r')
        i+=1
        print i
        print 'image info:',im.format, im.size, im.mode
        render(im,filename)
        print i
