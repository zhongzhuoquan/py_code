# -*- coding:utf-8 -*-
#读取xls文件,一定要把xlsx后缀改成xls
import xlrd
file_name = xlrd.open_workbook('G:\\info.xls')#得到文件
table =file_name.sheets()[0]#得到sheet页
nrows = table.nrows #总行数
ncols = table.ncols #总列数
i = 0
while i < nrows:
    cell = table.row_values(i)[1] #得到数字列数据
    username=table.row_values(i)[0]
    print()
    i=i+1