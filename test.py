a = {i:i+i for i in range(4)}
b = {i:j for i,j in zip(range(1,6),'abcde')}
c = {i:j.upper() for i,j in zip(range(1,6),'abdce')}
print(a)
print(b)
print(c)
