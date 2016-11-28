import calendar
import datetime

for y in range(1006,2006,10):
	d=datetime.date(y,1,26)
	if calendar.isleap(y) and d.weekday()==0:
		print(d)