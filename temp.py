# TempConvert.py
val =input("Please input the temp with temprature symbol: ")
if val[-1] in ['C','c']:
    f = 1.8 * float(val[0:-1])+32
    print("The converted temorature is: %.2fF"%f)
elif val[-1] in ['F','f']:
    c = (float(val[0:-1])-32)/1.8
    print("The converted temprature is: %.2fC"%c)
else:
    print("wrong input")
