def invest():
    amount = int(input('amount:'))
    rate = int(input('rate:'))
    time = int(input('time(year):'))
    if amount < 0:
        print('Invaild input')
        amount = int(input('amount:'))
    if rate < 0:
        print('Invaild input')
        rate = int(input('rate:'))
    if time < 0:
        print('Invaild input')
        time = int(input('time(year):'))
    finally_amount = 0
    finally_amount = amount*(1+rate/100)**time
    print('finally amount is',finally_amount)
invest()
