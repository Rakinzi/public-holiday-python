import  holidays

def printNumberofPublicHolidays(year):
    numOfHolidays = 0
    for date, name in sorted(holidays.ZW(years= year).items()):
        print(date, name)
        numOfHolidays += 1
    print(f'There are {numOfHolidays} holidays in the year {year}')

year = int(input('Enter a year: '))
printNumberofPublicHolidays(year)