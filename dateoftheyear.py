#!/usr/bin/python
# -*- coding: UTF-8 -*-

year = int(input('Input year: '))
month = int(input('Input month: '))
day = int(input('Input day: '))
total = 0
if year%4 == 0:
    days = 29
else:
    days = 28
if year%4 == 0:
    print year, 'year is leap, Feb has', days, 'days'
else:
    print year, 'year is common, Feb has', days, 'days'
if month <= 1:
    total = day
elif month == 2:
    total = 31 + day
elif month == 9 or month == 11:
    total = (month - 2) * 30 + days + month/2 + day + 1
else:
    total = (month - 2) * 30 + days + month/2 + day
print year, 'year',month, 'month', day, 'day is the', total, 'days'
