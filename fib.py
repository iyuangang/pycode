#coding:utf-8

def fib(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a,b = b,a+b
        n += 1
max = int(input('input max num: '))
for n in fib(max):
    print(n)
