import datetime as datetime

x = int(input("Enter the number of years: "))

year = int(datetime.datetime.today().year)

while x:
    new_year = datetime.datetime(year, 1, 1)
    print(new_year)
    print(new_year.strftime(f'%a'))
    x = x-1
    year = year - 1
