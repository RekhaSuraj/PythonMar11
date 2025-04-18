import time

t1 = time.localtime()
print(type(t1))
# <class 'time.struct_time'>
print(t1)
# time.struct_time(tm_year=2025, tm_mon=4, tm_mday=18, tm_hour=12, tm_min=11, tm_sec=23, tm_wday=4, tm_yday=108, tm_isdst=0)

# What does this mean?
# Field	Meaning
# tm_year	Year (e.g. 2025)
# tm_mon	Month (1–12)
# tm_mday	Day of the month (1–31)
# tm_hour	Hour (0–23)
# tm_min	Minute (0–59)
# tm_sec	Second (0–59)
# tm_wday	Weekday (0=Monday)
# tm_yday	Day of the year (1–366)
# tm_isdst	1=Daylight Saving Time, 0=Standard Time

# More readable format
# time.strftime("")
print(help(time.strftime))