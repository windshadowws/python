# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 21:41:15 2021

@author: USER
"""

#20210224作業

# 1.輸入迴圈次數,判斷那些數值是奇數,哪些是偶數
num = int(input('請輸入數字:'))
if num % 2 == 0 :
    print(num,"是偶數")
else:
    print(num,"是奇數")

# 2.輸入迴圈次數,計算數值中為偶數的總和,最後印出加總的值

k = 0
for i in range(2,10,2):
    k += i
    print(i)
print("偶數合:",k)
