# pi.py
from random import random
from math import sqrt
from time import clock
DARTS = 100000000
hits = 0
j =0
clock()
for i in range(1,DARTS):
    x, y = random(), random()
    dist = sqrt(x**2+y**2)
    if dist<=1.0:
        hits += 1
        j += 1
    if j==1000000:
        j=0
        t=4*hits/i
        print("Pi now is: %s" %t) 
pi = 4 * (hits/DARTS)
print("Pi equals to: %s" %pi)
print("program run time is %-5.5ss" % clock())
