#!/usr/bin/env python
#ref:
#https://goo.gl/URwBw3

from datetime import date
from datetime import timedelta
from dateutil.relativedelta import relativedelta
import calendar
import sys
import os

def save2f ( f, contents ):
    fout=open(f, 'w')
    fout.write(contents)

os.system('clear')

fyr=int(sys.argv[0])
iyr=fyr + 1
print fyr+1
print iyr
os.sys.exit()


enddate=date(fyr,11,30)
ldate=date(fyr,3,1)
lpdone=0

dict_date=dict()

ii=date(iyr,11,2)
fMmm=ii+relativedelta(months=1)
bfmonth=fMmm.strftime("%b")

i=date(iyr,12,2)
while i < enddate:
    fMmm=i+relativedelta(months=1)
    fmonth=fMmm.strftime("%b")

    #***work on this part trying to make dictionary.
    if fmonth != bfmonth:
        #todo: print forecasting month.
        print(fmonth)

    #todo: save the current fmonth as bfmonth.
    bfmonth=fmonth

    strout=i.strftime("%b").lower()+i.strftime('%d')+i.strftime('%Y')
    print("     " + strout)

    #todo: add dates to dictionary.
    if dict_date.has_key(fmonth):
        dict_date[fmonth].append(strout)
    else:
        dict_date[fmonth]=[strout]

    #todo: add 5 days. 
    i=i+timedelta(days=5)
   
    #todo: check leap year. If leap year, add 1 to i. 
    if calendar.isleap(i.year) and lpdone == 0:
        if ldate.month == i.month:
            i=i+timedelta(days=1)
            lpdone=1

for x in dict_date.keys():
    print x
    print dict_date[x]


os.sys.exit()









for name in calendar.month_abbr:
    print(name.lower())



c=calendar.isleap(2018)
print(c)



f='out.html'

for month in range (1,13):
    mycal = calendar.monthcalendar(2025,month)
    week1 = mycal[0]
    week2 = mycal[1]

    if week1[calendar.MONDAY] !=0 :
        auditday = week1[calendar.MONDAY]
    else:
        auditday=week2[calendar.MONDAY]
        

    print ("%10s %2d" % (calendar.month_name[month],auditday))


c=calendar.TextCalendar(calendar.SUNDAY)
#c=calendar.HTMLCalendar(calendar.SUNDAY)
#str=c.formatmonth(2025,1)
#
#save2f(f, str)
#print(str)

for name in calendar.month_name:
    print(name)


for i in c.itermonthdays(2025,4):
    print(i)



