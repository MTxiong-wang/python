#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
def quadratic(a,b,c):
    x1 = (-b + math.sqrt(b*b-4*a*c))/2/a
    x2 = (-b - math.sqrt(b*b-4*a*c))/2/a
    return x1,x2

""" a = int(input('a:'))
b = int(input('b:'))
c = int(input('c:'))

x = quadratic(a,b,c)
print(x) """

# 测试:
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')