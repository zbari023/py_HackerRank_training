# How to print a calendar for the given month and year in Python
print('How to print a calendar for the given month and year in Python?')
import calendar
year = int(input('Enter the year : '))
mont = int(input('Enter the month of year: '))
print(calendar.month(year,mont))