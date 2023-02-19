""" from datetime import date, timedelta
d=date.today()-timedelta(5)
print(d) """

""" from datetime import date, timedelta
today=date.today()
y=today-timedelta(days = 1)
t=today+timedelta(days = 1) 
print('Yesterday : ',y)
print('Today : ',today)
print('Tomorrow : ',t) """

""" import datetime
d=datetime.datetime.today().replace(microsecond=0)
print(d) """

""" from datetime import datetime
d1=input('Enter date in this format %d-%m-%Y %H:%M:%S ')
d2=input('Enter date in this format %d-%m-%Y %H:%M:%S ')
dateformat = '%d-%m-%Y %H:%M:%S'
date1= datetime.strptime(d1, dateformat)
date2=datetime.strptime(d2, dateformat)
diff=date2-date1
print('Difference between two dates in seconds:')
print(diff.total_seconds()) """