#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys
import random
import calendar
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

#run_tests()