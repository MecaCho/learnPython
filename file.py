#coding=utf-8
#coding=gbk
import xlrd 
import re
from datetime import datetime


file = xlrd.open_workbook('test.xlsx')
f = open('test.txt','w')
table = file.sheets()[0]

nrows = table.nrows
ncols = table.ncols

for i in range(nrows):
    s = table.row_values(i)
	print(s)
    f.write('s')
    print table.row_values(i)
	


print nrows,ncols


#table.row_values(i)
#table.col_values(i)

#def excel_table_byindex(file,a=0,b=0)



'''
with open('test.xlsx','w') as f:
		f.write('today is \n')
	
		f.write(datetime.now().strftime('%Y-%m-%d'))
		

		
with open('test.xlsx','r') as f:
	  s = f.read()
	  print('open for read...')
	  print(s)
	  '''

	  
#print