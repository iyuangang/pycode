def invest():
    amount = int(input('amount:'))
    rate = float(input('rate:'))
    time = int(input('time(year):'))
    if amount < 0:
        print('Invaild input')
        amount = int(input('amount:'))
    if rate < 0:
        print('Invaild input')
        rate = float(input('rate(float):'))
    if time < 0:
        print('Invaild input')
        time = int(input('time(year):'))
    finally_amount = 0
    finally_amount = amount*(1+rate)**time
    print('finally amount is {:.2f}'.format(finally_amount))
def invest2():
    amount = int(input('amount:'))
    rate = float(input('rate(float):'))
    time = int(input('time(year):'))
    if amount < 0:
        print('Invaild input')
        amount = int(input('amount:'))
    if rate < 0:
        print('Invaild input')
        rate = float(input('rate(float):'))
    if time < 0:
        print('Invaild input')
        time = int(input('time(year):'))
    print('amount:{}'.format(amount))
    for n in range(1,time + 1):
        amount = amount * (1 + rate)
        print('year {}: ${:.2f}'.format(n,amount))
def control_function():
    print('What\'s your choice?\ninvest=0,invest2=1')
    choice = int(input('your choice:'))
    if choice == 0:
       invest()
    elif choice == 1:
       invest2()
    else:
        print('invaild input')
        control_function()
control_function()
