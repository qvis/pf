#!/usr/bin/env python
'''
File Name       :   pf0001_fmfyr.py
Created         :   May 24, 2018
Description     :   Figure out next forecasting month and year based on the day 6th of the month.
Latest Updates  :   x/x/xxxx
Update Notes    :   x/x/xxxx
                :   x/x/xxxx     blah blah blah blah...
'''

import datetime 
import os
import sys

def get_fmfyr():

    #todo: get two deadline based on the current month and next month.itm
    d1,d2=date_two()
    now=datetime.date.today()
    #now=datetime.date(2018,12,6)

    #todo: figure out the future deadline date (6th of the month).
    fdate=date_comp(now,d1,d2)

    #todo: get forecasting month and year.
    fmonth=fdate.month
    fyr=fdate.year

    print str(fmonth)+':'+str(fyr)
    return

def date_comp(current,date1,date2):
    #todo: compare dates and figure out which date is in the future.
    #note: if current date is on 6th of the month, 6th will be 
    #       considered as the future date. 
    if current <= date1:
        fdate = date1

    elif current <=date2:
        fdate = date2

    return fdate

def date_two():    
    #todo: calculate two dates that are 6th of the month.
    now=datetime.date.today()
    mm0 =now.month
    #mm0 =12
    yyyy0=now.year
    dd=now.day

    if mm0 == 12:
        mm1=1
        yyyy1=yyyy0+1
    else:
        mm1=mm0+1
        yyyy1=yyyy0

    ddate0=datetime.date(yyyy0,mm0,6)   #<= used 6th of the month
    ddate1=datetime.date(yyyy1,mm1,6)
    return ddate0, ddate1

