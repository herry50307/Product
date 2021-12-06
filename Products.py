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
    
for p in Products:
    print(p[0], '的價格是', p[1])
    
with open('products.csv','w') as f:
    for p in Products:
        f.write(p[0] +',' + p[1] + '\n')
        
print(Products)
print(Products[0])