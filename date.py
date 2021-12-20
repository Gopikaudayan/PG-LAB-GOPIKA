import datetime
d=datetime.date.today()
print(d)
print("day",d.day)
print("month",d.month)
print("year",d.year)
d1=datetime.date.today()
print(d1)
td=datetime.timedelta(days=2)
print(td)
d2=d1+td
print(d2)
dt=datetime.datetime.combine(d1,td)
print(d2)
