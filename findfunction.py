def find(str, ch, off):
	index = 0
	str = str[off:]
	while index < len(str):
		if str[index] == ch:
			return index
		index += 1
	return -1

print find('Hello! who is there?', 'l', 1)