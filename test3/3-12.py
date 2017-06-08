#!/usr/bin/env python3
# coding=utf-8
import xlrd,logging,urllib,urllib2,json,sys

data = xlrd.open_workbook('C:\Users\chenzhixiang\Desktop\est.xlsx')#打开excel表格
print logging.info("打开%s excel表格成功"%data)
table = data.sheet_by_name(u'Sheet1')#打开工作表sheet2
print logging.info("打开%s表成功"%table)
nrows = table.nrows#统计行数
print logging.info("表中有%s行"%nrows)
ncols = table.ncols#统计列数
print logging.info("表中有%s列"%ncols)
print logging.info("开始进行循环")
name_1=[];url_1=[];params_1=[];type_1=[];Expected_result_1=[];Actual_result_1 =[];test_result_1=[];Remarks_1=[]#定义数组
Success=0;fail=0