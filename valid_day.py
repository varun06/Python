def valid_day(day):
	if day and day.isdigit():
		day = int(day)
		if 0 < day <= 31:
			return day
		return None

print valid_day('0')
print valid_day('1')
print valid_day('15')
print valid_day('500')
print valid_day(' ')