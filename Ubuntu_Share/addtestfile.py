#-*-coding=utf-8-*-
import os
import os.path
import xml.dom.minidom as ET
import time
import sqlite3


'''读取测试文件配置'''
#testfile = open("C:\\fortofour\\RenderScript\\testfile.xml",'r')
testfile = open("/mnt/Ubuntu_Share/fortofour/RenderScript/testfile.xml",'r')
TDOMTree = ET.parse(testfile)
TData = TDOMTree.documentElement

#测试文件根目录
testfiledir = TData.getElementsByTagName("testfiledir")[0]
testfiledir = testfiledir.childNodes[0].data
#print testfiledir

#文件数据库名称
dbpath = TData.getElementsByTagName("dbpath")[0]
dbpath = dbpath.childNodes[0].data
#print testfiledbname

#文件类型筛选
filefilter = TData.getElementsByTagName("filefilter")[0]
filefilter = filefilter.childNodes[0].data
#print filefilter

#md5
filemd5check = TData.getElementsByTagName("filemd5check")[0]
filemd5check = filemd5check.childNodes[0].data
#print filemd5check

#testfiledbtable
testfiledbtable = TData.getElementsByTagName("testfiledbtable")[0]
testfiledbtable =testfiledbtable.childNodes[0].data
#print testfiledbtable

def addtestfile():


    '''数据库操作，连接数据库生成测试文档表格'''
    #打开数据库
    cx = sqlite3.connect(dbpath)
    cu = cx.cursor()
    cu.execute("drop  table if exists "+ testfiledbtable)
    #创建数据库中的表格
    cu.execute("CREATE TABLE  "+testfiledbtable+" (filename TEXT,filepath,filefullpath,filesize);")

    for parent,dirnames,filenames in os.walk(testfiledir):
        for filename in filenames:
            print '-'*90
            print "Filename is :"+filename
            print '_'*90
            #print "parent is :"+ parent
            fullpath = os.path.join(parent,filename)
           #print("the full name of the file is :"+ fullpath)#输出文件路径信息
            filesize = os.path.getsize(os.path.join(parent,filename))
            #print filesize/1024
            FileInfo = [filename,parent,fullpath,filesize/1024]

            #判断文件是否是ofd文件，如果是则插入数据库
            flist = filename.split('.')
            if flist[-1]=="ofd":
                cu.execute("INSERT INTO "+ testfiledbtable +" VALUES(?,?,?,?)",FileInfo)
                cx.commit()
            else:
                print filename +" is not ofd"          
            
    cx.close()
