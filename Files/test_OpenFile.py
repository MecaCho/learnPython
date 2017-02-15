#-*-coding=utf-8-*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import os
import time
import os.path
import sqlite3
import shutil
import xml.dom.minidom as ET
import unittest
from HTMLTestRunner import HTMLTestRunner
from addtestfile import *
box_width = 90
item_width = 50
digtal_width = box_width - item_width
# addTestfile
addtestfile()

# 读取渲染配置文件
RenderConfig = open("C:\\fortofour\\RenderScript\\RenderConfig.xml", 'r')
RDOMTree = ET.parse(RenderConfig)
RData = RDOMTree.documentElement

#address = "D:\Windows_test_OFD\test_openfile\objectdemo_windows.html"
address = "C:\\foxit.ofd.ocx\\objectdemo_windows_time.html"


RenderSavePath = RData.getElementsByTagName("RenderSavePath")[0]
RenderSavePath = RenderSavePath.childNodes[0].data

DPINum = RData.getElementsByTagName("DPINum")[0]
DPINum = DPINum.childNodes[0].data

# 加载ie驱动
iedriver = "C:\Program Files (x86)\Internet Explorer\IEDriverServer.exe"
os.environ["webdriver.ie.driver"] = iedriver
browser = webdriver.Ie(iedriver)
browser.get(address)
time.sleep(1)
nowhandle = browser.current_window_handle
time.sleep(1)

'''数据库操作，连接数据库'''
# 打开数据库
cx = sqlite3.connect(dbpath)
cu = cx.cursor()
cu.execute("select * from " + testfiledbtable)
print 'Test Start'
print box_width*'*'
for fileinfo in cu.fetchall():

    # 清空所有数据
    browser.find_element_by_id("Text1").clear()
    browser.find_element_by_id("Text2").clear()
    browser.find_element_by_id("Text3").clear()
    browser.find_element_by_id("Text4").clear()
    browser.find_element_by_id("Text5").clear()
    browser.find_element_by_id("Text6").clear()
    browser.find_element_by_id("Text7").clear()
    browser.find_element_by_id("Text8").clear()
    browser.find_element_by_id("Text9").clear()
    browser.find_element_by_id("Text10").clear()
    browser.find_element_by_id("text_time").clear()
    browser.find_element_by_id("Text11").clear()

    print fileinfo[0], fileinfo[1]

    # 输入要打开的文件的路径

    browser.find_element_by_id("Text10").send_keys(fileinfo[1])
    time.sleep(1)

    browser.find_element_by_id("Text11").send_keys(fileinfo[0])
    time.sleep(1)
    # 打开文档
    starttime = time.time()
    print '%-*s%*s' % (item_width,'Rend Test Start Time :',digtal_width,time.ctime(starttime))
    browser.find_element_by_id("button1").send_keys(Keys.ENTER)
    browser.find_element_by_id("button_time").send_keys(Keys.ENTER)
    nTime = browser.find_element_by_id("text_time").get_attribute("value")
    print "nTime:",nTime
    #print '%-*s%*.2fs' % (item_width,'Open The OFD Files TestTime:',digtal_width,nTime)
    time.sleep(2)
    # 获取文档数量
    browser.find_element_by_id("Button4").send_keys(Keys.ENTER)
    time.sleep(1)

    # 获取页面数量
    browser.find_element_by_id("Button5").send_keys(Keys.ENTER)
    time.sleep(1)

    # 设置图片存放路径【通过配置文件读取】
    # dirpath = "E:\\foxit.ofd.ocx\\RenderResult"
    str1 = fileinfo[0][:-4]
    print '%-*s%*s'% (item_width,"Source File:",digtal_width,str1)
    str2 = str1 + "_" + time.strftime('%Y-%m-%d-%H-%M-%S-%M', time.localtime(time.time()))
    print '%-*s%*s'% (item_width,'Render File:',digtal_width,str2)

    # 设置要渲染图片的DPI【通过配置文件读取】
    # DPI = 144
    browser.find_element_by_id("Text7").send_keys(DPINum)

    fulldir = RenderSavePath + "\\" + str1 + "\\" + str2
    if os.path.exists(fulldir):
        # shutil.rmtree(fulldir)
        # os.makedirs(fulldir)
        browser.find_element_by_id("Text8").send_keys(fulldir)
    else:
        os.makedirs(fulldir)
        browser.find_element_by_id("Text8").send_keys(fulldir)

    # 如果计算时间则从该处开始计算
    RenderStart = time.time()
    RenderEnd = 0
    # 渲染全部页面2
    browser.find_element_by_id("Button8").send_keys(Keys.ENTER)
    time.sleep(2)

    print '%-*s%*.2fs' % (item_width,"Render Time:",digtal_width,(RenderEnd - RenderStart))
    print '-'*box_width


#time.sleep(10)
browser.quit()
endtime = time.time()
totaltime = endtime - starttime
print 100*'*'
print '%-*s%*.2fs' % (item_width,'Test total time:',digtal_width,totaltime)
print 100*'*'
print 'Test end'