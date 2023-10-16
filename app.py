import  holidays

def printNumberofPublicHolidays(year):
    year = input()
    for date, name in sorted(holidays.country_holidays(country='ZW', years= year).items()):
     print(date, name)