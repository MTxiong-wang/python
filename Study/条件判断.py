#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" print('Please Enter Your Age:')
s = input()
age = int(s)
if age >= 18 :
    print('your age is:',age)
    print('adult')

elif age >= 6:
    print('your age is:',age)
    print('teenager')
else:
    print('your age is:',age)
    print('kid') """

h = input('Please Enter Your Height:')
w = input('Please Enter Your Weight:')
height = float(h)
weight = float(w)
bmi = weight/height/height
if bmi >= 32:
    print('BMI高于32：严重肥胖')
elif bmi >= 28:
    print('BMI 28-32：肥胖')
elif bmi >= 25:
    print('BMI 25-28：过重')
elif bmi >= 18.5:
    print('BMI 18.5-25：正常')
else:
    print('BMI低于18.5：过轻')