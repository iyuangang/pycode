prime = []
for num in range(2,100):
    for i in range(2,num):
        if num%1 == 0:
            break
        else:
           prime.append(num)
print(prime)
