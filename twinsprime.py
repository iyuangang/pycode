#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 输出 2 到 100 简的质数
prime = []
for num in range(2,10000):  # 迭代 2 到 100 之间的数字
   for i in range(2,num): # 根据因子迭代
      if num%i == 0:      # 确定第一个因子
         break            # 跳出当前循环
   else:                  # 循环的 else 部分
      prime.append(num)
# print prime
# print '\n'
m = len(prime)
# print m, '\n'
j = 1
k = 2
while k < m: 
    if prime[k] - prime[j] == 2:
        print prime[j], '&', prime[k], ' ',
    k+=1
    j+=1
