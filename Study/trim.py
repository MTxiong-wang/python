#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def trim(s):
    while s[:1]==' ':
        s=s[1:len(s)]
    while s[-1:]==' ':
        s=s[0:len(s)-1]
    return s

# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
    