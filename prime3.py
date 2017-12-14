import math

def prime(start,end):
    count=0
    for i in range(start,end+1):
        if(i%2 == 0 and i != 2):
            continue
        for j in range(2,int(math.sqrt(i))+1):
            if(i%j==0):
                break
        else:
            count=count+1
            print(i)
    print("")
    print('count',count)
    return

start=int(input("start:\n"))
end=int(input("end:\n"))
prime(start,end)

#prime(1,1000)
