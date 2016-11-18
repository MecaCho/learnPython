#-*-coding=utf-8-*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import os
import sys
import time
import os.path
import sqlite3
import shutil
import xml.dom.minidom as ET
import unittest
from HTMLTestRunner import HTMLTestRunner
from selenium.common.exceptions import NoSuchAttributeException
from addtestfile import *
box_width = 70
item_width = 30
digtal_width = box_width - item_width
# addTestfile
addtestfile()
min_Time = 0
max_Time = 0
def prinf_functionTime(i):
    browser.implicitly_wait(10)
    try:
        time.sleep(1)
        result_function = browser.find_element_by_id("text_function").get_attribute("value")
        result_time = browser.find_element_by_id("text_time").get_attribute("value")
        time.sleep(1)
        num_result_time = int(result_time)
    except NoSuchAttributeException as e:
        print(e)
    finally:
        print '%-*s%*s%*dms' % (item_width-2, result_function,4,i,digtal_width-2, num_result_time)
        print '-'*box_width
    return num_result_time
def time_init():
    sum_Time =0
    avg_Time =0
def time_select(temp_Time,i,max_Time,min_Time):
    if i == 1:
        max_Time = temp_Time
        min_Time = temp_Time
    if temp_Time > max_Time:
        max_Time = temp_Time
    if temp_Time < min_Time:
        min_Time = temp_Time
    return (max_Time,min_Time)
# 读取渲染配置文件
RenderConfig = open("/mnt/Ubuntu_Share/fortofour/RenderScript/RenderConfig.xml", 'r')
RDOMTree = ET.parse(RenderConfig)
RData = RDOMTree.documentElement

address = RData.getElementsByTagName("address")[0]
address = address.childNodes[0].data
print 'Address:',address

RenderSavePath = RData.getElementsByTagName("RenderSavePath")[0]
RenderSavePath = RenderSavePath.childNodes[0].data

DPINum = RData.getElementsByTagName("DPINum")[0]

######加载Firefox驱动
starttime = time.time()
profile = webdriver.FirefoxProfile("/root/.mozilla/firefox/jasgfnfd.default")
browser = webdriver.Firefox(profile)
browser.implicitly_wait(10)
browser.get("file:///mnt/Ubuntu_Share/foxit.ofd.ocx/objectdemo_windows_time.html")

########数据库
status = 0;
cx1 = sqlite3.connect(dbpath)
cu1 = cx1.cursor()
cu1.execute("drop  table if exists RenderTime")
cu1.execute("CREATE TABLE  RenderTime"+" (filename TEXT,filepath,filefullpath,filesize,status,RenderTime);")
'''数据库操作，连接数据库'''
# 打开数据库
cx = sqlite3.connect(dbpath)
cu = cx.cursor()
cu.execute("select * from " + testfiledbtable)
print 'Test Start','Open the Performance Switch'
browser.find_element_by_id("Button_setPerformance_switch").send_keys(Keys.ENTER)
print box_width*'*'
for fileinfo in cu.fetchall():
    print box_width * '~'
    fileinfo1 = [fileinfo[0],fileinfo[1],fileinfo[2],fileinfo[3]]
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
    browser.find_element_by_id("Text11").clear()
    browser.find_element_by_id("Text11").clear()
    browser.find_element_by_id("Text_thisPageNo").clear()
    browser.find_element_by_id("Text_gotoPageNo").clear()
    browser.find_element_by_id("text_function").clear()
    browser.find_element_by_id("text_time").clear()

    print "File Dir:",fileinfo[1],fileinfo[0]

    # 输入要打开的文件的路径

    browser.find_element_by_id("Text10").send_keys(fileinfo[1])
    time.sleep(1)

    browser.find_element_by_id("Text11").send_keys(fileinfo[0])
    time.sleep(1)
    # 打开文档
    starttime = time.time()
    browser.find_element_by_id("button1").send_keys(Keys.ENTER)
    time.sleep(3)
    endtime =  time.time()
    print '%-*s%*dms' % (item_width-2,'Open The OFD Files TestTime:',digtal_width,(endtime - starttime)*1000)
    time.sleep(1)
    browser_open_file_time = browser.find_element_by_id("text_time").get_attribute("value")
    print '%-*s%*sms' % (item_width, 'Javascript Open OFD Files:',digtal_width, browser_open_file_time)
    # 获取文档数量
    browser.find_element_by_id("Button4").send_keys(Keys.ENTER)
    time.sleep(1)

    # 获取页面数量
    browser.find_element_by_id("Button5").send_keys(Keys.ENTER)
    time.sleep(1)

    #页面跳转性能测试
    page_max = browser.find_element_by_id("Text2").get_attribute("value")
    page_max = int(page_max)
    pageno_middle = (page_max +1)/2
    browser.find_element_by_id("Text_gotoPageNo").send_keys(pageno_middle)
    browser.find_element_by_id("text_function").clear()
    browser.find_element_by_id("text_time").clear()
    time.sleep(1)
    browser.find_element_by_id("Button_GotoPage").send_keys(Keys.ENTER)
    print "Button GotoPage:", pageno_middle
    sum_Time = prinf_functionTime(1)

    ######首页#####
    browser.find_element_by_id("text_function").clear()
    browser.find_element_by_id("text_time").clear()
    time.sleep(1)
    browser.find_element_by_id("Button_FirstPage").send_keys(Keys.ENTER)
    sum_Time = prinf_functionTime(1)

    ######下一页#####
    time_init()
    for i in range(1,page_max):
        browser.find_element_by_id("text_function").clear()
        browser.find_element_by_id("text_time").clear()
        time.sleep(1)
        browser.find_element_by_id("Button_NextPage").send_keys(Keys.ENTER)
        temp_Time = prinf_functionTime(i)
        sum_Time = sum_Time +temp_Time
        (max_Time, min_Time) = time_select(temp_Time, i, max_Time, min_Time)
    avg_Time = sum_Time / i
    print '%-*s%*.2fms' % (item_width, "#######Average Time:", digtal_width-20, avg_Time)
    print '%s%dms#%s%dms#%s%d######' % ("Max time of result list:", max_Time, "Min time of result list:", min_Time, "Total:", i)



    ######尾页#####
    browser.find_element_by_id("text_function").clear()
    browser.find_element_by_id("text_time").clear()
    time.sleep(1)
    browser.find_element_by_id("Button_LastPage").send_keys(Keys.ENTER)
    sum_Time = prinf_functionTime(1)

    ######上一页#####
    time_init()
    for i in range(1,page_max,1):
        browser.find_element_by_id("text_function").clear()
        browser.find_element_by_id("text_time").clear()
        time.sleep(1)
        browser.find_element_by_id("Button_PrevPage").send_keys(Keys.ENTER)
        temp_Time = prinf_functionTime(i)
        sum_Time = sum_Time + temp_Time

        (max_Time, min_Time) = time_select(temp_Time,i,max_Time,min_Time)
    avg_Time = sum_Time / i
    print '%-*s%*.2fms' % (item_width, "######Average Time:", digtal_width-20, avg_Time)
    print '%s%dms#%s%dms#%s%d######' % ("Max time of result list:", max_Time, "Min time os result list:", min_Time, "Total:", i)

browser.quit()
endtime = time.time()
totaltime = endtime - starttime
print 70*'*'
print '%-*s%*.2fs' % (item_width,'Test total time:',digtal_width,totaltime)
print 70*'*'
print 'Test end'