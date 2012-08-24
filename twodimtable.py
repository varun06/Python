def printMultiples(n,high):
	i = 1
	while i <= high:
		print n*i, '\t',
		i = i + 1
	print

def printMultTable(high):
	i = 1
	while i <= high:
		printMultiples(i,i)
		i = i + 1

printMultTable(5)