import random
number=random.randint(1,100)
guess=0
tries=0
print "AHH"
print "IT'S A NUMBER FROM 1-100"
while guess!=number and tries<6:
    guess= input("WHAT'S YOUR GUESS: ")
    if guess< number:
        print "TOO LOW, YOU HAVE" ,5-tries, "CHANCE"
    elif guess> number:
        print "TOO LARGE, YOU HAVE",5-tries,"CHANCE"
    tries = tries+1
if guess ==number:
    print "WELL DONE, BABY!"
else:
    print "FAIL! LOSER"
    print "THE NUMBER WAS", number
