# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 16:14:24 2021

@author: DSC Handsome
"""
import os # os系統

#讀取檔案

def read_file(filename):
    products=[]
    with open(filename,'r', encoding='utf-8') as f:
        for line in f:
            if '商品,價格' in line:  #把商品及價格這一欄不要顯示出來，跳過此次迴圈
                continue   #
            name,price = line.strip().split(',')        #strip為去除換行符號，split用逗號分割
            products.append([name,price])
    return products

#讓使用者輸入
def usr_input(products):
    while True:
        name = input('請輸入商品名稱：')
        if name == 'q':
            break
        price = input('請輸入商品價格：')
        price = int(price)
        products.append([name,price])
    print(products)
    return products
    
#印出商品價格
def print_products(products):
    for p in products:
        print(p[0], '的價格是', p[1])
    
#將商品資訊寫入檔案
def wirte_file(filename,products):
    with open(filename,'w', encoding='utf-8') as f:
        f.write('商品,價格 \n')
        for p in products:
            f.write(p[0] +',' + str (p[1]) + '\n')
            
            
def main():
    filename = 'products.txt'
    if os.path.isfile(filename):  #檢查檔案在不在
        print ("找到檔案了!!")
        products = read_file(filename)
        print(products)
    else:
        print("找不到檔案....")
        
    products = usr_input(products)
    print_products(products)
    wirte_file('products.txt',products)

main()



