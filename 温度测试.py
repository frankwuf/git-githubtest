#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 26 12:10:15 2019

@author: frankfwu
"""

#TempConvert.py
TempStr = input("请输入带有符合的温度值：")
if TempStr[-1] in ["F","f"]:
    C = (eval(TempStr[0:-1])-32)/1.8
    print("转换后的温度是{:.2f}C".format(C))
elif TempStr[-1] in ["C","c"]:
    F = 1.8*eval(TempStr[0:-1])+32
    print("转换后的温度是{:.2f}F".format(F))
else:
    print("输入格式错误")