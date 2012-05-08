#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys
import random
from datetime import *

def random_date(start, end):
    """
    This function will return a random datetime between two datetime 
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return (start + timedelta(seconds=random_second))

    
def insert_timestamps(imgname, timestamps):
    con = lite.connect('test.db')
    min_year = MAXYEAR #dummy min_year guaranteed to be replaced if database has values
    max_year = MINYEAR #dummy max_year guaranteed to be replaced if database has values
    
    with con:
    
        cur = con.cursor() 
        qstr = "CREATE TABLE \"*\" (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL  DEFAULT 1, year INTEGER, month INTEGER, day INTEGER, weekday INTEGER, hour INTEGER, minute INTEGER, second INTEGER, name TEXT, size DOUBLE, path TEXT);"
        cur.execute(qstr.replace("*", imgname))
        for timestamp in timestamps:
            year = timestamp.year
            if year < min_year:
                min_year = year
            if year > max_year:
                max_year = year
            month = timestamp.month
            day = timestamp.day
            weekday = timestamp.weekday()
            hour = timestamp.hour
            minute = timestamp.minute
            second = timestamp.second
            istr = "INSERT INTO \"*\" (year, month, day, weekday, hour, minute, second, name, size, path) VALUES (?, ?, ?, ?, ?, ?, ?, 'test.txt', 40, '/');"
            cur.execute(istr.replace("*", imgname), (year, month, day, weekday, hour, minute, second))  
        
        con.commit()
        if min_year == MAXYEAR:
            return None
        return (min_year, max_year)
            
def testCaller():
    start = datetime.fromordinal(1)
    end = datetime.today()
    rand = random.randint(3, 50)
    timestamps = []
    for i in range (0, rand):
        timestamps += [random_date(start, end)]
    return timestamps
    
        