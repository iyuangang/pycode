#!/usr/bin/python
# -*- coding: UTF-8 -*-

import datetime
i = datetime.datetime.now()
print ("the time is %s" % i)
print ("ISO format time is %s" % i.isoformat() )
print ("The year is %s" %i.year)
print ("Month is %s" %i.month)
print ("Day is%s" %i.day)
print ("dd/mm/yyyy format is%s/%s/%s" % (i.day, i.month, i.year) )
print ("Hour is %s" %i.hour)
print ("Minute is %s" %i.minute)
print ("Second is %s" %i.second)
