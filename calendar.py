import calendar
mm=int(input("enter the month"))
yy=int(input("enter the year"))
print(calendar.month(yy,mm))
print(calendar.calendar(2000))


import datetime
t=datetime.time(22,26,43)
print(t)
print("hour",t.hour)
print("minitue",t.minute)
print("second",t.second)
print("microsecond",t.microsecond)


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
dt=datetime.datetime.combine(d,t)
print(dt)

