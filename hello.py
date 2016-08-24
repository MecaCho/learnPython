#!/usr/bin/python
# -*- coding: UTF-8 -*-
print 'Hello World!'
str1=raw_input()
print len(str1.split()[-1])



'''
import sys
ds = sys.stdin.readline().split()
print len(ds)
print len(ds[len(ds) - 1])
'''
'''
str1= raw_input()
str2= raw_input()
def print_line(str):
   n=len(str)
   if n%8 != 0:
    str=str.ljust((n/8+1)*8,'0')
   for i in range(0,len(str)/8):
      print str[i*8:i*8+8]
print_line(str1)
print_line(str2)
'''

'''
n1=len(str1=raw_input())
n1=(n1/9+1)*9
n2=len(str2=raw_input())
n2=(n2/9+1)*9
for i in range(1,n1):
	print str1[i-1];
for i in range(1,n2):
	print str2[i-1];
   '''



'''
str=raw_input()
str1=str.lower()
substr=raw_input()
substr1=substr.lower()
print str1.count(substr1)


data=raw_input("") 
ch=raw_input("").strip() 
num=data.count(ch)
print num 
'''




'''
str=raw_input()
n=len(str)
print n
substr=' '
print str.rfind(substr)
i=str.rfind(substr,0,n)
print n-i-1
print 'line\nline\nline'
'''




'''
str = "this is hello world";
substr = " ";
n=len(str)
print n

print str.rfind(substr);
print str.rfind(substr, 0, n);
print str.rfind(substr, -1, 0);

print str.find(substr);
print str.find(substr, 0, 10);
print str.find(substr, 6, 0);
'''
