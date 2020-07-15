import datetime as datetime

today = datetime.datetime.now()
santa = datetime.datetime(today.year,12,25,3,33,33)

difference = santa-today

print(difference.total_seconds())
