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
from selenium.common.exceptions import NoSuchAttributeException
from addtestfile import *
'''RenderImage'''
def prinf_functionTime():
    #browser.switch_to_alert().accept()
    #browser.switch_to_alert().accept()
    browser.implicitly_wait(10)
    try:
        result_function = browser.find_element_by_id("text_function").get_attribute("value")
        result_time = browser.find_element_by_id("text_time").get_attribute("value")
    except NoSuchAttributeException as e:
        print(e)
    finally:
        print '%-*s%*s' % (item_width, result_function,digtal_width, result_time)
        print '-'*box_width

box_width = 70
item_width = 30
digtal_width = box_width - item_width
# addTestfile
addtestfile()
# 读取渲染配置文件
#RenderConfig = open("C:\\fortofour\\RenderScript\\RenderConfig.xml", 'r')#Windows Test
RenderConfig = open("/mnt/Ubuntu_Share/fortofour/RenderScript/RenderConfig.xml", 'r')
RDOMTree = ET.parse(RenderConfig)
print 'RDOMTree:',RDOMTree
RData = RDOMTree.documentElement
print 'RDate:',RData

address = RData.getElementsByTagName("address")[0]
#print address
address = address.childNodes[0].data
print 'address:',address

RenderSavePath = RData.getElementsByTagName("RenderSavePath")[0]
RenderSavePath = RenderSavePath.childNodes[0].data

DPINum = RData.getElementsByTagName("DPINum")[0]
# 加载ie驱动
profile = webdriver.FirefoxProfile()
profile.set_preference("font.language.group","zh-CN")
profile.set_preference("intl.accept_languages","zh-cn,zh,en-us,en")
profile.set_preference("iextensions.installCache",'[{"name":"app-global","addons":{"{972ce4c6-7e08-4474-a285-3208198ce6fd}":{"descriptor":"/opt/firefox/browser/extensions/{972ce4c6-7e08-4474-a285-3208198ce6fd}","mtime":1478142520000,"rdfTime":1478142520000}}},{"name":"app-system-user","addons":{"langpack-zh-CN@firefox.mozilla.org.xpi":{"descriptor":"/home/qwq/.mozilla/extensions/{ec8030f7-c20a-464f-9b0e-13a3a9e97384}/langpack-zh-CN@firefox.mozilla.org.xpi","mtime":0}}}]')
profile.set_preference("extensions.xpiState",'{"app-system-user":{"langpack-zh-CN@firefox.mozilla.org.xpi":{"d":"/root/.mozilla/extensions/{ec8030f7-c20a-464f-9b0e-13a3a9e97384}/langpack-zh-CN@firefox.mozilla.org.xpi","st":0}},"app-global":{"{972ce4c6-7e08-4474-a285-3208198ce6fd}":{"d":"/opt/firefox-35/browser/extensions/{972ce4c6-7e08-4474-a285-3208198ce6fd}","e":true,"v":"35.0","st":1478248992000,"mt":1478248992000}}}')
#profile.set_preference("general.useragent.locale","zh-CN")
#"/usr/lib/mozilla/plugins/libfoxitofficesuite.so"
browser = webdriver.Firefox(profile)
browser.implicitly_wait(10)
browser.get("file:///mnt/Ubuntu_Share/foxit.ofd.ocx/objectdemo_windows_time.html") #通过配置文件读取
nowhandle = browser.current_window_handle

#####刷新浏览器
time.sleep(3)
browser.refresh()
print "refresh"
time.sleep(3)

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
    #browser.find_element_by_id("text_function").clear()
    #browser.find_element_by_id("text_time").clear()

    print fileinfo[0], fileinfo[1]

    # 输入要打开的文件的路径

    browser.find_element_by_id("Text10").send_keys(fileinfo[1])
    time.sleep(1)

    browser.find_element_by_id("Text11").send_keys(fileinfo[0])
    time.sleep(1)
    # 打开文档
    starttime = time.time()
    browser.find_element_by_id("button1").send_keys(Keys.ENTER)
    time.sleep(3)
    #browser.switch_to_alert().accept()
    #browser.switch_to_alert().accept()
    endtime =  time.time()
    print '%-*s%*dms' % (item_width-2,'Open The OFD Files TestTime:',digtal_width,(endtime - starttime)*1000)
    time.sleep(3)
    browser_open_file_time = browser.find_element_by_id("text_time").get_attribute("value")
    print '%-*s%*s' % (item_width, 'Javascript Open OFD Files:',digtal_width, browser_open_file_time)
    # 获取文档数量
    browser.find_element_by_id("Button4").send_keys(Keys.ENTER)
    time.sleep(1)

    # 获取页面数量
    browser.find_element_by_id("Button5").send_keys(Keys.ENTER)
    time.sleep(1)

    #页面跳转性能测试
    page_max = browser.find_element_by_id("Text2").get_attribute("value")
    page_max = int(page_max)
    #time.sleep(10)
    pageno_middle = (page_max +1)/2
    browser.find_element_by_id("Text_gotoPageNo").send_keys(pageno_middle)
    #browser.find_element_by_id("text_function").clear()
    #browser.find_element_by_id("text_time").clear()
    time.sleep(1)
    browser.find_element_by_id("Button_GotoPage").send_keys(Keys.ENTER)
    print "Button GotoPage:", pageno_middle
    time.sleep(1)
    prinf_functionTime()

    ######首页#####
    #browser.find_element_by_id("text_function").clear()
    #browser.find_element_by_id("text_time").clear()
    time.sleep(1)
    browser.find_element_by_id("Button_FirstPage").send_keys(Keys.ENTER)
    prinf_functionTime()

    ######下一页#####
    for i in range(1,page_max):
        #browser.find_element_by_id("text_function").clear()
        #browser.find_element_by_id("text_time").clear()
        time.sleep(1)
        browser.find_element_by_id("Button_NextPage").send_keys(Keys.ENTER)
        prinf_functionTime()



    ######尾页#####
    #browser.find_element_by_id("text_function").clear()
    #browser.find_element_by_id("text_time").clear()
    time.sleep(1)
    browser.find_element_by_id("Button_LastPage").send_keys(Keys.ENTER)
    prinf_functionTime()

    ######上一页#####
    for i in range(1,page_max):
        #browser.find_element_by_id("text_function").clear()
        #browser.find_element_by_id("text_time").clear()
        time.sleep(1)
        browser.find_element_by_id("Button_PrevPage").send_keys(Keys.ENTER)
        time.sleep(2)
        prinf_functionTime()

browser.quit()
endtime = time.time()
totaltime = endtime - starttime
print 70*'*'
print '%-*s%*.2fs' % (item_width,'Test total time:',digtal_width,totaltime)
print 70*'*'
print 'Test end'