# !/usr/bin/python
# -*- coding: UTF-8 -*-
# 基础包：excel的封装

import xlrd

workbook = None

def open_excel(path):
   #打开excel
      global workbook
      if (workbook == None):
          workbook = xlrd.open_workbook(path, on_demand=True)

def get_sheet(sheetName):
     #获取行号
      global workbook
      return workbook.sheet_by_name(sheetName)

def get_rows(sheet):
    #获取行号
      return sheet.nrows

def get_content(sheet, row, col):
    #获取表格中内容
       return sheet.cell(row, col).value

def release(path):
    #释放excel减少内存
      global workbook
      workbook.release_resources()
      del workbook