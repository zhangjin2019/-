# -*- coding: utf-8 -*-
"""
Created on Friday January 4th 18:01:29 2019

@author: zhj
"""

import random
from fractions import Fraction

def newint():
    sign = ['+','-','x','/']
    num = random.randint(0,3)
    n1 = random.randint(1,20)
    n2 = random.randint(1,20)
    if num == 0:
        ans = n1 + n2
    elif num == 1:
        n1,n2 = max(n1,n2),min(n1,n2)
        ans = n1 - n2
    elif num == 2:
        ans = n1 * n2
    elif num == 3:
        while n1 % n2 != 0:
            n1 = random.randint(1,20)
            n2 = random.randint(1,20)
            n1,n2 = max(n1,n2),min(n1,n2)
        ans = n1 / n2
    print(n1,sign[num],n2,'=')
    return ans
    

def newfra():
    sign = ['+','-','x','/']
    num = random.randint(0,3)
    n1 = random.randint(1,20)
    n2 = random.randint(1,20)
    t1 = Fraction(n1,n2)
    n1 = random.randint(1,20)
    n2 = random.randint(1,20)
    t2 = Fraction(n1,n2)
    if num == 0:
        ans = t1 + t2
    elif num == 1:
        ans = t1 - t2
    elif num == 2:
        ans = t1 * t2
    elif num == 3:
        ans = t1 / t2
    print(t1,sign[num],t2,'=')
    return ans
    
def creat():
    n = int(input('请输入您要创建的题目数量：'))
    ans = []
    m = 0
    while m <= n-1:
        num = random.randint(0,2)
        if num == 0:
            print(m+1,'、')
            ans.append(newfra())
        else:
            print(m+1,'、')
            ans.append(newint())
        m += 1
    m = 0
    print('答案为：')
    while m <= n-1:
        print(m+1,'、',ans[m])
        m +=1


n = input('选择模式\n1、四则运算\n2、生成题库\n（任意时候输入q退出）:')
m = int(n)
if m == 1:
    while True:
        num = random.randint(0,2)
        if num == 0:
            ans = newfra()
            current = input()
            if current == 'q' or current == 'Q':
                break
            if int(current) == ans:
                print('回答正确！')
            else:
                print('回答错误，正确答案是：',ans)
        else:
            ans = newint()
            current = input()
            if current == 'q' or current == 'Q':
                break
            if int(current) == ans:
                print('回答正确！')
            else:
                print('回答错误，正确答案是：',ans)
elif m == 2:
    creat()
else:
    print('没有您的选择，请重新输入！')
    
    
    
    
    
    
    
    
    
    