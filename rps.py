#!/usr/bin/python
# -*- coding: UTF-8 -*-

import random
while 1:
    s = int(random.randint(1, 3))
    if s == 1:
        ind = "Rock"
    elif s == 2:
        ind = "Scissors"
    elif s == 3:
        ind = "Paper"
    m = raw_input('Input Rock, Paper, Scissors to start, Input "end" to exit:')
    blist = ['Rock', "Scissors", "Paper"]
    if (m not in blist) and (m != 'end'):
        print "Please input again"
    elif (m not in blist) and (m == 'end'):
        print "\nExiting..."
        break
    elif m == ind :
        print "AI: " + ind + ", Draw!"
    elif (m == 'Rock' and ind =='Scissors') or (m == 'Scissors' and ind =='Paper') or (m == 'Paper' and ind =='Rock'):
        print "AI: " + ind +", You Win"
    elif (m == 'Rock' and ind =='Paper') or (m == 'Scissors' and ind =='Rock') or (m == 'Paper' and ind =='Scissors'):
        print "AI: " + ind +", You Lose"
