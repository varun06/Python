def printbacklet(str):
	index = len(str)
	while index:
		print str[index-1]
		index = index - 1

print printbacklet('banana')