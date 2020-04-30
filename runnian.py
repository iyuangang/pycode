# -*- coding: UTF-8 -*-
tries=0
while tries<6:
    guess= input("请输入年份: ")
    if (((guess%4 == 0) and (guess%100 != 0)) or (guess%400 == 0)):
        print "闰年"
    else :
        print "平年"
    tries = tries+1
