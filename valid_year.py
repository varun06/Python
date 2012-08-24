def valid_year(year):
	if year and year.isdigit():
		year = int(year)
		if 1900 < year <= 2020:
			return year
		return None

print valid_year('0')
print valid_year('-11')
print valid_year('1950')
print valid_year('2000')
print valid_year('foo')