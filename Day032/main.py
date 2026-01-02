import datetime as dt

now=dt.datetime.now()
year=now.year
day=now.weekday() # int- counting from 0, so 4 is Friday
print(day)

date_of_birth=dt.datetime(year=1994,month=5, day=26, hour=12)
print(date_of_birth)
