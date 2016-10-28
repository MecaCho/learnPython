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
#from HTMLTestRunner import HTMLTestRunner
from addtestfile import *
box_width = 90
item_width = 50
digtal_width = box_width - item_width
# addTestfile
addtestfile()

# 读取渲染配置文件
#RenderConfig = open("C:\\fortofour\\RenderScript\\RenderConfig.xml", 'r')#Windows Test
RenderConfig = open("/mnt/Ubuntu_Share/fortofour/RenderScript/RenderConfig.xml", 'r')
RDOMTree = ET.parse(RenderConfig)
print RDOMTree
RData = RDOMTree.documentElement
print RData

address = RData.getElementsByTagName("address")[0]
#print address
address = address.childNodes[0].data
print address

RenderSavePath = RData.getElementsByTagName("RenderSavePath")[0]
RenderSavePath = RenderSavePath.childNodes[0].data

DPINum = RData.getElementsByTagName("DPINum")[0]
DPINum = DPINum.childNodes[0].data

# 加载ie驱动
#iedriver = "C:\Program Files (x86)\Internet Explorer\IEDriverServer.exe"
#os.environ["webdriver.ie.driver"] = iedriver
profile = webdriver.FirefoxProfile()
'''profile.set_preference("font.language.group","zh-CN")
profile.set_preference("intl.accept_languages","zh-CN,zh,en-us,en")
profile.set_preference("iextensions.installCache",'[{"name":"app-global","addons":{"{972ce4c6-7e08-4474-a285-3208198ce6fd}":{"descriptor":"/usr/lib/firefox/browser/extensions/{972ce4c6-7e08-4474-a285-3208198ce6fd}","mtime":1477462939000,"rdfTime":1403840949000}}},{"name":"app-system-user","addons":{"langpack-zh-CN@firefox.mozilla.org":{"descriptor":"/home/michael/.mozilla/extensions/{ec8030f7-c20a-464f-9b0e-13a3a9e97384}/langpack-zh-CN@firefox.mozilla.org.xpi","mtime":1403840979000}}}]')
profile.set_preference("extensions.bootstrappedAddons",'{"langpack-zh-CN@firefox.mozilla.org":{"version":"21.0","type":"locale","descriptor":"/home/michael/.mozilla/extensions/{ec8030f7-c20a-464f-9b0e-13a3a9e97384}/langpack-zh-CN@firefox.mozilla.org.xpi"}}')
'''
#profile.set_preference("iextensions.installCache",'[{"name":"app-global","addons":{"{972ce4c6-7e08-4474-a285-3208198ce6fd}":{"descriptor":"/usr/lib/firefox/browser/extensions/{972ce4c6-7e08-4474-a285-3208198ce6fd}","mtime":1477558056000,"rdfTime":1403840949000}}},{"name":"app-system-user","addons":{"langpack-zh-CN@firefox.mozilla.org":{"descriptor":"/home/test/.mozilla/extensions/{ec8030f7-c20a-464f-9b0e-13a3a9e97384}/langpack-zh-CN@firefox.mozilla.org.xpi","mtime":1403840979000}}},{"name":"app-profile","addons":{"{a6fd85ed-e919-4a43-a5af-8da18bda539f}":{"descriptor":"/home/test/.mozilla/firefox/tdxfogcg.default/extensions/{a6fd85ed-e919-4a43-a5af-8da18bda539f}.xpi","mtime":1477562685000}}}]')
#profile.set_preference("extensions.bootstrappedAddons",'{"langpack-zh-CN@firefox.mozilla.org":{"version":"21.0","type":"locale","descriptor":"/home/test/.mozilla/extensions/{ec8030f7-c20a-464f-9b0e-13a3a9e97384}/langpack-zh-CN@firefox.mozilla.org.xpi"}}')

browser = webdriver.Firefox(profile)
time.sleep(10)
browser.implicitly_wait(30)
browser.get("file:///mnt/Ubuntu_Share/foxit.ofd.ocx/objectdemo_windows.html") #通过配置文件读取
time.sleep(1)
nowhandle = browser.current_window_handle
time.sleep(1)

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
print 'Test Start'
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

    print fileinfo[0], fileinfo[1]

    # 输入要打开的文件的路径

    browser.find_element_by_id("Text10").send_keys(fileinfo[1])
    time.sleep(1)

    browser.find_element_by_id("Text11").send_keys(fileinfo[0])
    time.sleep(1)
    # 打开文档
    starttime = time.time()
    print '%-*s%*s' % (item_width,'Rend Test Start Time :',digtal_width,time.ctime(starttime))
    browser.find_element_by_xpath("/html/body/div[1]/input[3]").send_keys(Keys.ENTER)
    endtime =  time.time()
    print '%-*s%*.2fs' % (item_width,'Open The OFD Files TestTime:',digtal_width,(endtime - starttime))
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
    print 'flag'
    browser.find_element_by_id("Text7").send_keys(DPINum)
    time.sleep(2)
     
    fulldir = RenderSavePath + "/" + str1 + "/" + str2
    print '2'
    if os.path.exists(fulldir):
        # shutil.rmtree(fulldir)
        # os.makedirs(fulldir)
        browser.find_element_by_id("Text8").send_keys(fulldir)
    else:
        os.makedirs(fulldir)
        browser.find_element_by_id("Text8").send_keys(fulldir)
    print '3'
    # 如果计算时间则从该处开始计算
    RenderStart = time.time()
    RenderEnd = 0
    # 渲染全部页面2
    browser.find_element_by_id("Button8").send_keys(Keys.ENTER)
    time.sleep(2)
    print '4'
    flag = 0
    while 1:
        print flag
        flag += 1
        rdata = browser.find_element_by_id("Text9").get_attribute("value")
        print rdata
        time.sleep(2)
        if rdata != None and rdata == 'true':
            print "Render Success"
            status = "1"
            RenderEnd = time.time()-4
            # 关闭文档
            browser.find_element_by_xpath("/html/body/div[1]/input[4]").send_keys(Keys.ENTER)
            time.sleep(2)
            break
        elif rdata!= None and rdata != "true":
            status = "0"
            RenderEnd = time.time()-4
            print "Render Fail"
            RenderEnd = time.time()
            break
        else:
            continue
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
exit(1)

