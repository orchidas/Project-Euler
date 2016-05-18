# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 18:27:28 2016

@author: ORCHISAMA
"""

# Problem - 19
# You are given the following information, but you may prefer to do some research for yourself.

#     1 Jan 1900 was a Monday.
#     Thirty days has September,
#     April, June and November.
#     All the rest have thirty-one,
#     Saving February alone,
#     Which has twenty-eight, rain or shine.
#     And on leap years, twenty-nine.
#     A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

#counting number of sundays that fell on the first of a month in a century
day = dict()
day[1] = 'sun'
day[2] = 'mon'
day[3] = 'tue'
day[4] = 'wed'
day[5] = 'thur'
day[6] = 'fri'
day[0] = 'sat'

month = dict()
month[1] = 31
month[2] = 28
month[3] = 31
month[4] = 30
month[5] = 31
month[6] = 30
month[7] = 31
month[8] = 31
month[9] = 30
month[10] = 31
month[11] = 30
month[12] = 31

def calculateSundays(firstday, year):
    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                month[2] = 29
            else:
                month[2] = 28
        month[2] = 29
    else:
        month[2] = 28
   
    if firstday == 1:
        suncount = 1
    else:
        suncount = 0
        
    firstdaymonth = 0
    for i in range(2,13):
        firstdaymonth = (month[i-1]%7 + firstday)%7
        firstday = firstdaymonth
        if firstday == 1:
            suncount += 1
        #print 'Month', i ,'starts with a' , day[firstday]
    
    firstdayofnextyear = (month[12]%7 + firstday) % 7
    print 'First day of year', year+1, 'is', day[firstdayofnextyear]
    if year == 1900:
        suncount = 0
    return  (suncount, firstdayofnextyear)
    
 
sundaycount = 0 
firstdayofyear = 1
for year in range(1900,2001):
    res = calculateSundays(firstdayofyear, year)
    sundaycount += res[0]
    firstdayofyear = res[1]
    
print 'Number of months that start with sundays in the twentieth century', sundaycount
    
     
     
       