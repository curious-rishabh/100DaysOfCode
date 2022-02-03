# Days in months
# Day 6 of 100DaysOfCode

def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
    if month >12 or month <1:
      return "Invalid month"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leap = is_leap(year)
    if leap == True and month == 2:
      return 29
    for day in range(0,len(month_days)):
      return month_days[month -1]
    # or 
    # return month_days[month -1]
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)








