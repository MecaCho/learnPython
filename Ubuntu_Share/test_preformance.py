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
from selenium.common.exceptions import NoSuchAttributeException
#class Preformance(object):
#    def test_pre(self):
item_width   = 70
digtal_width = 30
addtestfile()

##########################独立测试用##################################
#读取文件
RenderConfig = open("/mnt/Ubuntu_Share/fortofour/RenderScript/RenderConfig.xml", 'r')
RDOMTree = ET.parse(RenderConfig)
RData = RDOMTree.documentElement

address = RData.getElementsByTagName("address")[0]
address = address.childNodes[0].data

#加载webdriver
profile = webdriver.FirefoxProfile()
profile.set_preference("font.language.group","zh-CN")
profile.set_preference("intl.accept_languages","zh-cn,zh,en-us,en")
profile.set_preference("iextensions.installCache",'[{"name":"app-global","addons":{"{972ce4c6-7e08-4474-a285-3208198ce6fd}":{"descriptor":"/opt/firefox/browser/extensions/{972ce4c6-7e08-4474-a285-3208198ce6fd}","mtime":1478142520000,"rdfTime":1478142520000}}},{"name":"app-system-user","addons":{"langpack-zh-CN@firefox.mozilla.org.xpi":{"descriptor":"/home/qwq/.mozilla/extensions/{ec8030f7-c20a-464f-9b0e-13a3a9e97384}/langpack-zh-CN@firefox.mozilla.org.xpi","mtime":0}}}]')
profile.set_preference("extensions.xpiState",'{"app-system-user":{"langpack-zh-CN@firefox.mozilla.org":{"d":"/home/qwq/.mozilla/extensions/{ec8030f7-c20a-464f-9b0e-13a3a9e97384}/langpack-zh-CN@firefox.mozilla.org.xpi","e":true,"v":"35.0","st":1429772456000}},"app-global":{"{972ce4c6-7e08-4474-a285-3208198ce6fd}":{"d":"/usr/lib/firefox/browser/extensions/{972ce4c6-7e08-4474-a285-3208198ce6fd}","e":true,"v":"35.0","st":1430102102000,"mt":1429771865000}}}')
profile.set_preference("general.useragent.locale","zh-CN")
browser = webdriver.Firefox(profile)
browser.implicitly_wait(10)
browser.get("file:///mnt/Ubuntu_Share/foxit.ofd.ocx/objectdemo_windows_time.html") #通过配置文件读取
nowhandle = browser.current_window_handle

#数据库
status = 0;
cx1 = sqlite3.connect(dbpath)
cu1 = cx1.cursor()
cu1.execute("drop  table if exists RenderTime")
cu1.execute("CREATE TABLE RenderTime"+" (filename TEXT,filepath,filefullpath,filesize,status,RenderTime);")

cx = sqlite3.connect(dbpath)
cu = cx.cursor()
cu.execute("select * from " + testfiledbtable)
for fileinfo in cu.fetchall():

    fileinfo1 = [fileinfo[0],fileinfo[1],fileinfo[2],fileinfo[3]]
    print fileinfo
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
    browser.find_element_by_id("Text_thisPageNo").clear()
    browser.find_element_by_id("Text_gotoPageNo").clear()
    browser.find_element_by_id("text_function").clear()
    browser.find_element_by_id("text_time").clear()

    print fileinfo[0], fileinfo[1]

    # 输入要打开的文件的路径

    browser.find_element_by_id("Text10").send_keys(fileinfo[1])
    time.sleep(1)

    browser.find_element_by_id("Text11").send_keys(fileinfo[0])
    time.sleep(1)
    #################################################性能测试###################################################
    browser.find_element_by_id("Button_setPerformance_switch").send_keys(Keys.ENTER)

    ######打开文档
    browser.find_element_by_id("button1").send_keys(Keys.ENTER)
    browser.implicitly_wait(10)
    try:
        print(time.ctime())
        browser_pre_function = browser.find_element_by_id("text_function").get_attribute("value")
        browser_open_file_time = browser.find_element_by_id("text_time").get_attribute("value")
        print '%-*s%*sms' % (item_width - 2, browser_pre_function, digtal_width, browser_open_file_time)
    except NoSuchAttributeException as e:
        print(e)

    # 获取页面数量
    browser.find_element_by_id("Button5").send_keys(Keys.ENTER)

    #随机选取页码
    browser.implicitly_wait(10)
    page_max = browser.find_element_by_id("Text2").get_attribute("value")
    pageno_middle = (int(page_max)+1)/2

    #跳转到指定页面
    browser.find_element_by_id("Text_gotoPageNo").send_keys(pageno_middle)
    print "Goto Page: ",pageno_middle
    time.sleep(3)
    browser.find_element_by_id("Button_GotoPage").send_keys(Keys.ENTER)
    browser.implicitly_wait(10)
    browser_pre_function = browser.find_element_by_id("text_function").get_attribute("value")
    browser_open_file_time = browser.find_element_by_id("text_time").get_attribute("value")
    print '%-*s%*sms' % (item_width - 2, browser_pre_function, digtal_width, browser_open_file_time)

    #############################################Test End#######################################################
    browser.quit()
    print 'Preformance Test End'
