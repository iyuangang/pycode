def control_function():
    print('what\'s your choice?\ninvest=0,invest2=1')
    choice =int(input('your choice:'))
    if choice == 0:
        amount = int(input('amount:'))
        rate = int(input('rate:'))
        time = int(input('time(year):'))
        finally_amount = 0
        finally_amount = amount*(1+rate/100)**time
        print('finally amount is',finally_amount)
    elif choice == 1:
        amount = int(input('amount:'))
        rate = int(input('rate:'))
        time = int(input('time(year):'))
        print('amount:{}'.format(amount))
        for t in range(1,time+1):
            amount = amount*(1+rate/100)
            print('year {}: ${}'.format(t,amount))
    else:
        print('invaild input')
control_function()    
