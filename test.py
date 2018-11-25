def func(x):
    print('x is',x)#这里的x是func(x)里的变量，是局部变量
    x = 2
    print('changed local x to',x)

x=50
func(x)
print('x is still',x)

def func():
    global x#x被global语句定义为全局变量

    print('x is',x)
    x = 2
    print('changed local x to',x)

x=50
func()
print('value of x is',x)
#你可以使用同一个global语句指定多个全局变量。例如global x, y, z。
