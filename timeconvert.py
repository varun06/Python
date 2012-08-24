def time24hr(tstr):
	temp = tstr.split(':')
	h = temp[0]
	m1 = temp[1]
	m = m1[0:2]
	if 'am' in tstr:
		if int(h)<12:
			return h+m+'hr'
		else:
			return '00'+m+'hr'
	if 'pm' in tstr:
		if int(h)==12:
			return h+m+'hr'
		else:
			h = int(h)+12
			return str(h)+m+'hr'
	

print time24hr('12:34pm')