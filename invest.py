amount = int(input('amount:'))
rate = int(input('rate:'))
time = int(input('time(year):'))
finally_amount = 0
finally_amount = amount*(1+rate/100)**time
print('finally amount is',finally_amount)
