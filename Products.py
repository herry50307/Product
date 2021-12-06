# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 16:14:24 2021

@author: DSC Handsome
"""


import os # os系統

Products=[]
if os.path.isfile('products.txt'):  #檢查檔案在不在
    print ("找到檔案")
    
#讀取檔案
    with open('products.txt','r', encoding='utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue   #
                name,price = line.strip().split(',')        #strip為去除換行符號，split用逗號分割
                Products.append([name,price])
    print(Products)
        
    
else:
     print("找不到檔案....")
     
#讓使用者輸入
while True:
    name = input('請輸入商品名稱')
    if name == 'q':
        break
    price = input('請輸入商品價格')
    
    p=[name,price]
    Products.append(p)
    
#印出商品價格
for p in Products:
    print(p[0], '的價格是', p[1])
    
#將商品資訊寫入檔案
with open('products.txt','w', encoding='utf-8') as f:
    f.write('商品,價格 \n')
    for p in Products:
        f.write(p[0] +',' + p[1] + '\n')
        
print(Products)
print(Products[0])