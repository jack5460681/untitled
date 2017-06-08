#!/usr/bin/python#
#-*- coding: UTF-8 -*-
# 基础包：接口测试的封装

import requests
import LOG as log
import gl
import excel
logging = log.getLogger()

def api_test(method, url, data ,headers):

    # 定义一个请求接口的方法和需要的参数
    # :Args:
    # method  - 企业名称 str
    # url - 用户昵称 str
    # data - 参数 str
    # headers - 请求头信息 dict
    # 非RESTful API请求另外的请求类型实际用不到。也不安全。

      try:
          if method == "post":
             results = requests.post(url, data, headers=headers)
          if method == "get":
             results = requests.get(url, data, headers=headers)
          # if method == "put":
          #     results = requests.put(url, data, headers=headers)
          # if method == "delete":
          #     results = requests.delete(url, headers=headers)
          # if method == "patch":
          #     results == requests.patch(url, data, headers=headers)
          # if method == "options":
          #     results == requests.options(url, headers=headers)
           response = results.json()
          code = response.get("code")
          return code
      except Exception, e:
             logging.error("service is error", e)

def run_test(sheet):
    #
    # 定义一个执行和断言的方法
    # :Args:
    # sheet  - 服务名称 str（excel页脚名称识别的）

    rows = excel.get_rows(sheet)
    fail = 0
    for i in range(2, rows):
        # 这里为什么从第二行开始跑，因为会先执行SQL进行数据准备如之前Excel展示的空白位置
        testData = excel.get_content(sheet, i, gl.CASE_DATA)
        testUrl = excel.get_content(sheet, i, gl.CASE_URL)
        testMethod = excel.get_content(sheet, i, gl.CASE_METHOD)
        testHeaders = eval(excel.get_content(sheet, i, gl.CASE_HEADERS))
        testCode = excel.get_content(sheet, i, gl.CASE_CODE)
        actualCode = requests.api(testMethod, testUrl, testData, testHeaders)
        expectCode = str(int(testCode))
        failResults = ' url: ' + testUrl + ' params: ' + testData + ' actualCode: ' +     actualCode + ' expectCode: ' + expectCode
        if actualCode == expectCode:
            logging.info("pass")
        elif actualCode != expectCode:
            logging.info("fail %s", failResults)
            fail += 1
    if fail > 0 :
        return False
    return True