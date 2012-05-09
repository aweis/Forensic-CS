#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys
import random
import calendar
import build_database as bd
from datetime import *

def by_year(imgname, min, max):
	con = lite.connect('test.db')
	yrs = []
	vals = []
	
	curyear = min
	
	with con:
		while curyear <= max:
			yrs.append(curyear)
			
			cur = con.cursor() 
			query = "SELECT COUNT(id) FROM \"IMG\" WHERE year=CURYEAR"
			cur.execute(query.replace("IMG", imgname).replace("CURYEAR", str(curyear)))
			vals.append(str(cur.fetchone())[1])
			
			curyear = curyear + 1
	
	return (yrs, vals)
	
def by_month(imgname, yr):
	con = lite.connect('test.db')
	months = []
	vals = []
	curmonth = 1
	
	with con:
		while curmonth <= 12:
			months.append(curmonth)
			
			cur = con.cursor()
			query = "SELECT COUNT(id) FROM \"IMG\" WHERE year=" + str(yr) + " AND month=MO"
			cur.execute(query.replace("IMG", imgname).replace("MO", str(curmonth)))
			vals.append(str(cur.fetchone())[1])
			
			curmonth = curmonth + 1
			
	return (months, vals)

def by_day(imgname, yr, mo):
	con = lite.connect('test.db')
	days = []
	vals = []
	maxday = calendar.monthrange(yr, mo)[1]
	curday = 1
	
	with con:
		while curday <= maxday:
			days.append(curday)
			
			cur = con.cursor()
			query = "SELECT COUNT(id) FROM \"IMG\" WHERE year=" + str(yr) + " AND month=" + str(mo) + " AND day=CDAY"
			cur.execute(query.replace("IMG", imgname).replace("CDAY", str(curday)))
			vals.append(str(cur.fetchone())[1])
			
			curday = curday + 1
	
	return (days, vals)
	
def by_hr(imgname, yr, mo, day):
	con = lite.connect('test.db')
	hrs = []
	vals = []
	curhr = 0
	
	with con:
		while curhr < 24:
			hrs.append(curhr)
			
			cur = con.cursor()
			query = "SELECT COUNT(id) FROM \"IMG\" WHERE year=" + str(yr) + " AND month=" + str(mo) + " AND day=" + str(day) + " AND hour=CHR"		
			cur.execute(query.replace("IMG", imgname).replace("CHR", str(curhr)))
			vals.append(str(cur.fetchone())[1])
			
			curhr = curhr + 1
	
	return (hrs, vals)
	
def by_min(imgname, yr, mo, day, hr):
	con = lite.connect('test.db')
	mins = []
	vals = []
	curmin = 0
	
	with con:
		while curmin < 60:
			mins.append(curmin)
			
			cur = con.cursor()
			query = "SELECT COUNT(id) FROM \"IMG\" WHERE year=" + str(yr) + " AND month=" + str(mo) + " AND day=" + str(day) + " AND hour=" + str(hr) + " AND minute=CMIN"		
			cur.execute(query.replace("IMG", imgname).replace("CMIN", str(curmin)))
			vals.append(str(cur.fetchone())[1])
			
			curmin = curmin + 1
	
	return (mins, vals)
	
def getTimeStampValues(imgname, xtype, ranges):
    minXVal = ranges[xtype][0]
    maxXVal = ranges[xtype][1]
    xs = []
    ys = []
    curXVal = minXVal
    con = lite.connect('test.db')
    qstr = "SELECT COUNT(id) FROM \""
    qstr += imgname
    qstr += "\" WHERE "
    units = {
        0 : "year",
        1 : "month",
        2 : "weekday",
        3 : "day",
        4 : "hour"
    }
    
    for i in range(len(units)):
        if i <> 0:
            qstr += " AND "
        if xtype == i:
            qstr += (units[i] + " = VAL")
        else:
            qstr += (units[i] + " BETWEEN " + str(ranges[i][0]) + " AND " + str(ranges[i][1]))
    print qstr
    
    with con:
        while curXVal < maxXVal:
            xs.append(curXVal)
            
            cur = con.cursor()
            cur.execute(qstr.replace("VAL", str(curXVal)))
            ys.append((cur.fetchone())[0])
            curXVal += 1
    return (xs, ys)
            
            
    

def run_tests():
	print "Years test"
	(yrs, vals) = by_year("Files", 2010, 2013)
	print '[%s]' % ', '.join(map(str, yrs))
	print '[%s]' % ', '.join(map(str, vals))
	
	print "Months test"
	(mos, vals) = by_month("Files", 2012)
	print '[%s]' % ', '.join(map(str, mos))
	print '[%s]' % ', '.join(map(str, vals))
	
	print "Days test"
	(days, vals) = by_day("Files", 2012, 5)
	print '[%s]' % ', '.join(map(str, days))
	print '[%s]' % ', '.join(map(str, vals))
	
	print "Hours test"
	(hrs, vals) = by_hr("Files", 2012, 5, 1)
	print '[%s]' % ', '.join(map(str, hrs))
	print '[%s]' % ', '.join(map(str, vals))
	
	print "Minutes test"
	(mins, vals) = by_min("Files", 2012, 5, 1, 22)
	print '[%s]' % ', '.join(map(str, mins))
	print '[%s]' % ', '.join(map(str, vals))
	
def run_dtests():
    ranges = [(0, 1400), (0, 11), (0, 5), (0, 28), (0, 18)]
    
    print "Years test"
    (yrs, vals) = getTimeStampValues("i_lookup", 0, ranges)
    print '[%s]' % ', '.join(map(str, yrs))
    print '[%s]' % ', '.join(map(str, vals))
    
    print "Months test"
    (mos, vals) = getTimeStampValues("i_lookup", 1, ranges)
    print '[%s]' % ', '.join(map(str, mos))
    print '[%s]' % ', '.join(map(str, vals))
    
    print "Days test"
    (days, vals) = getTimeStampValues("i_lookup", 2, ranges)
    print '[%s]' % ', '.join(map(str, days))
    print '[%s]' % ', '.join(map(str, vals))
    
    print "Hours test"
    (hrs, vals) = getTimeStampValues("i_lookup", 3, ranges)
    print '[%s]' % ', '.join(map(str, hrs))
    print '[%s]' % ', '.join(map(str, vals))
    
    print "Minutes test"
    (mins, vals) = getTimeStampValues("i_lookup", 4, ranges)
    print '[%s]' % ', '.join(map(str, mins))
    print '[%s]' % ', '.join(map(str, vals))

#run_tests()
#run_dtests()