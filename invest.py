def control_function():
    print('what\'s your choice?\ninvest=0,invest2=1')
    choice =int(input('your choice:'))
    if choice == 0:
        amount = int(input('amount:'))
        rate = float(input('rate:'))
        time = int(input('time(year):'))
        finally_amount = 0
        finally_amount = amount*(1+rate)**time
        print('finally amount is {:.2f}'.format(finally_amount))
    elif choice == 1:
        amount = int(input('amount:'))
        rate = float(input('rate:'))
        time = int(input('time(year):'))
        print('amount:{}'.format(amount))
        for t in range(1,time+1):
            amount = amount*(1+rate)
            print('year {}: ${:.2f}'.format(t,amount))
    else:
        print('invaild input')
        control_function()
control_function()    
