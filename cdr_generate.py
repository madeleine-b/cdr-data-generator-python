import random
from datetime import datetime, MINYEAR, MAXYEAR, timezone
import uuid


def get_random_dt():
	year = random.randint(1900, 2021)
	month = random.randint(1, 12)
	max_days_month = 30 if month in [4, 6, 9, 11] else 31
	if month == 2:
		max_days_month = 29 if random.randint(1, 4) == 1 else 28
	day = random.randint(1, max_days_month)
	hour = random.randint(0, 23)
	minute = random.randint(0, 59)
	second = random.randint(0, 59)
	microsecond = random.randint(0, 1000000 - 1)
	return datetime(year=year, month=month, day=day, hour=hour, 
		            minute=minute, second=second, microsecond=microsecond,
		            tzinfo=timezone.utc)


for i in range(100):
	id = uuid.uuid4()
	calling_num = ''.join([str(n) for n in random.choices(range(10), k=10)])
	called_num = ''.join([str(n) for n in random.choices(range(10), k=10)])

	d1 = get_random_dt()
	d2 = get_random_dt()
	callType = ""
	if random.choice(range(2)) == 0:
		callType = "VOICE"
	else:
		callType = "SMS"
	if "SMS" == callType:
		d2 = d1
	
	callResult = "ANSWERED"
	if (i % 10)== 0 and callType == "VOICE":
		callResult = "BUSY"
		d2 = d1	
	
	charge = random.uniform(0.0, 5000.0)
	dt1_str = str(d1).replace(' ', 'T')
	dt2_str = str(d2).replace(' ', 'T')
	print(str(id)+"|"+calling_num+"|"+called_num+"|"+dt1_str+"|"+dt2_str+"|"+callType+"|%0.2f" % charge+"|"+callResult)

