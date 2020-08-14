# -*- encoding: utf-8 -*-
'''
@File    : test.py
@Author  : vgzx
@Date    : 2020/08/13 22:37
@Contact : viewgrand@163.com
@Desc    :

'''
import xlrd
import os
import sys
from openpyxl import load_workbook


#读取excel文件
def excel():
    wb = xlrd.open_workbook(sys.path+'/doc/dev_log.xlsx')       # 打开Excel文件
    sheet = wb.sheet_by_name('Sheet1')                  #通过excel表格名称获取工作表
    datalist = []  #创建空list
    for a in range(1, sheet.nrows):  #循环读取表格内容（每次读取一行数据）
        cells = sheet.row_values(a)  # 每行数据赋值给cells
        print(type(cells), cells)
        # 根据sheet.cell[x][y].ctype 来具体转换
        # ctype： 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error     number 都是 浮点型

# excel()

print(sys.path)

# exel = load_workbook("D:/code/git/stax_blog/doc/dev_log.xlsx")
