#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#尾递归优化
#尾递归是指，在函数返回的时候，调用自身本身，
#并且，return语句不能包含表达式。
#这样，编译器或者解释器就可以把尾递归做优化，
#使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。

""" def fact(n):
    if n==1:
        return 1
    else:
        return n * fact(n-1)

x = input('x:')
xx = int(x)
print(fact(xx))


def fact(n):
    return fact_iter(n,1)

def fact_iter(num,product):
    if num == 1:
        return product
    return fact_iter(num - 1,num*product)

x = int(input('x:'))
print(fact(x)) """

#汉诺塔
def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    #n＞1,视为1个最大的圆盘和剩余n-1个圆盘当一个整体移动,
    #那n-1个移到b,最大那个移到c,即可实现递归
    else:
        move(n-1,a,c,b)
        #n-1个以整体移到b
        print(a,'-->',c)
        #剩下那个最大的移到c
        move(n-1,b,a,c)
        #n-1个变成新的问题:如何将n-1个从b移到c.(递归即可)

move(10, 'A', 'B', 'C')