#!/usr/bin/env python3
# coding=utf-8


from datetime import datetime

with open('Test1.xls', 'a') as f:
    f.write('今天是 ')
    f.write(datetime.now().strftime('%Y-%m-%d'))

with open('Test1.xls', 'r') as f:
    s = f.read()
    print('open for read...')
    print(s)

with open('Test1.xls', 'rb') as f:
    s = f.read()
    print('open as binary for read...')
print(s)