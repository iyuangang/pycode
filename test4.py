def invest2(): 
    amount = int(input('amount:'))
    rate = int(input('rate:'))
    time = int(input('time(year):'))
    print('amount:{}'.format(amount))
    for t in range(1,time+1):
        amount = amount*(1+rate/100)
        print('year {}: ${}'.format(t,amount))
invest2()
