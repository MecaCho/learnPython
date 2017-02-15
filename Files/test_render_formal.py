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
class Render(unittest.TestCase):
    '''Linux Render Test'''
    def test_Render(self):
        '''RenderImage'''
        box_width = 70
        item_width = 40
        digtal_width = box_width - item_width
        # addTestfile
        addtestfile()
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
        browser.get("file:///mnt/Ubuntu_Share/foxit.ofd.ocx/objectdemo_linux_new.html")

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
            #print '%-*s%*s' % (item_width,'Rend Test Start Time :',digtal_width,time.ctime(starttime))
            browser.find_element_by_xpath("/html/body/div[1]/input[3]").send_keys(Keys.ENTER)
            #print '%-*s%*.2fs' % (item_width,'Open The OFD Files TestTime:',digtal_width,(endtime - starttime))
            time.sleep(2)
            # 获取文档数量
            browser.find_element_by_id("Button4").send_keys(Keys.ENTER)
            time.sleep(1)

            # 获取页面数量
            browser.find_element_by_id("Button5").send_keys(Keys.ENTER)
            time.sleep(1)

            # 设置图片存放路径【通过配置文件读取】
            str1 = fileinfo[0][:-4]
            print '%-*s%*s'% (item_width,"Source File:",digtal_width,str1)
            str2 = str1 + "_" + time.strftime('%Y-%m-%d-%H-%M-%S-%M', time.localtime(time.time()))
            print '%-*s%*s'% (item_width,'Render File:',digtal_width,str2)

            # 设置要渲染图片的DPI【通过配置文件读取】
            DPINum = 144
            browser.find_element_by_id("Text7").send_keys(DPINum)
            time.sleep(2)

            fulldir = RenderSavePath + "/" + str1 + "/" + str2
            #print 'RenderSavePath:',fulldir
            if os.path.exists(fulldir):
                browser.find_element_by_id("Text8").send_keys(fulldir)
            else:
                os.makedirs(fulldir)
                browser.find_element_by_id("Text8").send_keys(fulldir)
            print 'RenderSavePath Success'
            # 如果计算时间则从该处开始计算
            RenderStart = time.time()
            RenderEnd = 0
            # 渲染全部页面2
            browser.find_element_by_id("Button8").send_keys(Keys.ENTER)
            time.sleep(2)
            flag = 0
            while 1:
                '''print flag
                flag += 1'''
                rdata = browser.find_element_by_id("Text9").get_attribute("value")
                print 'Render result rdate:',rdata
                time.sleep(2)
                if rdata != None and rdata == '0':
                    print "Render Success"
                    status = "1"
                    RenderEnd = time.time()-4
                    # 关闭文档
                    browser.find_element_by_xpath("/html/body/div[1]/input[4]").send_keys(Keys.ENTER)
                    time.sleep(2)
                    break
                elif rdata!= None and rdata != '0':
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
        print '%-*s%*.2fs' % (item_width,'Test total time:',digtal_width,totaltime)
        print 90*'*'
        print 'Test end'



