def find(str, ch, off):
	index = 0
	str = str[off:]
	while index < len(str):
		if str[index] == ch:
			return index
		index += 1
	return -1

def countLetters(inp, val):
	count = 0
	string = str(inp)
	val = str(val)
	index = 0
	while index < len(string):
		count += find(string, val, index)
		index += 1
	return count

# def countLetters(input,val):
# 	count = 0 
# 	string = str(input)
# 	val = str(val)
# 	for char in string:
# 		if char == val:
# 			count += 1
# 	return count

print countLetters('bananaba', 'a')