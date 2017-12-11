#!/usr/bin/python
# coding:utf-8

a = []
for i in range(10):
    a.append(input("entert the num:"))
print a

for i in range(9):
    for j in range(i+1,10):
        if a[i] > a[j]:
            a[i],a[j] = a[j],a[i]
print a
