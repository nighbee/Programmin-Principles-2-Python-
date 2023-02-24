import datetime
from datetime import datetime,timedelta
#1
curr_date= datetime.now()
new_date= curr_date-timedelta(days=5)
print(new_date)
#2
print(curr_date)
yesterday= curr_date-timedelta(days=1)
print(yesterday)
tomorrow=curr_date+timedelta(days=1)
print(tomorrow)
#3

#4
date1=datetime(2022,2,14,12,0,0)
date2=datetime(1999, 2,14,0,10)
diff=(date1-date2).total_seconds()
print(diff)