# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 16:14:24 2021

@author: DSC Handsome
"""



Products=[]
while True:
    name = input('請輸入商品名稱')
    if name == 'q':
        break
    price = input('請輸入商品價格')
    
    p=[name,price]
    Products.append(p)
    
print(Products)
print(Products[0])