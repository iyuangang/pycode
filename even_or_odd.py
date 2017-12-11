#!/usr/bin/python
 
numbers = [12,5,4,33,5,66,7,47,311]
even =[]
odd = []
while len(numbers) > 0 :
    number = numbers.pop()
    if(number % 2 == 0):
        even.append(number)
    else:
        odd.append(number)

print "even is ", even
print "odd is ", odd
