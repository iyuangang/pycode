def invest():
    amount = int(input('amount:'))
    rate = int(input('rate:'))
    time = int(input('time(year):'))
    print('amount:{}'.format(amount))
    for n in range(1,time + 1):
        amount = amount * (1 + rate)
        print('year {}: ${}'.format(n,amount))

invest()
