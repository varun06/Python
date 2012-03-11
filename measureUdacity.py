#Define a procedure, measure_udacity,
#that takes its input a list of Strings,
#and outputs a number that is a count
#of the number of elements in the input
#list that start with the letter 'U'
#(uppercase).

#For example,

#measure_udacity(['Dave','Sebastian','Katy']) => 0

#measure_udacity(['Umika','Umberto']) => 2

def measure_udacity(stringList):
	count = 0
	for s in stringList:
		if(s[0] == 'U'):
			count += 1
	return count

print measure_udacity(['Dave','Sebastian','Katy'])
print measure_udacity(['Umika','Umberto','Uno','Umo','ubo'])