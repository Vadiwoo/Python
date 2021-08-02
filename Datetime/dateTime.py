print("\n********** In Python, we need to import datetime module to work with date objects *********")

import datetime

today = datetime.datetime.now()
print("Today is ", today)

print("\n********** Extracting objects from datetime modules  *********")
print("Current year is ",today.year)
print("Current month is ",today.month)
print("Current date is ",today.day)
print("The day is ", today.strftime("%A"))
christmas = datetime.datetime(2021, 12, 25)
print("Christmas 2021 is on ", christmas.strftime("%A"))
print("\n********** The strftime() method can take one parameter and return the parameter in string *********")

print("Day in short: Today is  ",today.strftime("%a"))

print("\nDay in full: Today is  ",today.strftime("%A"))

print("\nDay in number (Sunday = 0): Today is  ",today.strftime("%w"))

print("\nDay of the month :Today is  ",today.strftime("%d"))

print("\nMonth in short: Today is ",today.strftime("%b"))

print("\nMonth in full : Today is  ",today.strftime("%B"))

print("\nMonth in number : Today is  ",today.strftime("%m"))

print("\nYear in short :Today is  ",today.strftime("%y"))

print("\nYear in full : Today is  ",today.strftime("%Y"))

print("\nHour in 24 hours system: Current time is ",today.strftime("%H"))

print("\nHour in 12 hours system: Current time is  ",today.strftime("%I"))

print("\nAM/PM : Now is ",today.strftime("%p"))

print("\nMinutes :Current minute is ",today.strftime("%M"))

print("\nSeconds :Current second is ",today.strftime("%S"))

print("\nMicroseconds :Current Microsecond is  ",today.strftime("%f"))

# print("\nUTC offset : Today is  ",today.strftime("%z"))

# print("\nTimezone: Timezone  is ",today.strftime("%Z"))

print("\nNumber of the day in a year : Today is  ",today.strftime("%j"))

print("\nWeek number of the yaar, Sunday as first day of week :Today is week of   ",today.strftime("%U"))

print("\nWeek number of the yaar, Monday as first day of week  : Today is week of",today.strftime("%W"))

print("\nLocal version of date and time : Today is ",today.strftime("%c"))

print("\nLocal version of date :  Today is  ",today.strftime("%x"))

print("\nLocal version of time : Today is  ",today.strftime("%X"))

print("\nA % character : Today is  ",today.strftime("%%"))

print("\nISO 8601 year : Today is ",today.strftime("%G"))

print("\nISO 8601 weekday (1-7) : Today is ",today.strftime("%u"))

print("\nISO 8601 week number (01-53): Current time is ",today.strftime("%V"))

